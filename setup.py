from setuptools import find_packages,setup


HPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->list[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HPEN_E_DOT in requirements:
            requirements.remove(HPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Abhijith',
    author_email='abhijithpilakka@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')

)