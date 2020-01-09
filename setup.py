from setuptools import setup

# Use README for the PyPI page
with open('README.md') as f:
    long_description = f.read()

setup(
    name='dotflz',
    version='0.2',
    packages=['dotflz'],
    url='https://github.com/ivanjermakov/dotflz',
    license='MIT',
    author='Ivan Ermakov',
    author_email='ivanjermakov1@gmail.com',
    description='Utility to keep copies of dotfiles in one place',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3',
    install_requires=['wheel', 'pyyaml', 'glob3', 'more-itertools', 'datetime', 'click']
)
