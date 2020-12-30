import re

def is_valid(isbn):
    wo_isbn = isbn.replace("-", "")
    if len(wo_isbn) != 10:
        return False
    if not bool(re.match("[0-9X]{10}", wo_isbn)):
        return False

    sum = 0
    for i, n in enumerate(isbn.replace("-", "")[::-1]):
        if i !=0 and n == 'X':
            return False
        if n == 'X':
            n = '10'
        sum += int(n) * (i+1)

    print(sum)
    print(sum % 11)
    return bool(sum % 11 == 0)


if __name__ == '__main__':
    is_valid("3-598-2X507-9")