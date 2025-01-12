map = {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'U'}

def to_rna(dna_strand):
    if dna_strand == '':
        return ''
    result = ''
    
    for letter in dna_strand:
        result += map[letter]

    return result
