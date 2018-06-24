from Bio import SeqIO
from Bio.Seq import Seq
#from Bio.Alphabet import IUPAC
from Bio.SeqUtils.ProtParam import ProteinAnalysis


with open ("compiled.csv", "w") as compiled:
	with open("Arch/Arch.csv", "w") as output:
		output.write("Length,A,C,E,D,G,F,I,H,K,M,L,N,Q,P,S,R,T,W,V,Y,Class\n")
		compiled.write("Length,A,C,E,D,G,F,I,H,K,M,L,N,Q,P,S,R,T,W,V,Y,Class\n")
		for seq_record in SeqIO.parse("Arch/ArchaeaData.fasta", "fasta"):
			analysed_seq = ProteinAnalysis(str(seq_record.seq))
			output.write(str(len(seq_record)) + ",")
			for amino_acid in analysed_seq.get_amino_acids_percent():
				output.write(str(analysed_seq.get_amino_acids_percent()[amino_acid]) + ",")
			output.write("P" + "\n")

			compiled.write(str(len(seq_record)) + ",")
			for amino_acid in analysed_seq.get_amino_acids_percent():
				compiled.write(str(analysed_seq.get_amino_acids_percent()[amino_acid]) + ",")
			compiled.write("P" + "\n")

	with open("Pro/Pro.csv", "w") as output:
		output.write("Length,A,C,E,D,G,F,I,H,K,M,L,N,Q,P,S,R,T,W,V,Y,Class\n")
		for seq_record in SeqIO.parse("Pro/ProkaryoteData.fasta", "fasta"):
			analysed_seq = ProteinAnalysis(str(seq_record.seq))
			output.write(str(len(seq_record)) + ",")
			for amino_acid in analysed_seq.get_amino_acids_percent():
				output.write(str(analysed_seq.get_amino_acids_percent()[amino_acid]) + ",")
			output.write("P" + "\n")

			compiled.write(str(len(seq_record)) + ",")
			for amino_acid in analysed_seq.get_amino_acids_percent():
				compiled.write(str(analysed_seq.get_amino_acids_percent()[amino_acid]) + ",")
			compiled.write("P" + "\n")

	with open("euk/Euk.csv", "w") as output:
		output.write("Length,A,C,E,D,G,F,I,H,K,M,L,N,Q,P,S,R,T,W,V,Y,Class\n")
		for seq_record in SeqIO.parse("Euk/EukaryoteData.fasta", "fasta"):
			analysed_seq = ProteinAnalysis(str(seq_record.seq))
			output.write(str(len(seq_record)) + ",")
			for amino_acid in analysed_seq.get_amino_acids_percent():
				output.write(str(analysed_seq.get_amino_acids_percent()[amino_acid]) + ",")
			output.write("E" + "\n")

			compiled.write(str(len(seq_record)) + ",")
			for amino_acid in analysed_seq.get_amino_acids_percent():
				compiled.write(str(analysed_seq.get_amino_acids_percent()[amino_acid]) + ",")
			compiled.write("E" + "\n")
