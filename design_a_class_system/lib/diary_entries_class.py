import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == '' or contents == '':
            raise Exception('Diary entries must have a title and contents')
        elif type(title) != str or type(contents) != str:
            raise Exception('Both values must be a string!')
        self.title = title
        self.contents = contents
        self.read_so_far = 0

    def format(self):
        return f'{self.title}: {self.contents}'

    def count_total_words(self):
        words = self.format().split()
        return int(len(words))
    
    def count_contents_words(self):
        words = self.contents.split()
        return int(len(words))

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception('Cannot calculate reading time with wpm of 0')
        contents_word_count = len(self.contents_words())
        return math.ceil(contents_word_count / wpm)

    def reading_chunk(self, wpm, minutes):
        words_user_can_read = wpm*minutes
        words = self.contents_words()
        if self.read_so_far >= len(words):
            self.read_so_far = 0
        chunk_start = self.read_so_far
        chunk_end = self.read_so_far + words_user_can_read
        chunk_words = words[chunk_start:chunk_end]
        self.read_so_far = chunk_end
        return ' '.join(chunk_words)
    
    def contents_words(self):
        return self.contents.split()
