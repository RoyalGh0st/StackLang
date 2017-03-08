#define  EOF               256
#define  NUMBER            257
/* Equals is the assignment operator. */
#define  EQUALS            258
/* Stack Prefix is the prefix that is used to show the type of stack being operated on. */
/* It is either "S" for String, "N" for Number, or "I" for instruction. */
#define  STACK_PREFIX      259
#define  OPERATOR          260
/* Stack selector is what comes after the Stack selector. */
/* It selects from the stack which slot you wish to operate on. */
/* So "S1" would be choosing the string stack with id 1. */
#define  STACK_SELECTOR    261
/* Slot selector is what selects the slot from the desired stack. */
#define  SLOT_SELECTOR     262

typedef struct { int class; char* rep } Token_type;

extern Token_type Token;
extern void getNextToken(void);
