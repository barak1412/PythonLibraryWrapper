from setuptools import setup, Extension
import shutil
import os


def copy_and_overwrite(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)

MAJOR = 1
MINOR = 0
BUGFIX = 0
VERSION = '{}.{}.{}'.format(MAJOR, MINOR, BUGFIX)
def copy_lib_files():
	WINDOWS_DST_PATH = "C:\\PythonLib\\v{}".format(VERSION)
	copy_and_overwrite("./libs/windows", WINDOWS_DST_PATH)

copy_lib_files()

setup(
    # Information
    name = "library_lib",
    version = VERSION,
    author = "Barak David",
    license = "MIT",
    keywords = "Example of cross-platform library wrapper.",
	packages = ['library_lib', 'library_lib.wrapper']
)