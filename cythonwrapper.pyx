cdef extern from "helloworld.h" namespace "cythontest":
	cdef cppclass CppWrapper:
		void helloWorld()

cdef class CythonWrapper:
	cdef CppWrapper* thisptr
	def helloWorld(self):
		self.thisptr.helloWorld()
