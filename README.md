# clspy
 

[clspy](https://clspy.readthedocs.io/) clspy is a set of fast programming tools 
that are gradually generated during the python learning process.


# [ChangeLog](ChangeLog.md)

* Only support `python3`
* Posted private [pypi server](https://pypi.lovelacelee.com/)

# How-To

Here is for the lost memory:

## Use clspy command toolsets

```
$ pip3 install clspy -U
$ clspy --version
$ clspy --help
```

## Running test cases

```
$ pip3 install pytest pytest-html
$ pip3 install -U -r requirements/dev.txt
$ pip3 install -U -r requirements/prod.txt
$ python3 pytest
```

## Develop environment build 

setup.py help

```
$ python3 setup.py --help-commands
```

build doc
```
$ python3 setup.py doccreate
$ python3 setup.py docbuild
$ python3 setup.py docrun
```

publish project to pypi or local pypi

```
$ python3 setup.py publish -r
$ python3 setup.py distclean
```

## Install to system or just for specified user

for user

```
python3 install clspy --user
python3 -m clspy.cli --help
```

# Depends

* [DEV requirements](requirements/dev.txt)
* [PROD requirements](requirements/prod.txt)