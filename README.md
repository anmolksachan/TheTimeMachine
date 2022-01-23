## The Time Machine - Weaponizing WaybackUrls for Recon, BugBounties , OSINT, Sensitive Endpoints and what not

![TheTimeMachine](https://raw.githubusercontent.com/anmolksachan/TheTimeMachine/main/logo.PNG)

### Detailed Description about this can be found here : 
Read Blog here : Will write blog soon, if you wrote DM me with link :)

### Introduction 

I have created this tool for making my work easier when it comes to recon and fetching sensitive endpoints for sensitive data exposure and further exploitation using waybackurls and sorting for Sensitive endpoints, it has also option to look for sensitive endpoints for information disclosure, It has have more capabilities like looking for possible endpoints vulnerable to XSS, LFI, JIRA Based Vulnerability, Open Redirection.

I'm not too much into bug bounty but recently found P1 with The Time Machine : https://bugcrowd.com/H4CK3R/crowdstream

It worked on multiple bug bounty program, reports are still under review :P

### How to install and use 

Note : Tested with python3 on Ubuntu/Kali

```
$ git clone https://github.com/anmolksachan/TheTimeMachine
$ cd TheTimeMachine
$ pip3 install -m requirements.txt
$ python thetimemachine.py

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

![enter image description here](https://raw.githubusercontent.com/anmolksachan/TheTimeMachine/main/run.PNG)

### Add your own list of payloads

```
you can edit multiple available payloads and Fuzz , 
Add your own in the interested text file !

```

### Contact

Shoot my DM : [@FR13ND0x7F](https://twitter.com/fr13nd0x7f)

## __Want to support my work?__
Give me a Star in the repository, thats enough for me :P
