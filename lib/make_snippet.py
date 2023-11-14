def make_snippet(string):
    words = string.split(' ')
    if len(words) <= 5:
        return string
    else:
        return ' '.join(words[0:5]) + '...'

