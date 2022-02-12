import os
import sys
from time import sleep
import webbrowser as web
from banner import ban,bye
import colorama
from colorama import Fore
colorama.init(autoreset=True)

def Star():
    ban()
    sleep(1)
    print(Fore.CYAN +'''
-----------------------------------------------------
    1)Documents
    2)Movies
    3)Advance
    4)About
    5)Help
    6)Exit
-----------------------------------------------------
        ''')
    query = input('Enter the no: ')
    ClearCon()
    if '1' in query:
        Doc()

    elif '2' in query:
        Mov()

    elif '3' in query:
        Adv()

    elif '4' in query:
        Abo()

    elif '5' in query or 'help' in query:
        Hel()

    elif '6' in query:
        Exe()

def ClearCon():
    try:
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
            os.system(command)
        else:
            os.system('clear')
    except:
        print('somthing want wrong')

def Doc():
        ClearCon()
        print(Fore.CYAN +'''
----------------------------------------------------
        1)pdf (normal pdf)
        2)Doc (ms-word)
        3)ppt (power point presentation)
        4)xls and xlsx (excel)
        5)txt (text)
        6)Go Back
----------------------------------------------------
            ''')
        query = input('Enter the no: ')
        ClearCon()
        if '1' in query:
            r = input('Enter Your Query Without Extension: ')
            rl = r.replace('pdf','').replace('PDF','')
            l = 'https://www.google.com/search?q='+rl+'filetype:pdf'
            web.open(l)
        
        elif '2' in query:
            r = input('Enter Your Query without Extension: ')
            rl = r.replace('Doc','').replace('DOC','')
            l = 'https://www.google.com/search?q='+rl+'filetype:DOC'
            web.open(l)

        elif '3' in query:
            r = input('Enter Your Query without Extension: ')
            rl = r.replace('ppt','').replace('PPT','')
            l = 'https://www.google.com/search?q='+rl+'filetype:ppt'
            web.open(l)

        elif '4' in query:
            r = input('Enter Your Query without Extension: ')
            rl = r.replace('xls','').replace('xlsx','')
            l = 'https://www.google.com/search?q='+rl+'filetype:xls'
            web.open(l)

        elif '5' in query:
            r = input('Enter Your Query without Extension: ')
            rl = r.replace('text','').replace('txt','')
            l = 'https://www.google.com/search?q='+rl+'filetype:txt'
            web.open(l)

        elif '6' in query:
            Star()

def Mov():
    ClearCon()
    print(Fore.CYAN +''' 
    -------------------------------
    1)Search movie by Direct link
    2)Best movie sites
    3)Go Back
    -------------------------------
    ''')
    query = input('Enter the No You wanna search with: ')
    ClearCon()
    if '1' in query:
        r = input('Enter Movie Name: ')
        l = 'https://www.google.com/search?q='+r+'''-inurl:(htm|html|php|pls|txt) intitle:index.of “last modified” (mp4|wma|aac|avi|mkv)'''
        web.open(l)
    
    elif '2' in query:
        print('''
        1)https://moviesverse.me/
        2)https://www.youtube.com/c/GoldminesTelefilms
        3)Go back
        ''')
        q = input('Enter your query: ')
        if '3' in q:
            Star()

        elif '1' in q:
            web.open('https://moviesverse.me/')
        
        elif '2' in q:
            web.open('https://www.youtube.com/c/GoldminesTelefilms')

def Adv():
  
    ClearCon()
    print(Fore.LIGHTBLUE_EX +'''
    --------------------------------------------------------------------
    1)link (will list webpages that have links to the specified webpage)

    2)related (will list web pages that are “similar” to a specified web
    page.)

    3)info (will present some information that Google has about that web
    page.)

    4)define (will provide a definition of the words you enter after it,
    gathered from various online sources.)

    5)Go Back
    -------------------------------------------------------------------
    Some commands are in next update \U0001F60A
    ''')
    query = input('Enter any no You want to search: ')
    ClearCon()
    if '1' in query:
        r = input('Enter link like www.google.com : ')
        l = 'https://www.google.com/search?q=link:'+r
        web.open(l)
    
    elif '2' in query:
        r = input('Enter link like www.google.com : ')
        l = 'https://www.google.com/search?q=related:'+r
        web.open(l)

    elif '3' in query:
        r = input('Enter your query: ')
        l = 'https://www.google.com/search?q=info:'+r
        web.open(l)
    
    elif '4' in query:
        r = input('Enter your query: ')
        l = 'https://www.google.com/search?q=define:'+r
        web.open(l)
    
    elif '5' in query:
        Star()

def Abo():
    ClearCon()
    print(Fore.LIGHTCYAN_EX +'''
    This tool is using google Dork and webbrowser for searching results made by Rajkishor patra.
------------------------------------------------------------------------------------------------
    contact him:
        instagram : https://www.instagram.com/im.raj.569
        github : https://github.com/imraj569
------------------------------------------------------------
    press [0] for Go Back:
    press [1] for Instagram:
    press [2] for Github:
------------------------------------------------------------
    ''')
    query = input('Enter any no: ')
    ClearCon()
    if '0' in query:
        Star()

    elif '1' in query:
        web.open('https://www.instagram.com/im.raj.569')

    elif '2' in query:
        web.open('https://github.com/imraj569')

def Hel():
    ClearCon()
    print(Fore.LIGHTYELLOW_EX +'''
    Just type any anything you want to use like -
---------------------------------------------
    Commands  | Activity
    _____________________
        1 -   |   Documents
        2 -   |   Movies
        3 -   |  Advance
        4 -   |  About
        5 -   |  Help
        6 -   |  Exit
---------------------------------------------
    Type [0] for Go Back
    ''')
    query = input('Enter any no: ')
    ClearCon()
    if '0' in query:
        Star()

def Exe():
    ClearCon()
    bye()
    sys.exit()

if __name__ == '__main__':
    while True:
        Star()
    
