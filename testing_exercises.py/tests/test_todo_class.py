import pytest
from lib.todo_class import *

def test_empty_todo():
    todo = ToDo()
    with pytest.raises(Exception) as e:
        todo.show_todo_list()
    error_message = str(e.value)
    assert error_message == 'ToDo list is empty'

def test_not_string():
    todo = ToDo()
    with pytest.raises(Exception) as e:
        todo.add_task(123)
    error_message = str(e.value)
    assert error_message == 'Task must be a valid string'

def test_one_task():
    todo = ToDo()
    todo.add_task('Bake a cake')
    assert todo.show_todo_list() == ['Bake a cake']

def test_three_task():
    todo = ToDo()
    todo.add_task('Bake a cake')
    todo.add_task('Water plants')
    todo.add_task('Eat chocolate')
    assert todo.show_todo_list() == ['Bake a cake', 'Water plants', 'Eat chocolate']

def test_add_two_remove_not_task():
    todo = ToDo()
    todo.add_task('Bake a cake')
    todo.add_task('Water plants')
    todo.add_task('Eat chocolate')
    with pytest.raises(Exception) as e:
        todo.remove_completed_tasks('Walk the dog')
    error_message = str(e.value)
    assert error_message == 'This task is not in the ToDo'

def test_add_three_remove_one():
    todo = ToDo()
    todo.add_task('Bake a cake')
    todo.add_task('Water plants')
    todo.add_task('Eat chocolate')
    todo.remove_completed_tasks('Bake a cake')
    assert todo.show_todo_list() == ['Water plants', 'Eat chocolate']


def test_add_and_remove():
    todo = ToDo()
    todo.add_task('Bake a cake')
    todo.remove_completed_tasks('Bake a cake')
    with pytest.raises(Exception) as e:
        todo.show_todo_list()
    error_message = str(e.value)
    assert error_message == 'ToDo list is empty'