import sys

from Palindrome import check_palindrome

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("python main.py word")
        print("where just one word will be tested as a palindrome")
        sys.exit(0)

    word = sys.argv[1]
    check_palindrome(word)