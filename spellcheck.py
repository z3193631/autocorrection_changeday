from symspellpy.symspellpy import SymSpell, Verbosity  # import the module

class Spellchecker:
    # maximum edit distance per dictionary precalculation
    max_edit_distance_dictionary = 2
    prefix_length = 7

    def __init__(self):
        # create object
        self.sym_spell = SymSpell(self.max_edit_distance_dictionary, self.prefix_length)
        # load dictionary
        dictionary_path = "frequency_dictionary_en_82_765.txt"
        bigram_path = "frequency_bigramdictionary_en_243_342.txt"
        # term_index is the column of the term and count_index is the
        # column of the term frequency
        if not self.sym_spell.load_dictionary(dictionary_path, term_index=0,
                                         count_index=1):
            print("Dictionary file not found")
            return
        if not self.sym_spell.load_bigram_dictionary(bigram_path, term_index=0,
                                                count_index=2):
            print("Bigram dictionary file not found")
            return

    def get_correction(self, input_term):
        max_edit_distance_lookup = 2 #must be equal or less than max_edit_distance_dictionary
        suggestion_verbosity = Verbosity.ALL  # TOP, CLOSEST, or ALL
        suggestions = self.sym_spell.lookup(input_term, suggestion_verbosity,
                                   max_edit_distance_lookup)
        # return suggestion terms (top 3)
        corrected_term = []
        for suggestion in suggestions:
            corrected_term.append(suggestion.term)
        if len(corrected_term) > 3:
            return corrected_term[0:3]
        else:
            return corrected_term
