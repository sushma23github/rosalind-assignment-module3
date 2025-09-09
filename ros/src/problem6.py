# Problem 6 - Translate DNA to Protein
from Bio.Seq import Seq
input_file = "/content/drive/MyDrive/ros/data/sample/problem6_input.txt"
with open(input_file, 'r') as f:
    dna_seq = f.read().strip()
dna = Seq(dna_seq)
protein = dna.translate()
print(protein)