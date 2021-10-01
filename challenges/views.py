from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("🤬 Invalid Month 🤬")
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("🤬 I don't know what you entered, but it's not supported. 🤬")


    return HttpResponse(challenge_text)