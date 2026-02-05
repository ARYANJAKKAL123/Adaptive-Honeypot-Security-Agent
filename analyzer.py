SENSITIVE_KEYWORDS = [
    "password",
    "backup",
    "salary",
    "config",
    "admin",
    "secret"
]

def analyze_path(path):

    print("ANALYZER RECEIVED:", path)

    score = 0
    reason = "NORMAL"

    if ".." in path:
        score += 3
        reason = "TRAVERSAL_ATTEMPT"

    for word in SENSITIVE_KEYWORDS:
     print("Checking:", word, "against", path.lower())

     if word in path.lower():
        print("MATCHED WORD:", word)
        score += 2
        reason = "SENSITIVE_KEYWORD"

    return reason, score
