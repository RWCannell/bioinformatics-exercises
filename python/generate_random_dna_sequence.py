
import random

def generate_random_dna_sequence(sequence_length):
    nucleotide_dictionary = {
        1: 'A',
        2: 'C',
        3: 'G',
        4: 'T'
    }
    nucleotide_list = []
    count = 0
    while count < sequence_length:
        num = random.randrange(1, 5)
        nucleotide = nucleotide_dictionary[num]
        nucleotide_list.append(nucleotide)
        count +=1
    return ''.join(nucleotide_list)

def generate_random_rna_sequence(sequence_length):
    nucleotide_dictionary = {
        1: 'A',
        2: 'C',
        3: 'G',
        4: 'U'
    }
    nucleotide_list = []
    count = 0
    while count < sequence_length:
        num = random.randrange(1, 5)
        nucleotide = nucleotide_dictionary[num]
        nucleotide_list.append(nucleotide)
        count +=1
    return ''.join(nucleotide_list)

if __name__ == '__main__':
    random_dna_sequence = generate_random_dna_sequence(150)
    random_rna_sequence = generate_random_rna_sequence(150)
    print(f"DNA Sequence: {random_dna_sequence}")
    print(f"RNA Sequence: {random_rna_sequence}")
