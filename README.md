# py
# mathematical expression
1.**Potřebné programy**
  - k používání kodu stačí mít nainstalovaný Python, jiný program nepotřebujeme 
  - Python můžeme nainstalovat na tomto [linku](https://www.python.org/downloads/)

2.**Návod k používání**
  - na konci kodu je promenná **výraz**
  - do něho stačí zadat náš matematický výraz a kod ho vyhodnotí
  - výraz bychom měli psát bez mezer, se správnými tokeny, jinak kod nám výraz vyhodnotí jako chybu
  - v našem výrazu můžeme používat základní funkce, logarimtus, exponencielu, sinus, cosinus, tangens a cotangens

3.**Jak program funguje**
  - na začátku kod převede kod převede náš výraz, který je v infixovém zápisu, do postfixového
  - dále jsme si pomocí Taylorových řad a vhodných vztahů zadefinovali naše funkce, které můžeme používat ve výrazu
  - následně, když máme výraz převedený do postfixu, nám náš kod vyhodnotí výraz a napíše výsledek
  - pokud ovšem během zpracovávání někde kod nalezne v řetězci chybu, do terminálu nám vypíše **SyntaxError**
  - pokud v kodu jsou nějaké chybné tokeny, kod následně napíše do terminálu náš výchozí výraz, avšak chybný kod vybarví červeně



