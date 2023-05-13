phone_number = input("input phone numbers in +XXOOOOOOOOOO format : ")
assert isinstance(phone_number, str), "Phone number must be a string."
assert len(phone_number) == 13, "Phone number length is not 13."
assert phone_number.startswith("+"), "Phone number does not start with '+'"
code = phone_number[1:3]
if code == "66":
    print("Thailand")
elif code == "34":
    print("Spain")
else:
    print("Other country")