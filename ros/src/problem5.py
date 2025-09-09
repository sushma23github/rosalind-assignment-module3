# Problem 5 - Count Motifs (ATG)
input_file = "/content/drive/MyDrive/ros/data/sample/problem5_input.txt"
with open(input_file, 'r') as f:
    dna = f.read().strip()
motif = "ATG"
count = 0
for i in range(len(dna)-len(motif)+1):
    if dna[i:i+len(motif)] == motif:
        count += 1
print(count)