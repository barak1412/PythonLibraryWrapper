import os
from ctypes.util import find_libraty
from ctypes import cdll

os.environ['PATH'] += 'C:\PythonLib;'
lib_dll_path = find_libraty('ExampleDLL')
dll_handle = cdll.LoadLibray(lib_dll_path)

class LibWrapper(object):
	@staticmethod
	def print_hello():
		print('Hello!')