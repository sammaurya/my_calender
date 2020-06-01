from django.shortcuts import render
from datetime import date
import calendar
from calendar import HTMLCalendar

# Create your views here.

def get_calender(request, year=date.today().year, month=date.today().month):
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099: 
        year = date.today().year
    month_name = calendar.month_name[month]
    title = "My Event Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    
    events = [
        {
            'date': '8-10-2019', 'announcement': "Club Registrations Open"
        },
        {
            'date': '8-15-2019', 'announcement': "First Match"
        }
    ]

    return render(request, 'calender_app/calender.html', {'title': title, 'cal': cal, 'events':events   })