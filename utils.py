import time



def calculate_duration(member, start_time):
    start_time = start_time
    duration = time.time() - start_time
    return seconds_to_minutes(duration)

def seconds_to_minutes(seconds):
    return round(seconds / 60)
def minutes_to_hours(minutes):
    return round(minutes / 60, 2)
