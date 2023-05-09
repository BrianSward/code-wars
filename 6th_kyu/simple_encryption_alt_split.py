# https://www.codewars.com/kata/57814d79a56c88e3e0000786/python
# DESCRIPTION:
# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

# Examples:

# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption function which reverses the process.

# If the string S is an empty value or the integer N is not positive, return the first argument without changes.

def decrypt(encrypted_text, n):
    text_bucket = encrypted_text
    if n <= 0:
        return text_bucket
    while n > 0:
        return_me = ""
        odd_bucket = ""
        even_bucket = ""
        for i,v in enumerate(text_bucket):
            if i > (len(text_bucket) / 2) -1 :
                even_bucket += v
            else:
                odd_bucket += v
        for x in range(0, len(encrypted_text)):
            if x % 2 == 0:
                return_me += even_bucket[x//2]
            else:
                return_me += odd_bucket[x//2]
        text_bucket = return_me
        n += -1
    return return_me


def encrypt(text, n):
    odd_bucket = ""
    even_bucket = ""
    text_bucket = text
    if n <= 0:
        return text
    while n > 0:
        odd_bucket = ""
        even_bucket = ""
        for i,v in enumerate(text_bucket):
            if i % 2 == 0:
                even_bucket += v
            else:
                odd_bucket += v
        text_bucket = odd_bucket + even_bucket
        n += -1
    return text_bucket