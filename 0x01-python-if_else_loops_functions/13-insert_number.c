#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - insert node in single linked list
 * @head: single linked list
 * @number: number to insert
 * Return: address memory of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *copy = *head;
	listint_t *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;
	while (copy != NULL)
	{
		if (copy->n <= number && copy->next->n >= number)
		{
			node->next = copy->next;
			copy->next = node;
			break;
		}
		copy = copy->next;
	}
	return (node);
}