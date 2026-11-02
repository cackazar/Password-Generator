import secrets

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['.', ':', ';', "'", '"', '-', '_', '=', '+', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', '<', '>', '[', ']', ',']

disallowedSymbols = []

if len(disallowedSymbols) > 0:
    for i in range(len(disallowedSymbols)):
        if disallowedSymbols[i] in symbols:
            symbols.remove(disallowedSymbols[i])

totalNum = 5
totalLowercase = 5
totalUppercase = 5
totalSymbols = 5

emptyContainer = []
password = []

def addCharacters(characterList, amount, listToAddTo):
    for i in range(amount):
        listToAddTo.append(secrets.choice(characterList))

addCharacters(numbers, totalNum, emptyContainer)

addCharacters(lowercase, totalLowercase, emptyContainer)

addCharacters(uppercase, totalUppercase, emptyContainer)

addCharacters(symbols, totalSymbols, emptyContainer)

while emptyContainer:
    item = secrets.choice(emptyContainer)
    emptyContainer.remove(item)
    password.append(item)

print(*password, sep = "")
