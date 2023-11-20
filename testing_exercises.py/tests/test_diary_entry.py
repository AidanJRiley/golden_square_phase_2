import pytest
from lib.diary_entry import *

"""
Given a title and contents
#format returns a formatted entry like:
"My Title: These are the contents"
"""

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry('My Title',"Some contents")
    result = diary_entry.format()
    assert result == 'My Title: Some contents'

"""
Given an empty title
# Raise an error
"""
def test_errors_on_empty_title():
    with pytest.raises(Exception) as e:
        DiaryEntry('','this is contents')
    assert str(e.value) == 'Diary entries must have a title and contents'

"""
Given an empty contents
# Raise an error
"""
def test_errors_on_empty_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry('My Title','')
    assert str(e.value) == 'Diary entries must have a title and contents'




"""
Given a title and a contents
#count_words returns the number of words (integer) in title and contents
"""

def test_count_words_in_contents():
    diary_entry = DiaryEntry('My Title',"Some contents")
    result = diary_entry.count_words()
    assert result == 4

"""
Given a words per minute integer of 2
and a contents with 4 words
Returns an estimate of reading time in minutes for the contents
"""
def test_reading_time_with_2_wpm_and_4_words():
    diary_entry = DiaryEntry('My Title','Some contents wrote here')
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given a words per minute integer of 2
and a contents with 3 words
Returns an estimate of reading time in minutes for the contents
Minutes rounded up
"""
def test_reading_time_with_2_wpm_and_3_words():
    diary_entry = DiaryEntry('My Title','Some contents here')
    result = diary_entry.reading_time(2)
    assert result == 2

"""
Given a words per minute integer of 0
Raises an error
"""
def test_reading_time_with_0_wpm():
    diary_entry = DiaryEntry('My Title','Some contents here')
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    error_message = str(e.value)
    assert error_message == "Cannot calculate reading time with wpm of 0"

"""
Given a contents of six words
and a wpm of 2
and a minutes of 1
#reading chunk returns the first two words
"""

def test_reading_chunk_with_two_wpm_and_one_minutes():
    diary_entry = DiaryEntry('My Title','one two three four five six')
    result = diary_entry.reading_chunk(2,1)
    assert result == 'one two'

"""
Given a contents of six words
and a wpm of 2
and a minutes of 2
#reading chunk returns the first four words
"""

def test_reading_chunk_with_two_wpm_and_two_minutes():
    diary_entry = DiaryEntry('My Title','one two three four five six')
    result = diary_entry.reading_chunk(2,2)
    assert result == 'one two three four'

"""
Given a contents of six words
and a wpm of 2
and a minutes of 1
#reading chunk call 1 returns the first two words
#reading chunk call 2 returns the next two words
#reading chunk call 3 returns the next two words
"""
def test_reading_chunk_with_two_wpm_and_one_minute_called_twice():
    diary_entry = DiaryEntry('My Title','one two three four five six')
    assert diary_entry.reading_chunk(2,1) == 'one two'
    assert diary_entry.reading_chunk(2,1) == 'three four'
    assert diary_entry.reading_chunk(2,1) == 'five six'

"""
Given a contents of six words
and a changing wpm
and a minutes of 1
#reading chunk call 1 returns the first two words
#reading chunk call 2 returns the next word
#reading chunk call 3 returns the next three words
"""
def test_reading_multiple_chunks_with_changing_wpm():
    diary_entry = DiaryEntry('My Title','one two three four five six')
    assert diary_entry.reading_chunk(2,1) == 'one two'
    assert diary_entry.reading_chunk(1,1) == 'three'
    assert diary_entry.reading_chunk(3,1) == 'four five six'

"""
Given a contents of six words
and a wpm of 2
and a minutes of 1
#reading chunk call 1 returns the first two words
#reading chunk call 2 returns the next word
#reading chunk call 3 returns the next three words
#After the text has been read the next call starts at the beginning again
#reading chunk call 4 returns the first word
"""
def test_reading_multiple_chunks_with_changing_wpm_wrap_around():
    diary_entry = DiaryEntry('My Title','one two three four five six')
    assert diary_entry.reading_chunk(2,2) == 'one two three four'
    assert diary_entry.reading_chunk(2,2) == 'five six'
    assert diary_entry.reading_chunk(2,2) == 'one two three four'

"""
Given a contents of six words
if #reading_chunk is called repeatedly with an exact ending
The last chunk is the last words in the text
The next chunk after that is at the start again
"""
def test_reading_multiple_chunks_with_changing_wpm_wrap_around_exact():
    diary_entry = DiaryEntry('My Title','one two three four five six')
    assert diary_entry.reading_chunk(2,2) == 'one two three four'
    assert diary_entry.reading_chunk(2,1) == 'five six'
    assert diary_entry.reading_chunk(2,2) == 'one two three four'