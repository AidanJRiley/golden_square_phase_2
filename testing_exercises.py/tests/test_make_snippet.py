from lib.make_snippet import *

def test_make_snippet_five_words():
    result = make_snippet('This sentence has five words')
    assert result == 'This sentence has five words'

def test_make_snippet_four_words():
    result = make_snippet('Four words here mate')
    assert result == 'Four words here mate'

def test_make_snippet_blank_string():
    result = make_snippet('')
    assert result == ''

def test_make_snippet_six_words():
    result = make_snippet('This one might be a problem')
    assert result == 'This one might be a...'

def test_make_snippet_seven_words():
    result = make_snippet('This is a long long long sentence')
    assert result == 'This is a long long...'

def test_make_snippet_commas():
    # Ensuring commas don't separate words
    result = make_snippet('1,2,3,4,5,6')
    assert result == '1,2,3,4,5,6'
