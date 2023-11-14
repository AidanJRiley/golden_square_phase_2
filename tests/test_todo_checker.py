import pytest
from lib.todo_checker import *

def test_todo_checker_for_nonstring_None():
    with pytest.raises(Exception) as e:
        todo_checker(None)
    error_message = str(e.value)
    assert error_message == 'Not a string!'

def test_todo_checker_for_nonstring_number():
    with pytest.raises(Exception) as e:
        todo_checker(7)
    error_message = str(e.value)
    assert error_message == 'Not a string!'

def test_todo_checker_for_nonstring_list():
    with pytest.raises(Exception) as e:
        todo_checker(['this is a string'])
    error_message = str(e.value)
    assert error_message == 'Not a string!'

def test_todo_checker_for_todo():
    result = todo_checker('#TODO Water the plants')
    assert result == True

def test_todo_checker_for_no_todo():
    result = todo_checker('Wash the dishes')
    assert result == False

def test_todo_checker_for_incorrect_todo():
    result = todo_checker('TODO Wash the dog')
    assert result == False

def test_todo_checker_for_todo_at_end():
    result = todo_checker('Feed the dog #TODO')
    assert result == True

def test_todo_checker_for_lowercase_todo():
    result = todo_checker('#todo get my capslock key fixed')
    assert result == True