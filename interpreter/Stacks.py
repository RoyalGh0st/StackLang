# This file is just a data file.
# It contains the stacks
# And a little bit of information about them.

VarStacks = [[[None] for x in range(AmtVarStacks)] for y in range(VarStackSize)]

# Is initialized to 50 by default, can be expanded
InstructStack = [[None] for x in range(InstructStackSize)]

InstructStackSize = 50

AmtVarStacks = 5
VarStackSize = 50
