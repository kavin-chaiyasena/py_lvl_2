def phone_number_country(phone_number):
    if not isinstance(phone_number, str):
        raise TypeError("Phone number must be a string.")
    if len(phone_number) != 13:
        raise IndexError("Phone number length is not 13.")
    if not phone_number.startswith("+"):
        raise ValueError("Phone number does not start with '+'")
    code = phone_number[1:3]
    if code == "66":
        return "Thailand"
    elif code == "34":
        return "Spain"
    else:
        return "Other country"

print(phone_number_country((input("input phone number in this format '+XXOOOOOOOOOO'"))))