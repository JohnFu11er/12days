from pprint import pprint

#The function must take two arguments- start day and end day, and return a list of the verses as a string for each day

def twelve_days(start_day, end_day):
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
    output = []
    for day in range(start_day, end_day+1):
        daily_string = (f"On the {days[day]} day of christmas my true love sent to me")
        for gift in gifts[-day:]:
            if day == 1:
                daily_string += gifts[-1] + '.'
            elif gift == gifts[-1]:
                daily_string += ' and' + gifts[-1] + '.'
            else:
                daily_string += gift + ','
        output.append(daily_string)
    return output
    #for day in days:
        
    
pprint(twelve_days(1, 12))