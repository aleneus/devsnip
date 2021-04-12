"""Setup script."""

from setuptools import setup
from my_package import __version__
import dist


entry_points = {
    'gui_scripts': [
        'pdc_demo = pdc_demo.gui:run'
    ]
}


setup(
    name=dist.NAME,
    version=__version__,
    description=dist.DESCRIPTION,
    author=dist.AUTHOR,
    author_email=dist.AUTHOR_EMAIL,
    keywords=dist.KEYWORDS,
    classifiers=dist.CLASSIFIERS,

    install_requires=dist.INSTALL_REQUIRES,
    packages=dist.PACKAGES,
    package_data=dist.PACKAGE_DATA,
    data_files=dist.DATA_FILES,

    entry_points=entry_points,
)
