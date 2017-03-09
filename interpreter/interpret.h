/* 
This file is the file that provides the functions for the interpreter. 
The driver file is in a file called driver.c.
*/

#include "driver.c"

#define  INTEGER    256

#define  EQUALS    257
#define  ADD       258
// I will add these in later, just testing the interpreter for the moment.
//#define  SUBT      259
//#define  MULT      260
//#define  DIV       261

#define  STACK_PREFIX    262
#define  SLOT_SELECT     263

typedef struct { int class; char* repr; } Token;

extern int getLayoutChar(int ch);
extern int getNextToken(char* ch);

int getLayoutChar(int ch) {
	switch(ch) {
		case ' ': case '\n': case '\t': return 1;
		default:						return 0;
	}
}

int getNextToken(char *ch) {
	
