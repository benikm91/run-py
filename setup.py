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
    install_requires=[
    ],
)
