from pathlib import Path
import stat
from typing import Optional

AICLI_path = Path.home() / ".config" / "AICLI" / "api_key.txt"

class ConfigError(Exception):
    pass    


def load_api_key() -> str:

    # 1. is there such

    if not AICLI_path.exists():
        raise ConfigError("API key file not found: {AICLI_path}")
    
    # 2. reading file
    try:
        with AICLI_path.open(mode='r', encoding='utf-8') as f:
            api_key = f.readline().strip()
    except OSError as e:
        raise ConfigError(f"Failed to read API key file: {e}")
    
    if not api_key: 
        raise ConfigError("API key is empty or contains only whitespace")
    
    return api_key

