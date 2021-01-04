def decode(string):

    # Check String is empty
    if not string:
        return string


def encode(string):
    en_str = ""

    # Check String is empty
    if not string:
        return string

    string += "." # Character end of string
    i = 1
    while True:
        if string[i] == ".": # Break Loop if end of string
            break
        if string[i-1] != ',' and string[i] != string[i-1]:
            string = string[:i] + "," + string[i:]
        i += 1

    string = string[:len(string)-1] # delete character end of string

    for i in string.split(","):
        if len(i) == 1:
            en_str += i[0]
        else:
            en_str += str(len(i)) + i[0]

    return en_str