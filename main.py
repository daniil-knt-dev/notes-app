def validate_string(value, min_len=3, max_len=20, contains=None):
    if type(value) != str:
        return False, "неверный тип данных"
    if not int(min_len) <= len(value) <= int(max_len):
        return False, "неверная длина"
    if contains != None:
        if not set(contains).issubset(value):
            return False, "неверное содержание"
    return True


def validate_int(value, min_val=1, max_val=15):
    if type(value) != int:
        return False, "неверный тип данных"
    if not min_val <= value <= max_val:
        return False, "неверное значение"
    return True


def validate_data(data, rules):
    res = {}
    for el in data:
        if rules[el]["type"] == "str":
            res[el] = validate_string(data[el], min_len=rules[el]["min_len"],
                                      max_len=rules[el]["max_len"], contains=rules[el]["contains"])
        elif rules[el]["type"] == "int":
            res[el] = validate_int(
                int(data[el]), int(rules[el]["min_val"]), int(rules[el]["max_val"]))
    return res


def set_fields_to_validate(fields):
    fields = tuple(x.strip() for x in fields.split(","))
    rules = {}
    for field in fields:
        rules.setdefault(field, {"type": None,
                                 "min_len": None,
                                 "max_len": None,
                                 "contains": None,
                                 "min_val": None,
                                 "max_val": None
                                 })
    return rules


def collect_and_save_data(rules):
    data = {}
    for field in rules:
        data[field] = input(f"Введите {field}: ").strip()
    return data


def set_filters(rules):
    for field in rules:
        rules[field]["type"] = data_type = input(
            f"Введите тип данных для {field}(str, int): ").strip().lower()
        if data_type == "int":
            rules[field]["min_val"] = int(
                input(f"Введите минимальное значение {field}: ").strip())
            rules[field]["max_val"] = int(
                input(f"Введите максимальное значение {field}: ").strip())
        elif data_type == "str":
            rules[field]["min_len"] = int(
                input(f"Введите минимальную длину {field}: ").strip())
            rules[field]["max_len"] = int(
                input(f"Введите максимальную длину {field}: ").strip())
            user_input = input(
                f"Введите (через запятую, если символов/слов несколько), "
                f"что должно содержаться в {field}: ").strip().split(",")
            # Удаление пробелов в словах(" яблоко" => "яблоко")
            if len(user_input) > 1:
                rules[field]["contains"] = [x.strip() for x in user_input]
            elif len(user_input) == 1:
                rules[field]["contains"] = user_input[0]


def main():
    rules = set_fields_to_validate(input(
        "Введите через запятую поля для проверки(например: email, username...): ").strip())
    set_filters(rules)
    data = collect_and_save_data(rules)
    print(validate_data(data, rules))
    input("Enter для выхода")
    

main()
