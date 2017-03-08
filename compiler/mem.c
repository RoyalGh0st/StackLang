#include <stdlib.h>
#include <stdargs.h>
#include <stdbool.h>

struct Stack {
	long *data;
	int currentSize;
	int maxSize;
	int (*push)(Stack*, int);
	int (*pop)(Stack*);
};

int push(Stack* self, int val) {
	if (self->currentSize = self->maxSize - 1) 
		return 0;
	
	self->data[self->currentSize] = val;
	self->currentSize++;
}

int pop(Stack* self) {
