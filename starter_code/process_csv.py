import pandas as pd

def process_sales_csv(file_path):
    df = pd.read_csv(file_path)
    df = df.drop_duplicates(subset=['id'], keep='first')
    
    df['price'] = df['price'].astype(str).str.replace(r'[^\d\.]', '', regex=True)
    df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0.0)
    
    df['date_of_sale'] = pd.to_datetime(df['date_of_sale'], errors='coerce').dt.strftime('%Y-%m-%d')
    df['date_of_sale'] = df['date_of_sale'].fillna('')
    
    results = []
    for _, row in df.iterrows():
        meta = row.to_dict()
        results.append({
            "document_id": str(meta.get('id', '')),
            "content": f"CSV Record ID: {meta.get('id', '')}",
            "source_type": "CSV",
            "author": None,
            "timestamp": None,
            "source_metadata": meta
        })
        
    return results
