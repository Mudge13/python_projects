import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + f'{query_char}'

    res = requests.get(url)

    if res.status_code != 200:
        raise Exception("Response is 400, y not working?")

    return res


def check_res(hashes, hash_to_check):
    hash_list_gen = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hash_list_gen:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char = sha1_password[:5]
    tail = sha1_password[5:]
    response = request_api_data(first5_char)
    return check_res(response, tail)


def main():
    enter_passwords = input("Enter passwords to check: ")
    for password in enter_passwords.split(" "):
        count = pwned_api_check(password)
        if count:
            print(f"Oh no {password} was found {count} time, Change it dummy")
        else:
            print(f'Nice {password} was Not found, till now that is')
    print("anything else boss 😎")


main()
