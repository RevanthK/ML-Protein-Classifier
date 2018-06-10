from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

percent = 100/10
counter = 0

with open ("compiled_10.csv", "w") as compiled:
	with open("Arch/Arch_10.csv", "w") as output:
		output.write("Class,Sequence,Length\n")
		compiled.write("Class,Sequence,Length\n")
		for seq_record in SeqIO.parse("Arch/ArchaeaData.fasta", "fasta"):
			if counter == 10:
				my_prot = str(seq_record.seq)
				output.write(str(0) + ",")
				output.write(my_prot)
				output.write("," + str(len(seq_record)) + "\n")
				compiled.write(str(0) + ",")
				compiled.write(my_prot)
				compiled.write("," + str(len(seq_record)) + "\n")
				counter = 0
			else:
				counter += 1
	with open("Pro/Pro_10.csv", "w") as output:
		output.write("Class,Sequence,Length\n")
		for seq_record in SeqIO.parse("Pro/ProkaryoteData.fasta", "fasta"):
			if counter == 10:
				my_prot = str(seq_record.seq)
				output.write(str(0) + ",")
				output.write(my_prot)
				output.write("," + str(len(seq_record)) + "\n")
				compiled.write(str(0) + ",")
				compiled.write(my_prot)
				compiled.write("," + str(len(seq_record)) + "\n")
				counter = 0
			else:
				counter += 1
	with open("euk/Euk_10.csv", "w") as output:
		output.write("Class,Sequence,Length\n")
		for seq_record in SeqIO.parse("Euk/EukaryoteData.fasta", "fasta"):
			if counter == 10:
				my_prot = str(seq_record.seq)
				output.write(str(1) + ",")
				output.write(my_prot)
				output.write("," + str(len(seq_record)) + "\n")
				compiled.write(str(1) + ",")
				compiled.write(my_prot)
				compiled.write("," + str(len(seq_record)) + "\n")
				counter = 0
			else:
				counter += 1