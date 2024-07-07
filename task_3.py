import re

def normalize_phone(phone_number: str) -> str:
    """
    Returns normalized phone number according to international format (UA).

    Parameters:
        phone_number (str): Phone number to normalize.

    Returns:
        str: Normalized phone number
    """
    normalized_number = re.sub(r"(?!^\+)[^\d]", "", phone_number)

    if not normalized_number.startswith("+"):
        if normalized_number.startswith("380"):
            normalized_number = "+" + normalized_number
        else:
            normalized_number = "+38" + normalized_number

    return normalized_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "+3805012345+++67",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Normalized phone numbers:", sanitized_numbers)
