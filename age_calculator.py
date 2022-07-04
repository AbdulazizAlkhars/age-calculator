from datetime import date, datetime
from xml.etree.ElementPath import prepare_descendant


year = int(input("Enter year of birth:"))
mont = int(input("Enter month of birth:"))
day = int(input("Enter day of birth:"))

prisentDate = date.today()


def get_dob():
    # write code here
    dob = date(year, mont, day)
    return dob


def get_age(dob):
    # write code here
    age = prisentDate - dob
    return age


def main():
    # write code here

    dateOfBirth = get_dob()
    age = int((prisentDate - dateOfBirth).days / 365)
    if prisentDate > dateOfBirth:
        print(f"You are {age} years old")
    else:
        print("Invalid Date")


if __name__ == '__main__':
    main()
