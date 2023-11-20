from lib.count_words import *

def test_count_words_initial():
    result = count_words('')
    assert result == 0

def test_count_words_four():
    result = count_words('Once upon a time')
    assert result == 4

def test_count_words_commas():
    result = count_words('Seperated, by, commas,')
    assert result == 3

def test_count_words_commas_no_spaces():
    result = count_words('seperated,by,commas,')
    assert result == 1

def test_count_words_number():
    result = count_words(7)
    assert result == 'This is not a string!'

def test_count_words_None():
    result = count_words(None)
    assert result == 'This is not a string!'

def test_count_words_list():
    result = count_words(['word'])
    assert result == 'This is not a string!'

def test_count_words_dictionary():
    result = count_words({'1':'word'})
    assert result == 'This is not a string!'