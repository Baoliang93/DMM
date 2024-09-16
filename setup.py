from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='DMM_PyTorch',
    version='0.1.2',
    description='Debiased Mapping for Full-Reference Image Quality Assessment',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['DMM_PyTorch'],
    author='Baoliang CHEN',
    author_email='blchen@scnu.edu.cn',
    install_requires=["torch>=1.0"],
    url='https://github.com/Baoliang93/DMM',
    keywords = ['pytorch', 'Quality','Debiased','Full-reference','metric'], 
    platforms = "python",
    license='MIT',
)

