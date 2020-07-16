import re

def word_count(s):
    # Your code here
    word_dict = {}
    s = re.sub(r'[^a-z \']+', ' ', s.lower()).split(" ")

    
    for w in s:
        if w == '':
            continue
        else:
            word_dict[w] = word_dict[w] + 1 if w in word_dict else 1

    return word_dict

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))