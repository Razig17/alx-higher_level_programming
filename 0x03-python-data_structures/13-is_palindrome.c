#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int i = 0, j;
	int *nums;

	nums = malloc(sizeof(int));
	tmp = *head;
	while (tmp)
	{
		i++;
		nums = realloc(nums, (sizeof(int) * i));
		nums[i - 1] = tmp->n;

		tmp = tmp->next;
	}

	for (j = 0; j < (i / 2); j++)
	{
		if (nums[j] != nums[i - j - 1])
		{
			return (0);
			free(nums);
		}
	}
	free(nums);
	return (1);
}
