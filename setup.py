from distutils.core import setup

setup(
    name = "sorl",
    version = "3.2ctl",
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
