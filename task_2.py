import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int] | list:
    """
    Returns list of unique and sorted ticket numbers.

    Parameters:
        min (int): Minimal possible number. Not lower than 1.
        max (int): Maximum possible number. Not greater than 1000.
        quantity (int): Quantity of numbers. Not lower than 1 and not greater than 1000.

    Returns:
        int: List of unique and sorted ticket numbers.

    Raises:
        TypeError: If the input params have incorrect types.
    """
    if (min < 1 or max > 1000 or not min <= quantity <= max):
        return []

    # makes sure we generate only unique numbers
    unique_numbers = set()

    while len(unique_numbers) < quantity:
        random_number = random.randint(min, max)
        unique_numbers.add(random_number)

    return sorted(unique_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
lottery_numbers_uniqueness_check = get_numbers_ticket(
    1, 1000, 1000
) # fills 1000 sorted items from 1 to 1000
lottery_numbers_with_wrong_argument = get_numbers_ticket(
    0, 49, 6
) # returns empty list because of incorrect min argument

print("Your numbers:", lottery_numbers)
print("Uniqueness check:", lottery_numbers_uniqueness_check)
print("Empty list on wrong args:", lottery_numbers_with_wrong_argument)
