import requests, colorama, time, random, os, subprocess, threading, easygui, json, datetime
from colorama import Fore
from requests.exceptions import InvalidHeader

os.system('cls')

colorama.init()

request_url = "https://canary.discordapp.com/api/v6/users/@me"

InvaildTokens = []
InvaildTokensInt = 0
WorkingTokens = []
WorkingTokensInt = 0
NitroTokens = []
NitroTokensInt = 0
TokenUsername = []
TotalChecked = 0

def TokenCheck(Token):
    global WorkingTokensInt
    global InvaildTokensInt
    global TotalChecked
    tokenStatus = requests.get(f"{request_url}", headers={'authorization': Token})
    TotalChecked +=1
    os.system(f'title [Token Checker] /// Total : {TotalChecked} /// Valid : {WorkingTokensInt} /// Invalid : {InvaildTokensInt}')
    if tokenStatus.status_code == 401:
        print(f"{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] {Token}")
        InvaildTokens.append(Token)
        InvaildTokensInt += 1
    elif tokenStatus.status_code == 200:
        print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Token}")
        WorkingTokens.append(Token)
        WorkingTokensInt += 1
    else:
        print(f"{Fore.WHITE}[{Fore.CYAN}!{Fore.WHITE}] {Fore.CYAN}ERROR")

def SaveTokens(TokensList, File):
    file1 = open(f"{File}.txt","w")
    for token in TokensList:
        file1.write(f"{token}\n")

def CheckNitro(TokenList):
    global NitroTokensInt
    global NitroTokens
    for token in TokenList:
        res = requests.get(f"{request_url}", headers={'authorization': token})
        res_json = res.json()

        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        phone_number = res_json['phone']
        email = res_json['email']
        mfa_enabled = res_json['mfa_enabled']
        verified = res_json['verified']

        has_nitro = False
        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions',headers = {'Authorization': token,'Content-Type': 'application/json'})
        nitro_data = res.json()
        has_nitro = bool(len(nitro_data) > 0)
        if has_nitro:
            print(f"{Fore.WHITE}[{Fore.MAGENTA}++{Fore.WHITE}] {token}")
            NitroTokensInt += 1
            NitroTokens.append(token)
        else:
            print(f"{Fore.WHITE}[{Fore.RED}!!{Fore.WHITE}] {token}")