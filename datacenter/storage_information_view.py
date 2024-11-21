import os
import django
import datetime
from models import Passcard
from models import Visit
from django.shortcuts import render

from django.utils.timezone import make_aware
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


def get_duration(visit):
    now = make_aware(datetime.datetime.now())
    then = visit.entered_at
    delta = now - then
    return delta

def format_duration(duration):
    minutes = (duration.total_seconds() % 3600) // 60
    return minutes, "minutes"


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = list()
    for visit in active_visits:
        duration = get_duration(visit)
        formated_duration = format_duration(duration)
        person = []
        person = {
            "who entered": str(visit.passcard),
            "entered_at": str(visit.entered_at),
            "duration": formated_duration
            }
        non_closed_visits.append(person)
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
