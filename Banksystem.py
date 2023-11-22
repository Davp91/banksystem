
saldo = 500
rentesats = 0.01

logg = [saldo,]


def velg():
    print('1 - vis saldo')
    print('2 - innskudd')
    print('3 - uttak')
    print('4 - Renteoppgjør')
    print('5 - Siste endringer')
    print('6 - Avslutt')
    handling = int(input('Velg handling: '))

    if handling == 1:
        bankkonto()
    elif handling == 2:
        innskudd()
    elif handling == 3:
        uttak()
    elif handling == 4:
        renteoppgjør()
    elif handling == 5:
        sisteEndringer()
    elif handling == 6:
        avslutt()
    else:
        print('Beklager, feil handling, prøv igjen')
        velg()


def innskudd():
    global saldo
    innskudd=int(input(' Skriv inn innskuddsbeløp:'))
    saldo+=innskudd
    print(' Din nye saldo er:',round(saldo,2))
    logg.append(saldo)
    velg()


def uttak():
    global saldo
    uttak=int(input('Skriv inn uttaksbeløp:'))
    if(uttak>saldo):
        print('Ingen dekning, du kan max ta ut',round(saldo,2))
        velg()

    else:
        saldo-=int(uttak)
        print('Din nye saldo er:',round(saldo,2))
        logg.append(saldo)
        velg()

def beregnRente():
    global saldo
    if(saldo>1000000):
        print('Du har bonusrente:',saldo*0.02)
    else:
        print('Din renteverdi er på:',saldo*0.01)

def renteoppgjør():
    global saldo
    if(saldo>1000000):
        saldo+=saldo*0.02
        print('Gratulerer du har bonusrente',round(saldo,2))
        logg.append(saldo)
        velg()
    else:
        saldo+=saldo*0.01
        print('Du har normal rente',round(saldo,2))
        logg.append(saldo)
        velg()

def sisteEndringer():
    print('Dine 3 siste saldo endringer:')
    print(logg[-3:])
    velg()


def bankkonto():
    print('Din saldo er:',round(saldo,2))
    velg()

def avslutt():
    print('Banktjenesteprogrammet er nå avsluttet')

velg()
