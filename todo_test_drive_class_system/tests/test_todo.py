import sys
print(sys.path)
from lib.to_do import *
def test_todo_exists():
    task1 = 'wash dishes'
    new_todo = Todo(task1)
    assert new_todo.task == task1
    assert new_todo.complete == False 

def test_todo_complete():
    task1 = 'wash dishes'
    new_todo = Todo(task1)
    new_todo.mark_complete()
    assert new_todo.complete == True




