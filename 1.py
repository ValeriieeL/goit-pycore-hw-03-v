
from datetime import datetime
def get_days_from_today (date:str) -> int:
    try:
      previous_date = datetime.strptime(date, "%Y-%m-%d").date()
      today=datetime.today().date()
      delta= previous_date - today
      return delta.days
    except Exception:
       print ("incorrect date format. Use format as YYYY-MM-DD.")
fixed_date= "2025-02-05"  
days_between= get_days_from_today(fixed_date)
print(f"Amount of days between {fixed_date} and date from today: {days_between}")
 


