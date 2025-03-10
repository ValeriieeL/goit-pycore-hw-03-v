

from datetime import datetime, timedelta
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
    
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
       
       
        delta_days = (birthday_this_year - today).days
        if 0 <= delta_days <= 7:
        
            if birthday_this_year.weekday() in [5, 6]:
                days_to_monday = 7 - birthday_this_year.weekday()
                congratulation_date = birthday_this_year + timedelta(days=days_to_monday)
            else:
                congratulation_date = birthday_this_year
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays
users = [
    {"name": "Christie Nelson","birthday": "1990.03.12"},
    {"name": "Sam Joe", "birthday": "1985.03.14"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)