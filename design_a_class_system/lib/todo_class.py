class ToDo:
    def __init__(self, task):
        if task == '':
            raise Exception('Task is empty!')
        elif type(task) != str:
            raise Exception('Task must be a string!')
        self.task = task
        self.complete = False

    def mark_complete(self):
        self.complete = True