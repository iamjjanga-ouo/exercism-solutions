def recite(start_verse, end_verse):
    days = ["twelfth", "eleventh", "tenth", "ninth", "eighth", "seventh", "sixth", "fifth", "fourth", "third", "second", "first"]
    verses = [
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, and ",
        "a Partridge in a Pear Tree."
    ]
    result = []
    for n in range(start_verse, end_verse+1):
        header = "On the " + days[12-n] + " day of Christmas my true love gave to me: "
        body = ''.join([x for x in verses[-n:]])
        result += [header + body]
    return result