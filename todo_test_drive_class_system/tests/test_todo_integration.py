from lib.to_do import *
from lib.todo_list import *

def test_todo_lists_tasks():
    task1 = Todo('wash dishes')
    task2 = Todo('walk dog')
    task3 = Todo('mop floor')
    new_list = TodoList()
    new_list.add(task1)
    new_list.add(task2)
    new_list.add(task3)
    assert new_list.list_of_todos == [task1,task2,task3]


def test_todo_marks_complete():
    new_list = TodoList()
    task1 = Todo('wash dishes')
    task2 = Todo('walk dog')
    task3 = Todo('mop floor')

    new_list.add(task1)
    new_list.add(task2)
    new_list.add(task3)
    new_list.list_of_todos[1].mark_complete()
    print(new_list.list_of_todos[1].task)

    print(new_list.list_of_todos[1].complete)
    print(new_list.list_of_todos[0].complete)

    print(task2.complete)
    # print(task2.todo)
    print(new_list.list_of_todos)
    assert new_list.list_of_todos[1].complete == True

def test_show_incomplete_todos():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    task2 = Todo('Bake a cake')
    todo_list.add(task1)
    todo_list.add(task2)
    print(vars(todo_list))
    todo_list.list_of_todos[1].mark_complete()
    incomplete_tasks = todo_list.incomplete()
    assert incomplete_tasks == [task1.task]

def test_show_incomplete_todos():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    task2 = Todo('Bake a cake')
    todo_list.add(task1)
    todo_list.add(task2)
    print(vars(todo_list))
    todo_list.list_of_todos[1].mark_complete()
    complete_tasks = todo_list.complete()
    assert complete_tasks == [task2.task]

def test_give_up():
    todo_list = TodoList()
    task1 = Todo("Walk the dog")
    task2 = Todo('Bake a cake')
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.give_up()
    complete_tasks = todo_list.complete()
    incomplete_tasks = todo_list.incomplete()
    assert complete_tasks == [task1.task, task2.task]
    assert incomplete_tasks == []