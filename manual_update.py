"""Manual update script for on-demand posts"""

import os
import asyncio
from dotenv import load_dotenv
from bot import HobbyBot

load_dotenv()

async def manual_update():
    """Manually trigger a post update"""
    try:
        print("Starting manual update...")
        
        bot = HobbyBot()
        await bot.create_post()
        
        print("Manual update completed successfully!")
        print("Each post is now a single message with varied content")
        print("Channel is read-only")
        print("No extra messages sent")
        print("Scheduled posting: every 3 hours (with initial post on startup)")
        print("For single test post, run: python bot.py --once")
        print("For scheduled automatic posting, run: python bot.py")
        
    except Exception as e:
        print(f"Manual update failed: {e}")

if __name__ == "__main__":
    asyncio.run(manual_update())