
from collections import Counter



#Turn Fasta into a Dictionary 
def read_Fasta(filePath):
    with open(filePath, 'r') as f:
        FASTAFile = [l.strip() for l in f.readlines()]

    FASTADict = {}
    FASTALabel = ""

    for line in FASTAFile:
        if '>' in line:
            FASTALabel = line 
            FASTADict[FASTALabel] = ""
        else:
            FASTADict[FASTALabel] += line 

    return FASTADict

dictionary = read_Fasta('dna2.fasta')




#Get the length of each sequence in the dictionary as well as corresponding 
#Sequence Id


length_dict = {key: len(value) for key, value in dictionary.items()}
#print(length_dict)

sorted_seq = sorted(length_dict.values())

#print(sorted_seq)




#Given input reading frame on forward strand == translate 
# def get_three_reading_frames(seq):
#     pass




# #Finding repeats of length n in sequences in the Fasta file 

def find_all_substrings_of_length_n(seq, n):
    substrings = [seq[i:j] for i in range(len(seq)) for j in range(i+1, len(seq)+1)]
    repeats_n_length = []
    for i in substrings:
        if len(i) == n:
            repeats_n_length.append(i)
    return repeats_n_length


#Lists of subsequences
lst_subseqs = []

# for key value in dictionary of fasta sequences, make all subsequences of length n into the lst_subseqs list 

for key, value in dictionary.items():
    lst_subseqs.append(find_all_substrings_of_length_n(value, 12))


#make a lists of lists one flat list 
flat_list = [item for sublist in lst_subseqs for item in sublist]


#count the occurences of subseqs in the list 
c = Counter(flat_list)
sorted_substrings = sorted(c.values())
print(sorted_substrings)

#Write to new file 
new_file = open('substrings.txt', 'w')
for i in c:
    if c[i] >1:
        new_file.write('{} appears {} times.'.format(i, c[i]))

new_file.close()

#max function 
print(max(sorted_substrings))
