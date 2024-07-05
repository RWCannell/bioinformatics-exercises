def calculate_gc_content_percentage(nucleotide_sequence: str):
    nucleotide_dict = {
        'A': 0, 
        'C': 0, 
        'G': 0,
        'T': 0,
    }
    if len(nucleotide_sequence) == 0:
        print("No nucleotide sequence, so GC content is zero.")
        return float(0)
    
    for nucleotide in nucleotide_sequence:
        if nucleotide.upper() == 'A':
            nucleotide_dict['A'] += 1
        elif nucleotide.upper() == 'C':
            nucleotide_dict['C'] += 1
        elif nucleotide.upper() == 'G':
            nucleotide_dict['G'] += 1
        elif nucleotide.upper() == 'T':
            nucleotide_dict['T'] += 1
        else:
            print("A letter that does not correspond to a nucleotide has been found in the sequence.")
    
    number_of_A = nucleotide_dict['A']
    number_of_C = nucleotide_dict['C']
    number_of_G = nucleotide_dict['G']
    number_of_T = nucleotide_dict['T']
    
    print(f"Nucleotide occurrences are: A - {number_of_A}, C - {number_of_C}, G - {number_of_G}, and T - {number_of_T}")
    
    gc_content_percentage = float((number_of_C + number_of_G) / (number_of_A + number_of_C + number_of_G + number_of_T)) * 100
    
    print(f"The GC-content percentage is: {gc_content_percentage}%")
    
    return gc_content_percentage

if __name__ == '__main__':
    seq = "AGGTACGCGATTTAGCCCGTTTATAATGTGTATGCTGCCTGATCCGATCCCGTAAGCCCTCAGTAGCTGCTGCTGAGCTACGTGAC"
    gc_content_percentage = calculate_gc_content_percentage(seq)
    print(gc_content_percentage)