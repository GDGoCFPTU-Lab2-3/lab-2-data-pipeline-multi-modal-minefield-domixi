import re

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================
# Task: Clean the transcript text and extract key information.

def clean_transcript(file_path):
    # --- FILE READING (Handled for students) ---
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # ------------------------------------------
    
    # TODO: Remove noise tokens like [Music], [inaudible], [Laughter]
    text = re.sub(r'\[.*?\]', '', text)
    
    # TODO: Strip timestamps [00:00:00]
    text = re.sub(r'\[\d{2}:\d{2}:\d{2}\]', '', text)
    # TODO: Find the price mentioned in Vietnamese words ("năm trăm nghìn")
    price_pattern = r'(\b\d+\s*(?:nghìn|triệu|tỷ)\b|\b(?:một|hai|ba|bốn|năm|sáu|bảy|tám|chín)\s*(?:nghìn|triệu|tỷ)\b)'
    price_match = re.search(price_pattern, text, re.IGNORECASE)
    # TODO: Return a cleaned dictionary for the UnifiedDocument schema.
    
    return {price_match.group(0).strip() if price_match else None}

