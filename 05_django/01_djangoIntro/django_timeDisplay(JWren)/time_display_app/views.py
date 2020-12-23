from django.shortcuts import render
from time import strftime


def index(request):
    context = {
        "weekday": strftime("Today is %A."),
        "twentyfour_hour_clock": strftime("Twenty-Four Hour: %H:%M"),
        "twelve_hour_clock": strftime("Twelve-Hour Clock: %I:%M %p"),
        "day_month_year": strftime("Day-Month-Year: %d-%b-%Y"),
    }
    return render(request, "index.html", context)
