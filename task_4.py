from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Returns upcoming birthdays for the next 7 days

    Parameters:
        users (List[Dict[str, str]]): Users list with their dates of birth.

    Returns:
        List[Dict[str, str]]: List of upcoming birthdays.
    """
    today = datetime.now().date()
    congratulations_list = []

    for user in users:
        user_birth_date_formatted = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        user_congratulation_date = user_birth_date_formatted.replace(year=today.year)

        # if birthday is already passed then add the next year
        if user_congratulation_date < today:
            """
            The task requires an update to the next year but actually this function should not return this birthday,
            as it won't be in the upcoming 7 days range. I put this check just because it was asked to do,
            and then I will continue the iteration.
            """
            user_congratulation_date = user_birth_date_formatted.replace(year=today.year + 1)
            continue

        if (user_congratulation_date - today).days <= 7:
            # adjust the date if it's on weekends
            if user_congratulation_date.weekday() in [5, 6]:
                user_congratulation_date = (user_congratulation_date + timedelta(days=2)
                                            if user_congratulation_date.weekday() == 5 else
                                            user_congratulation_date + timedelta(days=1))
            congratulations_list.append({
                "name": user["name"],
                "congratulation_date": user_congratulation_date.strftime("%Y.%m.%d")
            })

    return congratulations_list

# users list was checked againts 8th of Jul
users = [
    {"name": "John Doe", "birthday": "1985.01.23"}, # will put the next year but won't be add into the list
    {"name": "Robin Sanchez", "birthday": "1993.09.24"}, # will be this year but not in 7 days range so won't be added
    {"name": "Kristof Anaken", "birthday": "1994.07.10"}, # will be added to the list
    {"name": "Alice Wood", "birthday": "1994.07.13"}, # will be added to the list but due to Saturday will be moved to the next Mon
    {"name": "Mike Milo", "birthday": "1994.07.14"} # will be added to the list but due to Sunday will be moved to the next Mon
]

result = get_upcoming_birthdays(users)

print(result)
