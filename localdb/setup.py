import os
from setuptools import setup, find_packages

setup(name='localdb',
      version='1.0',
      description='Simple CRD supported key_value datastore',
      author='SasikiranJ',
      author_email='sasikiran1115@gmail.com',
      download_url='https://github.com/SasikiranJ/localdb',
      license='MIT',
      install_requires=['flask>=1.1.1'
                        ],
      packages=find_packages())
