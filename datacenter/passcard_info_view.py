import datetime


from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import make_aware
from django.shortcuts import get_object_or_404


def get_duration(visit):
    entering_time = visit.entered_at
    leaving_time = visit.leaved_at
    if leaving_time ==  None:
        leaving_time = make_aware(datetime.datetime.now())
    delta = leaving_time - entering_time
    return delta


def format_duration(duration):
    minutes = (duration.total_seconds() % 3600) // 60
    return minutes


def is_visit_long(visit):
    visit_duration = get_duration(visit)
    visit_minutes = format_duration(visit_duration)
    if visit_minutes>50:
        return visit
    else:
        return None
    
    
def passcard_info_view(request, passcode):
    owner_name = get_object_or_404(Passcard, passcode=passcode)
    visits_list = Visit.objects.filter(passcard = owner_name)
    print(visits_list)
    this_passcard_visits = []
    for visit in visits_list:
        if is_visit_long(visit) == visit:
            passcard_visit = {
            'entered_at': visit.entered_at,
            'duration': get_duration(visit),
            'is_strange': True
            }
        else:
            passcard_visit = {
            'entered_at': visit.entered_at,
            'duration': get_duration(visit),
            'is_strange': False
            }
        this_passcard_visits.append(passcard_visit) 
    context = {
        'passcard': owner_name,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
