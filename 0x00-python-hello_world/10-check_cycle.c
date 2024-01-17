#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *tmp;

	if (list == NULL)
		return (0);
	
	current = list;
	while (current)
	{
		tmp = current->next;
		while (tmp)
		{
			if (tmp == current)
				return (1);
			tmp = tmp->next;
		}
		current = current->next;
	}
	return (0);
}
