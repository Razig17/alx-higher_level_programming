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
	PyListObject *list = (PyListObject *)p long int size = PyList_Size(p)

	    printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->Allocated);

	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}
