# 📚 Тесты для приложения BooksCollector

---

## 🛠 Организация тестового окружения

- **Фикстура `collector`**  
  Определена в `conftest.py` и создаёт новый экземпляр класса `BooksCollector` перед каждым тестом.

- **Параметризация**  
  Тест `test_add_new_book_adds_two_books` параметризован для проверки двух разных названий без дублирования кода.

---

## 🎯 Покрытые сценарии

### 1. Добавление новых книг  
**Тест:** `test_add_new_book_adds_two_books`  
- Проверяет, что после добавления название появляется в коллекции  
- Жанр у новой книги по умолчанию — пустая строка

---

### 2. Валидация при добавлении  
**Тест:** `test_add_new_book_rejects_duplicates_and_long_names`  
- Дублирующее добавление не происходит  
- Название длиной более 40 символов игнорируется

---

### 3. Получение жанров и словаря жанров

- **`test_get_book_genre_returns_expected_genre`**  
  Проверяет, что метод `get_book_genre` возвращает установленный жанр.

- **`test_get_books_genre_returns_expected_dict`**  
  Убеждается, что `get_books_genre` возвращает полный словарь всех добавленных книг и их жанров.

---

### 4. Установка и получение жанра  
**Тест:** `test_set_and_get_book_genre_returns_correct_genre`  
- Устанавливает жанр из списка доступных  
- Попытка задать несуществующий жанр не меняет уже установленный

---

### 5. Фильтрация по жанру  
- **`test_get_books_with_specific_genre_returns_expected_genre`**  
  Проверяет, что метод возвращает только книги с указанным жанром  
- **`test_get_books_with_specific_genre_returns_empty_list_when_no_matching_books`**  
  Гарантирует, что при отсутствии совпадений возвращается пустой список

---

### 6. Книги для детей  
**Тест:** `test_get_books_for_children_excludes_age_rated`  
- Метод `get_books_for_children` исключает жанры с возрастным рейтингом  
- Включает все остальные жанры

---

### 7. Работа с «Избранным»  
- **`test_add_book_in_favorites_adds_book`**  
  Проверяет, что книга успешно добавляется в избранное  
- **`test_add_book_in_favorites_twice_does_not_duplicate`**  
  Убеждается, что повторное добавление не создаёт дубликаты  
- **`test_delete_book_from_favorites_deletes_book`**  
  Подтверждает, что удаление из избранного работает корректно  
- **`test_delete_book_from_favorites_which_isnt_in_favorites`**  
  Убеждается, что удаление несуществующей книги не вызывает ошибок
- **`test_get_list_of_favorites_books_returns_expected_list`**  
  Проверяет, что `get_list_of_favorites_books` возвращает именно добавленные в избранное книги

---

> Каждый метод класса **BooksCollector** имеет по крайней мере один тест.  
> Тесты полностью изолированы и не используют глобального состояния.

