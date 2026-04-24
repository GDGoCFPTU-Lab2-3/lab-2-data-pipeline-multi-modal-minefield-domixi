import pandas as pd

<<<<<<< HEAD
# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================
# Task: Process sales records, handling type traps and duplicates.

def process_sales_csv(file_path):
    # --- FILE READING (Handled for students) ---
    df = pd.read_csv(file_path)
    # ------------------------------------------
    
    # TODO: Remove duplicate rows based on 'id'
    # TODO: Clean 'price' column: convert "$1200", "250000", "five dollars" to floats
    # TODO: Normalize 'date_of_sale' into a single format (YYYY-MM-DD)
    # TODO: Return a list of dictionaries for the UnifiedDocument schema.
    
    return []

=======
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
>>>>>>> main
