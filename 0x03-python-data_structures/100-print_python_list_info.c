#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints information about a Python list object.
 * @p: Pointer to the Python list object.
 */
void print_python_list_info(PyObject *p) {
    if (p == NULL || !PyList_Check(p)) {
        fprintf(stderr, "Error: Invalid Python list object.\n");
        return;
    }

    long int size = PyList_Size(p);
    int i;
    PyListObject *list_obj = (PyListObject *)p;

    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", list_obj->allocated);
    for (i = 0; i < size; i++) {
        PyObject *item = list_obj->ob_item[i];
        printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
    }
}
