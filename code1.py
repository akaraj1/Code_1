def find_ind(s, words):
    from itertools import permutations
    word_len = len(words[0])
    concat_len = word_len * len(words)
    perms = set(''.join(p) for p in permutations(words))
    a=[]
    for i in range(len(s)):
        if s[i:i+concat_len] in perms:
            a.append(i)
    return a
#Eg 1 :
s = "heybrofjxcbroheybrohe"
words = ["hey", "bro"]
ar=(find_ind(s, words))
print(ar)

OUTPUT:-
[0, 10, 13]

#Eg 2 :
s = "foobarfoothjbarfoocg"
words=["bar","foo"]
ar=find_ind(s,words)
print(ar)

OUTPUT:-
[0, 3, 12]
