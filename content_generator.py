"""AI-powered content generation for hobby posts"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class ContentGenerator:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.model = os.getenv("AI_MODEL", "gpt-4")
        self.client = OpenAI(api_key=self.api_key) if self.api_key else None
    
    def generate_hobby_content(self, hobby_category):
        """Generate interesting content about a specific hobby"""
        if not self.client:
            return self._generate_fallback_content(hobby_category)
        
        try:
            prompt = f"""
            Generate an interesting, engaging post about {hobby_category['name']} as a hobby.
            
            Category: {hobby_category['name']}
            Description: {hobby_category['description']}
            Keywords: {', '.join(hobby_category['keywords'])}
            
            Create content that includes:
            1. A catchy title (under 60 characters)
            2. An engaging description (2-3 sentences, conversational tone)
            3. An interesting fact or tip about this hobby
            4. A call-to-action for engagement
            
            Format as JSON with keys: title, description, fact, call_to_action
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an engaging social media content creator specializing in hobbies and interests."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                response_format={"type": "json_object"}
            )
            
            import json
            content = json.loads(response.choices[0].message.content)
            return content
            
        except Exception as e:
            print(f"AI generation failed: {e}")
            return self._generate_fallback_content(hobby_category)
    
    def _generate_fallback_content(self, hobby_category):
        """Fallback content generation when AI is unavailable"""
        import random
        
        titles = [
            f"Discover {hobby_category['name']} Today!",
            f"Why {hobby_category['name']} is Amazing",
            f"Start Your {hobby_category['name']} Journey",
            f"{hobby_category['name']}: A New Adventure"
        ]
        
        descriptions = [
            f"Explore the exciting world of {hobby_category['name']} and discover new passions.",
            f"{hobby_category['description']} - it's easier to start than you think!",
            f"Join thousands of enthusiasts who love {hobby_category['name'].lower()}."
        ]
        
        facts = [
            f"Did you know? {hobby_category['name']} has been growing in popularity worldwide!",
            f"Studies show that {hobby_category['name'].lower()} can improve your well-being.",
            f"New research reveals surprising benefits of {hobby_category['name'].lower()}."
        ]
        
        return {
            "title": random.choice(titles),
            "description": random.choice(descriptions),
            "fact": random.choice(facts),
            "call_to_action": "What's your experience with this? Share in the comments!"
        }
    
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
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert at creating detailed image prompts for social media."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            print(f"Image prompt generation failed: {e}")
            return self._generate_fallback_image_prompt(hobby_category)
    
    def _generate_fallback_image_prompt(self, hobby_category):
        """Fallback image prompt generation"""
        return f"Beautiful, engaging photo showing {hobby_category['name']} activity, high quality, social media ready"