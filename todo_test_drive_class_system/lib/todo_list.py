from lib.to_do import *
class TodoList:
    def __init__(self):
        self.list_of_todos = []
        pass

    def add(self, todo):
        self.list_of_todos.append(todo)

    def incomplete(self):
        return [todo.task for todo in self.list_of_todos if todo.complete == False]

    def complete(self):
        return [todo.task for todo in self.list_of_todos if todo.complete == True]

    def give_up(self):
        for todo in self.list_of_todos:
            todo.mark_complete()
        
