def to_rna(dna_strand):

    translater = str.maketrans("GCTA", "CGAU")

    return dna_strand.translate(translater)