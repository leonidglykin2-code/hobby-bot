"""Platform-specific formatting and posting (Telegram/Facebook)"""

class PlatformAdapter:
    def __init__(self, platform="telegram"):
        self.platform = platform
    
    def format_message(self, content, advertisement, image_url=None):
        """Format message for specific platform"""
        if self.platform == "telegram":
            return self._format_telegram(content, advertisement, image_url)
        elif self.platform == "facebook":
            return self._format_facebook(content, advertisement, image_url)
        else:
            raise ValueError(f"Unsupported platform: {self.platform}")
    
    def _format_telegram(self, content, advertisement, image_url=None):
        """Format message for Telegram"""
        message = f"🌟 *{content['title']}*\n\n"
        message += f"{content['description']}\n\n"
        message += f"💡 {content['fact']}\n\n"
        message += f"📢 {advertisement['text']}\n\n"
        message += f"💬 {content['call_to_action']}"
        
        return {
            "text": message,
            "parse_mode": "Markdown",
            "image_url": image_url,
            "disable_web_page_preview": False
        }
    
    def _format_facebook(self, content, advertisement, image_url=None):
        """Format message for Facebook"""
        message = f"{content['title']}\n\n"
        message += f"{content['description']}\n\n"
        message += f"💡 {content['fact']}\n\n"
        message += f"📢 {advertisement['text']}\n\n"
        message += f"💬 {content['call_to_action']}"
        
        return {
            "text": message,
            "image_url": image_url,
            "link_url": advertisement.get('link_url')
        }
    
    def get_platform_limits(self):
        """Get platform-specific limits"""
        if self.platform == "telegram":
            return {
                "max_text_length": 4096,
                "supports_markdown": True,
                "supports_html": True
            }
        elif self.platform == "facebook":
            return {
                "max_text_length": 63206,
                "supports_markdown": False,
                "supports_html": False
            }