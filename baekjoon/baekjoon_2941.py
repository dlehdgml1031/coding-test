sentence = input()
word_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for word in word_list:
    sentence = sentence.replace(word,"*")

print(len(sentence))