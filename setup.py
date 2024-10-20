from setuptools import find_packages,setup
from typing import List
##automatically finds out all the packages
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    THIS FUCTION will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)



#This is like metadata version with all information about the project
setup(
name= 'mlproject',
version = '0.0.1',
author = 'samruddishetty',
author_email='65382899+samruddishetty@users.noreply.github.com',
packages=find_packages(), #is powerful
install_requires=get_requirements('requirements.txt')

)

