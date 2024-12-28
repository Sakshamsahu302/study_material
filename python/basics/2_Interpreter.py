'''THE INTERPRETER, AN INTERACTIVE SHELL'''

'''The term interactive trces back from latin expression 'inter agere' the verb 'agere' means 'to act or to do something' while the word 'inter' means 'betweeen or 
amongst' objects,person and events. So the term 'inter agere' means to 'to act b/w something' '''

'''The interactive shell is bw user and the OS. Instead of OS the interpreter can be used for a programming language like Python as well.'''

'''The interactive shell is also interactive as it stands bw the commands or actions and their execution'''

'''Shell waits for commmands from user, excutes them and returns the results to the user.afterwards it waits for next command or input from the user'''

'''Shell acts as a protective layer bw the kernel of the OS and the user'''

'''It's a "protection" in both directions. The user doesn't have to use the complicated basic functions of the OS but is capable of using the
 interactive shell which is relatively simple and easy to understand.'''

'''Python offers a comfortable command line ineterface with python shell which is also known as 'Python Interactive Shell'. '''

'''The Python interpreter can be invoked by typing the command "python" without any parameter followed by the "return" key at the shell prompt:
tonystark@tony:~$ python3
Python 3.12.3 (main, Nov  6 2024, 18:32:19) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.'''

'''Once the Python interpreter is started, you can issue any command at the command prompt ">>>". Let's see, what happens, if we type in the word "hello":

hello
OUTPUT:
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-f572d396fae9> in <module>
----> 1hello
NameError: name 'hello' is not defined


Of course, "hello" is not a proper Python command, so the interactive shell returns ("raises") an error.

'''

'''THE FIRST REAL COMMAND WHICH WE'LL USE IS THE PRINT COMMAND, AND PRINT THE MANDATORY CODE OF ANY PROGRAMMING LANGUAGE WHICH IS 'HELLO WORLD':'''

print("Hello World")

"""    OUTPUT:
    Hello World

'After that whatever we enter as a input will be printed even without having to use the print statement again:'

    Example:
    3
    Output:
    3 """
    

''' How to Quit the Python Shell
So, we have just started, and we are already talking about quitting the shell. We do this, because we know, how annoying it can be,
if you don't know how to properly quit a program.
'''
'''It's easy to end the interactive session: You can either use exit() or Ctrl-D'''


"""REAL-TIME RESULTS WHICH I WAS PRACTICISING ALONG ON MY UBUNTU CLI:

tonystark@tony:~/projects/study_material/python$ cd
tonystark@tony:~$ python
Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
tonystark@tony:~$ python3
Python 3.12.3 (main, Nov  6 2024, 18:32:19) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined. Did you mean: 'help'?
>>> print(Hello,World)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Hello' is not defined
>>> print("Hello World")
Hello World
>>> 3
3
>>> exit()
tonystark@tony:~$

"""