def add_time(start: str, duration: str, day: str = None) -> str:
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    start_lst = list(map(int, start[:-3].split(':')))
    duration_lst = list(map(int, duration.split(':')))

    total_min = start_lst[1] + duration_lst[1]
    extra_hours = total_min // 60
    total_hours = start_lst[0] + duration_lst[0] + extra_hours

    if 'PM' in start:
        total_hours += 12

    ans_minutes = total_min % 60
    ans_hours = total_hours % 12
    num_of_days = total_hours // 24

    ans_minutes = str(ans_minutes).rjust(2, '0')
    ans_hours = '12' if ans_hours == 0 else str(ans_hours)
    period = 'AM' if (total_hours % 24) < 12 else 'PM'

    new_time = f'{ans_hours}:{ans_minutes} {period}'
    if day is not None:
        day = day.lower().capitalize()
        days = days[days.index(day):] + days[:days.index(day)]  # from what day to start
        new_time += f', {days[num_of_days % 7]}'

    if num_of_days == 1:
        new_time += ' (next day)'
    elif num_of_days > 1:
        new_time += f' ({num_of_days} days later)'

    return new_time
