import os
import random
file_name = 'noun.tsv','verb.tsv','adj.tsv','adverb.tsv'
file_list = []
for file_name in os.listdir(os.getcwd()):
    if file_name.endswith(".tsv"):
        file_list.append(file_name)
result = ''
for file in file_list:
    result += random.choice([line for line in open(file, 'r')])[:-1] + ' '
print result

