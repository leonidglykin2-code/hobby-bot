"""Manual update script for on-demand posts"""

import os
from dotenv import load_dotenv
from bot import HobbyBot

load_dotenv()

def manual_update():
    """Manually trigger a post update"""
    try:
        print("Starting manual update...")
        
        bot = HobbyBot()
        bot.create_post()
        
        print("Manual update completed successfully!")
        
    except Exception as e:
        print(f"Manual update failed: {e}")

if __name__ == "__main__":
    manual_update()