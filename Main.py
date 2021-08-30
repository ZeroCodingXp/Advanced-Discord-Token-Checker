from tkinter.constants import DISABLED
import os, easygui, DiscordTokensPy
from colorama import Fore
os.system('title [Token Checker] Choose Tokens File...')
tokensFile = easygui.fileopenbox()


checkeddddtokes = []



with open(tokensFile, 'r', encoding="utf-8") as tokens:
    for token in tokens:
        if token not in checkeddddtokes:
            DiscordTokensPy.TokenCheck(token.strip())
            checkeddddtokes.append(token)
    DiscordTokensPy.CheckNitro(DiscordTokensPy.WorkingTokens)






print(f"\n{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Done Checking{Fore.GREEN}!{Fore.WHITE}\n\n{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}-{Fore.RED}Invaild{Fore.WHITE}-{Fore.RED}!{Fore.WHITE}] [{Fore.RED}{DiscordTokensPy.InvaildTokensInt}{Fore.WHITE}]\n{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}-{Fore.GREEN}Valid{Fore.WHITE}-{Fore.GREEN}+{Fore.WHITE}] [{Fore.GREEN}{DiscordTokensPy.WorkingTokensInt}{Fore.WHITE}]\n{Fore.WHITE}[{Fore.MAGENTA}++{Fore.WHITE}-{Fore.MAGENTA}Nitro{Fore.WHITE}-{Fore.MAGENTA}+{Fore.WHITE}] [{Fore.MAGENTA}{DiscordTokensPy.NitroTokensInt}{Fore.WHITE}]")
a = input("")





askSave = input(f"\n{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Would You Like To Save Working Tokens? ")
if askSave == "y":
    DiscordTokensPy.SaveTokens(DiscordTokensPy.WorkingTokens, easygui.filesavebox())





askSave1 = input(f"\n{Fore.WHITE}[{Fore.MAGENTA}++{Fore.WHITE}] Would You Like To Save Nitro Tokens? ")
if askSave1 == "y":
    DiscordTokensPy.SaveTokens(DiscordTokensPy.NitroTokens, easygui.filesavebox())





a = input("")
