python-package "Brain Games" (study only)
----

[![Maintainability](https://api.codeclimate.com/v1/badges/cb3c0c8f1e7c1d9ae86b/maintainability)](https://codeclimate.com/github/ivekhov/python-project-lvl1/maintainability)

![Python CI](https://github.com/ivekhov/python-project-lvl1/workflows/Python%20CI/badge.svg)

----
This is study package "Brain Games" made on Hexlet Project #1 in Python Programmer profession.

asciinema recordings:

brain-even(step #5):
[![asciicast](https://asciinema.org/a/hJJg7VLxFLCKi81eTyvjQiwqC.svg)](https://asciinema.org/a/hJJg7VLxFLCKi81eTyvjQiwqC)

brain-cals(step #6):
[![asciicast](https://asciinema.org/a/QVNPLCtuhRSmWtQSsIjiCoGkK.svg)](https://asciinema.org/a/QVNPLCtuhRSmWtQSsIjiCoGkK)

brain-gcd(step #7):
[![asciicast](https://asciinema.org/a/wcqJKfMf2BdL3X78UrLGV5Idj.svg)](https://asciinema.org/a/wcqJKfMf2BdL3X78UrLGV5Idj)

brain-progression(step #8): 
[![asciicast](https://asciinema.org/a/e5OiZpYWLicOOixoRMj5tlmu1.svg)](https://asciinema.org/a/e5OiZpYWLicOOixoRMj5tlmu1)

brain-prime(step #9):
[![asciicast](https://asciinema.org/a/x0OwsKo0KmvP875Fbk03ZHV7x.svg)](https://asciinema.org/a/x0OwsKo0KmvP875Fbk03ZHV7x)

-----
Poetry (just4memory).

**Создание окружения для разработки.**

* Инициализировать проект
```
poetry new project_name
```
* Добавить пакет в проект
```
poetry add package_name
```
* Установка зависимостей ([poetry basics](https://python-poetry.org/docs/basic-usage/) and [commands](https://python-poetry.org/docs/cli/))
```
poetry update
poetry install
```

* Тесты
```
make test
```
* Проверка кода линтером flake8:
```
make lint
```
* Установка репозитория:
```
poetry config repositories.testPyPi https://test.pypi.org/legacy
```
* Установка доступа к репозиторию:
```
poetry config http-basic.{login}_brain_games {login} {password}
```
* Сборка пакета:
```
poetry create package_name (в первый раз)
poetry build
```
* Публикация пакета:
```
poetry publish --repository testPyPi
```
* Загрузка опубликованного пакета: 
```
pip install --index-url https://test.pypi.org/simple/
poetry install (второй вариант обновления в локальной системе)
```
* Вызов функции из корня пакета
```
poetry run python -m brain_games.scripts.brain-even
poetry run brain-even (второй вариант вызова)
brain-even (при наличии шебанга)
```
* Запуск проверки стиля кода: 
```
poetry run flake8 brain_games
```
* Cделать аскинему ([about](https://asciinema.org/docs/how-it-works))
```
asciinema rec
```
