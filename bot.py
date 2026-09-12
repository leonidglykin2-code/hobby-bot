"""Main Telegram bot with scheduled posting"""

import os
import schedule
import time
from datetime import datetime
from dotenv import load_dotenv
from telegram import Bot
from telegram.request import HTTPXRequest

from hobby_pool import HobbyPool
from content_generator import ContentGenerator
from advertising import AdvertisingGenerator
from platform_adapter import PlatformAdapter

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
        self.advertising_generator = AdvertisingGenerator()
        self.platform_adapter = PlatformAdapter("telegram")
        
        # Initialize Telegram bot
        request = HTTPXRequest(connection_pool_size=8)
        self.bot = Bot(token=self.bot_token, request=request)
        
        print(f"Bot initialized for channel: {self.channel_id}")
    
    def create_post(self):
        """Create and post a new hobby update"""
        try:
            print(f"[{datetime.now()}] Creating new post...")
            
            # Select random hobby
            hobby = self.hobby_pool.get_random_hobby()
            print(f"Selected hobby: {hobby['name']}")
            
            # Generate content
            content = self.content_generator.generate_hobby_content(hobby)
            print(f"Generated content: {content['title']}")
            
            # Generate advertisement
            advertisement = self.advertising_generator.generate_advertisement(hobby)
            print(f"Generated advertisement for: {advertisement['keyword']}")
            
            # Format for platform
            formatted_message = self.platform_adapter.format_message(content, advertisement)
            
            # Post to Telegram
            self._post_to_telegram(formatted_message)
            
            print(f"[{datetime.now()}] Post successfully created and sent!")
            
        except Exception as e:
            print(f"Error creating post: {e}")
    
    def _post_to_telegram(self, formatted_message):
        """Post formatted message to Telegram channel"""
        try:
            # Send text message
            self.bot.send_message(
                chat_id=self.channel_id,
                text=formatted_message["text"],
                parse_mode=formatted_message["parse_mode"],
                disable_web_page_preview=formatted_message["disable_web_page_preview"]
            )
            
            # Note: Image posting would require actual image URLs or file uploads
            # This is a placeholder for image functionality
            if formatted_message.get("image_url"):
                print(f"Image posting not yet implemented - would post: {formatted_message['image_url']}")
            
        except Exception as e:
            print(f"Error posting to Telegram: {e}")
            raise
    
    def run_scheduled(self):
        """Run bot with scheduled posts"""
        # Schedule hourly posts for testing
        schedule.every().hour.do(self.create_post)
        
        print("Bot started with hourly posting schedule. Press Ctrl+C to stop.")
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\nBot stopped by user.")
    
    def run_once(self):
        """Run bot once for testing"""
        self.create_post()

def main():
    try:
        bot = HobbyBot()
        
        # For testing, run once
        print("Running single post for testing...")
        bot.run_once()
        
        # Uncomment below for scheduled posting
        # bot.run_scheduled()
        
    except Exception as e:
        print(f"Bot error: {e}")

if __name__ == "__main__":
    main()