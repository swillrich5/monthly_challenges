from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": 'Abstain from meat for the entire month',
    "february": "Walk every day for at least twenty minutes",
    "march": "Learn Django for at least 30 minutes every day",
    "april": "Drink at least 64 ounces of water every day",
    "may": "Think of something you're thankful for every day",
    "june": "Eat more chicken",
    "july": "Get at least seven hours of sleep every night",
    "august": "Buy something just for yourself",
    "september": "Make sure you're prepared for a natural disaster",
    "october": "Read at least one chapter of a book for pleasure every night",
    "november": "Write in a journal for at least 20 minutes evrery day",
    "december": "Meditate for at least five minutes every day"
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if (month > len(months)) or (month == 0):
        return HttpResponseNotFound("<h1>🤬 Invalid Month 🤬</h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
    except:
        return HttpResponseNotFound("<h1>🤬 I don't know what you entered, but it's not supported. 🤬</h1>")

    return HttpResponse(response_data)