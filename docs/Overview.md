## Overview

StackLang is a language based off of manipulating stacks. EVERYTHING is a stack. To affect memory stacks, you set an instruction stack slot to have your desired instruction. A pointer moves up the instruction stack, and 
its direction can be changed by an instruction on the instruction stack. In this sense, StackLang is a procedural language, in
that instructions are done in the order that they appear to the pointer. I like to call it a fluid-procedural language, because the
order of instructions is based off of a pointer moving on a stack, and the pointer's direction can be moved or changed. There are 
no explicit loops as of right now, because you can change/move the pointer.

Similarly, because of the <code>set</code> command, the language contains self-modifying code, and in fact, this is one of its main
features. Now I know, there are those of you who say: "Oh, that's bad", and to some extent, I agree with you. It ususally is bad,
because it can be managed incorrectly. But one of my main goals is to create a language in which this is an asset, not a liability.

This is a **WORK IN PROGRESS.** Most of the features in the documentation are not yet included, but they will be.
