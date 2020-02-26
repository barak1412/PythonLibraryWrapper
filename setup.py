from setuptools import setup, Extension
import shutil
import os


def copytree(src, dst, symlinks=False, ignore=None):
	for item in os.listdir(src):
		s = os.path.join(src, item)
		d = dst#os.path.join(dst, item)
		if os.path.isdir(s):
			shutil.copytree(s, d, symlinks, ignore)
		else:
			shutil.copy2(s, d)


def copy_lib_files():
	WINDOWS_DST_PATH = "C:\PythonLib"
	copytree("./libs/windows", WINDOWS_DST_PATH)

copy_lib_files()

setup(
    # Information
    name = "library_lib",
    version = "1.0.0",
    author = "Barak David",
    license = "MIT",
    keywords = "Example of cross-platform library wrapper.",
	packages = ['library_lib', 'library_lib.wrapper']
)