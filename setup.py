import pathlib
from setuptools import setup

from nqueenplay.version import VERSION


BASE_DIR = pathlib.Path(__file__).parent
README = (BASE_DIR / "README.md").read_text()

setup(
    name="nqueenplay",
    version=VERSION,
    author="eiproject",
    author_email="razifrizqullah@gmail.com",
    url='https://github.com/eiproject/nqueenplay',
    description='N-Queens puzzle player. This tool will generate randomly or randomly locked puzzle, you may use this as "a boxing bag" to practice problem solving algorithm.',
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=[
        'nqueenplay', 
        ],
    include_package_data=True,
    install_requires=[],
    keywords=['n-queens', 'nqueens', 'puzzle'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License",
    ]
)
