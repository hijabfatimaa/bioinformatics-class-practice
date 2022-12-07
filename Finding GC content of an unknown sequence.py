#Bioinformatic Python Presentation
#Finding the number of nucleotides in your DNA Sequence
DNA="GTGTGTGTGTGTGATGATAGTTGATATAATAGTAGTAGTAGTAGATGATAGTGATAGATAGATGACTGCCTGCTGAACCTAGGTCCAATAGCAATCCTGCTGCCAACTGCAACCCTGCAACCCGT"
number_of_nucleotides = len(DNA)
print("Number of nucleotides in sequence is:", number_of_nucleotides)
#Calculating Number of each nucleotide seprately
print("G Nucleotides:", DNA.count('G'))
print("C Nucleotides:", DNA.count('C'))
print("T Nucleotides:", DNA.count('T'))
print("A Nucleotides:", DNA.count('A'))
#Calculating the GC percentage in the sequence
gc=DNA.count('G')+ DNA.count('C')
gc_percentage=gc/number_of_nucleotides * 100
print("GC Content in percentage is:", gc_percentage)
#Calculating AT Content
at=DNA.count('A')+ DNA.count('T')
at_percentage=at/number_of_nucleotides * 100
print("AT Content in percentage is:", at_percentage)
#Make use of round function
GC_rounded=round(gc_percentage,2)  #the ,2 tells decimal place
print('percentage of GC rounded is:', GC_rounded)
#Make use of round function for AT
AT_rounded=round(at_percentage,2)  #the ,2 tells decimal place
print('percentage of AT rounded is:', AT_rounded)
#Number of Purines
ag=DNA.count('A')+ DNA.count('G')
print("Number of purines is:", ag)
#Number of Prymidines
Tc=DNA.count('T')+ DNA.count('C')
print("Pyrimidine Content in percentage is:", Tc)
#percentage of purines and Pyrimidine
Percentage_purines = ag/number_of_nucleotides * 100
print("Purine Percentage is:", Percentage_purines)
Percentage_pyrimidine = Tc/number_of_nucleotides * 100
print("PyrimidinePercentage is:", Percentage_pyrimidine)