import sys
import requests
import re
import numpy as np
from colorama import init
from termcolor import colored

init()
print("""
████████╗██╗░░██╗███████╗  ████████╗██╗███╗░░░███╗███████╗
╚══██╔══╝██║░░██║██╔════╝  ╚══██╔══╝██║████╗░████║██╔════╝
░░░██║░░░███████║█████╗░░  ░░░██║░░░██║██╔████╔██║█████╗░░
░░░██║░░░██╔══██║██╔══╝░░  ░░░██║░░░██║██║╚██╔╝██║██╔══╝░░
░░░██║░░░██║░░██║███████╗  ░░░██║░░░██║██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝

███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝""")
print(colored('    Coded with Love by Anmol K Sachan @Fr13ND0x7f\n','green'))                                                                               

if __name__ == "__main__":
    for i, arg in enumerate(sys.argv):
        i = (f"{arg}")

print("Usage : thetimemachine.py target.com\n")

print("Checking Your Internet Connection...")
thetimemachine = 'https://web.archive.org/'
try:
    response = requests.get(thetimemachine)
    res = requests.get(thetimemachine)
    print("\nThe Time Machine got WayBackMachine's Status Code as: ",res.status_code)
    print (colored('\nOK!, The Time Machine Will Work\nInternet Connection is Active.','green'))
    response.close()
except:
    print (colored('Boo! The Time Machine got invalid status code tool might not work properly in offline mode, check your internet connection. ','red'))
    print("\nUnable to load:",(colored(i,'red')))
    print((colored('\nExiting!!!','red')))
    exit()


url = f'https://web.archive.org/cdx/search/cdx?url=*.{i}/*&output=txt&fl=original&collapse=urlkey&page=/'
print("\nTarget Loaded:",(colored(i,'green')))

print('\nFetching URLs from The Time Machine :P \nHave Patience this may take some time depending on the size of asset\n[Dont press Enter or anykey while TheTimeMachine is Fetching URLs]')
response = requests.get(url)
url_list=response.text

targetFile=i+"_URLs.txt"
print("Storing links in :",(colored(targetFile,'green')))

xssFile=i+"_xss.txt"
openRedirect=i+"_OpenRedirect.txt"
lfi=i+"_lfi.txt"
sqli=i+"_sqli.txt"
jira=i+"_jira.txt"
subdomainFile=i+"_subdomain.txt"
wp=i+"_wp.txt"
customFuzz=i+"_customFuzz.txt"

file = open(targetFile, 'w')
file.write(url_list)
file.close()
print('Completed\n')

file = open(targetFile,"r")
Counter = 0  
Content = file.read()
CoList = Content.split("\n")
for i in CoList:
    if i:
        Counter += 1
print("Found",(colored(Counter,'green')), "instances in The Time Machine, Stored in ",targetFile)

#Find Subdomains 
txt = open(targetFile,'r')
lines = txt.readlines()
lines = [line.strip()+"/" for line in lines]
txt.close()

regex = "://(.*?)\.(.*?)/"

uniques = []

for i in lines:
    matches = re.search(regex,i)
    output = matches.group()
    data = 'http'+output+'\n'
    if data not in uniques:
        uniques.append(data)
        uniques.append('https'+output+'\n')


out = open(subdomainFile, 'w')
out.writelines(uniques)
out.flush()
out.close()
#Find Subdomains

file = open(subdomainFile,"r")
sub = 0  

Content = file.read()
CoList = Content.split("\n")
for i in CoList:
    if i:
        sub += 1
print("\nFound",(colored(sub,'green')),"subdomains instances in The Time Machine (all instances http and https are included)")
print("Stored in",(colored(subdomainFile,'green')))

def paramFinder():
    print(colored("\n...Fetch All Parameters From Custom File...",'white','on_green'))
    findme = (input("Enter location of file Eg. (target.com_URLs.txt) :"))
    parameter=findme+"_param.txt"
    pattern = re.compile("([\d\w]*?)=([\d\w+-_%()]*)")
    file=open(parameter,"w")
    for i, line in enumerate(open(findme)):
        for match in re.finditer(pattern, line):
            print(colored("URL : ",'red'),line,colored("\nFound on Line:",'red'),i+1,colored("\nParameter:",'red'),match.group())
            file.write(match.group())
            file.write('\n')
    file.close()
    print("\nAll Found parameters are Stored in",(colored(parameter,'green')))

def exit_or_explore():
 print(colored("\n---- [Select from below options] ----",'white','on_green'))
 print("1: Fetch /api/ endpoint")
 print("2: Fetch JSON in URL")
 print("3: Fetch conf(Config Possibility) in URL")
 print("4: All Possible Sensitive instances in URL from TheTimeMachine (Searches from Fuzz List) or Add Custom List")
 print("5: Show Fetched Links from:",targetFile,"having",Counter,"instances")
 print("6: Show subdomains from TheTimeMachine, Found",sub,"instances")
 print("7: Enter Custom Keyword of your choice")
 print("8:",colored("Attack Mode [Possible Vulnerable Endpoint : JIRA, XSS, Open Redirect, LFI, SQLi] ",'red'))
 print("9: Fetch Only Parameters From File")
 print("10: Exit")
 
 while True:
    try:
        inp = int(input("\nEnter a number: "))
    except ValueError:
        print(colored("Enter a valid option",'red'))
    else:
        break 
 

 if inp == 1:
    pattern = "/api/"
    patterns = " "
    print('\nFetching selected', pattern , 'input Given', inp ,'\n')
    with open(targetFile) as file:
        for line in file:
            urls = re.findall('(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})', line)
            if re.search(pattern, line):
                  print(urls)
    exit_or_explore()

 elif inp == 2:
    pattern = "JSON"
    patterns = " "
    print('\nFetching selected', pattern , 'input Given', inp ,'\n')
    with open(targetFile) as file:
        for line in file:
            urls = re.findall('(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})', line)
            if re.search(pattern, line):
                  print(urls)
    exit_or_explore()

 elif inp == 3:
    pattern = "conf"
    patterns = " "
    print('\nFetching selected', pattern , 'input Given', inp ,'\n')
    with open(targetFile) as file:
        for line in file:
            urls = re.findall('(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})', line)
            if re.search(pattern, line):
                  print(urls)
    exit_or_explore()

 elif inp == 7:
    pattern = input("\nEnter Custom Keyword to search (Blank output means Not Found) :")
    patterns = " "
    print('\nFetching custom instance', pattern , 'input Given', inp ,'\n')
    with open(targetFile) as file:
        for line in file:
            urls = re.findall('(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})', line)
            if re.search(pattern, line):
                  print(urls)    
    exit_or_explore()

 elif inp == 4:
   print(colored("\n---- [Select from below options] ----",'white','on_green'))
   print("1: Use Default Fuzz.txt")
   print("2: Add your own list")
   option = int(input("\nEnter a number: "))
   if option == 1:
    patterns = "\nFuzzing from default Fuzz.txt\n"
    print(patterns)
    keyfile = "fuzz.txt"
    testfile = targetFile
    keys = set(key.lower() for key in 
           re.findall(r'\w+', open(keyfile , "r").readline()))
    with open(testfile) as f:
           for line in f:
                words = set(word.lower() for word in re.findall(r'\w+', line))
                if keys & words:
                    print(line, end='')
    exit_or_explore()
   
   elif option == 2:
    patterns = "\nFuzzing from custom list\n"
    print(patterns)
    keyfile = (input("Enter location of file: "))
    testfile = targetFile
    keys = set(key.lower() for key in 
           re.findall(r'\w+', open(keyfile , "r").readline()))
    with open(testfile) as f:
           for line in f:
                words = set(word.lower() for word in re.findall(r'\w+', line))
                if keys & words:
                    print(line, end='')
    exit_or_explore()
   
   else:
    print("Wrong Option")
    exit_or_explore()

 elif inp == 5:
    file = open(targetFile,"r")  
    Content = file.read()
    print(Content)
    exit_or_explore()

 elif inp == 6:
    print("Stored in :",subdomainFile," found ",sub," instances from TheTimeMachine")
    file = open(subdomainFile,"r")  
    Content = file.read()
    print(Content)
    exit_or_explore()

 elif inp == 9:
    paramFinder()
    exit_or_explore()

 elif inp == 8:
   print(colored("\nAttack Mode Loaded",'white','on_green'))
   print("1: Fetch Possible XSS Vulnerable Endpoint")
   print("2: Fetch Possible Open Redirection Vulnerable Endpoint")
   print("3: Fetch Possible LFI Vulnerable Endpoint")
   print("4: Fetch Possible SQLi Vulnerable Endpoint")
   print("5: Fetch Possible JIRA Vulnerable Endpoint")
   print("6: Fetch Possible WordPress Vulnerable Endpoint")
   print("7: Fetch Custom Vulnerable Endpoint Ref Files available here : https://github.com/danielmiessler/SecLists/tree/master/Discovery ")
   print("8: Back")
   while True:
    try:
        option = int(input("\nEnter a number: "))
    except ValueError:
        print(colored("Enter a valid option",'red'))
    else:
        break

   if option == 1:
    patterns = "\nFinding Possible XSS Vulnerable links\n"
    print(patterns)
    print("Storing links in :",(colored(xssFile,'green')))
    keyfile = "xss.txt"
    testfile = targetFile
    k=open(keyfile,"r")
    t=open(testfile,"r")
    file = open(xssFile, 'w')
    lines = t.readlines()
    patterns = [i.strip() for i in k.readlines()]
    for l in lines:
       for p in patterns:
          if p in l:
            print(l)
            file.write(str(l))
    file.close()
    print('Completed\n')
    print("Stored in",(colored(xssFile,'green')))
    exit_or_explore()
   
   elif option == 2:
    patterns = "\nFuzzing for Possible Open Redirect Vulnerable links\n"
    print(patterns)
    keyfile = "openredirect.txt"
    testfile = targetFile
    k=open(keyfile,"r")
    t=open(testfile,"r")
    file = open(openRedirect, 'w')
    lines = t.readlines()
    patterns = [i.strip() for i in k.readlines()]
    for l in lines:
       for p in patterns:
          if p in l:
            print(l)
            file.write(str(l))
    file.close()
    print('Completed\n')
    print("Stored in",(colored(openRedirect,'green')))
    exit_or_explore()
   
   if option == 3:
    patterns = "\nFinding Possible LFI Vulnerable links\n"
    print(patterns)
    keyfile = "lfi.txt"
    testfile = targetFile
    k=open(keyfile,"r")
    t=open(testfile,"r")
    file = open(lfi, 'w')
    lines = t.readlines()
    patterns = [i.strip() for i in k.readlines()]
    for l in lines:
       for p in patterns:
          if p in l:
            print(l)
            file.write(str(l))
    file.close()
    print('Completed\n')
    print("Stored in",(colored(lfi,'green')))
    exit_or_explore()

   if option == 4:
    patterns = "\nFinding Possible SQLi Vulnerable links\n"
    print(patterns)
    keyfile = "sqli.txt"
    testfile = targetFile
    k=open(keyfile,"r")
    t=open(testfile,"r")
    file = open(sqli, 'w')
    lines = t.readlines()
    patterns = [i.strip() for i in k.readlines()]
    for l in lines:
       for p in patterns:
          if p in l:
            print(l)
            file.write(str(l))
    file.close()
    print('Completed\n')
    print("Stored in",(colored(sqli,'green')))
    exit_or_explore()

   if option == 5:
    patterns = "\nFinding Possible JIRA Vulnerable links\nHow to Exploit: https://gist.github.com/0x240x23elu/891371d46a1e270c7bdded0469d8e09c\n"
    print(patterns)
    keyfile = "jira.txt"
    testfile = targetFile
    k=open(keyfile,"r")
    t=open(testfile,"r")
    file = open(jira, 'w')
    lines = t.readlines()
    patterns = [i.strip() for i in k.readlines()]
    for l in lines:
       for p in patterns:
          if p in l:
            print(l)
            file.write(str(l))
    file.close()
    print('Completed\n')
    print("Stored in",(colored(jira,'green')))
    exit_or_explore()
   
   if option == 6:
    patterns = "\nFinding Possible WordPress Vulnerable links\n"
    print(patterns)
    keyfile = "wp-fuzz.txt"
    testfile = targetFile
    k=open(keyfile,"r")
    t=open(testfile,"r")
    file = open(wp, 'w')
    lines = t.readlines()
    patterns = [i.strip() for i in k.readlines()]
    for l in lines:
       for p in patterns:
          if p in l:
            print(l)
            file.write(str(l))
    file.close()
    print('Completed\n')
    print("Stored in",(colored(wp,'green')))
    exit_or_explore()

    if option == 7:
    patterns = "\nFinding Possible WordPress Vulnerable links\n"
    print(patterns)
    keyfile = (input("Enter location of file: "))
    testfile = targetFile
    k=open(keyfile,"r")
    t=open(testfile,"r")
    file = open(customFuzz, 'w')
    lines = t.readlines()
    patterns = [i.strip() for i in k.readlines()]
    for l in lines:
       for p in patterns:
          if p in l:
            print(l)
            file.write(str(l))
    file.close()
    print('Completed\n')
    print("Stored in",(colored(customFuzz,'green')))
    exit_or_explore()

   else:
    print(colored("Switching to main Menu",'red'))
    exit_or_explore()

 else:
    sys.exit("Quitting! Have a nice day ahead.")

exit_or_explore()
