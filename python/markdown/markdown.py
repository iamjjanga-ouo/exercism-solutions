import re

def bold(rep, curr):
    m1 = re.match(rep, curr)
    if m1:
        curr = m1.group(1) + '<strong>' + \
               m1.group(2) + '</strong>' + m1.group(3)
        return curr, True
    return curr, False

def italic(rep, curr):
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
    for i in lines:
        ## is Headers?
        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'
        ## is Lists?
        m = re.match(r'\* (.*)', i) # this code maybe check only unordered list
        if m:
            if not in_list:
                in_list = True
                is_bold = False
                is_italic = False
                curr = m.group(1)
                ### is bold? (Emphasis)
                # m1 = re.match('(.*)__(.*)__(.*)', curr)
                # if m1:
                #     curr = m1.group(1) + '<strong>' + \
                #         m1.group(2) + '</strong>' + m1.group(3)
                #     is_bold = True
                curr, is_bold = bold('(.*)__(.*)__(.*)', curr)
                ### is italic? (Emphasis)
                # m1 = re.match('(.*)_(.*)_(.*)', curr)
                # if m1:
                #     curr = m1.group(1) + '<em>' + m1.group(2) + \
                #         '</em>' + m1.group(3)
                #     is_italic = True
                curr, is_italic = italic('(.*)_(.*)_(.*)', curr)
                i = '<ul><li>' + curr + '</li>' # Unordered list open
            else: # not Lists
                is_bold = False
                is_italic = False
                curr = m.group(1)
                # m1 = re.match('(.*)__(.*)__(.*)', curr)
                # if m1:
                #     is_bold = True
                # m1 = re.match('(.*)_(.*)_(.*)', curr)
                # if m1:
                #     is_italic = True
                # if is_bold:
                #     curr = m1.group(1) + '<strong>' + \
                #         m1.group(2) + '</strong>' + m1.group(3)
                # if is_italic:
                #     curr = m1.group(1) + '<em>' + m1.group(2) + \
                #         '</em>' + m1.group(3)
                curr, is_bold = bold('(.*)__(.*)__(.*)', curr)
                curr, is_italic = italic('(.*)_(.*)_(.*)', curr)
                i = '<li>' + curr + '</li>' # list
        else:
            if in_list: ## in_list == True that means 'open list point'
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        ## just text
        if not m:
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        ## bold
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        ## italic
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        ## List append same depth
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    ## List append different depth
    if in_list:
        res += '</ul>'
    return res
