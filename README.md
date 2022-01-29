## The Time Machine - Weaponizing WaybackUrls for Recon, BugBounties , OSINT, Sensitive Endpoints and what not

![TheTimeMachine](https://raw.githubusercontent.com/anmolksachan/TheTimeMachine/main/logo.PNG)

### Detailed Description about this can be found here : 
Read Blog here : https://anmolksachan.medium.com/the-time-machine-weaponizing-waybackurls-for-recon-bugbounties-osint-sensitive-endpoints-and-40889a03feeb

### Introduction 

You must have heard about time travel in movies, series and comics. Well here we are Nah i'm not joking you can travel back in time and can fetch the endpoints from web applications to do further exploitation, don't believe me xD You will after Travelling from TheTimeMachine, PS Doesn't work offline you need internet to Travel In Time xD.

I have created this tool for making my work easier when it comes to recon and fetching sensitive endpoints for sensitive data exposure and further exploitation using waybackurls and sorting for Sensitive endpoints, it has also option to look for sensitive endpoints for information disclosure, It has have more capabilities like looking for possible endpoints vulnerable to XSS, LFI, JIRA Based Vulnerability, Open Redirection.

I'm not too much into bug bounty but recently Managed HOF in NOKIA (Soon will be updated in Website or is already there :P), and found P1 with The Time Machine : https://bugcrowd.com/H4CK3R/crowdstream

It worked on multiple bug bounty program, reports are still under review :P

### Features
1. Search for /api/ endpoint
2. Search for JSON endpoint
3. Fetch possible Conf(configuration) endpoint
4. All Possible Sensitive instances in URL from TheTimeMachine (Searches from Fuzz List) or can also Add your own Custom List
5. Fetches subdomains from waybackurl
6. Search Custom keyword of your choice Eg. backup, .log etc.
7. Attack Mode ( Searched for vulnerable possible endpoints for SQLi, LFI, XSS, Open Redirect, Wordpress, JIRA Based Vulnerability or via Custom File, PS More to be added soon )
8. Fetch only Parameters from any file (Eg. Fetched from way back urls, extracted file from Attack mode or any URLs file, also how creative you are can be used with burp spider file :P) 
9. You can manually edit all the files that searched for XSS, LFI, Fuzz etc.

### How to install and use 

Note : Tested with python3 on Ubuntu/Kali/Windows

```
$ git clone https://github.com/anmolksachan/TheTimeMachine
$ cd TheTimeMachine
$ pip3 install -r requirements.txt
$ python thetimemachine.py

```

If you're not able to install requirements.txt, run install.sh or install manually, run below mentioned commands
```
$ pip install numpy
$ pip install requests
$ pip install coloroma
$ pip install termcolor

```

Example Run : 

Note : Entered URL must look like domain.com or subdomain.domain.com no http or https is required

```
$ python thetimemachine.py domain.com
$ python thetimemachine.py subdomain.domain.com
.. .. .. .. 
.. .. .. .. 
AND SO ON 
```
![enter image description here](https://raw.githubusercontent.com/anmolksachan/anmolksachan.github.io/main/img/TTM.gif)
![enter image description here](https://raw.githubusercontent.com/anmolksachan/TheTimeMachine/main/run.PNG)

### Add your own list of payloads

```
you can edit multiple available payloads and Fuzz , 
Add your own in the interested text file !

```

### Contact

Shoot my DM : [@FR13ND0x7F](https://twitter.com/fr13nd0x7f)

### Special Thanks

[@nihitjain11](https://github.com/nihitjain11)

### Note

This is not a stable version as few things are missing soon it will be updated with other functionality.

## __Want to support my work?__
Give me a Star in the repository, thats enough for me :P
