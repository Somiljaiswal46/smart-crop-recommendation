import urllib.request
import urllib.parse
import json
import os
import time

# Complete Wikipedia page titles for all 22 crops (highly accurate, verified)
CROP_WIKI = {
    "rice":        "Rice",
    "maize":       "Maize",
    "jute":        "Jute",
    "cotton":      "Cotton",
    "coconut":     "Coconut",
    "papaya":      "Papaya",
    "orange":      "Orange_(fruit)",
    "apple":       "Apple",
    "muskmelon":   "Cantaloupe",
    "watermelon":  "Watermelon",
    "grapes":      "Grape",
    "mango":       "Mango",
    "banana":      "Cavendish_banana",
    "pomegranate": "Pomegranate",
    "lentil":      "Lentil",
    "blackgram":   "Vigna_mungo",
    "mungbean":    "Mung_bean",
    "mothbeans":   "Moth_bean",
    "pigeonpeas":  "Pigeon_pea",
    "kidneybeans": "Kidney_bean",
    "chickpea":    "Chickpea",
    "coffee":      "Coffee",
}

save_dir = os.path.join("static", "crops")
os.makedirs(save_dir, exist_ok=True)

# Compliant header for the Wikipedia API
headers_api = {
    'User-Agent': 'CropRecommendationEngine/1.1 (contact: student@example.com) Python-urllib/3.13',
    'Accept': 'application/json'
}

# Browser header for download from upload.wikimedia.org
headers_img = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def get_wiki_image_url(page_title):
    encoded = urllib.parse.quote(page_title)
    api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded}"
    req = urllib.request.Request(api_url, headers=headers_api)
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode())
    
    # We want high-definition (HD) originalimage first
    if 'originalimage' in data:
        return data['originalimage']['source']
    if 'thumbnail' in data:
        return data['thumbnail']['source']
    return None

print("Downloading high-definition HD crop images from Wikipedia...")
success = 0
failed = []

for crop, wiki_title in CROP_WIKI.items():
    save_path = os.path.join(save_dir, f"{crop}.jpg")
    print(f"\nProcessing: {crop} ({wiki_title})...")
    
    # We will overwrite existing files to ensure we get the high-resolution versions
    try:
        # Step 1: Query API to get direct image source URL
        img_url = get_wiki_image_url(wiki_title)
        if not img_url:
            print(f"  [FAIL] {crop}: No image URL found in API")
            failed.append(crop)
            continue
            
        print(f"  Found URL: {img_url}")
        
        # Step 2: Download high-resolution image using browser headers
        img_req = urllib.request.Request(img_url, headers=headers_img)
        with urllib.request.urlopen(img_req, timeout=20) as img_resp:
            data = img_resp.read()
            
        # Verify download size is substantial (not a broken response)
        if len(data) < 5000:
            print(f"  [WARNING] {crop} image size is too small ({len(data)} bytes), retrying as thumbnail...")
            # If original was tiny or blocked, try requesting thumbnail which is cached
            raise Exception("Tiny image")

        ext = ".jpg"
        if img_url.lower().endswith(".png"):
            ext = ".png"
            
        actual_path = os.path.join(save_dir, f"{crop}{ext}")
        with open(actual_path, 'wb') as f:
            f.write(data)
            
        # Copy to .jpg format for consistent backend routing
        if ext != ".jpg":
            import shutil
            shutil.copy(actual_path, save_path)
            
        print(f"  [OK] Saved {crop}{ext} ({len(data)//1024} KB)")
        success += 1
        
    except Exception as e:
        # Retry with thumbnail specifically if original failed (some original pages have rate limits)
        print(f"  [RETRYING AS THUMBNAIL] {crop} due to: {e}")
        try:
            # Re-fetch summary to extract thumbnail
            encoded = urllib.parse.quote(wiki_title)
            api_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded}"
            req = urllib.request.Request(api_url, headers=headers_api)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode())
            
            if 'thumbnail' in data:
                img_url = data['thumbnail']['source']
                # If it's a small thumbnail (e.g. 320px), let's boost it to 640px for decent quality
                if "/thumb/" in img_url and img_url.split("/")[-1].startswith("320px-"):
                    parts = img_url.split("/")
                    filename = parts[-1]
                    parts[-1] = filename.replace("320px-", "640px-")
                    img_url = "/".join(parts)
                elif "/thumb/" in img_url and img_url.split("/")[-1].startswith("220px-"):
                    parts = img_url.split("/")
                    filename = parts[-1]
                    parts[-1] = filename.replace("220px-", "640px-")
                    img_url = "/".join(parts)
                
                print(f"  Retrying with thumbnail URL: {img_url}")
                img_req = urllib.request.Request(img_url, headers=headers_img)
                with urllib.request.urlopen(img_req, timeout=20) as img_resp:
                    data = img_resp.read()
                
                ext = ".jpg"
                if img_url.lower().endswith(".png"):
                    ext = ".png"
                
                actual_path = os.path.join(save_dir, f"{crop}{ext}")
                with open(actual_path, 'wb') as f:
                    f.write(data)
                
                if ext != ".jpg":
                    import shutil
                    shutil.copy(actual_path, save_path)
                
                print(f"  [OK] Saved {crop}{ext} ({len(data)//1024} KB) from thumbnail source")
                success += 1
            else:
                print(f"  [FAIL] {crop}: No thumbnail source available")
                failed.append(crop)
        except Exception as err:
            print(f"  [FAIL] {crop} retry failed: {err}")
            failed.append(crop)
            
    # Polite sleep delay of 3.5 seconds to prevent rate limits entirely
    time.sleep(3.5)

print(f"\nCompleted! {success}/22 crop images downloaded successfully.")
if failed:
    print(f"Failed classes: {failed}")
