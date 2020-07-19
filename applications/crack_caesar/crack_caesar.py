# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import re

#variable declarations
freq_cache = {}
cipher_cache = {}
frequency_order = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
i = 0
j = 0
final_text = ""

#import text file
with open("ciphertext.txt") as f:
    text = f.read()
    
cipher = re.sub(r'[^A-Z]+', '', text)
    
#get letter counts     
while i < len(cipher):
    if cipher[i] in cipher_cache:
        cipher_cache[cipher[i]] += 1
    else:
        cipher_cache[cipher[i]] = 1
    i+=1

#sort letter counts    
sorted_cache = sorted(cipher_cache.items(), key=lambda x:x[1], reverse=True)

#create key hash table
while j < len(cipher_cache):
    cipher_cache[sorted_cache[j][0]] = frequency_order[j]
    j+=1   
    
#finally, decode the text
for n in text:
    n = cipher_cache[n] if n in cipher_cache else n
    final_text += n
        
print(final_text)