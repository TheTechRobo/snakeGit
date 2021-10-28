from setuptools import setup
import os
with open(os.devnull, 'w') as a:
    print("If this raises an error, you're using python 2 - not supported.", file=a) #get rid of python 2 users
with open("README.md", "r") as file:
    long_desc = file.read()
import sys
if sys.version_info < (3,7):
    sys.exit('Sorry, Python < 3.7 is not supported')
setup(
    name='pyyGit',
    version='0.4',
    description='the missing Python git module',
    long_description=long_desc,
    python_requires='>3.7.0',
    license='DBAD',
    packages=['pyGit'],
    author='TheTechRobo',
    author_email='thetechrobo@outlook.com',
    keywords=['git', 'easy', 'thetechrobo'],
    url='https://github.com/TheTechRobo/PyGit',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3'
    ],
    project_urls={
        'Documentation': 'https://github.com/thetechrobo/PyGit/wiki',
        'Source': 'https://github.com/thetechrobo/pygit',
        'Tracker': 'https://github.com/thetechrobo/pygit/issues',
    },

    long_description_content_type='text/markdown',

)
