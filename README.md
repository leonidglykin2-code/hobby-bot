# Hobby Bot

A multi-platform bot that shares interesting hobbies with pictures, descriptions, and hobby-related advertising. Currently running on Telegram with plans for Facebook integration.

## Features

- Automated posts every 3 hours (with initial post on startup)
- Manual update capability
- AI-generated interesting hobby content
- Single-message format with varied content
- Hobby-related recommendations
- Multi-platform ready (Telegram → Facebook)
- Read-only channel with clean format

## Current Hobby Categories

- Nature
- Hiking
- AI
- Sports

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables in `.env`:
```
BOT_TOKEN=your_telegram_bot_token
CHANNEL_ID=@your_channel
AI_API_KEY=your_ai_api_key
AI_MODEL=your_ai_model
```

3. Run the bot:
```bash
python bot.py
```

4. For manual updates:
```bash
python manual_update.py
```

## Architecture

- `bot.py` - Main Telegram bot with scheduled posting
- `manual_update.py` - Manual update script
- `content_generator.py` - AI content generation
- `hobby_pool.py` - Hobby data and selection logic
- `advertising.py` - Hobby-related advertising system
- `platform_adapter.py` - Platform-specific formatting (Telegram/Facebook)

## Future Plans

- Facebook channel integration
- Enhanced hobby pool
- Advanced content generation
