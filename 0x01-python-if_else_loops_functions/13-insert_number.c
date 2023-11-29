#include "lists.h"

/**
 * insert_node - Inserts a number into sing_list
 * @head: the head
 * @number: data
 * Return: the address of the new node, otherwise NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *node = *head;

	if (tmp == NULL || head == NULL)
		return (NULL);

	tmp = malloc(sizeof(listint_t));
	tmp->n = number;

	if (node == NULL || node->n >= number)
	{
		tmp->next = node;
		*head = tmp;
		return (tmp);
	}
	 while (node && node->next && node->next->n < number)
                node = node->next;

        tmp->next = node->next;
        node->next = tmp;

        return (tmp);
}
