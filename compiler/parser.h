#include  "lex.h"

static int layoutChar(char c) {
    switch (ch) {
        case ' ': case '\n': case '\t': return 1;
        default:                        return 0;
    }
}

