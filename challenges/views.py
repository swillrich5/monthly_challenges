from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'Abstain from meat for the entire month'
    elif month == 'february':
        challenge_text = 'Walk every day for at least twenty minutes'
    elif month == 'march':
        challenge_text = 'Learn Django for at least 20 minutes every day'
    else:
        return HttpResponseNotFound("🤬 This month is not supported 🤬")

    return HttpResponse(challenge_text)