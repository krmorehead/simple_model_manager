from typing import Dict, List

# Two-digit language code to language name mapping
LANGUAGE_CODES: Dict[str, str] = {
    'en': 'English',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'zh': 'Chinese',
    'ja': 'Japanese',
    'ru': 'Russian',
    'ar': 'Arabic',
    'pt': 'Portuguese',
    'it': 'Italian',
    # Add more as needed
}

def is_valid_language_code(code: str) -> bool:
    """
    Validates if the provided code is a supported two-digit language code.
    Args:
        code (str): The language code to validate.
    Returns:
        bool: True if valid, False otherwise.
    """
    return code in LANGUAGE_CODES

def get_supported_languages() -> List[str]:
    """
    Returns a list of supported two-digit language codes.
    Returns:
        List[str]: Supported language codes.
    """
    return list(LANGUAGE_CODES.keys())

def get_language_name(code: str) -> str:
    """
    Returns the language name for a given code, or an empty string if not found.
    Args:
        code (str): The language code.
    Returns:
        str: The language name or empty string.
    """
    return LANGUAGE_CODES.get(code, "") 