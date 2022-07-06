# фаил c тестами № 2
# Основной текст задания находится в файле main_summer_test.py
#
from functools import reduce

# Исходная функция:
import pytest


def multiplicator(*args):
    return reduce(lambda x, y: x*y, args)


# TODO здесь необходимо сделать рефакторинг
@pytest.fixture
def incoming_list():
    return [1, "2", 10, "20", 1, 5, 3, 8]


def test_multiplicator(list_creator):
    # TODO напишите тест здесь
    list_multi = reduce(lambda x, y: x*y, list_creator)
    assert multiplicator(*list_creator) == list_multi
