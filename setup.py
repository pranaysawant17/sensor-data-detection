from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:

    """
    this function will return list of requirements
    """

    requirement_list:List[str] = []
    

    """
    write code to read requiremnet.txt and return list
    """
    # with open ("sensor-data-detection/requirements.txt",'r') as f:
    #     for line in f:
    #         requirement_list.append(line)

    return requirement_list

setup(

    name="sensor",
    version="0.0.1",
    author="pranay",
    author_email="pranaysawant17394@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements() #["pymongo==4.2.0"]
    
)

