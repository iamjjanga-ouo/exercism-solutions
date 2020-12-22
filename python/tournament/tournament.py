def check_table_has_team(db, teams):
    if teams[0] not in db:
        db[teams[0]] = [0, 0, 0, 0, 0]
    if teams[1] not in db:
        db[teams[1]] = [0, 0, 0, 0, 0]


def cal_score(db, team1, team2, result):
    db[team1][0] += 1
    db[team2][0] += 1
    if result == 'win':
        db[team1][1] += 1
        db[team2][3] += 1
    elif result == 'draw':
        db[team1][2] += 1
        db[team2][2] += 1
    else:
        db[team1][3] += 1
        db[team2][1] += 1

    db[team1][4] = db[team1][1] * 3 + db[team1][2]
    db[team2][4] = db[team2][1] * 3 + db[team2][2]


def sort_by_score(db):
    alpha_sort_dict = sorted(db.items())
    return sorted(alpha_sort_dict, key=(lambda x : x[1][4]), reverse=True)


def tally(rows):
    db = {}
    for row in rows:
        team1, team2, result = row.split(";")
        # Check db has team already
        check_table_has_team(db, [team1, team2])

        cal_score(db, team1, team2, result)

    table = sort_by_score(db) # return list

    res = ["Team                           | MP |  W |  D |  L |  P",]
    for row in table:
        res.append(f'{row[0]}'.ljust(31) + f'|  {row[1][0]} |  {row[1][1]} |  {row[1][2]} |  {row[1][3]} |  {row[1][4]}')

    return res
