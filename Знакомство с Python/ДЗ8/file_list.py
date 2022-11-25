def lst():
    list = []
    with open('employees.csv', encoding="utf-8") as data:
        for line in data:
            list.append(line)
    return list
