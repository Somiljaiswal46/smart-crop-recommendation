import json

def fix_notebook(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            new_source = []
            for line in cell['source']:
                # 1. Fix distplot deprecation
                line = line.replace('sns.distplot', 'sns.histplot')
                
                # 2. Fix dropna
                if 'pd.read_csv("Crop_recommendation.csv")' in line:
                    line = line.replace('pd.read_csv("Crop_recommendation.csv")', 'pd.read_csv("Crop_recommendation.csv")\ncrop.dropna(inplace=True)')
                
                # 3. Idempotent mapping
                if "crop['label'] = crop['label'].map(crop_dict)" in line:
                    line = "if crop['label'].dtype == 'object':\n    crop['label'] = crop['label'].map(crop_dict)\n"
                
                # 4. Fix recommendation function
                if 'mx.fit_transform(features)' in line:
                    line = line.replace('mx.fit_transform(features)', 'mx.transform(features)')
                
                # 5. Fix features as DataFrame to avoid UserWarning
                if 'features = np.array([[N,P,K,temperature,humidity,ph,rainfall]])' in line:
                    line = line.replace('features = np.array([[N,P,K,temperature,humidity,ph,rainfall]])', 
                                        "features = pd.DataFrame([[N,P,K,temperature,humidity,ph,rainfall]], columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])")
                
                new_source.append(line)
            cell['source'] = new_source
            
            # Clear output for recommendation test to reset visual state
            if any('recommendation(N,P,K,temperature,humidity,ph,rainfall)' in line for line in new_source):
                cell['outputs'] = []

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

fix_notebook('Crop Recommendation Using Machine Learning.ipynb')
