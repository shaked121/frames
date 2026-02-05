import re
import os

# יצירת תיקיית תוצאות אם אינה קיימת (למניעת השגיאה הקודמת)
if not os.path.exists("Results"):
    os.makedirs("Results")

file1 = open("Data/orf_coding_all.fa.txt", "r")
file2 = open("Results/output.txt", "w")

gene = ""
count = 0
TAA_count = 0
TGA_count = 0
TAG_count = 0

# פונקציה קטנה כדי לא לחזור על הקוד פעמיים
def check_gene(sequence):
    global count, TAA_count, TGA_count, TAG_count
    
    match = re.fullmatch(r'^ATG([ATGC]{3})*(TAA|TGA|TAG)$', sequence)
    if match:
        count += 1
        stop_codon = sequence[-3:]
        if stop_codon == "TAA":
            TAA_count += 1
        elif stop_codon == "TGA":
            TGA_count += 1
        elif stop_codon == "TAG":
            TAG_count += 1

for line in file1:
    line = line.strip()
    if line.startswith(">"):
        # לפני שמתחילים גן חדש, בודקים את הגן הקודם שאספנו
        check_gene(gene)
        gene = "" # איפוס לגן הבא
    else:
        gene += line

# חשוב: בדיקת הגן האחרון שנשאר בזיכרון אחרי שהלולאה נגמרה
check_gene(gene)

# הדפסה לקובץ עם בדיקה שלא מחלקים ב-0
if count > 0:
    file2.write(f"Number of yeast coding sequences with start and end codons: {count}\n")  
    file2.write(f"Number of ORFs with TAA end codon: {TAA_count}, {(TAA_count/count)*100:.2f}% of all ORFs\n")
    file2.write(f"Number of ORFs with TGA end codon: {TGA_count}, {(TGA_count/count)*100:.2f}% of all ORFs\n")
    file2.write(f"Number of ORFs with TAG end codon: {TAG_count}, {(TAG_count/count)*100:.2f}% of all ORFs\n")


file1.close()
file2.close()