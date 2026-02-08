import re

def clean_text_for_speech(text: str) -> str:
    """
    Removes markdown formatting and special characters to make text more suitable for TTS.
    """
    # Remove bold/italic markers (* or _)
    text = re.sub(r'[\*_]{1,3}', '', text)
    
    # Remove code blocks or inline code (backticks)
    text = re.sub(r'`', '', text)
    
    # Remove links [text](url) -> text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # Remove headings (hashes)
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
    
    # Remove bullet points (at start of line)
    text = re.sub(r'^\s*[-*+]\s+', '', text, flags=re.MULTILINE)
    
    return text.strip()
