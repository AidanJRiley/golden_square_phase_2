class GrammarStats:
    def __init__(self):
        self.total_tests = {'good':0,'bad':0}

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if type(text) != str:
            raise Exception('This is not a string!')
        sentence_end_punc = '.!?'
        if text[0].isupper() and text[-1] in sentence_end_punc:
            self.total_tests['good'] += 1
            return True
        
        self.total_tests['bad'] += 1
        return False

        

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.total_tests['good'] + self.total_tests['bad'] == 0: 
            return 'There have been no checks completed'
        result = self.total_tests['good'] / (self.total_tests['good'] + self.total_tests['bad'])
        return round(result*100)