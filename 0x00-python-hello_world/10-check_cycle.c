#include "lists.h"
/**
 * check_cycle - check if there is a cycle
 * @list: single linked list
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *copy = list;

	while (list != NULL)
	{
		copy = copy->next;
		if (copy->next != NULL)
			copy = copy->next;
		else
			break;
		if (copy == list)
			return (1);
		list = list->next;
	}
	return (0);
}
