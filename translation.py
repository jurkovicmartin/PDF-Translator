
import deepl
from dotenv import load_dotenv, find_dotenv
import os
from tkinter import messagebox

def load_auth_key() -> str:
    # Specified path bcs automatic finding (even find_dotenv) could not find the .env file
    load_dotenv("res/env/key.env")
    api_key = os.getenv("API_KEY")
    
    if api_key is None or api_key == "your_deepl_api_key":
        messagebox.showerror("API key error", "Unable to load your DeepL API key. Check key.env file.")
    else:
        return api_key


def translation(auth_key: str, language: str, text: list[str]) -> list[str]:
    """
    Returns None if translation was not successful.
    
    Parameters
    -----
    language: language DeepL specified code
    """
    
    translator = deepl.Translator(auth_key)

    try:
        return translator.translate_text(text, target_lang=language)
    except Exception:
        messagebox.showerror("Connection error", "Connection error.")
        return None
    