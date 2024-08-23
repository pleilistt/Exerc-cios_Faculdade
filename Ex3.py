wordlist = input("Insira o nome da wordlist: ")

def runwordlist(wordlist):

    f = open(wordlist+".txt", "r")
    controle = 0
    for i in f:
        print(i.strip())
        controle +=1
        if controle == 10:
            break

runwordlist(wordlist)