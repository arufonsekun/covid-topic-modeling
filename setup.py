from setuptools import setup, find_packages

with open('readme.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='topic-modeling-final-project',
    version='0.0.1',
    description='Topic modeling concerning covid-19 news',
    long_description=readme,
    author='Junior Vitor Ramisch',
    author_email='junior.ramisch@gmail.com',
    url='https://github.com/arufonsekun/topic-modeling-final-project',
    license=license,
    packages=find_packages()
)
