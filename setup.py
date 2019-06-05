from setuptools import setup, find_packages

setup(
    name='run',
    version='1.0',
    description='Run.',
    url='https://github.com/benikm91/run-py',
    author='Benjamin Meyer',
    author_email='benikm91@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    python_requires='>=3',
    include_package_data=True,
    dependency_links=[
        "git+ssh://git@github.com/benikm91/timer-py.git"
    ],
    install_requires=[
        'Events==0.3',
        'python-dateutil==2.8.0',
        'six==1.12.0',
        'timer==1.0',
    ],
)
