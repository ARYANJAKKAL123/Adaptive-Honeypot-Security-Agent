from dataclasses import dataclass
from datetime import datetime

@dataclass
class Decoy:
    """
    Represents a decoy file in the honeypot system
    This is a pure business entity with no external dependencies
    """
    decoy_type: str      # Type: "credential", "document", "config", etc.
    file_path: str       # Where the decoy is placed
    content: str         # The fake content inside the decoy
    created_at: datetime # When the decoy was created 