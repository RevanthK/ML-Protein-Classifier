from Bio import SeqIO
from Bio.Seq import Seq
#from Bio.Alphabet import IUPAC
from Bio.SeqUtils.ProtParam import ProteinAnalysis


with open ("compiled_enhanced.csv", "w") as compiled:
	#compiled.write("Length,A,C,E,D,G,F,I,H,K,M,L,N,Q,P,S,R,T,W,V,Y,Molecular Weight,Aromaticity,Instability Index,Flexibility,Isoelectric Point,Helix,Turn,Sheet,Class\n")
	compiled.write("Length,A,C,E,D,G,F,I,H,K,M,L,N,Q,P,S,R,T,W,V,Y,Aromaticity,Isoelectric Point,Class\n")
	for seq_record in SeqIO.parse("Arch/ArchaeaData.fasta", "fasta"):
		analysed_seq = ProteinAnalysis(str(seq_record.seq))
		
		amino_acids = analysed_seq.get_amino_acids_percent()
		#mol_weight = analysed_seq.molecular_weight()
		arom = analysed_seq.aromaticity()
		#insta_index = analysed_seq.instability_index()
		#flex = analysed_seq.flexibility()
		iso_elec = analysed_seq.isoelectric_point()
		#sec_struct = analysed_seq.secondary_structure_fraction()

		compiled.write(str(len(seq_record)) + ",")
		for amino_acid in amino_acids:
			compiled.write(str(amino_acids[amino_acid]) + ",")		
		#compiled.write(str(mol_weight) + ",")
		compiled.write(str(arom) + ",")
		#compiled.write(str(insta_index) + ",")
		#compiled.write(str(flex) + ",")
		compiled.write(str(iso_elec) + ",")
		"""
		for index in range(len(sec_struct)):
			compiled.write(str(sec_struct[index]) + ",")
		"""
		compiled.write("P" + "\n")

	for seq_record in SeqIO.parse("Pro/Pro.csv", "fasta"):
		analysed_seq = ProteinAnalysis(str(seq_record.seq))
		
		amino_acids = analysed_seq.get_amino_acids_percent()
		#mol_weight = analysed_seq.molecular_weight()
		arom = analysed_seq.aromaticity()
		#insta_index = analysed_seq.instability_index()
		#flex = analysed_seq.flexibility()
		iso_elec = analysed_seq.isoelectric_point()
		#sec_struct = analysed_seq.secondary_structure_fraction()

		compiled.write(str(len(seq_record)) + ",")
		for amino_acid in amino_acids:
			compiled.write(str(amino_acids[amino_acid]) + ",")		
		#compiled.write(str(mol_weight) + ",")
		compiled.write(str(arom) + ",")
		#compiled.write(str(insta_index) + ",")
		#compiled.write(str(flex) + ",")
		compiled.write(str(iso_elec) + ",")
		"""
		for index in range(len(sec_struct)):
			compiled.write(str(sec_struct[index]) + ",")
		"""
		compiled.write("P" + "\n")
	
	for seq_record in SeqIO.parse("euk/Euk.csv", "fasta"):
		analysed_seq = ProteinAnalysis(str(seq_record.seq))
		
		amino_acids = analysed_seq.get_amino_acids_percent()
		#mol_weight = analysed_seq.molecular_weight()
		arom = analysed_seq.aromaticity()
		#insta_index = analysed_seq.instability_index()
		#flex = analysed_seq.flexibility()
		iso_elec = analysed_seq.isoelectric_point()
		#sec_struct = analysed_seq.secondary_structure_fraction()

		compiled.write(str(len(seq_record)) + ",")
		for amino_acid in amino_acids:
			compiled.write(str(amino_acids[amino_acid]) + ",")		
		#compiled.write(str(mol_weight) + ",")
		compiled.write(str(arom) + ",")
		#compiled.write(str(insta_index) + ",")
		#compiled.write(str(flex) + ",")
		compiled.write(str(iso_elec) + ",")
		"""
		for index in range(len(sec_struct)):
			compiled.write(str(sec_struct[index]) + ",")
		"""
		compiled.write("E" + "\n")
