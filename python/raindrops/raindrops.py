def convert(number):
    str_list = []
    if number % 3 == 0:
        str_list.append('Pling')
    if number % 5 == 0:
        str_list.append('Plang')
    if number % 7 == 0:
        str_list.append('Plong')

    if not str_list: # list is empty
        return str(number)
    return ''.join(str_list)