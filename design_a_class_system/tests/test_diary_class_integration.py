import pytest
from lib.contacts_class import Contact
from lib.diary_class import Diary
from lib.diary_entries_class import DiaryEntry
from lib.todo_class import ToDo

def test_create_diary_todo_contact_entries():
    diary = Diary()
    entry1 = DiaryEntry('Monday','Today I went shopping')
    todo1 = ToDo('Walk the dog')
    contact1 = Contact('Aidan','07532831661')
    diary.add_diary_entry(entry1)
    diary.add_todo_entry(todo1)
    diary.add_contact_entry(contact1)
    assert diary.diary_entries == [entry1]
    assert diary.see_diary_entries() == [entry1]
    assert diary.todo_list == [todo1]
    assert diary.see_todo_list() == [todo1]
    assert diary.contact_list == [contact1]
    assert diary.see_contacts_list() == [contact1]

def test_create_multiple_diary_todo_contact_entries():
    diary = Diary()
    entry1 = DiaryEntry('Monday','Today I went shopping')
    entry2 = DiaryEntry('Tuesday','It snowed today')
    todo1 = ToDo('Walk the dog')
    todo2 = ToDo('Clean the floor')
    contact1 = Contact('Aidan','07532831661')
    contact2 = Contact('Holly','07536826001')
    diary.add_diary_entry(entry1)
    diary.add_diary_entry(entry2)
    diary.add_todo_entry(todo1)
    diary.add_todo_entry(todo2)
    diary.add_contact_entry(contact1)
    diary.add_contact_entry(contact2)
    assert diary.diary_entries == [entry1,entry2]
    assert diary.see_diary_entries() == [entry1,entry2]
    assert diary.todo_list == [todo1,todo2]
    assert diary.see_todo_list() == [todo1,todo2]
    assert diary.contact_list == [contact1,contact2]
    assert diary.see_contacts_list() == [contact1,contact2]

def test_see_all_entries():
    diary = Diary()
    entry1 = DiaryEntry('Monday','Today I went shopping')
    entry2 = DiaryEntry('Tuesday','It snowed today')
    todo1 = ToDo('Walk the dog')
    todo2 = ToDo('Clean the floor')
    contact1 = Contact('Aidan','07532831661')
    contact2 = Contact('Holly','07536826001')
    diary.add_diary_entry(entry1)
    diary.add_diary_entry(entry2)
    diary.add_todo_entry(todo1)
    diary.add_todo_entry(todo2)
    diary.add_contact_entry(contact1)
    diary.add_contact_entry(contact2)
    all_entries = {'Diary Entries:':diary.diary_entries,'ToDo List:':diary.todo_list,'Contacts List:':diary.contact_list}
    assert diary.see_all_entries() == all_entries

def test_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry('Entry 1','Today has been a good day')
    entry2 = DiaryEntry('Entry 2','Today felt much longer. I am tired.')
    entry3 = DiaryEntry('Entry 3','I am not at work today or tomorrow.')
    diary.add_diary_entry(entry1)
    diary.add_diary_entry(entry2)
    diary.add_diary_entry(entry3)
    assert diary.diary_entry_with_best_reading_time(2,4) == 'I am not at work today or tomorrow.'

def test_todo_lists_tasks():
    task1 = ToDo('wash dishes')
    task2 = ToDo('walk dog')
    task3 = ToDo('mop floor')
    diary = Diary()
    diary.add_todo_entry(task1)
    diary.add_todo_entry(task2)
    diary.add_todo_entry(task3)
    assert diary.todo_list == [task1,task2,task3]


def test_todo_marks_complete():
    diary = Diary()
    task1 = ToDo('wash dishes')
    task2 = ToDo('walk dog')
    task3 = ToDo('mop floor')
    diary.add_todo_entry(task1)
    diary.add_todo_entry(task2)
    diary.add_todo_entry(task3)
    diary.todo_list[1].mark_complete()
    assert diary.todo_list[1].complete == True

def test_show_incomplete_todos():
    diary = Diary()
    task1 = ToDo("Walk the dog")
    task2 = ToDo('Bake a cake')
    diary.add_todo_entry(task1)
    diary.add_todo_entry(task2)
    diary.todo_list[1].mark_complete()
    incomplete_tasks = diary.see_incomplete_todos()
    assert incomplete_tasks == [task1.task]

def test_show_complete_todos():
    diary = Diary()
    task1 = ToDo("Walk the dog")
    task2 = ToDo('Bake a cake')
    diary.add_todo_entry(task1)
    diary.add_todo_entry(task2)
    diary.todo_list[1].mark_complete()
    complete_tasks = diary.see_complete_todos()
    assert complete_tasks == [task2.task]

def test_give_up():
    diary = Diary()
    task1 = ToDo("Walk the dog")
    task2 = ToDo('Bake a cake')
    diary.add_todo_entry(task1)
    diary.add_todo_entry(task2)
    diary.give_up()
    complete_tasks = diary.see_complete_todos()
    incomplete_tasks = diary.see_incomplete_todos()
    assert complete_tasks == [task1.task, task2.task]
    assert incomplete_tasks == []