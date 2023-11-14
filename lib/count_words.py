def count_words(string):
    if type(string) != str:
        return 'This is not a string!'
    if string == '': return 0
    words = string.split(' ')
    return len(words)