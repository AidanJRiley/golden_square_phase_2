import pytest
from lib.sentence_checker import *

def test_sentence_checker_None():
    with pytest.raises(Exception) as e:
        sentence_checker(None)
    error_message = str(e.value)
    assert error_message == 'This is not a string!'

def test_sentence_checker_number():
    with pytest.raises(Exception) as e:
        sentence_checker(100)
    error_message = str(e.value)
    assert error_message == 'This is not a string!'

def test_sentence_checker_list():
    with pytest.raises(Exception) as e:
        sentence_checker(['1','2','3'])
    error_message = str(e.value)
    assert error_message == 'This is not a string!'

def test_sentence_checker_dictionary():
    with pytest.raises(Exception) as e:
        sentence_checker({'1':2, '3':4})
    error_message = str(e.value)
    assert error_message == 'This is not a string!'

def test_sentence_checker_gramatically_correct_exclamation():
    result = sentence_checker('This is gramatically correct!')
    assert result == True

def test_sentence_checker_gramatically_correct_fullstop():
    result = sentence_checker('This is gramatically correct.')
    assert result == True

def test_sentence_checker_gramatically_incorrect_no_fullstop():
    result = sentence_checker('This is gramatically incorrect')
    assert result == False

def test_sentence_checker_gramatically_incorrect_no_fullstop():
    result = sentence_checker('.this is Gramatically incorrect?')
    assert result == False