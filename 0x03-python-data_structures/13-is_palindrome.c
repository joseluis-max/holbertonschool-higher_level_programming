#include <lists.h>
/**
 * listint_len - function that returns the number of elements
 * in a linked listint_t list.
 * @h: take a list type of listint_t
 * Return: number of elements of @h list
 **/
size_t listint_len(const listint_t *h)
{
	size_t s = 0;

	if (h == NULL)
		return (0);
	while (h)
	{
		s++;
		h = h->next;
	}

	return (s);
}
/**
 * is_palindrome - check if a single list is a palindrome
 * @head: head single linked list
 * Return: 0 false, 1 true
 */
int is_palindrome(listint_t **head)
{
	int buffer[1024];
	int i;
	size_t len;
	listint_t current = *head;

	len = listint_len(current);
	if (len == 0)
		return (1);
	while (current != NULL)
	{
		buffer[i] = current->n;
		current = current->next;
		i++;
	}
	for (i = 0; i < len; i++)
	{
		if (list[i] != list[len - i - 1])
			return (0);
	}
	return (1);
}
