from setuptools import find_packages
from setuptools import setup

setup(
    name='rosidl_runtime_py_tests',
    version='0.8.0',
    packages=find_packages(exclude=['test']),
    zip_safe=False,
    author='Dirk Thomas',
    author_email='dthomas@osrfoundation.org',
    maintainer='Jacob Perron',
    maintainer_email='jacob@openrobotics.org',
    url='https://github.com/ros2/rosidl_runtime_py/tree/master/rosidl_runtime_py_tests',
    download_url='https://github.com/ros2/rosidl_runtime_py/releases',
    keywords=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
    description='Runtime utilities for working with generated ROS interfaces in Python.',
    long_description=(
        'This package provides tests for functions for operations such as populating ROS messages '
        'and converting messages to different representations.'),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
)
