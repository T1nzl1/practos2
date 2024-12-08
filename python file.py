
users = [
    {
        'username': 'user',
        'password': 'user',
        'role': 'user',
        'bookings': [],
        'created_at': '2024-01-15'
    },
    {
        'username': 'admin',
        'password': 'admin',
        'role': 'admin'
    }
]


tours = [
    {
        'title': 'Экскурсия в Париж',
        'destination': 'Франция',
        'price': 3400,
        'start_date': '2024-06-01',
        'end_date': '2024-06-10',
        'description': 'Увлекательная экскурсия по лучшим местам Парижа.'
    },
    {
        'title': 'Отдых на Бали',
        'destination': 'Индонезия',
        'price': 5000,
        'start_date': '2024-07-01',
        'end_date': '2024-07-15',
        'description': 'Наслаждайтесь пляжами и культурой Бали.'
    },
    {
        'title': 'Эскурсия по всему Китаю!',
        'destination': 'Китай',
        'price': 4000,
        'start_date': '2024-08-01',
        'end_date': '2024-08-15',
        'description': 'Интересная экскурсия по Китаю.'
    }
]



def authenticate(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None



def user_menu(user):
    while True:
        print("\nДобро пожаловать в туристическое агентство!")
        print("Выберите действие:")
        print("1. Просмотреть доступные туры")
        print("2. Найти тур")
        print("3. Забронировать тур")
        print("4. Посмотреть историю бронирований")
        print("5. Изменить пароль")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            print_tours()
        elif choice == '2':
            search_tour()
        elif choice == '3':
            book_tour(user)
        elif choice == '4':
            view_bookings(user)
        elif choice == '5':
            change_password(user)
        elif choice == '6':
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")


def print_tours():
    print("\nДоступные туры:")
    for tour in tours:
        print(f"{tour['title']} - Направление: {tour['destination']}, Цена: {tour['price']}")


def search_tour():
    keyword = input("Введите название или направление тура для поиска: ")
    found_tours = [tour for tour in tours if
                   keyword.lower() in tour['title'].lower() or keyword.lower() in tour['destination'].lower()]
    if found_tours:
        print("\nНайденные туры:")
        for tour in found_tours:
            print(f"{tour['title']} - Направление: {tour['destination']}, Цена: {tour['price']}")
    else:
        print("Тур не найден.")


def book_tour(user):
    title = input("Введите название тура для бронирования: ")
    for tour in tours:
        if tour['title'] == title:
            user['bookings'].append(tour)
            print(f"Тур '{tour['title']}' успешно забронирован.")
            return
    print("Тур не найден.")


def view_bookings(user):
    if user['bookings']:
        print("История бронирований:")
        for tour in user['bookings']:
            print(tour['title'])
    else:
        print("История бронирований пуста.")


def change_password(user):
    new_password = input("Введите новый пароль: ")
    user['password'] = new_password
    print("Пароль успешно изменен.")



def admin_menu():
    while True:
        print("\nДобро пожаловать в систему управления туристическим агентством!")
        print("Выберите действие:")
        print("1. Добавить тур")
        print("2. Удалить тур")
        print("3. Редактировать тур")
        print("4. Управление пользователями")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == '1':
            add_tour()
        elif choice == '2':
            delete_tour()
        elif choice == '3':
            edit_tour()
        elif choice == '4':
            manage_users()
        elif choice == '5':
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз.")


def add_tour():
    title = input("Введите название тура: ")
    destination = input("Введите направление: ")
    price = float(input("Введите цену: "))
    start_date = input("Введите дату начала (YYYY-MM-DD): ")
    end_date = input("Введите дату окончания (YYYY-MM-DD): ")
    description = input("Введите описание: ")
    tours.append({
        'title': title,
        'destination': destination,
        'price': price,
        'start_date': start_date,
        'end_date': end_date,
        'description': description
    })
    print("Тур добавлен.")


def delete_tour():
    title = input("Введите название тура, который хотите удалить: ")
    global tours
    tours = [tour for tour in tours if tour['title'] != title]
    print("Тур удален.")


def edit_tour():
    title = input("Введите название тура для редактирования: ")
    for tour in tours:
        if tour['title'] == title:
            new_title = input("Введите новое название (оставьте пустым, если не хотите менять): ")
            new_destination = input("Введите новое направление (оставьте пустым, если не хотите менять): ")
            new_price = input("Введите новую цену (оставьте пустым, если не хотите менять): ")
            new_start_date = input("Введите новую дату начала (YYYY-MM-DD) (оставьте пустым, если не хотите менять): ")
            new_end_date = input("Введите новую дату окончания (YYYY-MM-DD) (оставьте пустым, если не хотите менять): ")
            new_description = input("Введите новое описание (оставьте пустым, если не хотите менять): ")

            if new_title:
                tour['title'] = new_title
            if new_destination:
                tour['destination'] = new_destination
            if new_price:
                tour['price'] = float(new_price)
            if new_start_date:
                tour['start_date'] = new_start_date
            if new_end_date:
                tour['end_date'] = new_end_date
            if new_description:
                tour['description'] = new_description

            print("Тур обновлен.")
            return
    print("Тур не найден.")


def manage_users():
    print("Список пользователей:")
    for user in users:
        print(f"Логин: {user['username']}, Роль: {user['role']}, Бронирования: {len(user['bookings'])}")


def main():
    print("Добро пожаловать в туристическое агентство!")
    while True:
        username = input("Введите логин: ")
        password = input("Введите пароль: ")

        user = authenticate(username, password)

        if user:
            if user['role'] == 'admin':
                admin_menu()
            else:
                user_menu(user)
        else:
            print("Неверные учетные данные. Попробуйте снова.")


if __name__ == '__main__':
    main()