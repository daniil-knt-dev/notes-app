import json


def load():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except:
        return {"password": "123", "notes": []}
    
    
def save(data):
    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except:
        print('Что-то пошло не так')
        
        
def add_note(data, title, text, category):
    data['notes'].append({'title': title, 'text': text, 'category': category})


def del_note(data, title_to_del):
    data['notes'] = [x for x in data['notes'] if x['title'] != title_to_del]
    

def show_notes(data):
    for i, note in enumerate(data['notes'], start=1):
        print(f"{i}. Заголовок: {note['title']}, Текст: {note['text']}, Категория: {note['category']}")
        
        
def is_correct_password(data, password):
    status = password == data['password']
    return status    


def update_password(data):
    last_password = input('Введите прошлый пароль: ')
    if is_correct_password(data, last_password):
        new_password = input('Введите новый пароль: ')
        data['password'] = new_password
        print('Пароль успешно сменён!')
    else:
        print('Неверно введён пароль')  
    save(data)
        

data = load()

while True:
    password = input('🔒Введите пароль: ')
    if is_correct_password(data, password):
        break
    else:
        exit()

menu = f"1. Все заметки📒\n2. Добавить заметку✏️\n3. Удалить заметку🗑️\n4. Поменять пароль🔏\n5. Выход и сохранение🚪\n> "
while True:
    choice = int(input(menu))
    if choice == 1:
        show_notes(data)
    elif choice == 2:
        add_note(data, input('Введите заголовок заметки: ').lower().strip(), input('Введите текст заметки: ').lower().strip(),\
            input('Введите категорию заметки: ').lower().strip())
    elif choice == 3:
        del_note(data, input('Введите заголовок заметки для удаления: ').lower().strip())
    elif choice == 4:
        update_password(data)
    elif choice == 5:
        save(data)
        break
    else:
        print('Некорректный ввод')