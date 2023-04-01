from setuptools import find_packages, setup
from typing import List

HYPH_E="-e ."
def get_requirements(file_path: str)->List[str]:
    """
    This function will return the list of requiements
    """
    requirements=[]
    with open('requirements.txt') as f:
        requirements= f.readlines()
        requirements= [req.replace('\n',"") for req in requirements]
        if HYPH_E in requirements:
            requirements.remove(HYPH_E)
    return requirements        
setup(
    name='mlproject',
    version="0.0.1",
    author="Naraendra",
    author_email="naraendradendi@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements("requirements.txt")


)