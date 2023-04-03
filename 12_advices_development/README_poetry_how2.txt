
==== PROJECT initialization ====


-- inside EMPTY parent folder:

1: $ poetry new NAME		# creating a project
2: $ ? -- optional  cd .NAMDE/ and edit pyprojects.toml in  [tool.poetry.dependencies] "python = "^3.8""


ENV USE or INIT:
3.1$ optional if py 38 needed: 
$ poetry env use ~/.pyenv/versions/3.8.13/bin/python

if not 3.1:
3.2 $ poetry init


checking: 
$ poetry run python
$ poetry config --list


4: add package:
$ poetry add PACK-NAME --group -dev 

5: install it 
$ poetry install

==== END of PROJECT  initialization ====



===== POETRY INSTALLATION on Mac ===============================================================

0
поставить поетри под 3 версию пайтоне - см подробно
https://ru.hexlet.io/blog/posts/ispolzovanie-neskolkih-versiy-python-na-unix-podobnyh-operatsionnyh-sistemah

---
- по степам тут 
https://ru.hexlet.io/projects/49/members/9745?step_id=207

 and here - 
https://ru.hexlet.io/courses/python-setup-environment/lessons/start-with-poetry/theory_unit 

---

# Trouble shooting:

$ pyenv install 3.8.13
$ python3 -m venv $HOME/.poetry.venv
$ source  $HOME/.poetry.venv/bin/activate
$ pip install poetry
$ ln -s $HOME/.poetry.venv/bin/poetry $HOME/.local/bin
$ export PATH="$HOME/.local/bin:$PATH"
$ poetry config virtualenvs.in-project true

$
vim .profile and write to it:
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
        . "$HOME/.bashrc"
    fi
fi
#

====================================================================



==== OLD info ====


#1 inside EMPTY directory call 	
"poetry new PROJECT_NAME"


//
Если нужно использовать в поетри версию питона другую, чем системную

1)  После "poetry new PROJECT_NAME" в .toml  прописать нужную версию питона, например:
==
[tool.poetry.dependencies]
python = "^3.8"
==

2) Задать в поетри: 
poetry env use .venv/bin/python

3) Проверить
poetry run python

//

#2 call "poetry init"



#3 установка пакетов в проект: 

Poetry add PACKAGE_NAME	      # для целей последующего использования юзером

Poetry add PACKAGE_NAME --dev # для целей разработки 


## 
Add in pyproject.toml

## 


poetry install

-- no need 4
-- no need activate env created

дальше проверка работы


https://python-poetry.org/docs/managing-environments/


-------
2 ЧАСТЬ
-------

#1 запуск скрипта проекта через поетри 
poetry run SCRIPTNAME (f.e. brain-gcd)

Example:
poetry run python -m brain_games.scripts.brain_games
poetry run python -m gendiff.scripts.gendiff -h


#2 проверка стиля через поетри
poetry run flake8 brain_games
OR
make lint


#3 перестроение пакета проекта через поетри после обновления кода пакета/проекта
poetry build
OR
make build 

#4 установка пакета через поетри  локально после обновления кода 
poetry install
OR 
make package-install 


#5 публикация пакета  во вншений репозиторий 
после внесения изменений
poetry publish --repository testPyPi
		name
		password

naaavI                                                                                               
Ns79rcPzp3gZcuq 



#6 установка глобально обновить из репозитория
python  -m pip install  -i https://test.pypi.org/simple/ ivekhov-gendiff

OR
pip install -i https://test.pypi.org/simple/ ivekhov-gendiff


#7 тесты
make test 


#8 запуск скрипта после установки пакета как самостоятельной программы
- прописать как точку входа в файле .toml
- SCRIPT-NAME
instead of "poetry run python -m gendiff.scripts.gendiff -h" call just "gendiff -h"


==============================

Для сдачи на проверку детали: 
#7 сделать аскинему
asciinema rec

#
asciinema recordings:

brain-even(step #5):
[![asciicast](https://asciinema.org/a/hJJg7VLxFLCKi81eTyvjQiwqC.svg)](https://asciinema.org/a/hJJg7VLxFLCKi81eTyvjQiwqC)
#


-------
##############################################################################################################



== INSTALLATION POETRY === 
new

install python version globally from sources and compillation (git, make, etc #0 step) +
	
	install pyenv globally (git clone #1 step)  +
		
		install python versions like "pyenv install 3.9.10"
		(and make it global "pyenv global [PYTHON VERSION NAME NUMBER like '3.9.10']" )
			
			install poetry https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions 
			(The installer installs the poetry tool to Poetry’s bin directory. On Unix it is located at $HOME/.poetry/bin)

			add poetry to bash_profile or bashrc
				bashrc - system watches  first 
				bash_profile - system watches after bashrc 
					(if bash_profile exists)
					if bash_profile has the same instructions
						it rewrites bashrc 
			
			#open in vim and add:
			export PATH="$HOME/.poetry/bin:$PATH" 

			#check 
			poetry --version


			#create venv inside project folder:
			poetry config virtualenvs.in-project true

##############################################################################################################

Useful commands 

poetry add PACK_NAME
	- add package in project dependencies

poetry remove PACK_NAME
	- delete

poetry update --lock
	- update packages from dependencies w/0 crushing


poetry build
	-- сборка пакета для последующей установки
	для его установки локально "python3 -m pip install --user dist/hello-0.1.0-py3-none-any.whl"

	если нужна локальная установка пакета без его сборки, то "python3 -m pip install ." где "." -  текущая директория

---

---
Если нужно использовать в поетри версию питона другую, чем системную

1  После "poetry new PROJECT_NAME" в .toml  прописать нужную версию питона




poetry env use .venv/bin/python

---
Если нужно использовать в поетри версию питона другую, чем системную, то подменить командой:
?
# temporary set python version as local
Poetry local 3.8.13

poetry env use /full/path/to/python

потом такой же командой вернуть нужную

---






