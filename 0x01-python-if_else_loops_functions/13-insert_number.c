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
	listint_t *pre;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	tmp = *head;
	tmp = tmp->next;
	pre = *head;
	while (pre)
	{
		if (tmp->n > number)
		{
			new->n = number;
			new->next = tmp;
			pre->next = new;
			return (new);
		}
		tmp = tmp->next;
		pre = pre->next;
	}
	return (NULL);
}
