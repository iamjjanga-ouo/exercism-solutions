def to_rna(dna_strand):
    # translate() is more powerful in multiple different letters than replace(), re.sub()
    return dna_strand.translate(str.maketrans({'C':'G', 'G':'C', 'T':'A', 'A':'U'}))

