"""Hobby data pool and selection logic"""

HOBBY_CATEGORIES = {
    "nature": {
        "name": "Nature",
        "description": "Explore the wonders of the natural world",
        "keywords": ["plants", "animals", "landscapes", "wildlife", "environment", "outdoors"],
        "advertising_keywords": ["gardening", "hiking gear", "nature photography", "camping", "wildlife watching"],
        "specific_hobbies": [
            {
                "name": "Bird Watching",
                "description": "Observe and identify birds in their natural habitats",
                "benefits": "Reduces stress, improves patience, connects you with nature, builds observational skills",
                "news_keywords": ["bird watching", "ornithology", "bird conservation", "wildlife"]
            },
            {
                "name": "Gardening",
                "description": "Cultivate plants and create beautiful outdoor spaces",
                "benefits": "Physical exercise, mental health benefits, fresh produce, environmental impact",
                "news_keywords": ["gardening", "horticulture", "plants", "sustainable living"]
            },
            {
                "name": "Photography",
                "description": "Capture stunning images of nature and wildlife",
                "benefits": "Creative expression, mindfulness, appreciation of beauty, technical skills",
                "news_keywords": ["nature photography", "wildlife photography", "landscape photography"]
            }
        ]
    },
    "hiking": {
        "name": "Hiking",
        "description": "Discover trails and outdoor adventures",
        "keywords": ["trails", "mountains", "backpacking", "trekking", "outdoor adventure", "camps"],
        "advertising_keywords": ["hiking boots", "backpacks", "trail maps", "outdoor clothing", "navigation"],
        "specific_hobbies": [
            {
                "name": "Mountain Hiking",
                "description": "Challenge yourself with mountain trails and peaks",
                "benefits": "Cardiovascular fitness, leg strength, mental resilience, spectacular views",
                "news_keywords": ["mountain hiking", "trail running", "mountaineering", "peaks"]
            },
            {
                "name": "Backpacking",
                "description": "Multi-day hiking trips with camping gear",
                "benefits": "Self-reliance, adventure, disconnecting from technology, nature immersion",
                "news_keywords": ["backpacking", "thru-hiking", "camping", "outdoor adventure"]
            },
            {
                "name": "Trail Running",
                "description": "Running on nature trails and paths",
                "benefits": "Intense cardio, agility, mental focus, varied terrain training",
                "news_keywords": ["trail running", "ultra running", "outdoor fitness", "racing"]
            }
        ]
    },
    "ai": {
        "name": "Artificial Intelligence",
        "description": "Explore the world of AI and machine learning",
        "keywords": ["machine learning", "neural networks", "automation", "robotics", "data science", "coding"],
        "advertising_keywords": ["AI courses", "programming tools", "machine learning platforms", "tech gadgets", "online learning"],
        "specific_hobbies": [
            {
                "name": "Machine Learning",
                "description": "Build intelligent systems that learn from data",
                "benefits": "Problem-solving skills, high-demand career skills, understanding technology trends",
                "news_keywords": ["machine learning", "AI research", "data science", "tech news"]
            },
            {
                "name": "Prompt Engineering",
                "description": "Craft effective prompts for AI systems",
                "benefits": "Communication skills, AI literacy, creative thinking, future-proof skill",
                "news_keywords": ["prompt engineering", "AI tools", "ChatGPT", "AI applications"]
            },
            {
                "name": "Robotics",
                "description": "Build and program robots for various purposes",
                "benefits": "Engineering skills, creativity, problem-solving, hands-on learning",
                "news_keywords": ["robotics", "automation", "robots", "engineering"]
            }
        ]
    },
    "sports": {
        "name": "Sports",
        "description": "Get active with various sports and fitness activities",
        "keywords": ["fitness", "training", "competition", "athletics", "team sports", "exercise"],
        "advertising_keywords": ["sports equipment", "fitness gear", "training programs", "sportswear", "nutrition"],
        "specific_hobbies": [
            {
                "name": "Soccer",
                "description": "The world's most popular team sport",
                "benefits": "Cardiovascular fitness, teamwork, coordination, social connection",
                "news_keywords": ["soccer", "football", "Premier League", "World Cup", "sports news"]
            },
            {
                "name": "Cycling",
                "description": "Ride bicycles for sport, transportation, and fitness",
                "benefits": "Low-impact cardio, leg strength, environmental benefits, exploration",
                "news_keywords": ["cycling", "Tour de France", "biking", "cycling news"]
            },
            {
                "name": "Tennis",
                "description": "Racquet sport combining physical and mental skills",
                "benefits": "Full-body workout, hand-eye coordination, mental strategy, social sport",
                "news_keywords": ["tennis", "Grand Slam", "ATP", "WTA", "tennis news"]
            },
            {
                "name": "Basketball",
                "description": "Fast-paced team sport with athletic moves",
                "benefits": "Cardio fitness, coordination, teamwork, explosive power",
                "news_keywords": ["basketball", "NBA", "basketball news", "sports"]
            },
            {
                "name": "Swimming",
                "description": "Water-based full-body exercise",
                "benefits": "Full-body workout, low-impact, cardiovascular health, mental relaxation",
                "news_keywords": ["swimming", "Olympics", "aquatics", "swimming news"]
            }
        ]
    }
}

class HobbyPool:
    def __init__(self):
        self.categories = list(HOBBY_CATEGORIES.keys())
        self.last_used_category = None
        self.last_used_specific_hobby = None
    
    def get_random_hobby(self):
        """Select a random hobby category, avoiding immediate repetition"""
        import random
        
        available_categories = [cat for cat in self.categories if cat != self.last_used_category]
        
        if not available_categories:
            available_categories = self.categories
        
        selected = random.choice(available_categories)
        self.last_used_category = selected
        
        category_data = HOBBY_CATEGORIES[selected]
        
        # Select a random specific hobby from the category
        specific_hobbies = category_data.get('specific_hobbies', [])
        if specific_hobbies:
            available_specific = [h for h in specific_hobbies if h['name'] != self.last_used_specific_hobby]
            if not available_specific:
                available_specific = specific_hobbies
            
            selected_specific = random.choice(available_specific)
            self.last_used_specific_hobby = selected_specific['name']
            
            # Merge category data with specific hobby data
            return {
                **category_data,
                'specific_hobby': selected_specific,
                'is_specific': True
            }
        
        return category_data
    
    def get_hobby_by_name(self, category_name):
        """Get specific hobby category by name"""
        return HOBBY_CATEGORIES.get(category_name.lower())
    
    def get_all_categories(self):
        """Get all available hobby categories"""
        return HOBBY_CATEGORIES