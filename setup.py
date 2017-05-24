"""Setup for question_generator_block XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='Question Generator XBlock',
    version='0.1',
    description='Question Generator XBlock',
    license='LGPL-3.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='xblock question generator',
    author='Vo Duc An',
    author_email='voducanvn@gmail.com',
    packages=[
        'question_generator_block',
    ],
    install_requires=[
    ],
    entry_points={
        'xblock.v1': [
            'question_generator_block = question_generator_block:QuestionGeneratorXBlock',
        ]
    },
    package_data=package_data("question_generator_block", ["static", "public"]),
)
