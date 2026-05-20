from pathlib import Path

from setuptools import setup, find_packages

# also change in version.py
VERSION = "2.1.3"
DESCRIPTION = "A trading framework for cryptocurrencies"
BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "requirements.txt", "r", encoding="utf-8") as f:
    REQUIRED_PACKAGES = f.read().splitlines()

with open(BASE_DIR / "README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='billi-bot',
    version=VERSION,
    author="Neda Digital Agency",
    packages=find_packages(),
    description="BILLI - A trading framework for cryptocurrencies",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/neweradigitaleagency-tech/Billi-bot",
    project_urls={
        'Source': 'https://github.com/neweradigitaleagency-tech/Billi-bot',
    },
    install_requires=REQUIRED_PACKAGES,
    entry_points='''
        [console_scripts]
        billi=billi.__init__:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    include_package_data=True,
    package_data={
        '': ['*.dll', '*.dylib', '*.so', '*.json'],
    },
)
