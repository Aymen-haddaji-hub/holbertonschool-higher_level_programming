#include "lists.h"

/**
 * check_cycle - checks if singly linked list has a cycle in it
 * @list: a pointer to the list
 *
 * Return: (1) if there is a cycle
 * ------- (0) otherwise
 */int check_cycle(listint_t *list)
{
    listint_t *head;
    listint_t *tmp;

    if (list == NULL)
        return (0);
    tmp = list;
    head = list->next;
    while (tmp && head && head->next)
    {
        if (tmp == head)
            return (1);
        tmp = tmp->next;
        head = head->next->next;
    }
    return (0);
}
