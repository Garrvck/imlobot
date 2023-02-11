from data.uzwords import words
from difflib import get_close_matches


def checkWords(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False  # bunday soz mavjud emas

    if word in matches:
        available = True
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words))
    elif 'к' in word:
        word = word.replace('к', 'қ')
        matches.update(get_close_matches(word, words))

    return {'available': available, 'matches': matches}
