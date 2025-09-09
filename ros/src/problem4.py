# Problem 4 - GC Content
input_file = "/content/drive/MyDrive/ros/data/sample/problem4_input.txt"
with open(input_file, 'r') as f:
    dna = f.read().strip()
gc_content = (dna.count('G') + dna.count('C')) / len(dna) * 100
print(round(gc_content,2))