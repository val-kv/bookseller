import json
import os
from typing import List, Optional


class Book:
    """
    Класс, представляющий книгу.
    """
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """
        Преобразует объект книги в словарь.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    @staticmethod
    def from_dict(data: dict) -> 'Book':
        """
        Создает объект книги из словаря.
        """
        return Book(
            book_id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"]
        )


class Library:
    """
    Класс для управления библиотекой.
    """
    def __init__(self, data_file: str = "data.json"):
        self.data_file = data_file
        self.books: List[Book] = []
        self.load_books()

    def load_books(self):
        """
        Загружает книги из файла JSON.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.books = [Book.from_dict(book) for book in data]
        else:
            self.books = []

    def save_books(self):
        """
        Сохраняет книги в файл JSON.
        """
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """
        Добавляет книгу в библиотеку.
        """
        new_id = max([book.id for book in self.books], default=0) + 1
        new_book = Book(book_id=new_id, title=title, author=author, year=year)
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' успешно добавлена с ID {new_id}.")

    def remove_book(self, book_id: int):
        """
        Удаляет книгу по ID.
        """
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Книга с ID {book_id} успешно удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        """
        Находит книгу по ID.
        """
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books(self, query: str, field: str):
        """
        Ищет книги по указанному полю (title, author, year).
        """
        result = [
            book for book in self.books
            if query.lower() in str(getattr(book, field)).lower()
        ]
        if result:
            print("Найденные книги:")
            self.display_books(result)
        else:
            print("Книги по указанному запросу не найдены.")

    def display_books(self, books: Optional[List[Book]] = None):
        """
        Отображает список книг.
        """
        books = books if books is not None else self.books
        if not books:
            print("Библиотека пуста.")
        else:
            print("Список книг:")
            for book in books:
                print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, "
                      f"Год: {book.year}, Статус: {book.status}")

    def update_status(self, book_id: int, status: str):
        """
        Обновляет статус книги.
        """
        book = self.find_book_by_id(book_id)
        if book:
            book.status = status
            self.save_books()
            print(f"Статус книги с ID {book_id} успешно обновлен на '{status}'.")
        else:
            print(f"Книга с ID {book_id} не найдена.")
