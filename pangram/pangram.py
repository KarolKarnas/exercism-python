import string

alphabet = list(string.ascii_lowercase)

def is_pangram(sentence: str):
    
    sentenceArr = list(sentence.lower().replace(' ',''))
    
    for letter in alphabet:
        if not letter in sentenceArr:
            return False
    
    return True