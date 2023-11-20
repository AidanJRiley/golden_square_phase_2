def todo_checker(words):
    if type(words) != str:
        raise Exception('Not a string!')
    if '#TODO' in words.upper():
        return True
    else:
        return False