#!/usr/bin/env python3
"""
Python version of the comprehensive breed database
Converted from breed-database.js for backend integration
"""

import math

BREED_DATABASE = {
    "buffalo": {
        "murrah": {
            "name": "Murrah",
            "origin": "India (Haryana)",
            "characteristics": {
                "color": "Jet black",
                "bodyType": "Heavy, compact body",
                "horns": "Short, tightly curled",
                "size": "Large",
                "weight": "Male: 500-600kg, Female: 400-500kg"
            },
            "colorProfile": {
                "black": 0.85,
                "gray": 0.10,
                "brown": 0.03,
                "white": 0.02
            },
            "milkProduction": "High (1500-2500 liters/lactation)",
            "temperament": "Docile, good for dairy",
            "distribution": "India, Pakistan, Bangladesh, Nepal"
        },
        "jaffarabadi": {
            "name": "Jaffarabadi",
            "origin": "India (Gujarat)",
            "characteristics": {
                "color": "Dark gray to black",
                "bodyType": "Massive, heavy build",
                "horns": "Long, curved downward",
                "size": "Very large",
                "weight": "Male: 600-800kg, Female: 500-600kg"
            },
            "colorProfile": {
                "black": 0.70,
                "gray": 0.25,
                "brown": 0.03,
                "white": 0.02
            },
            "milkProduction": "Very high (2000-3000 liters/lactation)",
            "temperament": "Calm, excellent dairy breed",
            "distribution": "India (Gujarat), Pakistan"
        },
        "surti": {
            "name": "Surti",
            "origin": "India (Gujarat)",
            "characteristics": {
                "color": "Light gray to dark gray",
                "bodyType": "Medium, well-proportioned",
                "horns": "Medium length, curved",
                "size": "Medium",
                "weight": "Male: 400-500kg, Female: 350-450kg"
            },
            "colorProfile": {
                "black": 0.20,
                "gray": 0.70,
                "brown": 0.05,
                "white": 0.05
            },
            "milkProduction": "Good (1200-1800 liters/lactation)",
            "temperament": "Gentle, easy to handle",
            "distribution": "India (Gujarat, Maharashtra)"
        },
        "mehsana": {
            "name": "Mehsana",
            "origin": "India (Gujarat)",
            "characteristics": {
                "color": "Black with white markings",
                "bodyType": "Medium to large",
                "horns": "Medium, curved",
                "size": "Medium-large",
                "weight": "Male: 450-550kg, Female: 400-500kg"
            },
            "colorProfile": {
                "black": 0.60,
                "gray": 0.20,
                "brown": 0.05,
                "white": 0.15
            },
            "milkProduction": "High (1500-2200 liters/lactation)",
            "temperament": "Docile, good milkers",
            "distribution": "India (Gujarat)"
        },
        "nili_ravi": {
            "name": "Nili-Ravi",
            "origin": "Pakistan (Punjab)",
            "characteristics": {
                "color": "Black with white markings",
                "bodyType": "Heavy, well-built",
                "horns": "Short, tightly curled",
                "size": "Large",
                "weight": "Male: 500-600kg, Female: 450-550kg"
            },
            "colorProfile": {
                "black": 0.70,
                "gray": 0.15,
                "brown": 0.05,
                "white": 0.10
            },
            "milkProduction": "Very high (1800-2500 liters/lactation)",
            "temperament": "Calm, excellent dairy",
            "distribution": "Pakistan, India (Punjab)"
        },
        "bhadawari": {
            "name": "Bhadawari",
            "origin": "India (Uttar Pradesh)",
            "characteristics": {
                "color": "Copper brown to dark brown",
                "bodyType": "Medium, compact",
                "horns": "Medium length",
                "size": "Medium",
                "weight": "Male: 400-500kg, Female: 350-450kg"
            },
            "colorProfile": {
                "black": 0.10,
                "gray": 0.20,
                "brown": 0.65,
                "white": 0.05
            },
            "milkProduction": "Good (1000-1500 liters/lactation)",
            "temperament": "Hardy, good for draught",
            "distribution": "India (Uttar Pradesh, Madhya Pradesh)"
        }
    },
    "cattle": {
        "holstein_friesian": {
            "name": "Holstein Friesian",
            "origin": "Netherlands/Germany",
            "characteristics": {
                "color": "Black and white spotted",
                "bodyType": "Large, angular",
                "horns": "Polled or horned",
                "size": "Very large",
                "weight": "Male: 700-900kg, Female: 500-700kg"
            },
            "colorProfile": {
                "black": 0.40,
                "gray": 0.05,
                "brown": 0.05,
                "white": 0.50
            },
            "milkProduction": "Very high (6000-8000 liters/lactation)",
            "temperament": "Docile, high milk producers",
            "distribution": "Worldwide (dairy industry)"
        },
        "jersey": {
            "name": "Jersey",
            "origin": "Jersey Island (UK)",
            "characteristics": {
                "color": "Light brown to dark brown",
                "bodyType": "Small, refined",
                "horns": "Small, curved",
                "size": "Small",
                "weight": "Male: 400-500kg, Female: 300-400kg"
            },
            "colorProfile": {
                "black": 0.05,
                "gray": 0.05,
                "brown": 0.85,
                "white": 0.05
            },
            "milkProduction": "High (4000-6000 liters/lactation)",
            "temperament": "Gentle, efficient milkers",
            "distribution": "Worldwide (dairy industry)"
        },
        "sahiwal": {
            "name": "Sahiwal",
            "origin": "Pakistan/India",
            "characteristics": {
                "color": "Red to dark red",
                "bodyType": "Medium to large",
                "horns": "Medium length",
                "size": "Medium-large",
                "weight": "Male: 500-600kg, Female: 400-500kg"
            },
            "colorProfile": {
                "black": 0.05,
                "gray": 0.05,
                "brown": 0.85,
                "white": 0.05
            },
            "milkProduction": "Good (2000-3000 liters/lactation)",
            "temperament": "Hardy, heat tolerant",
            "distribution": "India, Pakistan, Bangladesh"
        },
        "gir": {
            "name": "Gir",
            "origin": "India (Gujarat)",
            "characteristics": {
                "color": "Red to dark red with white spots",
                "bodyType": "Large, well-built",
                "horns": "Long, curved",
                "size": "Large",
                "weight": "Male: 500-600kg, Female: 400-500kg"
            },
            "colorProfile": {
                "black": 0.05,
                "gray": 0.05,
                "brown": 0.70,
                "white": 0.20
            },
            "milkProduction": "Good (2000-3000 liters/lactation)",
            "temperament": "Docile, good milkers",
            "distribution": "India (Gujarat, Rajasthan)"
        },
        "red_sindhi": {
            "name": "Red Sindhi",
            "origin": "Pakistan (Sindh)",
            "characteristics": {
                "color": "Deep red",
                "bodyType": "Medium, compact",
                "horns": "Medium length",
                "size": "Medium",
                "weight": "Male: 400-500kg, Female: 300-400kg"
            },
            "colorProfile": {
                "black": 0.05,
                "gray": 0.05,
                "brown": 0.85,
                "white": 0.05
            },
            "milkProduction": "Good (1500-2500 liters/lactation)",
            "temperament": "Hardy, heat tolerant",
            "distribution": "Pakistan, India, Bangladesh"
        },
        "tharparkar": {
            "name": "Tharparkar",
            "origin": "India (Rajasthan)",
            "characteristics": {
                "color": "White to light gray",
                "bodyType": "Medium to large",
                "horns": "Medium length",
                "size": "Medium-large",
                "weight": "Male: 450-550kg, Female: 350-450kg"
            },
            "colorProfile": {
                "black": 0.05,
                "gray": 0.20,
                "brown": 0.10,
                "white": 0.65
            },
            "milkProduction": "Good (1500-2500 liters/lactation)",
            "temperament": "Hardy, drought resistant",
            "distribution": "India (Rajasthan, Gujarat)"
        }
    }
}

def analyze_image_color_profile(image):
    """
    Analyze image to extract color profile for breed matching
    Returns dictionary with color percentages
    """
    import cv2
    import numpy as np
    
    # Convert to RGB if needed
    if len(image.shape) == 3 and image.shape[2] == 3:
        rgb_image = image
    else:
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Resize for consistent analysis
    rgb_image = cv2.resize(rgb_image, (224, 224))
    
    # Convert to HSV for better color analysis
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    
    # Define color ranges in HSV
    color_ranges = {
        'black': [(0, 0, 0), (180, 255, 50)],      # Very dark colors
        'white': [(0, 0, 200), (180, 30, 255)],   # Very light colors
        'brown': [(10, 50, 20), (20, 255, 200)],  # Brown/red range
        'gray': [(0, 0, 50), (180, 30, 200)]      # Gray range
    }
    
    total_pixels = rgb_image.shape[0] * rgb_image.shape[1]
    color_profile = {}
    
    for color_name, (lower, upper) in color_ranges.items():
        lower = np.array(lower)
        upper = np.array(upper)
        mask = cv2.inRange(hsv_image, lower, upper)
        pixel_count = np.sum(mask > 0)
        color_profile[color_name] = pixel_count / total_pixels
    
    # Normalize to ensure sum is 1.0
    total = sum(color_profile.values())
    if total > 0:
        color_profile = {k: v/total for k, v in color_profile.items()}
    else:
        # Fallback if no colors detected
        color_profile = {'black': 0.25, 'white': 0.25, 'brown': 0.25, 'gray': 0.25}
    
    return color_profile

def calculate_breed_match_score(breed_profile, image_profile):
    """Calculate similarity score between breed and image color profiles"""
    score = 0
    colors = ['black', 'gray', 'brown', 'white']
    
    for color in colors:
        breed_value = breed_profile.get(color, 0)
        image_value = image_profile.get(color, 0)
        # Calculate similarity (1 - absolute difference)
        similarity = 1 - abs(breed_value - image_value)
        score += similarity * (breed_value + image_value) / 2  # Weight by expected presence
    
    return min(score / len(colors), 1)  # Normalize to 0-1

def find_best_matching_breed(animal_type, image_color_profile):
    """
    Find the best matching breed based on color profile analysis
    """
    breeds = BREED_DATABASE.get(animal_type.lower(), {})
    if not breeds:
        return {"breed": "Unknown", "confidence": 0, "details": None}
    
    best_match = {"breed": "Unknown", "confidence": 0, "details": None}
    best_score = 0
    
    for breed_key, breed_data in breeds.items():
        score = calculate_breed_match_score(breed_data["colorProfile"], image_color_profile)
        if score > best_score:
            best_score = score
            best_match = {
                "breed": breed_data["name"],
                "confidence": round(score * 100),
                "details": breed_data
            }
    
    # Only return a breed if confidence is above threshold
    if best_match["confidence"] < 40:  # Lower threshold for better results
        return {"breed": "Unknown", "confidence": 0, "details": None}
    
    return best_match

def get_breed_information(breed_name, animal_type):
    """Get detailed information about a specific breed"""
    breeds = BREED_DATABASE.get(animal_type.lower(), {})
    
    # First try to match by breed key (URL parameter)
    if breed_name.lower() in breeds:
        return breeds[breed_name.lower()]
    
    # If not found by key, try to match by breed name
    for breed_key, breed_data in breeds.items():
        if breed_data["name"].lower() == breed_name.lower():
            return breed_data
    
    return None

def get_all_breeds(animal_type):
    """Get all breeds for a specific animal type"""
    return BREED_DATABASE.get(animal_type.lower(), {})

def get_breed_statistics():
    """Get statistics about the breed database"""
    buffalo_count = len(BREED_DATABASE.get("buffalo", {}))
    cattle_count = len(BREED_DATABASE.get("cattle", {}))
    
    return {
        "buffalo": buffalo_count,
        "cattle": cattle_count,
        "total": buffalo_count + cattle_count
    }