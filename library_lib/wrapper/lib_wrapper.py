import os
from ctypes.util import find_library
from ctypes import cdll

os.environ['PATH'] += 'C:\PythonLib;'
lib_dll_path = find_library('ExampleDLL')
dll_handle = cdll.LoadLibrary(lib_dll_path)
print(dll_handle)

class LibWrapper(object):
	@staticmethod
	def print_hello():
		print('Hello!')