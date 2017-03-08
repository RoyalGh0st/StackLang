/* First thing is to define constants. */
/* The numbers must be above 255, so they don't collide with any ASCII characters. */

#define  EOF          256
/* EOS = End Of Statement, or a semicolon. */
#define  EOS          257
/* The OP prefix means Operator, and this is the Equals operator. */
#define  OP_EQUALS    258
#define  OP_ADD       259
#define  OP_SUBTRACT  260
/* MULT = multiply */
#define  OP_MULT      261
#define  OP_DIV       262
