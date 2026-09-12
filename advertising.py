"""Hobby-related advertising system"""

import random

class AdvertisingGenerator:
    def __init__(self):
        pass
    
    def generate_advertisement(self, hobby_category):
        """Generate hobby-related advertising content"""
        advertising_keywords = hobby_category.get('advertising_keywords', [])
        
        if not advertising_keywords:
            return self._generate_generic_ad(hobby_category)
        
        selected_keyword = random.choice(advertising_keywords)
        
        ads = [
            f"🛒 Check out amazing {selected_keyword} for your {hobby_category['name'].lower()} journey!",
            f"🔥 Special deal on {selected_keyword} - perfect for {hobby_category['name'].lower()} enthusiasts!",
            f"💡 Tip: Quality {selected_keyword} can enhance your {hobby_category['name'].lower()} experience!",
            f"🎯 Looking for {selected_keyword}? We've got great recommendations for {hobby_category['name'].lower()} lovers!"
        ]
        
        return {
            "text": random.choice(ads),
            "type": "hobby_related",
            "keyword": selected_keyword
        }
    
    def _generate_generic_ad(self, hobby_category):
        """Generate generic hobby-related ad when no specific keywords available"""
        generic_ads = [
            f"🛒 Find the best equipment and supplies for {hobby_category['name'].lower()}!",
            f"🔥 Discover great resources to start your {hobby_category['name'].lower()} adventure!",
            f"💡 Everything you need for {hobby_category['name'].lower()} - learn more today!"
        ]
        
        return {
            "text": random.choice(generic_ads),
            "type": "generic",
            "keyword": hobby_category['name'].lower()
        }
    
    def get_affiliate_link(self, hobby_category, keyword):
        """Generate affiliate link (placeholder for actual implementation)"""
        # This would be replaced with actual affiliate network integration
        return f"https://example.com/{hobby_category['name'].lower()}/{keyword.replace(' ', '-').lower()}"