import re

file1 = open("Data/orf_coding_all.fa.txt", "r")
file2 = open("Result/output.txt", "w")

gene = ""
count = 0
TAA_count = 0
TGA_count = 0
TAG_count = 0

for line in file1:
    line = line.strip()
    if not line.startswith(">"):
        gene += line
    if line.startswith(">"):
        match = re.fullmatch(r'^ATG([ATGC]{3})*(TAA|TGA|TAG)$', gene)
        if match:
            count += 1
            stop_codon = gene[-3:]
            if stop_codon == "TAA":
                TAA_count += 1
            elif stop_codon == "TGA":
                TGA_count += 1
            elif stop_codon == "TAG":
                TAG_count += 1
        gene = ""
        
file2.write(f"Number of yeast coding sequences with start and end codons: {count}\n")  
file2.write(f"Number of ORFs with TAA end codon: {TAA_count},{(TAG_count/count)*100}% of all ORFs\n")
file2.write(f"Number of ORFs with TGA end codon: {TGA_count},{(TAG_count/count)*100}% of all ORFs\n")
file2.write(f"Number of ORFs with TAG end codon: {TAG_count},{(TAG_count/count)*100}% of all ORFs\n")