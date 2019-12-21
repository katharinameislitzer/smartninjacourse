import datetime
import json
import operator

BIRTHDAYS = {
    "Nina": datetime.datetime(1991, 2, 23),
    "Adrian": datetime.datetime(1986, 11, 6),
    "Thomas": datetime.datetime(1981, 12, 30),
    "Tamara": datetime.datetime(1986, 12, 2)
}

def write_birthdays_to_json(birthdays: dict, filename: str):

    tmp_dict = {}
    for name, birthdate in birthdays.items():
        print(name, birthdate)     # müssen value in string verwandeln
        tmp_dict[name] = birthdate.isoformat()

    with open(filename, "w")  as f:
        json.dump(tmp_dict, f)

def read_birthdays_from_json(filename: str) -> dict:
    with open(filename, "r") as f:
        content = json.load(f)


        for name in content:
            content[name] = datetime.datetime.fromisoformat(content[name])
        return content

def get_upcoming_birthdays(birthdays_dict: dict) -> dict:
    today = datetime.date.today()

    tmp_birthdays = birthdays_dict.copy()

    for name in tmp_birthdays:
        tmp_date = birthdays_dict[name].date()
        tmp_date = datetime.date(today.year, tmp_date.month, tmp_date.day)
        if tmp_date<today:
            del birthdays_dict[name]
        else:
            birthdays_dict[name] = tmp_date
    return birthdays_dict

if __name__ == '__main__':
    #write_birthdays_to_json(BIRTHDAYS, "birthdays.json") (jedes mal, wenn man was hinzufügt, wieder einblenden)
    my_birthdays = read_birthdays_from_json("birthdays.json")
    upcoming_birthdays = get_upcoming_birthdays(my_birthdays)
    upcoming_birthdays = dict(sorted(upcoming_birthdays.items(), key=operator.itemgetter(1)))

    for k, v in upcoming_birthdays.items():
        print(k, v)