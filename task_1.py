from datetime import datetime

def get_days_from_today(date: str) -> int:
    """
    Returns the number of days from the given date to today's date.

    Parameters:
        date (str): The target date in the format 'YYYY-MM-DD'.

    Returns:
        int: The number of days between the given and the current dates. Returns a negative number if the given date is later than the current.

    Raises:
        ValueError: If the input date format is incorrect.
    """
    try:
        converted_date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        return (current_date - converted_date).days
    except ValueError as e:
        print(f"The input date format is incorrect. Details: {e}")
        return None

result = get_days_from_today("2020-10-09")
result_with_later_date = get_days_from_today("2025-10-09") # returns negative number

print(result, result_with_later_date)

get_days_from_today("2020-111-111") # handles exception and prints error details

