class Diary:
    def __init__(self):
        #initialisation variable, sets empty lists for diary entries, todo list and contacts
        self.diary_entries = []
        self.todo_list = []
        self.contact_list = []

    def add_diary_entry(self, entry):
        #adds diary entry to list of diary entries
        entry.contacts = self.contact_list.copy()
        entry.__dict__.pop('read_so_far')
        self.diary_entries.append(entry)

    def see_diary_entries(self):
        #returns a list of diary entries
        return self.diary_entries

    def add_todo_entry(self, entry):
        #adds todo entry to list of todo entries
        self.todo_list.append(entry)

    def see_todo_list(self):
        #returns a list of tasks in todo list
        return self.todo_list
    
    def see_incomplete_todos(self):
        return [todo.task for todo in self.todo_list if todo.complete == False]

    def see_complete_todos(self):
        return [todo.task for todo in self.todo_list if todo.complete == True]
    
    def give_up(self):
        for todo in self.todo_list:
            todo.mark_complete()

    def add_contact_entry(self, entry):
        #adds contact to list of contacts
        self.contact_list.append(entry)

    def see_contacts_list(self):
        #returns a list of contacts
        return self.contact_list

    def diary_entry_with_best_reading_time(self, wpm, minutes):
        #given a reading speed and number of minutes, reccomends the longest diary entry for the time available
        total_words_that_can_be_read = wpm*minutes
        best_entry = ''
        for entry in self.diary_entries:
            if entry.count_contents_words() <= total_words_that_can_be_read and entry.count_total_words() > len(best_entry.split()):
                best_entry = entry.contents
        return best_entry

    def see_all_entries(self):
        #returns a list of diary entries, todos and contacts
        all_entries = {'Diary Entries:':self.diary_entries,'ToDo List:':self.todo_list,'Contacts List:':self.contact_list}
        return all_entries
