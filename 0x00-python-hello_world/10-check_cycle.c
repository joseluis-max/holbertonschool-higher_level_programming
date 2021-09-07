#include "lists.h"
/**
 * check_cycle - check if there is a cycle
 * @list: single linked list
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *copy = list;
	int status = 0;

	while (list != NULL)
	{
		copy = copy->next;
		if (copy->next != NULL)
			copy = copy->next;
		else
			break;
		if (copy == list)
		{
			status = 1;
			break;
		}
		list = list->next;
	}
	return (status);
}
