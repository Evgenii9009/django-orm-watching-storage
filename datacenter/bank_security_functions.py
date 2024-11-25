from django.utils.timezone import make_aware
import datetime

def is_visit_long(visit):
    visit_duration = get_duration(visit)
    visit_minutes = format_duration(visit_duration)
    if visit_minutes>50:
        return visit
    else:
        return None
    
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