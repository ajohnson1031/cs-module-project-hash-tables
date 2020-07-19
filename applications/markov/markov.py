import random, re

#important variables
cache = {}
paragraph = ""
TGREEN =  '\033[32m'
ENDC = '\033[m'

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    
# TODO: analyze which words can follow other words
# Your code here

#converts text into an array of words
def split_into_words(txt):
    s = txt.strip().split(" ")
    i = 0
    
    while i < len(s) - 1:
        if s[i] in cache: 
            if s[i+1] not in cache[s[i]]:
                cache[s[i]].append(s[i+1]) 
        else:     
            cache[s[i]] = [s[i+1]] 
        i+=1
    
    return len(s),s,cache

#instantiate split word cache
s = split_into_words(words)

def get_random_wordlist():
    return cache[s[1][random.randrange(0, s[0])]]

def get_random_word(wordlist):
    return random.choice(wordlist).replace('\n', ' ').strip()

def get_random_key():
    return random.choice(list(cache.keys()))

def get_start_word():
    start_word = get_random_word(get_random_wordlist())
    
    if start_word[0] == '"' or start_word[0].isupper() or start_word[1].isupper():
        return start_word
    else:
        return get_start_word()

def get_end_word():
    end_word = get_random_word(get_random_wordlist())
    ew_qualifiers = ['.', '!', '?', '"']

    if end_word[-1] in ew_qualifiers:
        return end_word
    else:
        return get_end_word()

def get_sentence_word():
    sentence_word = get_random_word(get_random_wordlist())
    
    if sentence_word[0].isupper() or sentence_word[0] == '"' or sentence_word[-1] == '"':
        return get_sentence_word()
    else:
        return sentence_word

def make_sentence(limit=8):
    sentence = get_start_word()
    end_word = get_end_word()
    i = 0
    
    while i < limit - 2:
        sentence += " " + get_sentence_word()
        i+=1
    
    sentence += " " + end_word + " "
    
    return sentence

for _ in range(5): paragraph += make_sentence()
print(TGREEN, paragraph, ENDC)