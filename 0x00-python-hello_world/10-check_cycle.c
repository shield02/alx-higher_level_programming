#include "lists.h"

/**
 * check_cycle - checks for cycle in a singly linked list
 * @list: listint_t var
 *
 * Description: This function checks if a singly linked list
 * has a cycle in it
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	int counter = 0, k = 0, l = 0, i = 0;
	listint_t *checklist = NULL, *temp = NULL;

	if (list == NULL)
		return (0);

	checklist = list;
	for (k = 0; checklist->next != NULL; k++)
	{
		checklist = checklist->next;
		if (k > 100)
			return (1);
	}
	counter = checklist->n;
	temp = list;

	do {
		if (counter == temp->n)
			l++;
		if (l == 2)
			return (1);
		if (i > 100)
			return (0);
		temp = temp->next;
		i++;
	} while (temp);
	return (0);
}
