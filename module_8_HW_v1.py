from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    res_str = ""
    mistake_input = 0
    while mistake_input == 0: 
        try:
            control_date_input_str = input('Input current or need date (yyyy-mm-dd):')
            control_date_input_list = control_date_input_str.split('-')
            year_input = int(control_date_input_list[0])
            month_input = int(control_date_input_list[1])
            day_input = int(control_date_input_list[2])
            control_date = datetime(year=year_input, month=month_input, day=day_input)
            print('--------------------------------')
            print('Today: ', control_date.strftime('%A'))
            print('--------------------------------')
            mistake_input = 1
        except ValueError:
            print('Try else!')

    list_birthday_weekend = []

    # delta for checking last weekend's birthday
    t = 0
    if control_date.strftime('%A') == 'Monday':
        t = -2
    elif control_date.strftime('%A') == 'Sunday':
        t = -1
    
    # viewing the next 7 days (if necessary, analysis of the previous weekend)
    for i in range(7):
        weekdelta = control_date + timedelta(days=i + t)
        list_birthday_one_day = []
        if weekdelta.strftime('%A') == 'Saturday' or weekdelta.strftime('%A') == 'Sunday':
            flag = 'weekend'
        elif weekdelta.strftime('%A') == 'Monday':
            flag = 'monday'
        else:
            flag = 0
        
        # collection list_birthday_weekend and list_birthday_non-weekend
        for i in range(len(users)):
            if weekdelta.month == users[i]['birthday'].month and weekdelta.day == users[i]['birthday'].day and flag != 'weekend':
                list_birthday_one_day.append(users[i]['name'])
            elif weekdelta.month == users[i]['birthday'].month and weekdelta.day == users[i]['birthday'].day and flag == 'weekend':
                list_birthday_weekend.append(users[i]['name'])
                
        # collection result out strings
        if len(list_birthday_one_day) > 0 and flag == 0:
            res_str = res_str + weekdelta.strftime('%A') + ": " + ", ".join(list_birthday_one_day) + '\n'
        elif len(list_birthday_one_day) > 0 or len(list_birthday_weekend) > 0 and flag == 'monday':
            list_birthday_one_day += list_birthday_weekend
            res_str = res_str + weekdelta.strftime('%A') + ": " + ", ".join(list_birthday_one_day) + '\n'
    if res_str:
        return res_str
    else:
        return "Good news! You'll take a break from your friends' birthdays! :-)"


users = [
    {"name":"Bob2", "birthday":datetime(2022, 2, 21)}, 
    {"name":"Kira1", "birthday":datetime(2023, 2, 22)}, 
    {"name":"Diana", "birthday":datetime(1991, 2, 22)},
    {"name":"Katya", "birthday":datetime(1988, 2, 23)}, 
    {"name":"Leshka", "birthday":datetime(1988, 2, 23)},
    {"name":"Danya", "birthday":datetime(1988, 2, 24)}, 
    {"name":"Benya", "birthday":datetime(1988, 2, 25)}, 
    {"name":"Bon", "birthday":datetime(1988, 2, 26)},
    {"name":"Bob5", "birthday":datetime(1991, 2, 27)},
    {"name":"Bob6", "birthday":datetime(1991, 2, 28)},
    {"name":"Bob7", "birthday":datetime(1991, 3, 1)},
    {"name":"Bob8", "birthday":datetime(1991, 3, 2)},]

print(get_birthdays_per_week(users))