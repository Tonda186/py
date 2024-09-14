import re

def tokenize(výraz):
    if ' ' in výraz:
        return SyntaxError
    # používáme, abychom zůstali u stejné tokenizace
    členy = re.findall(r'\d+|[a-zA-Z_][a-zA-Z_0-9]*|[+*/^()-]', výraz)
    return členy

# převedeme z výraz z infixu do postfixu
def infix_to_postfix(členy):
    # vyrobíme si slovník, který nám říká, ktzerá operace má přednost (čím větší číslo, tím má větší přednost)
    přednost = {'+': 1, '-': 1, '*': 2, '/': 2, '^':3}
    # sem zapisujeme výsledný výraz v postfixu 
    výsledek = []
    # sem dáváme všechna znaménka a funkce, dokud na ně nepřijde správná řada 
    znaménka = []
    # označené funkce s předností
    funkce = {'sin': 4, 'ln': 4, 'cos':4, 'exp':4, 'tan':4, 'cotg':4, 'log':4} 
    

    def před(op):
        return přednost.get(op, funkce.get(op, 0))
    # funkce, která nám pouze vrací příslušnou funkci ve slovníku 
    def fun(prvek):
        return prvek in funkce
    # funkce, která nám vrací příslušné znaménko ve slovníku
    def znam(prvek):
        return prvek in přednost
    
    if isinstance(členy,type):
        return SyntaxError
    # procházíme člen po členu ve výrazu
    for člen in členy:

        # pokud je člen číslo, nic neděláme a pouze ho dáme do výsledku 
        if člen.isdigit():
            výsledek.append(float(člen))

        # pokud je člen funkce, tak jí dáme pouze za číslo v zásobníku
        elif fun(člen):
            znaménka.append(člen)

        # pokud je člen znaménko, tak se koukneme, zda je zásobník se znaménky není prázdný, poslední člen není první závorka
        # a zda náš člen má menší přednost než poslední člen v zásobníku
        # pokud vše platí, odebereme ze zásobníku poslední člen a dáme ho do našeho výsledku
        # pokud ne, dáme náš člen nakonec výsledku 
        elif znam(člen):
            while (znaménka and znaménka[-1] != '(' and před(člen) <= před(znaménka[-1])):
                výsledek.append(znaménka.pop())
            znaménka.append(člen)

        # pokud je člen první závorka, pouze ji přidáme mezi znaménka
        elif člen == '(':
            znaménka.append(člen)

        # pokud je člen druhá závorka, vezmeme všechny znaménka, co jsou v zásobníku mezi druhou a první závorkou a dáme je do výsledku
        # nakonec přidáme i druhou závorku do zásobníku
        elif člen == ')':
            while znaménka and znaménka[-1] != '(':
                výsledek.append(znaménka.pop())
            if znaménka and znaménka[-1] =='(':
                znaménka.pop()
            else:
                return SyntaxError 
            
    # pokud zásobník znamének ještě není prázdný, dáme postupně všechny znaménka ze zásobníku nakonec našeho výsledku
    while znaménka:
        výsledek.append(znaménka.pop())

    #vracíme výsledek
    
    return výsledek




import math

# FUNKCE

def faktorial(n):
    # pomocí rekurze 
    # známe první stav (n=0) a od něho vypočítáme postupně ostatní
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)
  
def sin_n(x, n_terms=10):
        # x je reálné číslo
        # terms je počet desetinných míst, tedy jak moc chceme výpočet aproximovat

        # stupně si převedeme na radiány v základním tvaru
        y=math.radians(x%360)

        #pomocí Taylora vypočítáme sinus pro libovolné x
        sin_x = 0
        for n in range(n_terms):
            znamenko=((-1)**n)
            clen = znamenko * (y**(2*n + 1)) / faktorial(2*n + 1)
            sin_x += clen
        sin=round(sin_x,8)
        return sin

def cos_n(x, terms=10):
        # x je reálné číslo
        # terms je počet desetinných míst, tedy jak moc chceme výpočet aproximovat

        # převedeme stupně na radiány v základním tvaru
        y=math.radians(x%360)

        # Výpočet cosinu pomocí Taylora
        cosine_value = 0
        for n in range(terms):
            znamenko = (-1)**n
            clen = znamenko * (y**(2*n)) / faktorial(2*n)
            cosine_value += clen
        cos=round(cosine_value,8)
        return cos

def tan(x,pocet=10):
        # x je reálné číslo
        # pocet je počet desetinných míst 

        # Výpočet tangentu pomocí sinu a cosinu
        prvni=sin_n(x,pocet)
        druhy=cos_n(x,pocet)
    
        # jmenovatel (cosinus) nesmí být nula
        if druhy !=0:
            tan_hodnota=prvni/druhy
        else:
            return ZeroDivisionError
    
        tan=round(tan_hodnota,8)
        return tan

def cotg(x,pocet=10):
        # x je reálné číslo
        # pocet je počet desetinných míst 

        # Výpočet cotangentu pomocí sinu a cosinu
        prvni=sin_n(x,pocet)
        druhy=cos_n(x,pocet)
    
        # jmenovatel (sinus) nesmí být nula
        if prvni !=0:
            cotg_hodnota=druhy/prvni
        else:
            return ZeroDivisionError
    
        cotg=round(cotg_hodnota,8)
        return cotg 

def exp(x,pocet=100):
    # x je reálné číslo
    #pocet je počet desetinných míst

    # Výpočet pomocí Taylora
    exp_hodnota = 0
    for n in range(pocet):
        clen = (x**n) / faktorial(n)
        exp_hodnota += clen
    exp=round(exp_hodnota,8)
    return exp

def exp_n(x, n=100):
    # x je reálné číslo
    # pocet je počet desetinných míst
    # výpočet e pro větší x

    # Rozdělení výpočtu na menší části
    exp_mensi = exp(x/n)
    
    # Výpočet e^x jako (e^(x/n))^n
    vysledek = 1.0
    for _ in range(n):
        vysledek *= exp_mensi
    
    return vysledek


def log_c(x, pocet=10000):
    # x musí být větší než 0, definice logaritmu
    if x <= 0:
        raise ValueError
    
    # Převod na formát ln(1 + y)
    y = (x - 1) / (x + 1)
    y2 = y * y

    # Taylorova řada pro ln(1 + y)
    výsledek = 0
    for n in range(1, pocet + 1, 2):
        výsledek += (y / n)
        y *= y2

    return 2 * výsledek


def log_n(x):
    # x musí být větší než 0
    if x <= 0:
        raise ValueError
    
    # Zjistíme, jaký je exponent v binárním vyjádření x
    # To nám umožní zjistit, kolikrát můžeme číslo rozdělit na mocniny dvou
    exponent = int(log_c(x)/log_c(2))
    
    # Nyní přepočítáme x na menší hodnotu tím, že ho vydělíme 2^exponent
    mensi_hodnota = x / (2 ** exponent)
    
    # Vypočítáme přirozený logaritmus mantissy
    log_mensi = log_c(mensi_hodnota)
    
    # Výsledný logaritmus je tedy:
    # ln(x) = ln(2^exponent * mensi_hodnota) = exponent * ln(2) + log_mensi
    return exponent * log_c(2) + log_mensi

def log(x,základ):
    if základ <=0 or základ ==1:
        return ValueError
    elif x<=0:
        return ValueError
    čitatel=log_n(x)
    jmenovatel=log_n(základ)
    if jmenovatel !=0:
        return round(čitatel/jmenovatel,8)
    else:
        return ZeroDivisionError
         




def postfix(postfix_členy):
    # zásobník slouží k ukládání hodnot 
    zásobník = []
    # slovník, který ke každé funkci přiřadí námi vytvořenou funkci
    funkce = {'ln': log_n, 'sin': sin_n, 'cos':cos_n, 'tan':tan, 'cotg':cotg,'exp':exp_n, 'log':log}
    
    # procházíme výraz v postfixu a koukáme, zda je to číslo, znaménko nebo funkce
    if isinstance(postfix_členy,type):
        return SyntaxError
    
    for člen in postfix_členy:

        # jestli to je číslo, dáme ho do zásobníku
        if isinstance(člen, (int, float)):
            zásobník.append(člen)

        # jestli to je funkce, tak vyndáme ze zásobníku předešlé číslo a s ním uděláme příslušnou operaci a výslednou hodnotu uložíme do zásobníku
        elif člen in funkce:
            logar='log'
            if  člen ==logar:
                if len(zásobník)<=1:
                    return SyntaxError
                else:
                    x=zásobník.pop()
                    y=zásobník.pop()
                    zásobník.append(log(y,x))
                
            else:
                x = zásobník.pop()
                zásobník.append(funkce[člen](x))

        # jestli je člen znaménko, vybereme ze zásobníku 2 poslední čísla, použijeme na ně to znaménko a výsledek vrátíme do zásobníku 
        else: 
            if len(zásobník)==0:
                return SyntaxError
            b = zásobník.pop()
            if len(zásobník) ==0:
                return SyntaxError 
            a = zásobník.pop()
            if člen == '+':
                zásobník.append(a + b)
            elif člen == '-':
                zásobník.append(a - b)
            elif člen == '*':
                zásobník.append(a * b)
            elif člen == '/':
                zásobník.append(a / b)
            elif člen == '^':
                zásobník.append(a**b)
    if len(zásobník)>1:
        print(zásobník[1])
        return SyntaxError
    # ze zásobníku nakonec vybereme poslední číslo (výsledek)
    return zásobník[0]


# výsledná funkce 
def vyhodnocení(výraz):
    # zůstáváme u stejné tokenizace
    členy=tokenize(výraz)  
    # převod z infixu na postfix
    postfix_tokens = infix_to_postfix(členy)
    # vypočtení výsledku
    return postfix(postfix_tokens)



def správnost(výraz):
    # Definice povolených tokenů (čísla, operátory, závorky, matematické funkce)
    povolené_tokeny = re.compile(r'\d+\.?\d*|[+\-*/^()]|sin|cos|ln|tan|cotg|log|exp')

    # Rozdělení řetězce na tokeny
    tokeny = re.findall(r'\d+\.?\d*|[+\-*/^()]|sin|cos|ln|tan|cotg|log|exp|\S', výraz)

    i = 0
    while i < len(tokeny):
        token = tokeny[i]
        
        # Kontrola platnosti tokenu
        if not povolené_tokeny.fullmatch(token):
            problem(výraz, token)
            return None
        
        # Kontrola speciálního případu pro 'log'
        if token == 'log':
            # Zkontrolujte, zda následuje číslo
            if i + 2 < len(tokeny) and re.match(r'\d+\.?\d*', tokeny[i + 2]):
                # Zkontrolujte, zda následuje čárka
                if i + 3 < len(tokeny) and tokeny[i + 3] == ',':
                    i += 4  # přeskočit tři tokeny
                    continue
                else:
                    problem(výraz, 'log')
                    return None
            else:
                problem(výraz, 'log')
                return None
        
        i += 1

    print("Žádný chybný token nenalezen")
    return True

def problem(výraz, špatný_prvek):
    # Vytvoření barevného zvýraznění (červeně)
    upravený_výraz = výraz.replace(špatný_prvek, f'\033[91m{špatný_prvek}\033[0m')
    print("Chybný výraz:")
    print(upravený_výraz)


# Testování funkce
výraz = "3+5++sin(2)"
if správnost(výraz) is not None:
    výsledek = vyhodnocení(výraz)
    print(f"Výsledek výrazu '{výraz}' je: {výsledek}")

