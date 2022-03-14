import itertools
import os

character = 'abcdefghijklmnopqrstuvwxyz'
Capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Num = '0123456789'
chars='!,@,#,$,%%,&,*'
years = '1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020'



MinSize = int(input('[*] Please enter Minimum size of the words'))
while MinSize < 1:
    print("Sorry, Please enter an integer number")
    MinSize = int(input('[*] Please enter Minimum size of the words'))
else:
    MaxSize = int(input('[*] Please enter Maximum size of the words'))

print("\n[1] only Character,"
        "\n[2] only Capital letter,"
        "\n[3] Only Numbers,"
        "\n[4] Character + Capital letter,"
        "\n[5] Character + number,"
        "\n[6] Capital Letter + years,"
        "\n[7] Character Letter + years,"
        "\n[8] Capital Letter + character + special chars + num,"
        "\n[9] Character + Char,"
        "\n[10] character + Capital + special chars\n"
        "\n[11]Mix\n")

# let user select
UserR = int(input('Please select a number'))


Character_Capital = character + Capital
Character_number = character + Num
Character_Year= character + years
Capital_Year = Capital + years
char_characters = character + chars
char_capital = Capital + chars
char_capital_characters = character + char_capital
num_charcapital = char_capital_characters + Num
Mix = num_charcapital + years


# create the file name
filename = input('Please Enter a name of the wordlist:')

Combination = [character, Capital, Num, Character_Capital, Character_number,Capital_Year,Character_Year, num_charcapital,char_characters, Mix]

name = open(filename, "w")
count = 0
for i in range(MinSize,MaxSize + 1):
    for xs in itertools.product(Combination[UserR-1], repeat=i):
        name.write(''.join(xs) + '\n')
        count+=1

name.close()


