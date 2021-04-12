"""Build for windows."""

import os.path
from cx_Freeze import setup, Executable
from appteka.distrib import build_folder_name
from my_package import __version__
import dist

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))

os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


MATURE_MINOR_VERSION = 5

BASE = None
if int(__version__.split('.')[-1]) > MATURE_MINOR_VERSION:
    BASE = "Win32GUI"

EXECUTABLES = [Executable("gui", base=BASE)]


OPTIONS = {
    'build_exe': {
        'packages': ['pkg_resources._vendor', 'pyqtgraph', 'espmu', 'appteka'],
        'build_exe': build_folder_name(dist.NAME, __version__),
        # 'include_msvcr': True,
        # 'excludes': [
        #     'tkinter',
        #     'lib2to3',
        #     'distutils',
        #     'setuptools',
        #     'unittest',
        #     'test',
        #     'scipy',
        #     'matplotlib',
        # ],
    }
}


setup(
    name=dist.NAME,
    version=__version__,
    packages=dist.PACKAGES,
    package_data=dist.PACKAGE_DATA,
    data_files=dist.DATA_FILES,
    executables=EXECUTABLES,
    options=OPTIONS,
)
