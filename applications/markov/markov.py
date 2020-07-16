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
s = re.sub(r'[^a-zA-Z\'\.\"]+', ' ', words.strip()).split(" ")
i = 0
 
while i < len(s) - 1:
    if s[i] in cache: 
        if s[i+1] not in cache[s[i]]:
            cache[s[i]].append(s[i+1]) 
    else:     
        cache[s[i]] = [s[i+1]] 
    i+=1

# TODO: construct 5 random sentences
# Your code here

def make_sentence(max_length=8):
    i = 0
    sentence = ""
   
    while i < max_length:
        #get random index
        rand_cache_index = s[random.randrange(0, len(cache))]
        #get value at random index (list)
        rand_word_list = cache[rand_cache_index]
        #get random word from value at random index
        rand_word = rand_word_list[random.randrange(0, len(rand_word_list))].strip()
        
        """
        Using random.choice()
        rand_cache_index = random.choice(s)
        rand_word_list = cache[rand_cache_index]
        rand_word = random.choice(rand_word_list)
        """
        
        #case where last char is '.'
        #adds random word with trailing space to sentence and breaks out of loop, ending sentence
        if rand_word[-1] == ".":
            sentence += rand_word + " "
            break
        #case where last char is '"' 
        #since we know the only case where the last char is going to be a quotation mark is at the end of a sentence, we remove the last two chars and append the edited word with a trailing space to the end of the sentence
        if rand_word[-1] == '"':
            sentence += rand_word[0:-2] + " "
            break
        #case where word is a quotation mark, period or a space, skip
        #skips to next loop cycle
        elif rand_word == '"' or rand_word == "." or rand_word == " ":
            continue
        #case where both random word and sentence have a quotation mark. 
        #sanitizes random word, removing quotation, then adds it to the sentence with a trailing space
        elif '"' in rand_word and '"' in sentence:
            rand_word = re.sub(r'[^a-zA-Z]+', "", rand_word.strip())
            sentence += rand_word + " "    
        #default case
        #adds random word to sentence with trailing space
        else:
            sentence += rand_word + " " 
          
        i+=1
    
    #checks number of quotations in sentence and whether or not sentence has a period
    #if there is a quotation mark and there is no period, it adds a trailing period, followed by a quotation mark and space to the sentence
    if sentence.count('"') >= 1 and sentence.count('.') == 0:
        sentence = sentence.strip() + '." '
    #if there is a quotation mark and a period, just adds the quotation mark and trailing space to the end of sentence  
    elif sentence.count('"') >= 1 and sentence.count('.') > 0:
        sentence = sentence.strip() + '" '
    #if there is no period on the sentence, adds period and trailing space to end
    elif sentence.count(".") == 0:
        sentence = sentence.strip() + ". " 
    
    return sentence
      

for _ in range(5): paragraph += make_sentence()

print(TGREEN + paragraph, ENDC)