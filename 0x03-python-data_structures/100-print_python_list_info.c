#include <listobject.h>
#include <object.h>
#include <stdio.h>
#include <Python.h>

/**
* print_python_list_info - prints some basic info about Python lists
* @p: a python list
*/

void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *list;

	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", list->Allocated);

	for (i = 0; i < PyList_Size(p); i++)
	{
		list = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(list)->tp_name);
	}
}
