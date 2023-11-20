from lib.diary import Diary
from lib.diary_entry_class import DiaryEntry

"""
Create two diary entries and add them to the diary.
Return the list of diary entries
"""
def test_create_add_two_entries():
    diary = Diary()
    entry1 = DiaryEntry('Entry 1','Today has been a good day')
    entry2 = DiaryEntry('Entry 2','Today felt much longer. I am tired.')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.all() == [entry1,entry2]
"""
Create two diary entries.
Count the number of words in each diary entries contents.
Add these entries to the diary and count the number of words in all entries
"""
def test_create_count_then_add_then_count_total_words():
    diary = Diary()
    entry1 = DiaryEntry('Entry 1','Today has been a good day')
    entry2 = DiaryEntry('Entry 2','Today felt much longer. I am tired.')
    words_entry_1 = entry1.count_words()
    words_entry_2 = entry2.count_words()
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == words_entry_1 + words_entry_2
"""
Create a diary entry and add them to the diary.
Calculate the reading time for the entry
"""
def test_reading_time_for_one_entry():
    entry1 = DiaryEntry('Entry 1','Today has been a good day')
    assert entry1.reading_time(2) == 3

"""
Create two diary entries and add them to the diary.
Calculate the reading time for the entire diary
"""
def test_reading_time_for_multiple_entries():
    diary = Diary()
    entry1 = DiaryEntry('Entry 1','Today has been a good day')
    entry2 = DiaryEntry('Entry 2','Today felt much longer. I am tired.')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.reading_time(2) == 7

"""
Create a diary entry.
return the first reading chunk on first call.
return the next reading chunk on second call.
return the first reading chunk on third call.
"""
def test_reading_chunk_for_entry():
    entry1 = DiaryEntry('Entry 1','Today has been a very good day')
    assert entry1.reading_chunk(2,1) == 'Today has'
    assert entry1.reading_chunk(2,1) == 'been a'
    assert entry1.reading_chunk(2,1) == 'very good'
    assert entry1.reading_chunk(2,1) == 'day'
    assert entry1.reading_chunk(2,1) == 'Today has'

"""
Create four diary entries of varying length and add them to the diary.
Return the best entry for reading time.
"""
def test_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry('Entry 1','Today has been a good day')
    entry2 = DiaryEntry('Entry 2','Today felt much longer. I am tired.')
    entry3 = DiaryEntry('Entry 3','I am not at work today or tomorrow.')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    assert diary.find_best_entry_for_reading_time(2,4) == 'I am not at work today or tomorrow.'
