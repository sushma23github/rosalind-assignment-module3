# Problem 9 - Pattern Occurrences
input_file = "/content/drive/MyDrive/ros/data/sample/problem9_input.txt"
with open(input_file, 'r') as f:
    dna = f.read().strip()
pattern = "ATGC"
positions = [i+1 for i in range(len(dna)-len(pattern)+1) if dna[i:i+len(pattern)] == pattern]
print(positions)