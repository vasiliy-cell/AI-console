I've decided to make the CLI much more user-friendly by integrating AI.
From now on, you can simply describe what you want in plain English (or any natural language), 
and the AI-powered API will automatically convert it into the correct command. 


# Installation Guide

## 1. Create API Key
1. Go to: https://platform.deepseek.com/api_keys
2. Create an **API Key** (paid service, but affordable)

## 2. Configure API Key
1. Copy your **API Key**
2. Create directory: `.config/AICLI/`
3. Create file: `.config/AICLI/api_key.txt`
4. Paste your API key into the file

## ⚠️ Important Note
**File name matters!**  
If you want to use a different filename, you must also update:  
`AICLI_path` in `utils/config_loader.py`
