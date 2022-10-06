HOW TO RELEASE
==============

```bash
PYTHONPATH="tests" python -m unittest 2>&1
PYTHONPATH="tests" python -m unittest 2>&1 | grep "***"
PYTHONPATH="tests" python -m unittest 2>&1
git status

vi setup.py 
git add setup.py 



pip install -r requirements-dev.txt --upgrade


rm -rf dist/*
python setup.py sdist bdist_wheel
#python -m twine upload --repository testpypi dist/*
python -m twine upload --repository robotica --repository-url http://pypi.robotica.ml/ dist/*
```
