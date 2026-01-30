from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """This function will return the list of requirements"""
    req_list:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()

                if requirement and requirement != '-e .':
                    req_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found ")

    return req_list

print(get_requirements())

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Manthan",
    author_email="manthan@networksecurity.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)