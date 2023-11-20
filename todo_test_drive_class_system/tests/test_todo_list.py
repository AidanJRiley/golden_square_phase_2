import pytest
from lib.todo_list import *
from lib.to_do import *

def test_todo_lists_exists():
    todo_list = TodoList()
    assert todo_list.list_of_todos == []

def test_add_to_incomplete_list():
    todo_list = TodoList()
    # task1 = {'Walk the dog': False}
    task1 = Todo("Walk the dog")
    todo_list.add(task1)
    assert todo_list.list_of_todos == [task1]

# def test_given_non_string_list():
#     todo_list = TodoList()
#     task1 = ['Walk','the','dog']
#     with pytest.raises(Exception) as e:
#         todo_list.add(task1)
#     error_message = str(e.value)
#     assert error_message == 'Not valid!'

# def test_given_empty_string():
#     todo_list = TodoList()
#     task1 = ""
#     with pytest.raises(Exception) as e:
#         todo_list.add(task1)
#     error_message = str(e.value)
#     assert error_message == 'Not valid!'

def test_show_incomplete_todo_list():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    task2 = Todo('Bake a cake')

    # task1 = {'Walk the dog': False}
    # task2 = {'Bake a cake': False}
    todo_list.add(task1)
    todo_list.add(task2)
    assert todo_list.list_of_todos == [task1, task2]