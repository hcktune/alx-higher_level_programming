#ifndef __LISTS_H
#define __LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
}
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
