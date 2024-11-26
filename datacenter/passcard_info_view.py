import datetime


from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.bank_security_functions import get_duration
from datacenter.bank_security_functions import format_duration
from datacenter.bank_security_functions import is_visit_long
from django.shortcuts import render
from django.utils.timezone import make_aware
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    owner_name = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=owner_name)
    this_passcard_visits = []
    for visit in visits:
        passcard_visit = {
            'entered_at': visit.entered_at,
            'duration': get_duration(visit),
            'is_strange': False
            }
        if is_visit_long(visit):
            passcard_visit['is_strange'] = True
        this_passcard_visits.append(passcard_visit)
    context = {
        'passcard': owner_name,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
