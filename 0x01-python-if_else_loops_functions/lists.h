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
size_t print_listint(const listint_s *h);
listint_s *add_nodeint_end(listint_s **head, const int n);
listint_s *insert_node(listint_s **head, int number);

#endif /* LISTS_H */
