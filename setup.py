import os
import imp
from setuptools import setup, find_packages

VERSIONFILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'src', 'crl', 'doc', '_version.py')

def get_version():
    return imp.load_source('_version', VERSIONFILE).get_version()


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='crl.doc',
    version=get_version(),
    author='Petri Huovinen',
    author_email='petri.huovinen@nokia.com',
    description='Documenation tools for Common Robot Libraries',
    install_requires=['ute-doc'],
    long_description=read('README.rst'),
    url='https://gerrite1.ext.net.nokia.com/#/admin/projects/crl/crl-doc',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    namespace_packages=['crl'],
    entry_points={
        'console_scripts': [
            'crl_doc_generate_rst = crl.doc.cmdline:cmdline']}
)
