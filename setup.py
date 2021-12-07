from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in incidents/__init__.py
from incidents import __version__ as version

setup(
	name="incidents",
	version=version,
	description="Gestion des incidents groupe cosumar",
	author="Cosumar digital factory",
	author_email="m.boujaha@cosumar.ma",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
