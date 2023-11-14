#Exercise 1
def say_hello(name):
    return f"hello {name}"

# print(say_hello('Kay'))

#Exercise 2
def encode(text, key):
    cipher = make_cipher(key)
    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        #chr(num)
        ciphertext_chars.append(ciphered_char)
    # print(ciphertext_chars)
    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)
    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i)-65]
        #ord(i) == num
        #num - 65 == cipher.index(i)
        plaintext_chars.append(plain_char)
    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 98) for i in range(-1, 26)]
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# print(encode("theswiftfoxjumpedoverthelazydog", "secretkey"))
# print('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL' == 'EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL')
# print(decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey"))
# print("theswiftfoxjumpedoverthelazydog" == 'theswiftfoxjumpedoverthelazydog')

# End of section challenge 
import re
def get_most_common_letter(text):
    counter = {}
    text = re.sub(r"[^a-zA-Z]", "", text)
    for char in text:
        counter[char] = counter.get(char, 0) + 1
        print(counter)
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    # print(counter.items())
    # print(sorted(counter.items(), key=lambda item: item[1])[-1][0])
    return letter


# print(f"""
# Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
# Expected: o
# Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
# """)

print(get_most_common_letter("the roof, the roof, the roof is on fire!"))
