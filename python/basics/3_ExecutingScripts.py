"""we want to write a "serious" program now, i.e. a program which resides in a file. This way, 
we can use a program over and over again without having to type it in again. Some may like to call such a little program "script".
We will use a slight variation of the "Hello World" theme. We have to include our print function into a file.
To save and edit our program in a file we need an editor. There are lots of editors, but you should choose one,
which supports syntax highlighting and indentation.
For Linux you can use vi, vim, emacs, geany, gedit and umpteen others.
The Emacs works for Windows as well, but Notepad++ may be the better choice in many cases.
Of course, you can also use an IDE (Integrated Development Environment) like PyCharm or Spyder for this purpose.

So, after you have found the editor or the IDE of your choice, you are ready to develop your mini program, i.e."""

print("My first Python Script")

"""Start a Python program
Let's assume our script is in a subdirectory under the home directory of the user tonystark:

tonystark@tony:~$ cd projects/study_material/python/basics/
tonystark@tony:~/projects/study_material/python/basics$ python3 3_ExecutingScripts.py
My first Python Script
tonystark@tony:~/projects/study_material/python/basics$

    """

"""Python is a interpreted programming or Scripting Language but the truth is it is the both but calling python a compiled language will be misleading"""

"""Python code is translated into intermidiate code, which has to executed in a virtual environment known as the PVM, python virtual machine.
   This is a similar approach to the one taken by JAVA. There is even a way of translating python programs into Java byte code for the JVM(Java Virtual Machine)
   This can be achieved by jython  """

"""Do I have to complie my python script in order to make them fast or more optimized?
   The answer is no because the python is already doing the thinking work for you and you should'nt bother unless you know what you're doing otherwise "python" is already taking all the neccesary steps for you """

"""for whatever reason you need to complie the program manually it's not a problem we can achieve this by module py_compile, either using the interpeter shell"""

"""use the below method """
import py_compile

py_compile.compile('3_ExecutingScripts.py')

"""I'm unable to find out at the movement wy the above method is not working for me right nwo when I'm trying to finish it in VS code"""

"""I've used an alternative method to do so which is by using the following command at the shell prompt:
   python -m py_compile 3_ExecutingScripts.py"""

"""Either way you do it you're going to notice two things:
   First, there will bw new sub-directory  '__pycache__' if it does'nt already exist.
   You will find a file '3_ExecutingScripts.cpython-312.pyc' in this sub-directory and this is the compiled version of our file in byte code."""

"""You can also automatically compile all Python files using the compileall module. You can do it from the shell prompt by
   running compileall.py and providing the path of the directory containing the Python files to compile:"""

"""But as we have said, you don't have to and shouldn't bother about compiling Python code. The compilation is hidden from the user for a good reason.
Some newbies wonder sometimes where these ominous files with the .pyc suffix might come from. If Python has write-access for the directory where the Python program resides,
it will store the compiled byte code in a file that ends with a .pyc suffix. If Python has no write access, the program will work anyway.
The byte code will be produced but discarded when the program exits. Whenever a Python program is called,
Python will check, if a compiled version with the .pyc suffix exists.
This file has to be newer than the file with the .py suffix. If such a file exists, Python will load the byte code, which will speed up the start up time of the script.
If there is no byte code version, Python will create the byte code before it starts the execution of the program."""

"""Execution of a Python program means execution of the byte code on the Python."""

""" SOURCE CODE-------->BYTE CODE--------->VIRTUAL MACHINE(PVM/JVM)"""

"""DIFFRENCES BW COMPILER AND INTERPETER

COMPILER:Definition- A compiler is a computer program that transforms(translates) source code of a programming language(the source language) into another computer language(The target language).
In most cases compilers are used to transform source code into executable programs i.e. they translate code from a High-Level programming language to a Lower-Level
programmig languages,mostly Assembly Language or machine code.

INTERPRETER:Definition- An interpreter is a computer program that executes programs written in a programming language.
It can either execute the source code directly or translate the source code in a first step into a more efficient representation and execute this code.
"""

