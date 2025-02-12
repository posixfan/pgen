#!/usr/bin/env python3
import random
import string
import argparse

def generate_password(length=12):
    first_char = random.choice(string.ascii_letters)
    rest_chars = ''.join(
        random.choice(string.ascii_letters + string.digits + string.punctuation)
        for _ in range(length - 1))
    password = first_char + rest_chars
    return password

def main():
    parser = argparse.ArgumentParser(
        description='A password generator conforming to the NIST 800-63B standard.')
    parser.add_argument('length', type=int, nargs='?', default=12,
                        help='Password length (default is 12)')
    parser.add_argument('number', type=int, nargs='?', default=1,
                        help='Number of passwords (1 by default)')

    args = parser.parse_args()

    if args.length < 8:
        print('The password must be at least 8 characters long.')
        return

    for _ in range(args.number):
        print(generate_password(args.length))

if __name__ == "__main__":
    main()
