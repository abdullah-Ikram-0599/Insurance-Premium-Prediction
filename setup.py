from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:

    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(

    name = 'Insurance-Premium-Prediction',
    version = '0.0.1',
    author= 'Abdullah',
    author_email= 'abdullah.ikram.0599@gmail.com',
    packages= find_packages(),
    # install_requires = ['pandas', 'numpy', 'seaborn', 'matplotlib', 'sklearn', 'xgboost', 'joblib']
    install_requires = get_requirements('requirements.txt')








)