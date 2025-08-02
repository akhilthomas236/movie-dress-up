#!/usr/bin/env python3
"""
Script to update placeholder image URLs with actual fashion/costume images
"""

import pandas as pd
import random

# Fashion and costume image URLs from Unsplash (free to use)
FASHION_IMAGES = [
    "https://images.unsplash.com/photo-1490114538077-0a7f8cb49891?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1485462537746-965f33f7f6a7?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1581044777550-4cfa60707c03?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1594736797933-d0501ba2fe65?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1520637836862-4d197d17c35a?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1544966503-7cc5ac882d5d?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1585996038682-eb4821e5fe14?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1506629905057-8b9741ca9c5d?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1463453091185-61582044d556?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1541216970279-affbfdd55aa8?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1502323777036-f29e3972d82f?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1500917293891-ef795e70e1f6?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1489424731084-a5d8b219a5bb?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=300&h=400&fit=crop&crop=face",
    "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=300&h=400&fit=crop&crop=face",
]

# Theme-specific image URLs
THEME_SPECIFIC_IMAGES = {
    "Sports Monday": [
        "https://images.unsplash.com/photo-1544966503-7cc5ac882d5d?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1506629905057-8b9741ca9c5d?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1463453091185-61582044d556?w=300&h=400&fit=crop&crop=face",
    ],
    "Wedding Tuesday": [
        "https://images.unsplash.com/photo-1583391733956-6c78276477e1?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1585996038682-eb4821e5fe14?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1594736797933-d0501ba2fe65?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1517841905240-472988babdf9?w=300&h=400&fit=crop&crop=face",
    ],
    "Formal Wednesday": [
        "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1520637836862-4d197d17c35a?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=300&h=400&fit=crop&crop=face",
    ],
    "Movie Thursday": [
        "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1490114538077-0a7f8cb49891?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1485462537746-965f33f7f6a7?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1469334031218-e382a71b716b?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1581044777550-4cfa60707c03?w=300&h=400&fit=crop&crop=face",
    ],
    "Retro Friday": [
        "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1502323777036-f29e3972d82f?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1500917293891-ef795e70e1f6?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=300&h=400&fit=crop&crop=face",
        "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=300&h=400&fit=crop&crop=face",
    ]
}

def update_image_urls():
    """Update all placeholder image URLs with actual fashion images"""
    try:
        # Read the CSV file
        df = pd.read_csv('data/costumes.csv')
        
        print(f"Found {len(df)} costume entries to update")
        
        # Update each row that has a placeholder URL
        for index, row in df.iterrows():
            if 'placeholder.com' in str(row['image_url']):
                theme = row['theme_day']
                
                # Use theme-specific images if available, otherwise use general fashion images
                if theme in THEME_SPECIFIC_IMAGES:
                    new_url = random.choice(THEME_SPECIFIC_IMAGES[theme])
                else:
                    new_url = random.choice(FASHION_IMAGES)
                
                df.at[index, 'image_url'] = new_url
                print(f"Updated {row['character_name']} ({row['actor_name']}) - {theme}")
        
        # Save the updated CSV
        df.to_csv('data/costumes.csv', index=False)
        print(f"\nSuccessfully updated all image URLs!")
        print(f"Saved to data/costumes.csv")
        
    except Exception as e:
        print(f"Error updating image URLs: {e}")

if __name__ == "__main__":
    update_image_urls()
