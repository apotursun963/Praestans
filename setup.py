from setuptools import setup, find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="praestans",
    version="0.1.0",
    author="Abdullah Tursun",
    author_email="tursunapo333@gmail.com",
    description="python module that enables easy conversions between number systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apotursun963/praestans",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
