class ConfigError(Exception):
    pass    

def load_api_key() -> str:
    filename = "api_key.txt"  # файл в той же директории
    
    # 1. Проверка существования файла и чтение
    try:
        with open(filename, "r", encoding="utf-8") as f:
            api_key = f.readline().strip()
    except FileNotFoundError:
        raise ConfigError(f"API key file not found: {filename}")
    except OSError as e:
        raise ConfigError(f"Failed to read API key file: {e}")
    
    # 2. Проверка на пустой ключ
    if not api_key:
        raise ConfigError("API key is empty or contains only whitespace")
    
    return api_key
