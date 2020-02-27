import os
from ctypes.util import find_library
from ctypes import cdll
import ctypes
import platform


class LibWrapper(object):
	MAJOR = 1
	MINOR = 0
	BUGFIX = 0
	VERSION = '{}.{}.{}'.format(MAJOR, MINOR, BUGFIX)
	PLATFORM = 'x64' if ctypes.sizeof(ctypes.c_voidp) * 8 == 64 else 'x86'
	__dll_handler = None

	# initialize handler
	if platform.system() == 'Windows':
		new_path = 'C:\\PythonLib\\v{}\\{}'.format(VERSION, PLATFORM)
		if os.environ['PATH'][-1] == ';':
			os.environ['PATH'] += new_path+';'
		else:
			os.environ['PATH'] += ';'+new_path
		lib_dll_path = find_library('ExampleDLL')
		__dll_handler = cdll.LoadLibrary(lib_dll_path)
	else:
		raise Exception('Unsupported OS: {}'.format(platform.system()))

	@staticmethod
	def mul_op(x, y):
		c_x = ctypes.c_int(x)
		c_y = ctypes.c_int(y)
		return LibWrapper.__dll_handler.mul_op(c_x, c_y)