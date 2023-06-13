from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd



def home_view(request):
    data = pd.read_csv('/home/andrewmoss/PycharmProjects/djangoProject/static/Usable_Lineups.csv')
    context = {
        'dataframe': data
    }
    return render(request, 'player_ownership.html', context)

def lineups_team_exposure_caps_view(request):
    return render(request, 'Lineups_team_exposure_caps.html')