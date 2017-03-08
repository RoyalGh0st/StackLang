/* Defining constants for the lexer.
   Cannot use identification numbers between 0 and 255,
   as they are ASCII numbers.
*/
/* EOF = End Of File, in this case, #E. */
#define  END             256
/* BOF = Beginning Of File, in this case, #B. */
#define  BEGIN           257
/* Stack prefix, in this case "$", shows that you are selecting a stack. */
#define  STACK_PREFIX    258
/* Stack select selects the stack. It is encased in braces.*/
#define  STACK_SELECT    259
/* Slot selector. */
#define  SLOT_SELECT     260

#define  OP_EQUALS    261
#define  OP_ADD       262
#define  OP_SUBTRACT  263
#define  OP_MULT      264
#define  OP_DIV       265


typedef struct { int class; const char* repr; } Token_type;

extern Token_type Token;
extern void getNextToken(void);

// tests if character is a layout char or not
static int isLayoutChar(int ch) {
    switch(ch) {
        case ' ': case '\t': case '\n': return 1;
        default:                        return 0;
    }
}

void getNextToken(char* in) {
    int ch;
    
    do {
        ch = getchar(in);
        if (ch < 0) {
            Token.class = EOF; Token.repr = "$E";
            return;
        } while (isLayoutChar(ch));
    }
    
