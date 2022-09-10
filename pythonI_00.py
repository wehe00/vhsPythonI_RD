
"""Das ist ein Multiline Kommentar. Dieser beginnt mit 3 Anführungszeichen
* Name : ???????????????
* Date created: 20200318
* vhsPythonI_Mod_00.py
* Purpose: Kennenlernen von Variablen, Typen, print-Ausgabe auf dem Bildschirm
*          Einfache arithmetische Operationen:
*          Arithmetische Zuweisungsoperatoren - Assignment Operators
*          Arithmetische Vergleichsoperatoren
*          Print Ausgaben formatiert
*
* Revision:  20100816
* History:
*
*  Date       Author      Ref     Revision
*  20200318   svogel      1       Erste Version
*  20200814   svogel      1       kleine Ergänzungen
Ende des Multiline Kommentar mit 3 Anführungszeichen"""

# Das ist ein Einzeilen Kommentar. Dieser beginnt mit einem Hashtag '#' und geht bis zum Zeilenende


""" **************Block0******************
Wie sind die Übungsaufgaben aufgebaut
* beliebiger Text 
""              # 3tes Anführungszeichen setzen, dann wird Programmblock aktiv

# Programm Code
a = 5   # ab hier jetzt Programmier.......
print(a, a*3, a*6)
print("Heute wird es schoen")

# **************Ende Block0**************** """


""" **************Block1******************
Einfache Assignment und Bildschirmausgaben
* Integer
* Float
* String 
* Gültige Variablennamen ....aber PEP 8 beachten!!
    Großbuchstaben A bis Z
    Kleinbuchstaben a bis z
    Unterstrich _
    Die Zahlen 0 bis 9 (nicht an erster Stelle) 
""              # 3tes Anführungszeichen setzen, dann wird Programmblock aktiv
a = 5   # ab hier jetzt Programmier.......
print('Ich bin ein "Superman"')
print(a, a*3, a*6)
print("hallo", " ,Du")
print("Hi", a)
print("Heute wird es schoen")

# **************Ende Block1**************** """



""" **************Block2******************
Bildschirmausgaben mit print()
Variablen werden mit Komma getrennt
* z.B. print(a, b) 
* Ausgabe von Strings und Stringvariablen
* z.B. my_string = "Hello World"
* print(my_string, "wie geht es dir")

""
my_string = "Hello World"  # ab hier jetzt Programmier.......
print(my_string, "wie geht es dir", "dfdsfds", my_string)



# **************Ende Block2****************"""



""" **************Block3******************
Spezielle Formatierungszeichen (Escapesequenzen) : \n, \t, \', \"
Die Verwendung von Anführungszeichen in einer print Ausgabe
* z.B. print("ich bin ein '1A Student' !") 
* print('ich bin ein "1A Student" !'
"""
# my_str = "\\Hallo\""
# my_str = "Hallo,\t\twie gehts es Dir?"
# print(my_str)
# my_string = "Hello World"  # ab hier jetzt Programmier.......
# print(my_string, "wie geht es dir")

title = "Winnetou"
genre = 7   # Roman
author = "Karl May"
publ = 1940

#print("title\t\t\t\t", "genre\t","author\t\t","publ")
#print(title, "\t\t\t", genre, "\t\t", author, "\t", publ)

title = "Dracula"
genre = 8   # Horror
author = "Bram Stoker"
publ = 1950

# Überschriften, Sep, end
print(f'{"Title":<25}{"Genre":^7}{"Author":<25}{"Publ":>6}')
print(f"{title:<25}{genre:^7}{author:<25}{publ:>6}")


# **************Ende Block3**************** """


""" **************Block4******************
zusätzliche Parameter in der print Funktion: end="", sep="*"
* z.B. print("ich bin ", end="") 
* print('ein "1A Student" !')
""

print("values", "hallo", sep=" ")

my_string = "Ich bin Student an"  # ab hier jetzt Programmier.......
print(my_string, "der VHS Neukoelln", sep=' ')
print(my_string, "der VHS Neukoelln", end='')
print(" und programiere in Python")
print("1","2", sep='+')


# **************Ende Block4**************** """


""" **************Block5******************
formatierte print Ausgabe von Integer
* z.B. a = 3 
* print(f'{a}')
""
print("Spalte1", "      Spalte2")
print("Spalte1000", "   Spalte2")
print("Spalte1000000", "Spalte2")

b = 7
#print(f"V: {b:>25}")
#print(f"V: {b:<25}")
#print(f"V: {b:^25}")
c = 777
d = 9999
e = 1

print(f'{b:10}{c:10}{d:10}{e:10}')
print(f'{d:10}{c:10}{b:10}{e:10}')
print(f'Das ist ein:{b:>10}haloo du')

a = 3
print(f'{a:10}')
print(f'{a:^10}')
print(F'{a:<10}')
my_integer = 1
print(f"Meine Zahl {my_integer:06d}")
print(f"Meine Zahl {my_integer:+6d}")
# **************Ende Block5**************** """

""" **************Block6******************
formatierte print Ausgabe von Float
* z.B. a = 3.3 
* print(f'{a}')
""
my_float = 3.3
print(f"Meine Zahl {my_float:6}")
print(f"Meine Zahl {my_float:+6.2f}")
print(f"The value is {my_float:12.5f}")
# **************Ende Block6**************** """


""" **************Block7******************
formatierte print Ausgabe von String Variablen
* z.B. a = "hallo" 
* print(f'{a}')
""
#print("Spalte1", "      Spalte2")
#print("Spalte1000", "   Spalte2")
#print("Spalte1000000", "Spalte2")

# lfd.No.    Titel        Genre        Autor       publ
# No.    Title        Genre        Author       publ
#001     Dracula      005          Bram Stoker  1894
# :4     :25          :5           :25          :6
no = "001"
title = "Dracula"
genre = "005"
author = "Bram Stoker und Jules"
publ = "1894"

print(f'{no:4}{title:25}{genre:5}{author:25}{publ:6}')

no = "001"
title = "Drfdfdfacula"
genre = "005"
author = "Bram Stoker "
publ = "1897"

#print(f'{"no5":4}{title:25}{genre:5}{author:25}{publ:6}')
print(f'{no:4}{title:25}{genre:5}{author:25}{publ:6}')

# **************Ende Block7**************** """



""" **************Block8******************
alternative Formatierung Techniken
""

print("Hallo\n")
print('world')
print('Hello "my" world')
print("Hello 'your' world")
print("Hello \"your\" world")

hello = 3
print("hello my best numBer: {}".format(hello))
print("Sammy the {0} has a pet {1}!".format("shark", "pilot fish"))

# **************Ende Block8**************** """


""" **************Block9******************
Programmieraufgabe:
Deklariere String Variablen
Tabelle mit 5 Feldern alle rechtsbündig
Feld1: Eine laufende Nummer
Feld2: Buchtitel 25 Felder
Feld3: Eine Zahl mit führender Null, 3 Zeichen
Feld4: Author 25 Felder 
Feld5: Erscheinungsjahr
insgesamt 5 Zeilen  
""

no = "001"
title = "Dracula"
genre = "005"
author = "Bram Stoker und Jules"
publ = "1894"

print(f'{no:4}{title:25}{genre:5}{author:25}{publ:>6}')
# **************Ende Block9**************** """

