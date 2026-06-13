"""
Uses Unsplash source API (no key needed) to get valid, working images.
https://source.unsplash.com is a redirect service that returns real images.
Run: python get_unsplash_ids.py
"""
import urllib.request
import urllib.parse
import json

# Unsplash source API - returns real images, no API key needed
# Format: https://source.unsplash.com/800x600/?{keyword}
# The redirect URL gives us the actual photo ID

queries = {
    "Rice":        "rice+paddy+field",
    "Maize":       "corn+maize+field",
    "Jute":        "jute+plant+green",
    "Cotton":      "cotton+field+farm",
    "Coconut":     "coconut+palm+tree",
    "Papaya":      "papaya+fruit+tree",
    "Orange":      "orange+fruit+citrus",
    "Apple":       "apple+red+fruit+orchard",
    "Muskmelon":   "cantaloupe+melon+fruit",
    "Watermelon":  "watermelon+farm+green",
    "Grapes":      "grapes+vineyard+bunch",
    "Mango":       "mango+fruit+tropical",
    "Banana":      "banana+plant+tropical",
    "Pomegranate": "pomegranate+red+fruit",
    "Lentil":      "lentil+legume+seeds",
    "Blackgram":   "black+lentil+dal",
    "Mungbean":    "mung+bean+green+sprout",
    "Mothbeans":   "moth+bean+legume",
    "Pigeonpeas":  "pigeon+pea+plant",
    "Kidneybeans": "kidney+bean+red",
    "Chickpea":    "chickpea+legume+seeds",
    "Coffee":      "coffee+plant+beans",
}

print("CROP_IMAGES = {")
for crop, query in queries.items():
    url = f"https://source.unsplash.com/800x600/?{query}"
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0'
        })
        resp = urllib.request.urlopen(req, timeout=15)
        final_url = resp.url
        # Extract just the photo ID part
        if "images.unsplash.com/photo-" in final_url:
            photo_part = final_url.split("images.unsplash.com/photo-")[1].split("?")[0]
            clean_url = f"https://images.unsplash.com/photo-{photo_part}?w=800&q=80"
            print(f'    "{crop}": "{clean_url}",')
        else:
            print(f'    # "{crop}": FAILED - got {final_url[:80]}')
    except Exception as e:
        print(f'    # "{crop}": ERROR - {e}')

print("}")
