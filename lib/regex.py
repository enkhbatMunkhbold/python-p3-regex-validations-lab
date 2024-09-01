import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][']*([A-Za-z][ \'-]{0,1})+"
# name = r"\w+\s\w+\W\w+"
name_regex = re.compile(name)

phone_number = r"([(]*[0-9]{3}[ )-]*)+[0-9]+gm"
# phone_number = r"[(]*[0-9]{3}[ )-]*"
phone_regex = re.compile(phone_number)

email_address = r""
email_regex = re.compile(email_address)
