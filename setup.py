from os import path
from setuptools import setup

# read the contents of your description file

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="DirectPayOnline",
    version="0.4",
    description="A python package to easy the integration with Direct Online Pay (Mpesa, TigoPesa, AirtelMoney, Card Payments)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kalebu/python-dpo",
    download_url="https://github.com/Kalebu/python-dpo/archive/refs/tags/v0.2.tar.gz",
    author="Jordan Kalebu",
    author_email="isaackeinstein@gmail.com",
    license="MIT",
    packages=["DirectPayOnline"],
    keywords=[
        "mobile payments",
        "DirectPayOnline(DPO)",
        "dpo",
        "payment aggregator",
        "mobile money package",
    ],
    install_requires=["requests", "xmltodict", "pydantic"],
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
