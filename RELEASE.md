HOW TO RELEASE
==============

PYTHONPATH="tests" python -m unittest 2>&1
PYTHONPATH="tests" python -m unittest 2>&1 | grep "***"
PYTHONPATH="tests" python -m unittest 2>&1
git status

vi setup.py 
git add setup.py 



pip install -r requirements-dev.txt --upgrade


python setup.py sdist bdist_wheel
#python -m twine upload --repository testpypi dist/English_to_IPA-0.3.0a14-py3-none-any.whl dist/English-to-IPA-0.3.0a14.tar.gz 
python -m twine upload --repository robotica --repository-url http://admin:admin@pypi.robotica.ml/ dist/*
