from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}

# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

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
        return render(request, "challenges/challenge.html", { 
            "text": challenge_text,
            "month_name": month
         })
    except:
        raise Http404()
