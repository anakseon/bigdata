# Сделайте mapper и reducer, чтобы посчитать среднее и дисперсию оценок за фильм.
import math
import sys
from unittest.util import sorted_list_difference


def mapper():
    # Читаем входные данные из stdin
    # Разбиваем строку на отдельные значения
    for line in sys.stdin:
        movie_id, rating = line.strip().split("\t")


# Отправляем каждую оценку в виде пары ключ-значение
# ключ: номер фильма
# значение: кортеж из оценки и единицы (для последующего расчета суммы и количества оценок)
print(f"{movie_id}\t{rating}\t1")

if __name__ == "__main__":
    mapper()


# Reducer.py:


def reducer():
    current_movie_id = None
    rating_sum = 0
    rating_count = 0
    rating_squared_sum = 0


for line in sys.stdin:
    movie_id, rating, count = line.strip().split("\t")

# Проверяем, изменился ли номер фильма
# Рассчитываем среднее и дисперсию для предыдущего фильма
if current_movie_id != movie_id:
    if current_movie_id is not None:
        average_rating = rating_sum / rating_count
        variance = rating_squared_sum / rating_count - (average_rating ** 2)

# Выводим результаты в stdout в формате "номер фильма\tсреднее\tдисперсия"
print(f"{current_movie_id}\t{average_rating}\t{variance}")

# Сбрасываем значения для нового фильма
current_movie_id = movie_id
rating_sum = 0
rating_count = 0
rating_squared_sum = 0

rating_sum += float(rating)
rating_count += int(count)
rating_squared_sum += float(rating) ** 2

# Рассчитываем среднее и дисперсию для последнего фильма
if current_movie_id is not None:
    average_rating = rating_sum / rating_count
    variance = rating_squared_sum / rating_count - (average_rating ** 2)
    print(f"{current_movie_id}\t{average_rating}\t{variance}")

if __name__ == "__main__":
    reducer()
