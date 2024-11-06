# https://python-intermedio.readthedocs.io/es/latest/virtual_environment.html
# https://pipenv-es.readthedocs.io/es/latest/
# https://stackoverflow.com/a/41573588/1727383
# virtualenv is a very popular tool that creates isolated Python environments for Python libraries.
# pipenv aims to combine Pipfile, pip and virtualenv into one command on the command-line.
# pyenv is used to isolate Python versions.

from datetime import date

from a3py.simplified.datetime import date2str

if __name__ == '__main__':
    # STEP 1: Install the virtual environment.
    #   `pip install virtualenv`
    # STEP 2: Create a virtual environment.
    #   `python3 -m venv venv2`
    # STEP 3: Activate the virtual environment.
    #   `source venv/bin/activate`
    #   `whereis python`
    #   `whereis pip`
    # STEP 4: Show and install the requirements.txt file.
    #   `pip install -r requirements.txt`
    # STEP 5: Execute this file.
    my_date = date2str(date(2019, 10, 3))

    assert my_date == '2019-10-03'
    print(f'My date: {my_date} ({type(my_date)})')
