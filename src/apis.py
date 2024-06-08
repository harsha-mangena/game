from src.utils import get_word_info
from security import safe_requests

def get_random_word(length: int):
    response = safe_requests.get(f"https://random-word-api.vercel.app/api?words=1&length={length}")
    if response.status_code == 200:
        return response.json()[0].lower()
    else:
        return "hangman"  # Default word if API call fails
    
def get_word_definition(word):
    response = safe_requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word))
    if response.status_code == 404:
        return {}, False
    
    data = get_word_info(response.json())

    return data, True

def get_valid_word_with_definition(length: int):
    while True:
        word = get_random_word(length)
        word_data, success = get_word_definition(word)
        if success:
            return word_data
