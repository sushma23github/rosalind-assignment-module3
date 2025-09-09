# Problem 7 - Reverse Complement
from Bio.Seq import Seq
input_file = "/content/drive/MyDrive/ros/data/sample/problem7_input.txt"
with open(input_file, 'r') as f:
    dna_seq = f.read().strip()
dna = Seq(dna_seq)
rev_comp = dna.reverse_complement()
print(rev_comp)