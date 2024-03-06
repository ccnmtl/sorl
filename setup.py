from setuptools import setup

setup(
    name = "sorl",
    version = "3.4",
    install_requires=[
        "Django",
    ],
    packages = [
        "sorl",
        "sorl.thumbnail",
        "sorl.thumbnail.templatetags",
        "sorl.thumbnail.tests",
    ],
)
