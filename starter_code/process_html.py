from bs4 import BeautifulSoup

def parse_html_catalog(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    results = []
    table = soup.find('table', id='main-catalog')
    if not table:
        return results
        
    headers = [th.get_text(strip=True) for th in table.find_all('th')]
    
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        if not cols:
            continue
            
        row_dict = {}
        for idx, col in enumerate(cols):
            key = headers[idx] if idx < len(headers) else f"col_{idx}"
            val = col.get_text(strip=True)
            
            if key.lower() in ['price', 'giá']:
                if val.lower() in ['n/a', 'liên hệ']:
                    val = 0.0
                else:
                    clean_val = ''.join(c for c in val if c.isdigit() or c == '.')
                    try:
                        val = float(clean_val) if clean_val else 0.0
                    except ValueError:
                        val = 0.0
            
            row_dict[key] = val
        
        doc_id = row_dict.get('id', row_dict.get('ID', ''))
        results.append({
            "document_id": str(doc_id),
            "content": " | ".join(f"{k}: {v}" for k, v in row_dict.items()),
            "source_type": "HTML",
            "author": None,
            "timestamp": None,
            "source_metadata": row_dict
        })
        
    return results
