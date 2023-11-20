import pytest
from lib.diary_class import *

def test_diary_todo_contact_exists():
    diary = Diary()
    assert diary.diary_entries == []
    assert diary.todo_list == []
    assert diary.contact_list == []

def test_seeing_diary_todo_contact():
    diary = Diary()
    diary.diary_entries = ['test diary entries']
    diary.todo_list = ['test todo entries']
    diary.contact_list = ['test contact entries']
    assert diary.see_diary_entries() == ['test diary entries']
    assert diary.see_todo_list() == ['test todo entries']
    assert diary.see_contacts_list() == ['test contact entries']

def test_seeing_all():
    diary = Diary()
    diary.diary_entries = ['test diary entries']
    diary.todo_list = ['test todo entries']
    diary.contact_list = ['test contact entries']
    all_entries = {'Diary Entries:':diary.diary_entries,'ToDo List:':diary.todo_list,'Contacts List:':diary.contact_list}
    assert diary.see_all_entries() == all_entries