class GrammarStats:
    def __init__(self):
        pass

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if type(text) != str:
            raise Exception('This is not a string!')
        upper_case_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        sentence_end_punc = '.!?'
        if text[0] in upper_case_chars and text[-1] in sentence_end_punc:
            return True

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass