"""Hobby data pool and selection logic"""

HOBBY_CATEGORIES = {
    "nature": {
        "name": "Nature",
        "description": "Explore the wonders of the natural world",
        "keywords": ["plants", "animals", "landscapes", "wildlife", "environment", "outdoors"],
        "advertising_keywords": ["gardening", "hiking gear", "nature photography", "camping", "wildlife watching"]
    },
    "hiking": {
        "name": "Hiking",
        "description": "Discover trails and outdoor adventures",
        "keywords": ["trails", "mountains", "backpacking", "trekking", "outdoor adventure", "camps"],
        "advertising_keywords": ["hiking boots", "backpacks", "trail maps", "outdoor clothing", "navigation"]
    },
    "ai": {
        "name": "Artificial Intelligence",
        "description": "Explore the world of AI and machine learning",
        "keywords": ["machine learning", "neural networks", "automation", "robotics", "data science", "coding"],
        "advertising_keywords": ["AI courses", "programming tools", "machine learning platforms", "tech gadgets", "online learning"]
    },
    "sports": {
        "name": "Sports",
        "description": "Get active with various sports and fitness activities",
        "keywords": ["fitness", "training", "competition", "athletics", "team sports", "exercise"],
        "advertising_keywords": ["sports equipment", "fitness gear", "training programs", "sportswear", "nutrition"]
    }
}

class HobbyPool:
    def __init__(self):
        self.categories = list(HOBBY_CATEGORIES.keys())
        self.last_used_category = None
    
    def get_random_hobby(self):
        """Select a random hobby category, avoiding immediate repetition"""
        import random
        
        available_categories = [cat for cat in self.categories if cat != self.last_used_category]
        
        if not available_categories:
            available_categories = self.categories
        
        selected = random.choice(available_categories)
        self.last_used_category = selected
        
        return HOBBY_CATEGORIES[selected]
    
    def get_hobby_by_name(self, category_name):
        """Get specific hobby category by name"""
        return HOBBY_CATEGORIES.get(category_name.lower())
    
    def get_all_categories(self):
        """Get all available hobby categories"""
        return HOBBY_CATEGORIES