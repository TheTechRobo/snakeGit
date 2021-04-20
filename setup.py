from setuptools import setup

with open("README.md", "r") as file:
    long_desc = file.read()

setup(
    name='pyyGit',
    version='0.3.1',
    description='the missing Python git module',
    long_description=long_desc,
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

    python_requires='>=3',
)
