start_day = 1
end_day = 3

days = (
        ("first"," a partridge in a pear tree"),
        ("second"," two turtle doves"),
        ("third"," three french hens"),
        ("fourth"," four calling birds"),
        ("fifth"," five gold rings"),
        ("sixth"," six geese a-laying"),
        ("seventh"," seven swans a-swimming"),
        ("eigth"," eight maids a-milking"),
        ("ninth"," nine ladies dancing"),
        ("tenth"," ten lords a-leaping"),
        ("eleventh"," eleven pipers piping"),
        ("twelvfth"," twelve drummers drumming"),
)

for day in range(start_day-1,end_day):
    print(f"On the {days[day][0]} day of christmas...")
    for verse in range(day,-1,-1):
        print(days[verse][1])
        
# for day in range(start_day,end_day):
#     print(day)
#     # for verse in range(day,-1,-1):
#     #     print(days[verse][1])