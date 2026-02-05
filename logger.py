import json
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "access_log.json"

def log_event(ip, path, reason="NORMAL"):

    entry = {
        "timestamp": datetime.now().isoformat(),
        "ip": ip,
        "path": path,
        "reason": reason
    }

    if LOG_FILE.exists():
        data = json.loads(LOG_FILE.read_text())
    else:
        data = []

    data.append(entry)

    LOG_FILE.write_text(json.dumps(data, indent=2))
