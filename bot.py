"""Main Telegram bot with scheduled posting"""

import os
import asyncio
import schedule
import time
import sys
from datetime import datetime
from dotenv import load_dotenv
from telegram import Bot
from telegram.request import HTTPXRequest

from hobby_pool import HobbyPool
from content_generator import ContentGenerator
from advertising import AdvertisingGenerator
from platform_adapter import PlatformAdapter

# Set UTF-8 encoding for Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

load_dotenv()

class HobbyBot:
    def __init__(self):
        self.bot_token = os.getenv("BOT_TOKEN")
        self.channel_id = os.getenv("CHANNEL_ID")
        
        if not self.bot_token or not self.channel_id:
            raise ValueError("BOT_TOKEN and CHANNEL_ID must be set in .env file")
        
        # Initialize components
        self.hobby_pool = HobbyPool()
        self.content_generator = ContentGenerator()
        self.activity_link_generator = AdvertisingGenerator()
        self.platform_adapter = PlatformAdapter("telegram")
        
        # Initialize Telegram bot
        request = HTTPXRequest(connection_pool_size=8)
        self.bot = Bot(token=self.bot_token, request=request)
        
        print(f"Bot initialized for channel: {self.channel_id}", flush=True)
    
    async def create_post(self):
        """Create and post a new hobby update"""
        try:
            print(f"[{datetime.now()}] Creating new post...", flush=True)
            
            # Select random hobby
            hobby = self.hobby_pool.get_random_hobby()
            print(f"Selected hobby: {hobby['name']}", flush=True)
            
            # Generate content
            content = self.content_generator.generate_hobby_content(hobby)
            print(f"Generated content: {content['title']}", flush=True)
            
            # Generate activity link
            hobby_name = hobby.get('specific_hobby', {}).get('name', hobby['name']) if hobby.get('is_specific') else hobby['name']
            activity_link = self.activity_link_generator.generate_activity_link(hobby_name)
            print(f"Generated activity link: {activity_link['title']}", flush=True)
            
            # Format for platform
            formatted_message = self.platform_adapter.format_message(content, activity_link)
            
            # Post to Telegram
            await self._post_to_telegram(formatted_message)
            
            print(f"[{datetime.now()}] Post successfully created and sent!", flush=True)
            
        except Exception as e:
            print(f"Error creating post: {e}", flush=True)
    
    async def _post_to_telegram(self, formatted_message):
        """Post formatted message to Telegram channel as single message"""
        try:
            # Send single text message without any extra features
            await self.bot.send_message(
                chat_id=self.channel_id,
                text=formatted_message["text"],
                parse_mode=formatted_message["parse_mode"],
                disable_web_page_preview=True
            )
            
            print("Sent single message only", flush=True)
            
        except Exception as e:
            print(f"Error posting to Telegram: {e}", flush=True)
            raise
    
    def run_scheduled(self):
        """Run bot with scheduled posts"""
        # Schedule posts every 3 hours
        schedule.every(3).hours.do(lambda: asyncio.run(self.create_post()))
        
        print("Bot started with 3-hour posting schedule.", flush=True)
        print("Initial post will be sent immediately upon startup.", flush=True)
        print("Subsequent posts every 3 hours. Press Ctrl+C to stop.", flush=True)
        
        # Send initial post immediately
        try:
            asyncio.run(self.create_post())
            print("Initial post sent successfully.", flush=True)
        except Exception as e:
            print(f"Initial post failed: {e}", flush=True)
        
        try:
            print("Scheduler started. Next post in 3 hours.", flush=True)
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\nBot stopped by user.", flush=True)
    
    def run_once(self):
        """Run bot once for testing"""
        asyncio.run(self.create_post())

def main():
    try:
        print("Starting bot initialization...")
        bot = HobbyBot()
        print("Bot initialized successfully")
        
        # Check if should run once or scheduled
        import sys
        if len(sys.argv) > 1 and sys.argv[1] == "--once":
            print("Running single post for testing...")
            asyncio.run(bot.create_post())
        else:
            # Run with scheduled posting (every 3 hours with initial post)
            print("Starting scheduled bot (3-hour intervals with initial post)...")
            bot.run_scheduled()
        
    except Exception as e:
        print(f"Bot error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()