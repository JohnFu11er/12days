from pprint import pprint

#The function must take two arguments- start day and end day, and return a list of the verses as a string for each day

def twelve_days(start_day, end_day):
    days = "first second third fourth fifth sixth seventh eighth nineth tenth eleventh twelfth".split()

    gifts = [
        " a partridge in a pear tree",
        " two turtle doves",
        " three french hens",
        " four calling birds",
        " five gold rings",
        " six geese a-laying",
        " seven swans a-swimming",
        " eight maids a-milking",
        " nine ladies dancing",
        " ten lords a-leaping",
        " eleven pipers piping",
        " twelve drummers drumming",
    ]
    
    output = []
    for day in range(start_day, end_day+1):
        daily_string = (f"On the {days[day-1]} day of christmas my true love sent to me")
        for i in range(day-1,-1,-1):
            if day == 1:
                daily_string += gifts[0] + '.'
            elif gifts[i] == gifts[0]:
                daily_string += ' and' + gifts[0] + '.'
            else:
                daily_string += gifts[i] + ','
        output.append(daily_string)
    return output
    #for day in days:
        
    
pprint(twelve_days(1, 12))