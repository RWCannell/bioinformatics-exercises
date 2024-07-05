class BoyerMooreAlgorithm():
    def __init__(self, sequence: str, subsequence: str):
        self.sequence = sequence
        self.subsequence = subsequence
        
    def construct_matching_dict(self):
        matching_dict = {}
        for char in self.subsequence:
            char_index = self.subsequence.index(char)
            shift_value = max(1, len(self.subsequence) - char_index - 1)
            matching_dict[char] = shift_value
        return matching_dict
    
    def shift_subsequence(self, matching_dict):
        matching_characters = []
        current_index_of_subsequence = (len(self.subsequence) - 1)
        current_index_of_sequence = current_index_of_subsequence
        
        while current_index_of_sequence <= len(self.sequence):
            if self.sequence[current_index_of_sequence] != self.subsequence[current_index_of_subsequence]:
                if self.sequence[current_index_of_sequence] in matching_dict.keys():
                    current_index_of_sequence += matching_dict[self.sequence[current_index_of_sequence]]
                else:
                    current_index_of_sequence += len(self.subsequence)
                current_index_of_subsequence = (len(self.subsequence) - 1)
                matching_characters = []
            else:
                matching_characters.insert(0, self.subsequence[current_index_of_subsequence])
                current_index_of_sequence -= 1
                current_index_of_subsequence -= 1
                if len(matching_characters) == len(self.subsequence):
                    break
        return current_index_of_sequence
            
    def find_index_of_subsequence(self):
        matching_dict = self.construct_matching_dict()
        print(f"matching_dict: {matching_dict}")
        index_of_subsequence = self.shift_subsequence(matching_dict) + 1
        print(f"The subsequence '{self.subsequence}' begins at index {index_of_subsequence} of the sequence '{self.sequence}'.")
        return index_of_subsequence
    
if __name__ == '__main__':
    sequence = "CGGCGATTAGCAGCACAGTTAGCGATGACCAGAATGTAGGTA"
    subsequence = "TAGCGAT"
    # sequence = "I am a baby blue bird"
    # subsequence = "baby"
    # sequence = "this is a test my friend"
    # subsequence = "test"
    boyer_moore_algorithm = BoyerMooreAlgorithm(sequence, subsequence)
    index_of_subsequence = boyer_moore_algorithm.find_index_of_subsequence()
    print(index_of_subsequence)