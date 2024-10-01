def add_time(start, duration, day=None):
    # to convert time to minutes
    def time_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(':'))
        return hours * 60 + minutes

    # to convert minutes to time
    def minutes_to_time(minutes):
        hours = minutes // 60
        minutes = minutes % 60
        return f"{hours}:{minutes:02d}"

    # Parse start time
    start_time, period = start.split()
    start_minutes = time_to_minutes(start_time)
    if period == "PM":
        start_minutes += 12 * 60

    # Parse duration
    duration_minutes = time_to_minutes(duration)

    # Calculate total minutes
    total_minutes = start_minutes + duration_minutes

    # Calculate days passed
    days_passed = total_minutes // (24 * 60)
    total_minutes = total_minutes % (24 * 60)

    # Calculate new time
    new_hours = total_minutes // 60
    new_minutes = total_minutes % 60
    
    # Determine period (AM/PM)
    if new_hours >= 12:
        period = "PM"
        if new_hours > 12:
            new_hours -= 12
    else:
        period = "AM"
        if new_hours == 0:
            new_hours = 12

    # Format new time
    new_time = f"{new_hours}:{new_minutes:02d} {period}"

    # Handle day of week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day:
        day = day.capitalize()
        current_day_index = days_of_week.index(day)
        new_day_index = (current_day_index + days_passed) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    # Add days later information
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time
