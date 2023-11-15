import pytest
from lib.grammar_stats import *

"""
Given an integer (non-string)
Returns 'This is not a string!'
"""
def test_grammar_stats_check_for_integer():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check(100)
    error_message = str(e.value)
    assert error_message == 'This is not a string!'

"""
Given a list (non-string)
Returns 'This is not a string!'
"""
def test_grammar_stats_check_for_list():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check(['This','is','a','sentence.'])
    error_message = str(e.value)
    assert error_message == 'This is not a string!'

"""
Given a sentence that starts with a capital letter
and ends with suitable punctuation
Returns true
"""
def test_grammar_stats_check_for_correct_sentence():
    grammar_stats = GrammarStats()
    result = grammar_stats.check('This is a sentence.')
    assert result == True

"""
Given a sentence that starts with a capital letter
and ends with suitable punctuation
Returns true
"""
def test_grammar_stats_check_for_correct_sentence_exclamation_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check('This is a sentence!')
    assert result == True

def test_sentence_checker_gramatically_incorrect_no_fullstop():
    grammar_stats = GrammarStats()
    result = grammar_stats.check('This is gramatically incorrect')
    assert result == False

def test_sentence_checker_gramatically_incorrect_wrong_chars():
    grammar_stats = GrammarStats()
    result = grammar_stats.check('.this is Gramatically incorrect?')
    assert result == False

"""
Give it one correct sentence and one incorrect
percentage_good should return 50
"""
def test_percentage_good_50():
    grammar_stats = GrammarStats()
    grammar_stats.check('This is a sentence!')
    grammar_stats.check('this is a sentence')
    result = grammar_stats.percentage_good()
    assert result == 50

"""
Give it no sentences
percentage_good should return 'There have been no checks completed'
"""
def test_percentage_good_no_tests():
    grammar_stats = GrammarStats()
    result = grammar_stats.percentage_good()
    assert result == 'There have been no checks completed'

"""
Give it one incorrect sentence
percentage_good should return 0
"""
def test_percentage_good_0():
    grammar_stats = GrammarStats()
    grammar_stats.check('bad sentence')
    result = grammar_stats.percentage_good()
    assert result == 0

"""
Give it two correct sentences
percentage_good should return 100
"""
def test_percentage_good_100():
    grammar_stats = GrammarStats()
    grammar_stats.check('This is a sentence!')
    grammar_stats.check('This is a sentence!')
    result = grammar_stats.percentage_good()
    assert result == 100

"""
Give it 5 correct sentences
4 incorrect
percentage_good should return 
"""
def test_percentage_good_100():
    grammar_stats = GrammarStats()
    grammar_stats.check('This is a sentence!')
    grammar_stats.check('This is a sentence!')
    grammar_stats.check('This is a sentence!')
    grammar_stats.check('This is a sentence!')
    grammar_stats.check('This is a sentence!')
    grammar_stats.check('his is a sentence')
    grammar_stats.check('his is a sentence')
    grammar_stats.check('his is a sentence')
    grammar_stats.check('his is a sentence')
    result = grammar_stats.percentage_good()
    assert result == 56