# Password-Generator
A password generator written in python that uses the secret module to generate a secure password

Before you ask: 
yes this code uses the secret module.
yes I read the documentation.
no I won't give you any context on that joke go read the documentation.

**EXPLANATION**
This program uses the python programming language to generate a secure password based on how many characters you want.

The disallowedSymbols list on line 8 is there for you to add any symbols that may not be allowed by the website that you are generating a password for.

Below the if statement are the variable to add however many of a specific character you want.

The program first selects characters from the appropriate list based on how many you want. It selects from the different character lists using the secret module and then adds that to a holding list called container.

Then after it is done adding to the container list it uses the secret module again to take the characters from the container list and add them to the password list and then prints the password list a.k.a. the password.

**USE**
To use the program simply change the values of variables totalNum, totalLowercase, totalUppercase, and totalSymbols to whatever you want and run the program to see the password output to the terminal.

To remove symbols not allowed by the website then add those symbols to the disallowedSymbols list on line 8 like so:
In this example say that these symbols are not allowed: ;, [, ]
the disallowedSymbols list should look something like this: disallowedSymbols = [";", "[", "]"]

Make sure each character is surrounded by a double quote and seperated by a comma, the comma goes outside the double quotes.

**DISCLAIMER**
This program was written as a personal project to see if I could do it and was not made with ai(this is just normal human slop).
It is free for anyone to use or copy I don't care, you don't even have to credit me, I imagine there are many other programs like it out there.
