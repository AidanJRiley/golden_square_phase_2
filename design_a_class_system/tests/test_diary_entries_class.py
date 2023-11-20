import pytest
from lib.diary_entries_class import *

def test_for_nonstring_given():
    with pytest.raises(Exception) as e:
        diary = DiaryEntry('Aidan', 100)
    error_message = str(e.value)
    assert error_message == 'Both values must be a string!'

def test_for_empty_string_given():
    with pytest.raises(Exception) as e:
        diary = DiaryEntry('', '')
    error_message = str(e.value)
    assert error_message == 'Diary entries must have a title and contents'

def test_errors_on_empty_title():
    with pytest.raises(Exception) as e:
        DiaryEntry('','this is contents')
    assert str(e.value) == 'Diary entries must have a title and contents'

def test_errors_on_empty_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry('My Title','')
    assert str(e.value) == 'Diary entries must have a title and contents'

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry('My Title',"Some contents")
    result = diary_entry.format()
    assert result == 'My Title: Some contents'

def test_count_words_in_contents():
    diary_entry = DiaryEntry('My Title',"Some contents")
    result = diary_entry.count_total_words()
    assert result == 4

def test_reading_time_with_2_wpm_and_4_words():
    diary_entry = DiaryEntry('My Title','Some contents wrote here')
    result = diary_entry.reading_time(2)
    assert result == 2

def test_reading_time_with_2_wpm_and_3_words():
    diary_entry = DiaryEntry('My Title','Some contents here')
    result = diary_entry.reading_time(2)
    assert result == 2

def test_reading_time_with_0_wpm():
    diary_entry = DiaryEntry('My Title','Some contents here')
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    error_message = str(e.value)
    assert error_message == "Cannot calculate reading time with wpm of 0"

def test_reading_chunk_with_two_wpm_and_one_minutes():
    diary_entry = DiaryEntry('My Title','one two three four five six')
    result = diary_entry.reading_chunk(2,1)
    assert result == 'one two'

def test_reading_chunk_with_two_wpm_and_two_minutes():
    diary_entry = DiaryEntry('My Title','one two three four five six')
    result = diary_entry.reading_chunk(2,2)
    assert result == 'one two three four'

def test_reading_chunk_with_two_wpm_and_one_minute_called_twice():
    diary_entry = DiaryEntry('My Title','one two three four five six')
    assert diary_entry.reading_chunk(2,1) == 'one two'
    assert diary_entry.reading_chunk(2,1) == 'three four'
    assert diary_entry.reading_chunk(2,1) == 'five six'

def test_reading_multiple_chunks_with_changing_wpm():
    diary_entry = DiaryEntry('My Title','one two three four five six')
    assert diary_entry.reading_chunk(2,1) == 'one two'
    assert diary_entry.reading_chunk(1,1) == 'three'
    assert diary_entry.reading_chunk(3,1) == 'four five six'

def test_reading_multiple_chunks_with_changing_wpm_wrap_around():
    diary_entry = DiaryEntry('My Title','one two three four five six')
    assert diary_entry.reading_chunk(2,2) == 'one two three four'
    assert diary_entry.reading_chunk(2,2) == 'five six'
    assert diary_entry.reading_chunk(2,2) == 'one two three four'

def test_reading_multiple_chunks_with_changing_wpm_wrap_around_exact():
    diary_entry = DiaryEntry('My Title','one two three four five six')
    assert diary_entry.reading_chunk(2,2) == 'one two three four'
    assert diary_entry.reading_chunk(2,1) == 'five six'
    assert diary_entry.reading_chunk(2,2) == 'one two three four'