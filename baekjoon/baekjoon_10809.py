word = input()
alphabet_list = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
idx_list = [str(word.index(x)) if x in word else str(-1) for x in alphabet_list]

print(' '.join(idx_list))