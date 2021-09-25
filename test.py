import json
import random


def write_json(data, file_name):
    """Запись в json"""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, sort_keys=True, ensure_ascii=False)


def read_json(file_name):
    """Чтение из json"""
    try:
        with open(file_name, "r", encoding="utf-8-sig") as file:
            for line in file:
                yield json.loads(line)
    except Exception as e:
        print("Error:", e)


def get_name():
    names = []
    for field in read_json("names_table.jsonl"):
        if 'gender' in field and "text" in field:
            names.append({'Name': field["text"], 'Sex': field['gender']})
    max_n = len(names)
    print(max_n, "names")
    while True:
        yield names[random.randint(0, max_n - 1)]


def get_surname():
    surnames = []
    for field in read_json("surnames_table.jsonl"):
        if 'gender' in field and "text" in field:
            surnames.append({'Surname': field["text"], 'Sex': field['gender']})
    max_n = len(surnames)
    print(max_n, "surnames")
    while True:
        yield surnames[random.randint(0, max_n - 1)]


def get_midname():
    midnames = []
    for field in read_json("midnames_table.jsonl"):
        if 'gender' in field and "text" in field:
            midnames.append({'Midname': field["text"], 'Sex': field['gender']})
    max_n = len(midnames)
    print(max_n, "midnames")
    while True:
        yield midnames[random.randint(0, max_n - 1)]


def get_fio(sex):
    """sex = m or f"""
    for surname in get_surname():
        if surname['Sex'] == sex:
            for name in get_name():
                if name['Sex'] == sex:
                    for midname in get_midname():
                        if midname['Sex'] == sex:
                            yield {'Surname': surname['Surname'],
                                    'Name': name['Name'],
                                    'Midname': midname['Midname'],
                                    'Sex': sex}


for n, name in enumerate(get_surname()):
    print(name, n)
    if n == 2:
        break
for n, name in enumerate(get_name()):
    print(name, n)
    if n == 2:
        break
for n, name in enumerate(get_midname()):
    print(name, n)
    if n == 2:
        break
# count = 0
# fio = {}
# while count < 1500:
#     try:
#         fio[count] = next(get_fio('m'))
#         print(count, fio[count])
#         count += 1
#     except:
#         print("error add man")
#     try:
#         fio[count] = next(get_fio('f'))
#         print(count, fio[count])
#         count += 1
#     except:
#         print("error add man")
#
#
# write_json(fio, "1500_fio.json")
