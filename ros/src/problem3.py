# Problem 3 - Complement DNA Strand
input_file = "/content/drive/MyDrive/ros/data/sample/problem3_input.txt"
with open(input_file, 'r') as f:
    dna = f.read().strip()
complement = dna.replace('A','t').replace('T','a').replace('C','g').replace('G','c').upper()
print(complement)