# Password-Generator
A password generator written in python that uses the secret module to generate a secure password

Before you ask: 
yes this code uses the secret module.
yes I read the documentation.
no I won't give you any context on that joke go read the documentation.

This program uses the python programming language to generate a secure password based on how many characters you want.

The disallowedSymbols list on line 8 is there for you to add any symbols that may not be allowed by the website that you are generating a password for.

Below the if statement are the variable to add however many of a specific character you want.

The program first selects characters from the appropriate list based on how many you want. It selects from the different character lists using the secret module and then adds that to a holding list called container.

Then after it is done adding to the container list it uses the secret module again to take the characters from the container list and add them to the password list and then prints the password list a.k.a. the password.

To use the program simply change the values of variables 
