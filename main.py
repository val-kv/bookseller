from library import Library


def main():
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            library.add_book(title, author, year)

        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            library.remove_book(book_id)

        elif choice == "3":
            field = input("Искать по (title, author, year): ").strip().lower()
            query = input("Введите запрос для поиска: ")
            if field in ["title", "author", "year"]:
                library.search_books(query, field)
            else:
                print("Некорректное поле для поиска.")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            book_id = int(input("Введите ID книги для изменения статуса: "))
            status = input("Введите новый статус (в наличии, выдана): ").strip()
            if status in ["в наличии", "выдана"]:
                library.update_status(book_id, status)
            else:
                print("Некорректный статус.")

        elif choice == "6":
            print("До свидания!")
            break

        else:
            print("Некорректный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()
