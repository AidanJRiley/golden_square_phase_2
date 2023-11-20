import pytest
from lib.todo_class import *

def test_create_empty_todo():
    with pytest.raises(Exception) as e:
        todo = ToDo('')
    error_message = str(e.value)
    assert error_message == 'Task is empty!'

def test_not_string():
    with pytest.raises(Exception) as e:
        todo = ToDo(123)
    error_message = str(e.value)
    assert error_message == 'Task must be a string!'

def test_one_task():
    todo = ToDo('Bake a cake')
    assert todo.task == 'Bake a cake'
    assert todo.complete == False

def test_create_then_mark_complete():
    todo = ToDo('Bake a cake')
    todo.mark_complete()
    assert todo.task == 'Bake a cake'
    assert todo.complete == True