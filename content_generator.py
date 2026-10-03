"""AI-powered content generation for hobby posts"""

import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
from news_fetcher import NewsFetcher

load_dotenv()

class ContentGenerator:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = os.getenv("AI_MODEL", "gemini-1.5-flash")
        self.news_fetcher = NewsFetcher()
        
        if self.api_key:
            genai.configure(api_key=self.api_key)
            try:
                self.client = genai.GenerativeModel(self.model)
            except Exception as e:
                print(f"Error initializing Gemini model {self.model}: {e}")
                # Try fallback model
                try:
                    self.client = genai.GenerativeModel("gemini-pro")
                except:
                    self.client = None
        else:
            self.client = None
    
    def generate_hobby_content(self, hobby_category):
        """Generate detailed, engaging content about a specific hobby in Facebook style"""
        # Check if this is a specific hobby
        is_specific = hobby_category.get('is_specific', False)
        specific_hobby = hobby_category.get('specific_hobby', None)
        
        if is_specific and specific_hobby:
            hobby_name = specific_hobby['name']
            hobby_description = specific_hobby['description']
            hobby_benefits = specific_hobby['benefits']
            keywords = specific_hobby['news_keywords']
        else:
            hobby_name = hobby_category['name']
            hobby_description = hobby_category['description']
            hobby_benefits = f"Great for mental health, physical fitness, and personal growth"
            keywords = hobby_category['keywords']
        
        # Fetch news for this hobby
        news_data = self.news_fetcher.fetch_hobby_news(hobby_name, keywords)
        
        if not self.client:
            return self._generate_detailed_fallback_content(hobby_category, is_specific, specific_hobby, news_data)
        
        try:
            prompt = f"""
            Generate a comprehensive, engaging Facebook-style post about {hobby_name} as a hobby.
            
            Hobby: {hobby_name}
            Description: {hobby_description}
            Benefits: {hobby_benefits}
            Keywords: {', '.join(keywords)}
            
            Today's News:
            {', '.join(news_data['headlines'][:3])}
            
            Create a detailed post that includes:
            1. A catchy, emoji-rich title (like "⚽ TODAY'S SOCCER ADVENTURE")
            2. A subtitle mentioning it's a specific focus
            3. A section about the benefits of this hobby
            4. Today's news section with the provided headlines
            5. Detailed sections with emoji headers
            6. A specific activity or recommendation
            7. Practical information (duration, difficulty, requirements)
            8. A rating table with multiple categories
            9. Multiple discussion questions (at least 5) to engage the audience
            10. A final verdict/recommendation
            11. Strong call-to-action
            
            Format as JSON with these keys:
            - title: Main title with emojis
            - subtitle: Subtitle with context
            - benefits: Description of hobby benefits
            - news_section: Today's news headlines
            - pick: "Our pick" section
            - why: Why this is special
            - sections: Array of detailed sections with headers and content
            - practical_info: Duration, difficulty, requirements
            - ratings: Object with category names and star ratings
            - discussion_questions: Array of at least 5 engaging questions
            - verdict: Final recommendation and score
            - call_to_action: Strong engagement prompt
            - images: Array of 3-6 placeholder image URLs (use https://via.placeholder.com/800x600?text=Image1, etc.)
            
            Make it very detailed, engaging, and conversational like a sports/hobby Facebook page.
            """
            
            response = self.client.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    temperature=0.8,
                    response_mime_type="application/json"
                )
            )
            
            content = json.loads(response.text)
            return content
            
        except Exception as e:
            print(f"AI generation failed: {e}", flush=True)
            return self._generate_detailed_fallback_content(hobby_category, is_specific, specific_hobby, news_data)
    
    def _generate_detailed_fallback_content(self, hobby_category, is_specific=False, specific_hobby=None, news_data=None):
        """Fallback detailed content generation when AI is unavailable - varied and non-template"""
        import random
        
        if is_specific and specific_hobby:
            hobby_name = specific_hobby['name']
            hobby_description = specific_hobby['description']
            hobby_benefits = specific_hobby['benefits']
        else:
            hobby_name = hobby_category['name']
            hobby_description = hobby_category['description']
            hobby_benefits = f"Great for mental health, physical fitness, and personal growth"
        
        # Varied opening styles
        openings = [
            f"🌟 {hobby_name} - {random.choice(['A Life-Changing Adventure', 'Your Next Passion', 'Discover Something New', 'Transform Your Routine'])}",
            f"🚀 Ready to explore {hobby_name}? {random.choice(['This could change everything', 'Time to start your journey', 'Let\'s dive in', 'Perfect timing to begin'])}",
            f"✨ {hobby_name} awaits! {random.choice(['Here\'s why you should start today', 'The ultimate guide awaits', 'Your adventure begins here', 'Discover the possibilities'])}"
        ]
        
        title = random.choice(openings)
        
        # Varied content structures
        content_styles = random.choice([
            "narrative",  # Story-like format
            "benefits_first",  # Focus on benefits
            "practical",  # Focus on how-to
            "inspiring"  # Motivational focus
        ])
        
        if content_styles == "narrative":
            message = f"{title}\n\n"
            message += f"Imagine {random.choice(['waking up excited', 'having a new passion', 'transforming your weekends', 'discovering hidden talents'])} to practice {hobby_name}. "
            message += f"{hobby_description} This isn't just another activity - it's a lifestyle change.\n\n"
            message += f"🎯 Why Start Today?\n{hobby_benefits}\n\n"
        elif content_styles == "benefits_first":
            message = f"{title}\n\n"
            message += f"🌟 Key Benefits:\n{hobby_benefits}\n\n"
            message += f"💡 What makes {hobby_name} special: {hobby_description}\n\n"
        elif content_styles == "practical":
            message = f"{title}\n\n"
            message += f"📋 Getting Started:\n{hobby_description}\n\n"
            message += f"✨ Why people love it: {hobby_benefits}\n\n"
        else:  # inspiring
            message = f"{title}\n\n"
            message += f"🔥 Ready to transform your life with {hobby_name}?\n\n"
            message += f"{hobby_description}\n\n"
            message += f"💪 Here's what you'll gain: {hobby_benefits}\n\n"
        
        # Add current events/news with varied presentation
        if news_data and news_data.get('headlines'):
            news_style = random.choice([
                "📰 Today's Highlights",
                "🌍 What's Happening Now",
                "⚡ Latest News",
                "📈 Trending Topics"
            ])
            message += f"{news_style}\n"
            for headline in news_data['headlines'][:2]:
                message += f"• {headline}\n"
            message += "\n"
        
        # Add varied practical information
        practical_info = {
            "Time commitment": random.choice(["15-30 min daily", "1-2 hours weekly", "Flexible schedule", "Weekend warrior"]),
            "Skill level": random.choice(["Beginner-friendly", "All levels welcome", "Easy to start, hard to master", "No experience needed"]),
            "Equipment": random.choice(["Minimal gear required", "Just start with basics", "Invest gradually", "Many free options available"])
        }
        
        info_style = random.choice([
            "📋 Quick Facts",
            "🎯 Practical Details",
            "💡 Need to Know",
            "⚡ Fast Facts"
        ])
        message += f"{info_style}\n"
        for key, value in practical_info.items():
            message += f"• {key}: {value}\n"
        message += "\n"
        
        # Varied rating system
        ratings = {
            random.choice(["Fun Factor", "Enjoyment Level"]): random.choice(["⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"]),
            random.choice(["Difficulty", "Learning Curve"]): random.choice(["⭐⭐", "⭐⭐⭐", "⭐"]),
            random.choice(["Social Potential", "Community"]): random.choice(["⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐⭐"]),
            random.choice(["Cost", "Investment"]): random.choice(["⭐⭐", "⭐", "⭐⭐⭐"])
        }
        
        rating_style = random.choice([
            "⭐ Quick Rating",
            "🎯 Score Breakdown",
            "💫 What to Expect",
            "📊 Our Take"
        ])
        message += f"{rating_style}\n"
        for category, rating in ratings.items():
            message += f"{category}: {rating}\n"
        message += "\n"
        
        # Single varied discussion question
        questions = [
            f"What aspect of {hobby_name} interests you most?",
            f"Have you tried {hobby_name} before? Share your experience!",
            f"What's holding you back from starting {hobby_name}?",
            f"If you could master one part of {hobby_name}, what would it be?",
            f"How would {hobby_name} fit into your current lifestyle?"
        ]
        message += f"💬 {random.choice(questions)}\n\n"
        
        # Varied verdict
        verdicts = [
            f"{hobby_name} gets our highest recommendation - it's accessible, rewarding, and perfect for beginners.",
            f"Start {hobby_name} today - you won't regret it. The benefits far outweigh any initial effort.",
            f"This is one hobby that truly delivers on its promises. Give it a try and see for yourself.",
            f"Highly recommended for anyone looking to add something meaningful to their routine."
        ]
        message += f"🏅 {random.choice(verdicts)}\n\n"
        
        # Varied call to action
        ctas = [
            f"Ready to begin your {hobby_name} journey? Check out the resource below!",
            f"Start small, dream big. Your {hobby_name} adventure awaits!",
            f"The best time to start {hobby_name} was yesterday. The second best time is now!",
            f"Take the first step toward {hobby_name} - you won't look back!"
        ]
        message += f"🚀 {random.choice(ctas)}"
        
        return {
            "title": title,
            "message": message,
            "images": []  # No images for now to avoid extra messages
        }
    
    def _get_hobby_images(self, hobby_name):
        """Get hobby-specific images"""
        hobby_images = {
            "soccer": [
                {
                    "url": "https://placehold.co/1600x900/22c55e/white?text=Soccer+Field+Action",
                    "content_section": "header",
                    "description": "Soccer field with action"
                },
                {
                    "url": "https://placehold.co/1600x900/16a34a/white?text=Soccer+Training+Drills",
                    "content_section": "skill_levels",
                    "description": "Soccer action and training"
                },
                {
                    "url": "https://placehold.co/1600x900/15803d/white?text=Soccer+Stadium+Competition",
                    "content_section": "training",
                    "description": "Soccer stadium and competition"
                }
            ],
            "cycling": [
                {
                    "url": "https://placehold.co/1600x900/3b82f6/white?text=Scenic+Cycling+Road",
                    "content_section": "header",
                    "description": "Scenic cycling road"
                },
                {
                    "url": "https://placehold.co/1600x900/2563eb/white?text=Mountain+Biking+Adventure",
                    "content_section": "skill_levels",
                    "description": "Mountain biking adventure"
                },
                {
                    "url": "https://placehold.co/1600x900/1d4ed8/white?text=Cyclist+Training+Technique",
                    "content_section": "training",
                    "description": "Cyclist training and technique"
                }
            ],
            "tennis": [
                {
                    "url": "https://placehold.co/1600x900/ef4444/white?text=Professional+Tennis+Court",
                    "content_section": "header",
                    "description": "Professional tennis court"
                },
                {
                    "url": "https://placehold.co/1600x900/dc2626/white?text=Tennis+Player+Action",
                    "content_section": "skill_levels",
                    "description": "Tennis player in action"
                },
                {
                    "url": "https://placehold.co/1600x900/b91c1c/white?text=Tennis+Equipment+Gear",
                    "content_section": "training",
                    "description": "Tennis equipment and gear"
                }
            ],
            "basketball": [
                {
                    "url": "https://placehold.co/1600x900/f97316/white?text=Basketball+Court",
                    "content_section": "header",
                    "description": "Basketball court"
                },
                {
                    "url": "https://placehold.co/1600x900/ea580c/white?text=Basketball+Action+Shot",
                    "content_section": "skill_levels",
                    "description": "Basketball action shot"
                },
                {
                    "url": "https://placehold.co/1600x900/c2410c/white?text=Basketball+Training+Drills",
                    "content_section": "training",
                    "description": "Basketball training drills"
                }
            ],
            "swimming": [
                {
                    "url": "https://placehold.co/1600x900/06b6d4/white?text=Olympic+Swimming+Pool",
                    "content_section": "header",
                    "description": "Olympic swimming pool"
                },
                {
                    "url": "https://placehold.co/1600x900/0891b2/white?text=Competitive+Swimmer",
                    "content_section": "skill_levels",
                    "description": "Competitive swimmer"
                },
                {
                    "url": "https://placehold.co/1600x900/0e7490/white?text=Swimming+Technique+Form",
                    "content_section": "training",
                    "description": "Swimming technique and form"
                }
            ],
            "photography": [
                {
                    "url": "https://placehold.co/1600x900/8b5cf6/white?text=Professional+Camera+Equipment",
                    "content_section": "header",
                    "description": "Professional camera equipment"
                },
                {
                    "url": "https://placehold.co/1600x900/7c3aed/white?text=Photographer+Action",
                    "content_section": "skill_levels",
                    "description": "Photographer in action"
                },
                {
                    "url": "https://placehold.co/1600x900/6d28d9/white?text=Photography+Studio+Setup",
                    "content_section": "training",
                    "description": "Photography studio setup"
                }
            ],
            "bird watching": [
                {
                    "url": "https://placehold.co/1600x900/84cc16/white?text=Beautiful+Birds+Nature",
                    "content_section": "header",
                    "description": "Beautiful birds in nature"
                },
                {
                    "url": "https://placehold.co/1600x900/65a30d/white?text=Bird+Watching+Binoculars",
                    "content_section": "skill_levels",
                    "description": "Bird watching with binoculars"
                },
                {
                    "url": "https://placehold.co/1600x900/4d7c0f/white?text=Nature+Habitat+Birds",
                    "content_section": "training",
                    "description": "Nature habitat with birds"
                }
            ],
            "gardening": [
                {
                    "url": "https://placehold.co/1600x900/22c55e/white?text=Beautiful+Vegetable+Garden",
                    "content_section": "header",
                    "description": "Beautiful vegetable garden"
                },
                {
                    "url": "https://placehold.co/1600x900/16a34a/white?text=Healthy+Plants+Flowers",
                    "content_section": "skill_levels",
                    "description": "Healthy plants and flowers"
                },
                {
                    "url": "https://placehold.co/1600x900/15803d/white?text=Gardening+Tools+Equipment",
                    "content_section": "training",
                    "description": "Gardening tools and equipment"
                }
            ],
            "hiking": [
                {
                    "url": "https://placehold.co/1600x900/a3e635/white?text=Mountain+Hiking+Trail",
                    "content_section": "header",
                    "description": "Mountain hiking trail"
                },
                {
                    "url": "https://placehold.co/1600x900/84cc16/white?text=Hiker+Mountain+Peak",
                    "content_section": "skill_levels",
                    "description": "Hiker on mountain peak"
                },
                {
                    "url": "https://placehold.co/1600x900/65a30d/white?text=Hiking+Group+Adventure",
                    "content_section": "training",
                    "description": "Hiking group adventure"
                }
            ],
            "backpacking": [
                {
                    "url": "https://placehold.co/1600x900/fbbf24/white?text=Backpacker+Gear",
                    "content_section": "header",
                    "description": "Backpacker with gear"
                },
                {
                    "url": "https://placehold.co/1600x900/f59e0b/white?text=Camping+in+Nature",
                    "content_section": "skill_levels",
                    "description": "Camping in nature"
                },
                {
                    "url": "https://placehold.co/1600x900/d97706/white?text=Outdoor+Adventure+Setup",
                    "content_section": "training",
                    "description": "Outdoor adventure setup"
                }
            ],
            "machine learning": [
                {
                    "url": "https://placehold.co/1600x900/6366f1/white?text=AI+Machine+Learning",
                    "content_section": "header",
                    "description": "AI and machine learning visualization"
                },
                {
                    "url": "https://placehold.co/1600x900/4f46e5/white?text=Technology+Data+Science",
                    "content_section": "skill_levels",
                    "description": "Technology and data science"
                },
                {
                    "url": "https://placehold.co/1600x900/4338ca/white?text=Code+Programming+Screen",
                    "content_section": "training",
                    "description": "Code and programming screen"
                }
            ],
            "prompt engineering": [
                {
                    "url": "https://placehold.co/1600x900/ec4899/white?text=AI+Chat+Interface",
                    "content_section": "header",
                    "description": "AI chat interface"
                },
                {
                    "url": "https://placehold.co/1600x900/db2777/white?text=Computer+Technology",
                    "content_section": "skill_levels",
                    "description": "Computer and technology"
                },
                {
                    "url": "https://placehold.co/1600x900/be185d/white?text=Abstract+Technology+Concept",
                    "content_section": "training",
                    "description": "Abstract technology concept"
                }
            ],
            "robotics": [
                {
                    "url": "https://placehold.co/1600x900/14b8a6/white?text=Advanced+Robot+Technology",
                    "content_section": "header",
                    "description": "Advanced robot technology"
                },
                {
                    "url": "https://placehold.co/1600x900/0d9488/white?text=Robotics+Automation",
                    "content_section": "skill_levels",
                    "description": "Robotics and automation"
                },
                {
                    "url": "https://placehold.co/1600x900/0f766e/white?text=AI+Robotics+Integration",
                    "content_section": "training",
                    "description": "AI and robotics integration"
                }
            ],
            "default": [
                {
                    "url": "https://placehold.co/1600x900/64748b/white?text=General+Activity+Sports",
                    "content_section": "header",
                    "description": "General activity and sports"
                },
                {
                    "url": "https://placehold.co/1600x900/475569/white?text=Active+Lifestyle+Fitness",
                    "content_section": "skill_levels",
                    "description": "Active lifestyle and fitness"
                },
                {
                    "url": "https://placehold.co/1600x900/334155/white?text=Achievement+Success",
                    "content_section": "training",
                    "description": "Achievement and success"
                }
            ]
        }
        
        # Get specific images for this hobby
        hobby_key = hobby_name.lower().replace(" ", "")
        if hobby_key in hobby_images:
            return hobby_images[hobby_key]
        else:
            return hobby_images["default"]
    
    def generate_image_prompt(self, hobby_category, content):
        """Generate a prompt for creating/retrieving hobby-related images"""
        if not self.client:
            return self._generate_fallback_image_prompt(hobby_category)
        
        try:
            prompt = f"""
            Create a detailed image prompt for a social media post about {hobby_category['name']}.
            
            Content: {content['title']}
            Description: {content['description']}
            
            Generate a detailed image description that would be perfect for social media,
            focusing on visual appeal and relevance to the hobby.
            """
            
            response = self.client.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    temperature=0.7
                )
            )
            
            return response.text
            
        except Exception as e:
            print(f"Image prompt generation failed: {e}")
            return self._generate_fallback_image_prompt(hobby_category)
    
    def _generate_fallback_image_prompt(self, hobby_category):
        """Fallback image prompt generation"""
        return f"Beautiful, engaging photo showing {hobby_category['name']} activity, high quality, social media ready"