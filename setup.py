from setuptools import setup, find_packages


def read(filename):
    return [
        req.strip() for req in open(filename).readlines()
    ]


setup(
    name="Brasil Prev",
    version="1.0.0",
    description="Sistema teste Brasil Prev",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt")
)
