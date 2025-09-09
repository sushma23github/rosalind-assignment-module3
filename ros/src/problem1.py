# Problem 1 - Counting DNA nucleotides
input_file = "/content/drive/MyDrive/ros/data/sample/problem1_input.txt"
with open(input_file, 'r') as f:
    dna = f.read().strip()
A = dna.count('A')
C = dna.count('C')
G = dna.count('G')
T = dna.count('T')
print(A, C, G, T)