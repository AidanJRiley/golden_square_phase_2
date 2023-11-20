class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.words_read = 0

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        words = self.contents.split()
        return len(words)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        if self.count_words() < wpm:
            return 1
        return round(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        words_to_read = wpm * minutes
        entry_as_list = self.contents.split()
        if self.words_read + words_to_read > self.count_words():
            start_point = self.words_read
            self.words_read = 0
            return ' '.join(entry_as_list[start_point:])
        result = ' '.join(entry_as_list[self.words_read:self.words_read+words_to_read])
        self.words_read = self.words_read + words_to_read
        return result