/**
 * India Map Data and Crop Cultivation Zones
 * Contains production data for 22 crops.
 * GeoJSON is loaded separately for Leaflet rendering.
 */

const cultivationZones = {
    "Rice": {
        high: ["West Bengal", "Uttar Pradesh", "Punjab", "Andhra Pradesh", "Odisha", "Telangana"],
        moderate: ["Chhattisgarh", "Bihar", "Tamil Nadu", "Assam", "Haryana"],
        low: ["Others"]
    },
    "Maize": {
        high: ["Karnataka", "Madhya Pradesh", "Maharashtra", "Telangana", "Bihar"],
        moderate: ["Rajasthan", "Andhra Pradesh", "Uttar Pradesh", "Gujarat"],
        low: ["Others"]
    },
    "Chickpea": {
        high: ["Madhya Pradesh", "Maharashtra", "Rajasthan", "Gujarat", "Karnataka"],
        moderate: ["Uttar Pradesh", "Andhra Pradesh", "Telangana"],
        low: ["Others"]
    },
    "Kidneybeans": {
        high: ["Himachal Pradesh", "Uttarakhand", "Jammu and Kashmir"],
        moderate: ["Punjab", "Haryana", "Uttar Pradesh"],
        low: ["Others"]
    },
    "Pigeonpeas": {
        high: ["Maharashtra", "Karnataka", "Madhya Pradesh", "Gujarat", "Telangana"],
        moderate: ["Uttar Pradesh", "Andhra Pradesh", "Odisha"],
        low: ["Others"]
    },
    "Mothbeans": {
        high: ["Rajasthan"],
        moderate: ["Gujarat", "Maharashtra", "Haryana"],
        low: ["Others"]
    },
    "Mungbean": {
        high: ["Rajasthan", "Maharashtra", "Karnataka", "Andhra Pradesh"],
        moderate: ["Gujarat", "Tamil Nadu", "Odisha", "Bihar"],
        low: ["Others"]
    },
    "Blackgram": {
        high: ["Madhya Pradesh", "Maharashtra", "Andhra Pradesh", "Uttar Pradesh"],
        moderate: ["Tamil Nadu", "Gujarat", "Karnataka", "Rajasthan"],
        low: ["Others"]
    },
    "Lentil": {
        high: ["Uttar Pradesh", "Madhya Pradesh", "Bihar", "West Bengal"],
        moderate: ["Rajasthan", "Assam", "Haryana"],
        low: ["Others"]
    },
    "Pomegranate": {
        high: ["Maharashtra", "Karnataka", "Gujarat"],
        moderate: ["Andhra Pradesh", "Tamil Nadu", "Rajasthan"],
        low: ["Others"]
    },
    "Banana": {
        high: ["Andhra Pradesh", "Gujarat", "Maharashtra", "Tamil Nadu", "Karnataka"],
        moderate: ["Kerala", "Bihar", "West Bengal", "Uttar Pradesh"],
        low: ["Others"]
    },
    "Mango": {
        high: ["Uttar Pradesh", "Andhra Pradesh", "Karnataka", "Bihar", "Gujarat"],
        moderate: ["Maharashtra", "Tamil Nadu", "West Bengal", "Odisha", "Telangana"],
        low: ["Others"]
    },
    "Grapes": {
        high: ["Maharashtra", "Karnataka"],
        moderate: ["Tamil Nadu", "Andhra Pradesh", "Punjab", "Haryana"],
        low: ["Others"]
    },
    "Watermelon": {
        high: ["Uttar Pradesh", "Andhra Pradesh", "Tamil Nadu", "Karnataka", "Maharashtra"],
        moderate: ["Gujarat", "Rajasthan", "Punjab", "West Bengal"],
        low: ["Others"]
    },
    "Muskmelon": {
        high: ["Uttar Pradesh", "Punjab", "Haryana", "Maharashtra"],
        moderate: ["Rajasthan", "Andhra Pradesh", "Gujarat", "Tamil Nadu"],
        low: ["Others"]
    },
    "Apple": {
        high: ["Jammu and Kashmir", "Himachal Pradesh"],
        moderate: ["Uttarakhand"],
        low: ["Others"]
    },
    "Orange": {
        high: ["Maharashtra", "Madhya Pradesh", "Punjab", "Rajasthan"],
        moderate: ["Andhra Pradesh", "Telangana", "Karnataka"],
        low: ["Others"]
    },
    "Papaya": {
        high: ["Andhra Pradesh", "Gujarat", "Maharashtra", "Madhya Pradesh"],
        moderate: ["Karnataka", "West Bengal", "Assam"],
        low: ["Others"]
    },
    "Coconut": {
        high: ["Kerala", "Tamil Nadu", "Karnataka", "Andhra Pradesh"],
        moderate: ["West Bengal", "Odisha", "Gujarat"],
        low: ["Others"]
    },
    "Cotton": {
        high: ["Gujarat", "Maharashtra", "Telangana", "Rajasthan", "Karnataka"],
        moderate: ["Andhra Pradesh", "Haryana", "Punjab", "Madhya Pradesh"],
        low: ["Others"]
    },
    "Jute": {
        high: ["West Bengal", "Bihar", "Assam"],
        moderate: ["Odisha", "Meghalaya"],
        low: ["Others"]
    },
    "Coffee": {
        high: ["Karnataka", "Kerala"],
        moderate: ["Tamil Nadu", "Andhra Pradesh", "Odisha"],
        low: ["Others"]
    }
};

window.indiaMapData = {
    zones: cultivationZones
};
