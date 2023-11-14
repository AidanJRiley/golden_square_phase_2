import pytest
from lib.calculate_reading_time import *

def test_on_number():
    with pytest.raises(Exception) as e:
        calculate_reading_time(100)
    error_message = str(e.value)
    assert error_message == 'This is not a string!'

def test_on_None():
    with pytest.raises(Exception) as e:
        calculate_reading_time(None)
    error_message = str(e.value)
    assert error_message == 'This is not a string!'

def test_on_list():
    with pytest.raises(Exception) as e:
        calculate_reading_time(['1','2','3'])
    error_message = str(e.value)
    assert error_message == 'This is not a string!'

def test_on_dictionary():
    with pytest.raises(Exception) as e:
        calculate_reading_time({'1':'2','3':'4'})
    error_message = str(e.value)
    assert error_message == 'This is not a string!'

def test_length_200():
    result = calculate_reading_time('a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a')
    assert result == '1 minute 0 seconds'

def test_length_100():
    result = calculate_reading_time('a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a ')
    assert result == '0 minutes 30 seconds'

def test_length_500():
    result = calculate_reading_time('a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a')
    assert result == '2 minutes 30 seconds'

def test_length_0():
    result = calculate_reading_time('')
    assert result == '0 minutes 0 seconds'