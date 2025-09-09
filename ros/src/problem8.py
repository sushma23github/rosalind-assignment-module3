# Problem 8 - Count Sub-sequences
input_file = "/content/drive/MyDrive/ros/data/sample/problem8_input.txt"
with open(input_file, 'r') as f:
    dna = f.read().strip()
subseq = "ATG"
count = 0
for i in range(len(dna)-len(subseq)+1):
    if dna[i:i+len(subseq)] == subseq:
        count += 1
print(count)