#include "lists.h"

/**
 *  insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head of list
 * @number: integer
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *tmp;

	if (head == NULL)
		return (NULL);
	tmp = *head;
	while (tmp)
	{
		if (tmp->n < number)
		{
			new->n = number;
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
	}
	return (NULL);
}
