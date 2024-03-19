#include "lists.h"

/**
 * is_palindrome - Check if a singly linked list is a palindrome.
 * @head: Address of the list to check
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *current = *head;
    listint_t *last = *head, *prev = NULL;

    if (!head || !(*head))
        return (1);
    if (!(*head)->next)
        return (1);

    /* Reach the end of the list */
    while (last->next)
        last = last->next;

    while (current)
    {
        if (prev)
        {
            while ((last->next != prev) && last->next)
                last = last->next;

            if (last == current)
                break;
        }

        if (last->n == current->n)
        {
            if (current->next == last)
                break;

            prev = last;
            current = current->next;
            last = current;
        }
        else
            return (0);
    }
    return (1);
}
