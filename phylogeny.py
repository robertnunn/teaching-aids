# find the species that should be the outgroup based solely on DNA sequence data
# given in "phylo seqs.txt". Assumes the sequences are already aligned.
#
# python 3.6
# Oct 21, 2017

from my_lib import load_list
from pprint import pprint as pp

seqs = load_list("phylo seqs2.txt")
seqs[0] = seqs[0][1:]

pp(seqs)

def find_diffs(seqs):
    diffs = []
    for i in range(len(seqs[0])):
        pos = [seqs[j][i] for j in range(len(seqs))]
        if len(set(pos)) > 1:
            diffs.append((i+1, pos))

    return diffs

results = find_diffs(seqs)
pp(results)

# score positions
scores = []
for i in results:
    pos_score = []
    for j in i[1]:
        score = i[1].count(j) / len(i[1])
        pos_score.append(score)
    scores.append(pos_score)

# pp(scores)
species_scores = []
for i in range(len(seqs)):
    species_scores.append(0)
pp(species_scores)

for i in scores:
    for j in range(len(i)):
        species_scores[j] += i[j]

pp(species_scores)

outgroup = species_scores.index(min(species_scores))+1
print(outgroup)
print(seqs[outgroup-1])
