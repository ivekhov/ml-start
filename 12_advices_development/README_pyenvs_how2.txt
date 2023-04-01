
PYENV INSTALLATION AND ENV MANAGEMENET

#0 install python version from git and compile it 
(when no python version is on the system)


#1 install pyenv 
git clone https://github.com/pyenv/pyenv.git ~/.pyenv

#2 Configure your shell's environment for Pyenv into .bashrc

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi


# 3 ON MAC
pyenv-virtualenv

#4 taken from https://akrabat.com/creating-virtual-environments-with-pyenv/
$ brew install readline xz
$ brew install pyenv pyenv-virtualenv


# NOT ON MAC install virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc


== FINISH INSTALLATION ==




HOW TO USE

# install python version
$ pyenv install 3.7.4

#  create environment
$ pyenv virtualenv 3.7.4 apps3
pyenv virtualenv [PYTHON VERSION] [NAME of ENV]


# envs are stored in .pyenv/versions/

#  activate environment
pyenv activate NAME

# deactivate 
pyenv deactivate


PIPENV TOOL
---------
#0 Install tool
pip3.7 install --user pipenv

or 
sudo -H pip3.7 install -U pipenv


#1 initilize project and create environment (env name = will be name of folder)
# from catalog with project
pipenv --python python3.7


#2 while working daily 
# from project folder -- activate  this command 
pipenv shell

# install packages (after activating environment) 
pipenv install PACKAGENAME



------

install package inside environment
$ pip install -e .
