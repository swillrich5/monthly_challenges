from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january": "Eat no meat in January.",
    "february": "Walk for at least 30 minutes every other day",
    "march": "Learn Django for at least 30 minutes every day.",
    "april": "Weight workout every other day for at least 30 minutes",
    "may": "Learn Docker and Kubernetes",
    "june": "Drink at least 8 glasses of water every day",
    "july": "Learn more JavaScript and React!",
    "august": "Meditate for at least five minutes every day.",
    "september": "Do Yoga at least one time a week",
    "october": "Get ready for Halloween",
    "november": "Get ready for Thanksgiving",
    "december": None
}


def index(request):

    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:        
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month,
        })
    except:
        raise Http404()
    
