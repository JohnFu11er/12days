days = {
    1 : "first",
    2 : "second",
    3 : "third",
    4 : "fourth",
    5 : "fifth",
    6 : "sixth",
    7 : "seventh",
    8 : "eighth",
    9 : "nineth",
    10 : "tenth",
    11 : "eleventh",
    12 : "twelfth",
}

gifts = [
    " twelve drummers drumming",
    " eleven pipers piping",
    " ten lords a-leaping",
    " nine ladies dancing",
    " eight maids a-milking",
    " seven swans a-swimming",
    " six geese a-laying",
    " five gold rings",
    " four calling birds",
    " three french hens",
    " two turtle doves",
    " a partridge in a pear tree",
]


def main():
    for day in days:
        start(day)
        verse(day)
        print("\n")
    
    
def start(d):
    """Prints the start of the verse for the twelve days"""
    print(f"On the {days[d]} day of christmas my true love sent to me")


def verse(d):
    """Prints the verses for the twelve days"""
    for gift in gifts[-d:]:
        # if, elif, else added to address the adding of "and" to the last line of the verse for days 2 - 12
        if d == 1:
            print(gift)
        elif d > 1 and gift == gifts[11]:
            print(f" and{gifts[11]}")
        else:
            print(gift)


if __name__ == "__main__":
    main()