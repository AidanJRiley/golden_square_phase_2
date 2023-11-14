def sentence_checker(string):
    if type(string) != str:
        raise Exception('This is not a string!')
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sentence_enders = '!?.'
    if string[0] in capital_letters and string[-1] in sentence_enders:
        return True
    else:
        return False