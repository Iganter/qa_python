import pytest
from main import BooksCollector


class TestBooksCollector:
    @pytest.mark.parametrize('title', [
        'Гордость и предубеждение и зомби',
        'Что делать, если ваш кот хочет вас убить'
    ])
    def test_add_new_book_adds_two_books(self, collector, title):
        collector.add_new_book(title)
        assert title in collector.get_books_genre()
        assert collector.get_book_genre(title) == ''

    def test_add_new_book_rejects_duplicates_and_long_names(self, collector):
        collector.add_new_book('Тестирование Дот Ком')
        collector.add_new_book('Тестирование Дот Ком')
        collector.add_new_book('A' * 41)
        books_dict = collector.get_books_genre()
        assert 'Тестирование Дот Ком' in books_dict and len(books_dict) == 1

    def test_set_and_get_book_genre_returns_correct_genre(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

        collector.set_book_genre('Дюна', 'Научная фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_books_with_specific_genre_returns_expected_genre(self, collector):
        collector.add_new_book('Трое в лодке, не считая собаки')
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Трое в лодке, не считая собаки', 'Комедии')
        collector.set_book_genre('Десять негритят', 'Детективы')

        result = collector.get_books_with_specific_genre('Комедии')
        assert result == ['Трое в лодке, не считая собаки']

    def test_get_books_with_specific_genre_returns_empty_list_when_no_matching_books(self, collector):
        assert collector.get_books_with_specific_genre('Фантастика') == []

    def test_get_books_for_children_excludes_age_rated(self, collector):
        collector.add_new_book('Вредные советы')
        collector.add_new_book('Зов Ктулху')
        collector.set_book_genre('Вредные советы', 'Комедии')
        collector.set_book_genre('Зов Ктулху', 'Ужасы')
        result = collector.get_books_for_children()
        assert result == ['Вредные советы']

    def test_add_book_in_favorites_adds_book(self, collector):
        collector.add_new_book('Изучаем Python')
        collector.add_book_in_favorites('Изучаем Python')
        assert collector.get_list_of_favorites_books() == ['Изучаем Python']

    def test_add_book_in_favorites_twice_does_not_duplicate(self, collector):
        collector.add_new_book('Тестирование ПО')
        collector.add_book_in_favorites('Тестирование ПО')
        collector.add_book_in_favorites('Тестирование ПО')
        favorite_books = collector.get_list_of_favorites_books()
        assert favorite_books == ['Тестирование ПО'] and len(favorite_books) == 1

    def test_delete_book_from_favorites_deletes_book(self, collector):
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_which_isnt_in_favorites(self, collector):
        collector.delete_book_from_favorites('Бесы')
        assert collector.get_list_of_favorites_books() == []

    def test_get_book_genre_returns_expected_genre(self, collector):
        collector.add_new_book('Гиперион')
        collector.set_book_genre('Гиперион', 'Фантастика')
        assert collector.get_book_genre('Гиперион') == 'Фантастика'

    def test_get_books_genre_returns_expected_dict(self, collector):
        collector.add_new_book('Солярис')
        collector.add_new_book('Шутки Господа')
        collector.set_book_genre('Солярис', 'Фантастика')
        collector.set_book_genre('Шутки Господа', 'Комедии')
        expected_dict = {
            'Солярис': 'Фантастика',
            'Шутки Господа': 'Комедии'
        }
        assert collector.get_books_genre() == expected_dict

    def test_get_list_of_favorites_books_returns_expected_list(self, collector):
        collector.add_new_book('Собака Баскервилей')
        collector.add_book_in_favorites('Собака Баскервилей')
        assert collector.get_list_of_favorites_books() == ['Собака Баскервилей']
