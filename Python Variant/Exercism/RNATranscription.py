def to_rna(dna_strand):

    rna_strand = ""
    
    for letter in dna_strand: 
    
        match letter:
            case "G":
                rna_strand += "C"
            case "C":
                rna_strand += "G"
            case "T":
                rna_strand += "A"
            case "A":
                rna_strand += "U"
    
            case _:
                continue
    
    return rna_strand
