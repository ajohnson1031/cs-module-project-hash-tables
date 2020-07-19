# Your code here
cache = {}

with open("robin.txt") as f:
    words = f.read()
    
s = [n for n in words.replace('\n', ' ').split(' ') if n != '']

i = 0
while i < len(s):
    if s[i] in cache:
        cache[s[i]] += 1
    else:
        cache[s[i]] = 1
    i+=1

sorted_cache = sorted(cache.items(), key=lambda x:x[1], reverse=True)
longest_word = ""

for j in sorted_cache:
    if len(j[0]) > len(longest_word):
        longest_word = j[0]

for k in sorted_cache:
    print(k[0] + " "*(len(longest_word) - len(k[0])) + "  " + "#"*k[1])