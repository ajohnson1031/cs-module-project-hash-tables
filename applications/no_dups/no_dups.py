def no_dups(s):
    # Your code here
    sentence = ""
    
    for w in s.split(" "):
        if w in sentence:
            continue
        else:
            sentence += w + " "
    
    return sentence.rstrip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))