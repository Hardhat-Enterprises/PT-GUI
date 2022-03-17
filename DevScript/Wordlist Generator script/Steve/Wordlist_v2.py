import argparse
from itertools import product
import itertools
import os
from re import X
import time
# initialize
character = 'abcdefghijklmnopqrstuvwxyz'
Capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Num = '0123456789'
chars="!,@,#,$,%%,&,*"
years = '1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020'
numfrom = 0
numto = 100
wordlistfrom = 5
wordlistto = 12
__Author__ = 'Steve Tee'
__version__ = '1.0.0'

def version():
    print("\nVersion" + __version__)
    print("\n")
    print("\nWordlist generator made by" + __Author__)
    print("\n")
    print("\nReference: "
    "\n[1]https://github.com/Mebus/cupp"
    "\n[2]https://github.com/4n4nk3/Wordlister/blob/master/wordlister.py"
    "\n[3]https://github.com/berzerk0/BEWGor"
    "\n[4]https://github.com/sc0tfree/mentalist"
    "\n[5]https://github.com/G0uth4m")


def randommode() :
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
    
    Combination = [character, Capital, Num, Character_Capital, Character_number, Capital_Year, Character_Year, num_charcapital, char_characters, char_capital_characters, Mix]
    
    name = open(filename, "w")
    count = 0
    for i in range(MinSize,MaxSize + 1):
        for xs in itertools.product(Combination[UserR-1], repeat=i):
            name.write(''.join(xs) + '\n')
            count+=1
    
    name.close()





# for concatenations...
def concats(seq, start, stop):
    for mystr in seq:
        for num in range(start, stop):
            yield mystr + str(num)


# for sorting and making combinations...
def combination(seq, start, special=""):
    for mystr in seq:
        for mystr1 in start:
            yield mystr + special + mystr1


def __init__():
    print("\n[*]insert the information about your attack target to make a dictionary")
    print("\n[*] hit enter if you don't want to add or don't know the info")

    #create a box to store information(like array)

    data = {}

    #The lower() method converts all
    # uppercase characters in a string into lowercase characters and returns it.
    Name = input(">First Name: ").lower()
    #to make sure user input is not blank or spack
    while len(Name.strip()) == 0:
        print("\n[-] You must enter a name at least!")
        Name = input(">name:").lower()
    data["name"] = str(Name)

    data["surname"] = input("> Surname: ").lower()
    data["nickname"] = input("> Nickname: ").lower()

    birthday = input(">Birthday (DDMMYYYY): ")
    while len(birthday) != 8:
        print("\r\n[-] You must enter 8 digits for birthday!")
        birthday = input("> Birthday (DDMMYYYY): ")
    data["birthday"] = str(birthday)
    
    print("\n")

    data["words"] = [""]
    words1 = input(
        "> Do you want to add some key words about the victim? Y/[N]: "
    ).lower()
    words2 = ""
    if words1 == "y":
        words2 = input(
            "> Please enter the words, separated by comma. [i.e. hacker,Food , color]: "
        ).replace(" ", "")
    data["words"] = words2.split(",")

    data["spechars1"] = input(
        "> Do you want to add special chars at the end of words? Y/[N]: "
    ).lower()

    data["randnum"] = input(
        "> Do you want to add some random numbers at the end of words? Y/[N]:"
    ).lower()

    generate_wordlist(data)  # generate the wordlist

def generate_wordlist(data):
    ## generate wordlist from data

    data["spechars"] = []

    if data["spechars1"] == "y":
        for spec1 in chars:
            data["spechars"].append(spec1)
            for spec2 in chars:
                data["spechars"].append(spec1 + spec2)
                for spec3 in chars:
                    data["spechars"].append(spec1 + spec2 + spec3)

    print("\r\n[+] Now making a dictionary...")

    # Now me must do some string modifications...

    # Birthdays first

    birthday_yy = data["birthday"][-2:]
    birthday_yyy = data["birthday"][-3:]
    birthday_yyyy = data["birthday"][-4:]
    birthday_xd = data["birthday"][1:2]
    birthday_xm = data["birthday"][3:4]
    birthday_dd = data["birthday"][:2]
    birthday_mm = data["birthday"][2:4]


    # Convert first letters to uppercase...

    nameup = data["name"].title()
    surnameup = data["surname"].title()
    nicknameup = data["nickname"].title()

    wordsup = []
    wordsup = list(map(str.title, data["words"]))

    word = data["words"] + wordsup

    # reverse a name

    #【：：-1】= 1234 to 4321
    rev_name = data["name"][::-1]
    rev_nameup = nameup[::-1]
    rev_nickname = data["nickname"][::-1]
    rev_nicknameup = nicknameup[::-1]

    reverse = [
        rev_name,
        rev_nameup,
        rev_nickname,
        rev_nicknameup,

    ]
    rev_n = [rev_name, rev_nameup, rev_nickname, rev_nicknameup]

    # Let's do some serious work! This will be a mess of code, but... who cares? :)

    # Birthdays combinations

    bds = [
        birthday_yy,
        birthday_yyy,
        birthday_yyyy,
        birthday_xd,
        birthday_xm,
        birthday_dd,
        birthday_mm,
    ]

    bdss = []

    for bds1 in bds:
        bdss.append(bds1)
        for bds2 in bds:
            if bds.index(bds1) != bds.index(bds2):
                bdss.append(bds1 + bds2)
                for bds3 in bds:
                    if (
                        bds.index(bds1) != bds.index(bds2)
                        and bds.index(bds2) != bds.index(bds3)
                        and bds.index(bds1) != bds.index(bds3)
                    ):
                        bdss.append(bds1 + bds2 + bds3)



    combinations = [
        data["name"],
        data["surname"],
        data["nickname"],
        nameup,
        surnameup,
        nicknameup,
    ]


    combinationsa = []
    for combinations1 in combinations:
        combinationsa.append(combinations1)
        for combinations2 in combinations:
            if combinations.index(combinations1) != combinations.index(combinations2) and combinations.index(
                combinations1.title()
            ) != combinations.index(combinations2.title()):
                combinationsa.append(combinations1 + combinations2)

 

    combinationi = {}
    combinationi[1] = list(combination(combinationsa, bdss))
    combinationi[1] += list(combination(combinationsa, bdss, "_"))
    combinationi[2] = list(combination(combinationsa, years))
    combinationi[2] += list(combination(combinationsa, years, "_"))
    combinationi[3] = list(combination(word, bdss))
    combinationi[3] += list(combination(word, bdss, "_"))
    combinationi[4] = list(combination(word, years))
    combinationi[4] += list(combination(word, years, "_"))
    combinationi[5] = [""]
    combinationi[6] = [""]
    combinationi[7] = [""]
    combinationi[8] = [""]
    if data["randnum"] == "y":
        combinationi[5] = list(concats(word, numfrom, numto))
        combinationi[6] = list(concats(combinationsa, numfrom, numto))
        combinationi[7] = list(concats(reverse, numfrom, numto))
    combinationi[9] = list(combination(reverse, years))
    combinationi[9] += list(combination(reverse, years, "_"))
    combinationi[10] = list(combination(rev_n, bdss))
    combinationi[10] += list(combination(rev_n, bdss, "_"))
    combination001 = [""]
    combination002 = [""]
    combination003 = [""]
    if len(data["spechars"]) > 0:
        combination001 = list(combination(combinationsa, data["spechars"]))
        combination002 = list(combination(word, data["spechars"]))
        combination003 = list(combination(reverse, data["spechars"]))

    print("[+] Sorting list and removing duplicates...")

    combination_unique = {}
    for i in range(1, 11):
        combination_unique[i] = list(dict.fromkeys(combinationi[i]).keys())

    combination_unique01 = list(dict.fromkeys(combinationsa).keys())
    combination_unique02= list(dict.fromkeys(word).keys())
    combination_unique03 = list(dict.fromkeys(combination001).keys())
    combination_unique04 = list(dict.fromkeys(combination002).keys())
    combination_unique05 = list(dict.fromkeys(combination003).keys())

    uniqlist = (
        bdss
        + reverse
        + combination_unique01
        + combination_unique02
        + combination_unique03
    )

    for i in range(1, 10):
        uniqlist += combination_unique[i]

    uniqlist += (
        combination_unique04
        + combination_unique03
        + combination_unique05

    )
    unique_lista = list(dict.fromkeys(uniqlist).keys())

    unique_list = unique_lista 

    unique_list_finished = []
    unique_list_finished = [
        x
        for x in unique_list
        if len(x) < wordlistto and len(x) > wordlistfrom
    ]
