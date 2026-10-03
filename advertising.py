"""Hobby-related activity links system"""

import random

class AdvertisingGenerator:
    def __init__(self):
        self.activity_links = {
            "basketball": [
                {
                    "title": "Courts of the World",
                    "description": "Locate basketball courts with conditions, availability, lighting, and organized games.",
                    "link": "https://www.courtsoftheworld.com"
                },
                {
                    "title": "ILoveBasketballTV",
                    "description": "Basketball training programs. Shooting mechanics, ball handling, defensive strategies.",
                    "link": "https://www.youtube.com/c/ILoveBasketballTV"
                },
                {
                    "title": "Dick's Basketball Equipment",
                    "description": "Complete basketball equipment guide. Shoes, balls, training aids, apparel.",
                    "link": "https://www.dickssportinggoods.com/c/basketball"
                }
            ],
            "swimming": [
                {
                    "title": "USMS Pool Finder",
                    "description": "Discover swimming pools with lane availability, lap swim schedules, swim lessons.",
                    "link": "https://www.usms.org/pools"
                },
                {
                    "title": "Skills N Drills",
                    "description": "Professional swimming instruction. Stroke mechanics, breathing, starts and turns.",
                    "link": "https://www.youtube.com/user/SkillsNTDrills"
                },
                {
                    "title": "SwimOutlet",
                    "description": "Essential swimming equipment. Swimsuits, goggles, training tools, safety gear.",
                    "link": "https://www.swimoutlet.com"
                }
            ],
            "soccer": [
                {
                    "title": "US Club Soccer",
                    "description": "Find amateur soccer leagues in your area. Local leagues for all skill levels.",
                    "link": "https://www.usclubsoccer.org/find-a-club"
                },
                {
                    "title": "Online Soccer Academy",
                    "description": "Free professional training videos and drills. Ball control, shooting, tactics.",
                    "link": "https://www.youtube.com/c/OnlineSoccerAcademy"
                },
                {
                    "title": "Soccer.com Equipment Guide",
                    "description": "Complete guide to boots, balls, and gear. Playing surface and skill level advice.",
                    "link": "https://www.soccer.com/guide/equipment"
                }
            ],
            "cycling": [
                {
                    "title": "Strava Routes",
                    "description": "Discover bike paths and cycling routes with distance, elevation, and terrain details.",
                    "link": "https://www.strava.com/routes"
                },
                {
                    "title": "Cycling Meetup Groups",
                    "description": "Join local cycling groups and find riding partners. Group rides and advice.",
                    "link": "https://www.meetup.com/topics/cycling/"
                },
                {
                    "title": "Park Tool Company",
                    "description": "Learn bicycle maintenance and repair. From flat tires to complete overhauls.",
                    "link": "https://www.youtube.com/user/ParkToolCompany"
                }
            ],
            "tennis": [
                {
                    "title": "USTA Tennis Courts",
                    "description": "Locate tennis courts by surface type, lighting, and playing hours. All skill levels.",
                    "link": "https://www.ustanorcal.com/tennis/find-court"
                },
                {
                    "title": "Essential Tennis",
                    "description": "Free tennis lessons and technique videos. Strokes, footwork, strategies.",
                    "link": "https://www.youtube.com/user/essentialtennis"
                },
                {
                    "title": "Tennis Warehouse Guide",
                    "description": "Racket and gear selection guide. Playing style, skill level, physical characteristics.",
                    "link": "https://www.tennis-warehouse.com/learning_center/racquet_guide.html"
                }
            ],
            "photography": [
                {
                    "title": "Skillshare Photography",
                    "description": "Free and paid photography courses. Composition, lighting, editing techniques.",
                    "link": "https://www.skillshare.com/browse/photography"
                },
                {
                    "title": "500px Community",
                    "description": "Share photos and get feedback. Global community, themed challenges, critiques.",
                    "link": "https://www.500px.com"
                },
                {
                    "title": "DPReview Buying Guide",
                    "description": "Camera equipment guide. Models, lenses, accessories, expert recommendations.",
                    "link": "https://www.dpreview.com/buying-guides"
                }
            ],
            "hiking": [
                {
                    "title": "AllTrails",
                    "description": "Discover hiking trails with distance, elevation, difficulty, and user reviews.",
                    "link": "https://www.alltrails.com"
                },
                {
                    "title": "Hiking Meetup Groups",
                    "description": "Join local hiking groups and find adventure partners. Guides and hidden gems.",
                    "link": "https://www.meetup.com/topics/hiking/"
                },
                {
                    "title": "REI Hiking Gear Guide",
                    "description": "Essential hiking equipment and packing lists. Footwear, layers, navigation, safety.",
                    "link": "https://www.rei.com/learn/expert-advice/hiking-gear-checklist"
                }
            ],
            "bird watching": [
                {
                    "title": "Merlin Bird ID",
                    "description": "Identify birds by sight and sound. AI recognition, comprehensive databases.",
                    "link": "https://www.merlin.allaboutbirds.org"
                },
                {
                    "title": "Audubon Bird Guide",
                    "description": "Find bird watching spots near you. Species diversity, seasonal patterns, habitats.",
                    "link": "https://www.audubon.org/bird-a-z"
                },
                {
                    "title": "Bird Watching Daily",
                    "description": "Connect with local bird watching groups. Sightings, guided walks, citizen science.",
                    "link": "https://www.birdwatchingdaily.com/community"
                }
            ],
            "gardening": [
                {
                    "title": "Gardening Know How",
                    "description": "Complete guides for growing vegetables, flowers, herbs. Climate zones, soil types.",
                    "link": "https://www.gardeningknowhow.com"
                },
                {
                    "title": "RHS Plant Database",
                    "description": "Comprehensive plant database with care instructions. Visual identification tools.",
                    "link": "https://www.rhs.org.uk/plants"
                },
                {
                    "title": "Garden.org Forums",
                    "description": "Join gardening forums and share tips. Problem solving, seed exchanges, techniques.",
                    "link": "https://www.garden.org/forum"
                }
            ],
            "machine learning": [
                {
                    "title": "Coursera ML Courses",
                    "description": "Free ML courses from top universities. Fundamentals to advanced neural networks.",
                    "link": "https://www.coursera.org/browse/data-science/machine-learning"
                },
                {
                    "title": "Kaggle Datasets",
                    "description": "Download datasets to practice ML skills. Image recognition, NLP, finance, healthcare.",
                    "link": "https://www.kaggle.com/datasets"
                },
                {
                    "title": "Reddit Machine Learning",
                    "description": "Join ML community discussions. Research papers, code sharing, debugging help.",
                    "link": "https://www.reddit.com/r/MachineLearning"
                }
            ],
            "default": [
                {
                    "title": "Coursera",
                    "description": "Find comprehensive courses for your hobby. Beginner to advanced levels available.",
                    "link": "https://www.coursera.org"
                },
                {
                    "title": "Reddit",
                    "description": "Connect with enthusiastic hobbyists. Techniques, equipment, events discussions.",
                    "link": "https://www.reddit.com"
                },
                {
                    "title": "Amazon Reviews",
                    "description": "Read detailed equipment reviews. Match your skill level, budget, and needs.",
                    "link": "https://www.amazon.com"
                }
            ]
        }
    
    def generate_activity_link(self, hobby_name):
        """Generate real activity-related links for the hobby"""
        hobby_key = hobby_name.lower().replace(" ", "")
        
        if hobby_key in self.activity_links:
            activities = self.activity_links[hobby_key]
        else:
            activities = self.activity_links["default"]
        
        selected = random.choice(activities)
        
        return {
            "title": selected["title"],
            "description": selected["description"],
            "link": selected["link"],
            "type": "activity_link"
        }