from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Folder sort',
    author='Maksym Blazhev',
    author_email='maximkhersonua@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
)
