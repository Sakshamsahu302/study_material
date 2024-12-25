"""
BLOCK:
A block is a group of statements in a program or script.Usually it contains atleast one statement and declrations for the block
depending on the programming or the scripting language. A language which allows grouping of blocks is known as block structured language."""

"""Normally block can contain more blocks as well,so we get a nested block structure.A block in a script or programming language
is a group of statements whic functions as if they were just one statement.In many cases,it also servers as a way to limit the lexical scope
of variables and functions."""

"""Initially in simple languages like Basic and Fortran there was no way of explicitly using block structures.
Programmers had to rely on "go to" structures,because 'go to programs' can easily turn into spegati codes i.e. tangled and instructable control structures. """

"""Block Structures were first formalized in ALGOL(programming lang) as a compound statement
Programming languages such as ALGOL,pascal and others use certain methods to group statements into blocks:

1. Methods for Grouping Blocks in Programming Languages
Different languages use different ways to define these blocks.

a. begin ... end (Pascal)

Pascal (and some other older languages) use begin and end to mark the start and end of a block of code.

Example:
    with ptoNode^ do
        begin
            x := 42;
            y := 'X';
        end;

begin: Marks the start of a block.
end: Marks the end of the block.
"""

"""
b. do ... done or if ... fi (Shell Scripts)

Shell scripting languages like Bash use keywords like do ... done or if ... fi to group blocks.

Example:
bash-
if [ $x -eq 42 ]
then
    echo "Answer to the Ultimate Question!"
fi

if ... then ... fi: Indicates the start and end of a conditional block"""

"""
c. Braces { ... } (C, Java, etc.)

Most modern programming languages (like C, C++, Java) use curly braces to group code blocks.

Example:

c(language)-

if (x == 42) {
    printf("The Answer to the Ultimate Question of Life, the Universe, and Everything\n");
} else {
    printf("Just a number!\n");
}

Code inside '{' and '}' belongs to the same block.

Without Proper Indentation: You can write the entire block on one line, but this makes the code less readable:
c
if (x == 42) { printf("Answer!\n"); } else { printf("Not Answer!\n"); }
"""

""" INDENTING CODE:
    
        --BLOCK1--
            --BLOCK2--
                --BLOCK3--
            --BLOCK2,continuation--
        --BLOCK1,continuation--

(Totally depends on which line we started from for example if we add more space to the block2 continuation it'll 
eventually become part of block3)        

Python uses a diffrent principal.Python programs gets structured through intentation i.e. code blocks are defined by
their intentation.Okay that's what we expect from any program code, isn't it? Yes, but in the case of Python it's a language requirement,
not a matter of style. This principle makes it easier to read and understand other people's Python code.

All statements with the same distance to the right belongs to the same block of the code i.e. the statements within a block line up vertically.
The block ends at a line less indented or at the end of the file.
If a block has to be more deeply nested it is simply indented further to the right.

Example:

from math import sqrt
n = input("Maximum Number? ")
n = int(n)+1
for a in range(1,n):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2) == 0):
            print(a, b, c)

OUTPUT:
3 4 5
5 12 13
6 8 10
8 15 17
9 12 15
12 16 20
15 20 25

Loops and Conditional statements end with a colon ":" - the same is true for functions and other structures introducing blocks.
All in all, Python structures by colons and indentation.

"""

