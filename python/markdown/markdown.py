import re


def check_header(line):
    if re.match('###### (.*)', line) is not None:
        line = '<h6>' + line[7:] + '</h6>'
    elif re.match('## (.*)', line) is not None:
        line = '<h2>' + line[3:] + '</h2>'
    elif re.match('# (.*)', line) is not None:
        line = '<h1>' + line[2:] + '</h1>'
    return line


def check_list(line, in_list):
    m = re.match(r'\* (.*)', line)  # this code maybe check only unordered list
    if m: # List
        if not in_list: # List start
            in_list = True
            is_bold = False
            is_italic = False
            curr = m.group(1)
            ### is bold?
            curr, is_bold = check_bold(curr)
            ### is italic?
            curr, is_italic = check_italic(curr)
            line = '<ul><li>' + curr + '</li>'  # Unordered list open
        else:  # not List start
            is_bold = False
            is_italic = False
            curr = m.group(1)

            curr, is_bold = check_bold(curr)
            curr, is_italic = check_italic(curr)
            line = '<li>' + curr + '</li>'  # list
    else: # not List
        if in_list:
            in_list_append = True
            in_list = False

    return line

def check_bold(curr):
    rep = '(.*)[_*]{2}(.*)[_*]{2}(.*)'
    m1 = re.match(rep, curr)
    if m1:
        curr = m1.group(1) + '<strong>' + \
               m1.group(2) + '</strong>' + m1.group(3)
        return curr, True
    return curr, False


def check_italic(curr):
    rep = '(.*)[_*](.*)[_*](.*)'
    m1 = re.match(rep, curr)
    if m1:
        curr = m1.group(1) + '<em>' + m1.group(2) + \
               '</em>' + m1.group(3)
        return curr, True
    return curr, False


def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    for line in lines:
        ## is Header?
        line = check_header(line)
        ## is Lists?
        line = check_list(line)

        m = re.match('<h|<ul|<p|<li', line)
        ## just text
        if not m:
            line = '<p>' + line + '</p>'
        m = re.match('(.*)__(.*)__(.*)', line)
        ## Bold
        if m:
            line = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', line)
        ## italic
        if m:
            line = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        ## List append same depth
        if in_list_append:
            line = '</ul>' + line
            in_list_append = False
        res += line
    ## List append different depth
    if in_list:
        res += '</ul>'
    return res
