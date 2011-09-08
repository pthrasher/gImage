from distutils.core import setup

setup(
    name='gImage',
    version='1.0.1',
    author='Philip Thrasher',
    author_email='philipthrasher@gmail.com',
    packages=['gimage'],
    scripts=[],
    url='https://github.com/pthrasher/gimage',
    license='LICENSE.txt',
    description='Search google images, return first result.',
    long_description=open('README.txt').read(),
)

