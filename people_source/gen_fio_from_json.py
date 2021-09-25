#!../venv/bin/python3
# -*- coding: utf-8 -*-
import datetime
import json
import random

from site_config import N_PEOPLE, NAME, SURNAME, MIDNAME


def write_json(data, file_name):
    """Запись в json"""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, sort_keys=True, ensure_ascii=False)


def read_json(file_name):
    """Чтение из json"""
    try:
        data = []
        with open(file_name, "r", encoding="utf-8-sig") as file:
            for line in file:
                data.append(json.loads(line))
            return data
    except Exception as e:
        print("Error:", e)


def get_list_from_json(sex, base_fields):
    """Function return list of names, surnames or midnames for current sex"""
    return [field["text"] for field in base_fields
            if 'gender' in field and "text" in field and field['gender'] == sex]


def gen_birthday():
    """Function gen birthday between 1.1.1955 and 1.1.1995"""
    start_date = datetime.date(1955, 1, 1)
    end_date = datetime.date(1995, 1, 1)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days

    def gen_random_date():
        nonlocal days_between_dates
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date.strftime("%d.%m.%Y")
    return gen_random_date


gen_birth = gen_birthday()


def get_fio(surnames, names, midnames, sex):
    """Function generate random surname, name, middle name and birthday for sex"""
    return {'Surname': random.choice(surnames),
            'Name': random.choice(names),
            'Midname': random.choice(midnames),
            'Sex': sex, "DateOfBirth": gen_birth()}


def gen_n_people(n_people):
    """Function generate N people with random FIO and date of birthday"""
    count = 0
    fio = {}
    try:
        base = {'names': read_json(NAME), 'surnames': read_json(SURNAME),
                'midnames': read_json(MIDNAME)}
        n_man = get_list_from_json('m', base['names'])
        s_man = get_list_from_json('m', base['surnames'])
        m_man = get_list_from_json('m', base['midnames'])
        n_woman = get_list_from_json('f', base['names'])
        s_woman = get_list_from_json('f', base['surnames'])
        m_woman = get_list_from_json('f', base['midnames'])
        while count < n_people:
            try:
                fio[count] = get_fio(s_man, n_man, m_man, 'm')
                count += 1
            except Exception as e:
                print("error add man: ", e)
            if count < n_people:
                try:
                    fio[count] = get_fio(s_woman, n_woman, m_woman, 'f')
                    count += 1
                except Exception as e:
                    print("error add woman: ", e)
        return fio
    except Exception as e:
        print("error read source people files from jsons: ", e)


if __name__ == "__main__":
    write_json(gen_n_people(N_PEOPLE), "fio.json")
