from setuptools import setup

with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setup(
    name='python-test',
    version='0.1.0',
    url='https://github.com/JesusBandaG/python-test.git',
    author='Jesús Banda',
    author_email='banda.j94@gmail.com',
    description='Colektia ETL process test.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='3.8'
)
