"""Checks if a string is a palindrome"""


def is_palindrome(s: str) -> bool:
    """Returns True if s is a palindrome, False otherwise"""
    return s == s[::-1]         # check if the string is equal to its reverse