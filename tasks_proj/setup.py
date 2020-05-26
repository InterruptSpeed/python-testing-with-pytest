from setuptools import setup, find_packages

setup(
    name="tasks",
    description="Tasks project from Python Testing with pytest",
    version="0.1",
    author="Brian Okken",
    author_email="brian@pythontesting.net",
    url="https://pragprog.com/book/bopytest/python-testing-with-pytest",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
),
