def validate_input(id_number):
    if len(id_number) != 13 or id_number[-2] != "8":
        return False
    try:
        all_numbers = int(id_number)
        return True
    except Exception:
        return False


def year(id_number):
    date_numbers = id_number[:6]
    try:
        year = int(date_numbers[:2])
    except Exception:
        return False
    return True


def month(id_number):
    date_numbers = id_number[:6]
    try:
        month = int(date_numbers[2:4])
    except Exception:
        return False
    return True


def day(id_number):
    date_numbers = id_number[:6]
    try:
        day = int(date_numbers[4:])
    except Exception:
        return False
    return True


def gender(id_number):
    try:
        gender = int(id_number[6:10])
        return True
    except Exception:
        return False


def citizenship(id_number):
    return id_number[-3] in ["0", "1"]


def checksum_digit(id_number):
    sum_of_all_numbers = 0
    for number in id_number[1::2]:
        doubled_no = int(number) * 2
        if doubled_no > 9:
            doubled_no = str(doubled_no)
            sum_of_all_numbers += int(doubled_no[0]) + int(doubled_no[1])
        else:
            sum_of_all_numbers += doubled_no
    for number in id_number[::2]:
        sum_of_all_numbers += int(number)
    result = 10 - (sum_of_all_numbers % 10)
    if result in [10, 1]:
        return True
    return False


def validate_sa_id(id_number):
    validate_string = validate_input(id_number)
    validate_year = year(id_number)
    validate_month = month(id_number)
    validate_day = day(id_number)
    validate_gender = gender(id_number)
    validate_citizenship = citizenship(id_number)
    validate_checksums_digit = checksum_digit(id_number)
    return all(
        [
            validate_string,
            validate_year,
            validate_month,
            validate_day,
            validate_gender,
            validate_citizenship,
            validate_checksums_digit,
        ]
    )

print(validate_sa_id("0205160459082"))