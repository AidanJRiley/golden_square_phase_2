import math

def calculate_reading_time(text):
    if type(text) != str:
        raise Exception('This is not a string!')
    number_of_words = len(text.split(' '))
    reading_time_float = float(number_of_words/200)
    reading_time_mins = math.floor(reading_time_float)
    reading_time_secs = int((reading_time_float - float(reading_time_mins)) * 60)
    
    if reading_time_mins == 1:
        min = 'minute'
    else:
        min = 'minutes'
    
    if reading_time_secs == 1:
        sec = 'second'
    else:
        sec = 'seconds'

    return f'{reading_time_mins} {min} {reading_time_secs} {sec}'