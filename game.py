import time

parola = "Forklein"
secret = ""
conteggio = 1
limite = 3

while secret != parola:
    secret = input('Inserisci la parola segreta: ')
    if secret == parola:
        print('Hai vinto!')
        time.sleep(5)
        break
    elif conteggio == limite:
        print('Mi dispiace, hai perso!')
        time.sleep(5)
        break
    elif conteggio == 2:
         print('Hai ancora un tentativo!')
         conteggio += 1
         continue
    else:
        print('Riprova, hai ancora 2 tentativi!')
        conteggio += 1
        continue
