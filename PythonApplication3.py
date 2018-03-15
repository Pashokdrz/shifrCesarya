key=input('Чтобы программа заработала введите 1: ')
key=int(key)
t=(' ')
while key==1:
    print('1.Зашифровать слово(предложение)')
    print('2.Расшифровать слово(предложение)')
    print('3.Выход')
    z=input()
    z=int(z)
    ABC='abcdefghijklmnopqrstuvwxyzABCDEFGHIMNOPQRSTUVWXYZ.,?!;:-_abcdefghijklmnopqrstuvwxyzABCDEFGHIMNOPQRSTUVWXYZ.,?!;:-_'
    if z==3:
        key=0
    if z==1:
        b=input("Введите слово(предложение): ")
        n=len(b)
        e=('')
        x=input("Введите смещение символов шифрования: ")
        x=int(x)
        while x > 61:
            x=x-62
        y=0
        while n > 0:
            a=b[y]
            c=b[y]
            if c==t:
                c=b[y+1]
                e=(e+' ')
            else:
                w=ABC.find(a)
                a=ABC[w+x]
                e=(e+a)
            n=n-1
            y=y+1
        print(e)
        key=input("Если хотите продолжить работу введите 1: ")
        key=int(key)
    elif z==2:
        print(e)
        key2=0
        x=0
        while key2==0:
            r=('')
            n=len(b)
            y=0
            while n > 0:
                a=e[y]
                c=e[y]
                if c==t:
                    c=b[y+1]
                    r=(r+' ')
                else:
                    w=ABC.find(a)
                    a=ABC[w-x]
                    r=(r+a)
                n=n-1
                y=y+1
            print(x, r)
            x=x+1
            if x==62:
                key2=1
            
        key=input("Если хотите продолжить работу введите 1: ")
        key=int(key)
