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
	{
		free(node);
		return (NULL);
	}
	node->n = number;
	node->next = NULL;
	while (copy != NULL)
	{
		if (copy->next == NULL)
		{
			copy->next = node;
			break;
		}
		if (copy->n > number)
		{
			node->next = copy;
			*head = node;
			break;
		}
		if (copy->next->n >= number)
		{
			node->next = copy->next;
			copy->next = node;
			break;
		}
		copy = copy->next;
	}
	if (copy == NULL)
	{
		copy = node;
	}
	return (node);
}
