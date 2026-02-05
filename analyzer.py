SENSITIVE_KEYWORDS = [
    
    "Password",
    "backup",
    "salary",
    "config",
    "admin",
    "secret"
]

def analyze_path(path):
    if ".." in path:
        return "TRAVERSAL_ATTEMPT"
    
    for word in SENSITIVE_KEYWORDS:
        if word in path:
            return "SENSITIVE_KEYWORDS"
        
    return "NORMAL"    
        
     