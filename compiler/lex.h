/* Define constants */
/* End of a file must be "END" */
#define  EOF             256
/* Digit is a number 0-9 */
#define  DIGIT           257
/* Operator is +, -, *, or /. */
#define  OPERATOR        259
/* End statement is, obviously, a semicolon. */
#define  END_STATEMENT   260
/* Begin of a file must be "BEGIN" */
#define  BEGIN           261
/* The stack prefixes are used to specify what type of stack you are operating on. */
/* For example, S1[0] is the first element of String Stack 1. */
/* And N1[0] is the first element of Number Stack 1. */
#define  STACKPREFIX_S   262
#define  STACKPREFIX_N   263
#define  STACKPREFIX_I   264
/* Stack Locator is which element of the stack you are operating on. */
#define  S_LOCATOR       266

typedef struct { int class; char *rep } Token_type;

extern Token_type Token;
extern void getNextToken(void);
