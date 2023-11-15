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
