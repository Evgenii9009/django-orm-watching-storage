import django
import datetime


from datacenter.models import Visit
from datacenter.bank_security_functions import get_duration
from datacenter.bank_security_functions import format_duration
from django.shortcuts import render
from django.utils.timezone import make_aware


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = list()
    for visit in active_visits:
        duration = get_duration(visit)
        formated_duration = format_duration(duration)
        person = {
            "who_entered": visit.passcard.owner_name,
            "entered_at": visit.entered_at,
            "duration": formated_duration
            }
        non_closed_visits.append(person)
    context = {
        'non_closed_visits': non_closed_visits
    }
    return render(request, 'storage_information.html', context)
