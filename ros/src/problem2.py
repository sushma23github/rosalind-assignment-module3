# Problem 2 - Transcribe DNA to RNA
input_file = "/content/drive/MyDrive/ros/data/sample/problem2_input.txt"
with open(input_file, 'r') as f:
    dna = f.read().strip()
rna = dna.replace('T', 'U')
print(rna)