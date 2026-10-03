"""Platform-specific formatting and posting (Telegram/Facebook)"""

class PlatformAdapter:
    def __init__(self, platform="telegram"):
        self.platform = platform
    
    def format_message(self, content, activity_link, image_url=None):
        """Format message for specific platform"""
        if self.platform == "telegram":
            return self._format_telegram(content, activity_link, image_url)
        elif self.platform == "facebook":
            return self._format_facebook(content, activity_link, image_url)
        else:
            raise ValueError(f"Unsupported platform: {self.platform}")
    
    def _format_telegram(self, content, activity_link, image_url=None):
        """Format message for Telegram with single message format"""
        # If content has a "message" field (new varied format), use it directly
        if "message" in content:
            message = content["message"]
        else:
            # Fallback to old structured format
            message = f"{content['title']}\n\n"
            
            if 'subtitle' in content:
                message += f"{content['subtitle']}\n\n"
            
            # Add benefits section
            if 'benefits' in content:
                message += f"{content['benefits']}\n\n"
            
            # Add news section
            if 'news_section' in content:
                message += f"{content['news_section']}\n\n"
            
            if 'pick' in content:
                message += f"🏆 {content['pick']}\n\n"
            
            if 'why' in content:
                message += f"{content['why']}\n\n"
            
            # Add detailed sections
            if 'sections' in content:
                for section in content['sections']:
                    message += f"{section['header']}\n\n"
                    # Convert markdown links to plain text for better compatibility
                    section_content = section['content'].replace('**', '').replace('[', '').replace('](', ': ').replace(')', '')
                    message += f"{section_content}\n\n"
            
            # Add practical info
            if 'practical_info' in content:
                message += "📋 Practical Info\n\n"
                for key, value in content['practical_info'].items():
                    message += f"• {key.title()}: {value}\n"
                message += "\n"
            
            # Add ratings table with proper alignment
            if 'ratings' in content:
                message += "⭐ Ratings\n\n"
                for category, rating in content['ratings'].items():
                    message += f"{category}: {rating}\n"
                message += "\n"
            
            # Add discussion question
            if 'discussion_questions' in content:
                message += "💬 Join the Conversation\n\n"
                message += "Comments are enabled - share your thoughts!\n\n"
                for question in content['discussion_questions']:
                    message += f"{question}\n\n"
            
            # Add verdict
            if 'verdict' in content:
                message += f"🏅 My Verdict\n\n"
                message += f"{content['verdict']}\n\n"
        
        # Add activity link instead of advertisement
        message += f"\n🎯 Recommended Activity\n\n"
        message += f"{activity_link['title']}\n\n"
        # Shorten description for Telegram limits
        short_desc = activity_link['description'][:150] + "..." if len(activity_link['description']) > 150 else activity_link['description']
        message += f"{short_desc}\n\n"
        message += f"Visit: {activity_link['link']}\n\n"
        
        # Add call to action if exists
        if 'call_to_action' in content:
            message += f"💬 Join the Discussion\n\n"
            message += f"{content['call_to_action']}"
        
        return {
            "text": message,
            "parse_mode": None,  # Disable Markdown to avoid parsing errors
            "disable_web_page_preview": True
        }
    
    def _format_facebook(self, content, advertisement, image_url=None):
        """Format message for Facebook with detailed formatting"""
        message = f"{content['title']}\n\n"
        
        # Add multiple images at the top
        if 'images' in content and content['images']:
            message += "📸 **Images:**\n\n"
            for i, img_url in enumerate(content['images'], 1):
                message += f"![Image {i}]({img_url})\n"
            message += "\n"
        
        if 'subtitle' in content:
            message += f"{content['subtitle']}\n\n"
        
        if 'pick' in content:
            message += f"## 🏆 {content['pick']}\n\n"
        
        if 'why' in content:
            message += f"{content['why']}\n\n"
        
        # Add detailed sections
        if 'sections' in content:
            for section in content['sections']:
                message += f"## {section['header']}\n\n"
                message += f"{section['content']}\n\n"
        
        # Add practical info
        if 'practical_info' in content:
            message += "## 📋 Practical Info\n\n"
            for key, value in content['practical_info'].items():
                message += f"• **{key.title()}**: {value}\n"
            message += "\n"
        
        # Add ratings table with proper alignment
        if 'ratings' in content:
            message += "## ⭐ Ratings\n\n"
            message += "```\n"
            for category, rating in content['ratings'].items():
                message += f"{category} : {rating}\n"
            message += "```\n\n"
        
        # Add discussion questions
        if 'discussion_questions' in content:
            message += "## � Discussion\n\n"
            for i, question in enumerate(content['discussion_questions'], 1):
                message += f"### Question {i}️⃣\n\n"
                message += f"{question}\n\n"
        
        # Add verdict
        if 'verdict' in content:
            message += f"## 🏅 My Verdict\n\n"
            message += f"{content['verdict']}\n\n"
        
        # Add advertisement
        message += f"## 📢 Advertisement\n\n"
        message += f"{advertisement['text']}\n\n"
        
        # Add call to action
        if 'call_to_action' in content:
            message += f"## 🎯 Call to Action\n\n"
            message += f"{content['call_to_action']}"
        
        return {
            "text": message,
            "image_url": image_url,
            "images": content.get('images', []),
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