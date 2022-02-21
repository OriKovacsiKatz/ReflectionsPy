from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Python reflections module'
LONG_DESCRIPTION = 'Reflections Use inspect python module to get run time details of python entities'

# Setting up
setup(
       # the name must match the folder name 'pyreflections'
        name="pyreflections", 
        version=VERSION,
        author="Ori Kovacsi Katz",
        author_email="<ori.newk@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'reflections'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)