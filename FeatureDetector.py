from Bio import SeqIO
from Bio.Seq import Seq
#from Bio.Alphabet import IUPAC
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def generateOuput(ArchaeaFile, ProkaryoteFile, EukaryoteFile):
	Pro_count=0
	Euk_count=0
	with open ("output.csv", "w") as compiled:
		compiled.write("Length,A,C,E,D,G,F,I,H,K,M,L,N,Q,P,S,R,T,W,V,Y,Class\n")
		#for seq_record in SeqIO.parse("Arch/ArchaeaData.fasta", "fasta"):
		for seq_record in SeqIO.parse(ArchaeaFile, "fasta"):	
			analysed_seq = ProteinAnalysis(str(seq_record.seq))
			compiled.write(str(len(seq_record)) + ",")
			for amino_acid in analysed_seq.get_amino_acids_percent():
				compiled.write(str(analysed_seq.get_amino_acids_percent()[amino_acid]) + ",")
			compiled.write("P" + "\n")
			Pro_count += 1

		#for seq_record in SeqIO.parse("Pro/ProkaryoteData.fasta", "fasta"):
		for seq_record in SeqIO.parse(ProkaryoteFile, "fasta"):
			analysed_seq = ProteinAnalysis(str(seq_record.seq))
			compiled.write(str(len(seq_record)) + ",")
			for amino_acid in analysed_seq.get_amino_acids_percent():
				compiled.write(str(analysed_seq.get_amino_acids_percent()[amino_acid]) + ",")
			compiled.write("P" + "\n")
			Pro_count += 1

		#for seq_record in SeqIO.parse("Euk/EukaryoteData.fasta", "fasta"):
		for seq_record in SeqIO.parse(EukaryoteFile, "fasta"):
			analysed_seq = ProteinAnalysis(str(seq_record.seq))
			compiled.write(str(len(seq_record)) + ",")
			for amino_acid in analysed_seq.get_amino_acids_percent():
				compiled.write(str(analysed_seq.get_amino_acids_percent()[amino_acid]) + ",")
			compiled.write("E" + "\n")
			Euk_count += 1

	print("Prokaryote count: " + str(Pro_count))
	print("Eukaryote count: " + str(Euk_count))

