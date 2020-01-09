from setuptools import setup

setup(
    name='dotflz',
    version='0.1',
    packages=['dotflz'],
    url='https://github.com/ivanjermakov/dotflz',
    license='MIT',
    author='Ivan Ermakov',
    author_email='ivanjermakov1@gmail.com',
    description='Utility to keep copies of dotfiles in one place',
    install_requires=['wheel', 'pyyaml', 'glob3', 'more-itertools', 'datetime', 'click']
)
