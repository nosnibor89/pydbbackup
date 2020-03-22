from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='pgbackup',
    version='0.1.0',
    author='Robinson Marquez',
    author_email='nosnibor1989@gmail.com',
    description='A utility for backing up postgres databases',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/nosnibor89/pgbackup",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main'
        ]
    }
)
