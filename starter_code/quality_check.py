# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================
# Task: Implement quality gates to reject corrupt data or logic discrepancies.

def run_quality_gate(document_dict):
    # TODO: Reject documents with 'content' length < 20 characters
    # TODO: Reject documents containing toxic/error strings (e.g., 'Null pointer exception')
    # TODO: Flag discrepancies (e.g., if tax calculation comment says 8% but code says 10%)
    
    # Return True if pass, False if fail.
<<<<<<< HEAD
=======
    if len(document_dict.get('content', '')) < 20:
        print("Quality Gate Failed: Content length is less than 20 characters.")
        return False
    if 'Null pointer exception' in document_dict.get('content', ''):
        print("Quality Gate Failed: Document contains toxic/error string 'Null pointer exception'.")
        return False
    if 'Invalid input' in document_dict.get('content', ''):
        print("Quality Gate Failed: Document contains toxic/error string 'Invalid input'.")
        return False
    if 'Tax calculation error' in document_dict.get('content', ''):
        print("Quality Gate Failed: Document contains toxic/error string 'Tax calculation error'.")
        return False
>>>>>>> main
    
    return True
