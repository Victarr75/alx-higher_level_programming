#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints information about a Python list
 * @list_obj: Pointer to a PyObject representing the list
 *
 * Return: Void
 */
void print_python_list_info(PyObject *list_obj)
{
    long int size, i;
    PyListObject *py_list;
    PyObject *item;

    size = Py_SIZE(list_obj);
    printf("[*] Python List Size: %ld\n", size);

    py_list = (PyListObject *)list_obj;
    printf("[*] Allocated Memory: %ld\n", py_list->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(list_obj, i);
        printf("Element %ld: Type = %s\n", i, Py_TYPE(item)->tp_name);
    }
}
