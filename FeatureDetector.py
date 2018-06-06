from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
with open("Arch/Arch.csv", "w") as output:
	for seq_record in SeqIO.parse("Arch/ArchaeaData.fasta", "fasta"):
		my_prot = str(seq_record.seq)
		output.write(my_prot)
		output.write("," + str(len(seq_record)) + "\n")
with open("Pro/Pro.csv", "w") as output:
	for seq_record in SeqIO.parse("Pro/ProkaryoteData.fasta", "fasta"):
		my_prot = str(seq_record.seq)
		output.write(my_prot)
		output.write("," + str(len(seq_record)) + "\n")
with open("euk/Euk.csv", "w") as output:
	for seq_record in SeqIO.parse("Euk/EukaryoteData.fasta", "fasta"):
		my_prot = str(seq_record.seq)
		output.write(my_prot)
		output.write("," + str(len(seq_record)) + "\n")