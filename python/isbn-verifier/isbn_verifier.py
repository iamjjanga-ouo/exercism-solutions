import re

def is_valid(isbn):
    wo_isbn = isbn.replace("-", "") # delete hypen

    if len(wo_isbn) != 10:
        return False
    if not bool(re.match("[0-9]{9}[0-9X]", wo_isbn)): # type only 9 digits + check Character 'X' (locate only last in the words)
        return False                                  # or 10 digits

    res = sum([10*(i+1) if n == 'X' else int(n)*(i+1)
               for i, n in enumerate(wo_isbn[::-1])])

    return bool(res % 11 == 0)