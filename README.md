# CTF FOFIC
![CTF_FOFIC_EXEC](https://i.ibb.co/dLFTNt0/CTF-FOFIC.gif)

### I - [ INTRODUCTION ]

**CTF FOFIC** (Folder File Creator) is a python3 script that generates a folder with a note-taking file for *CTF challenges* on **Linux only**.
In the **example.txt** file, there's an example of note-taking.
The **install.sh** file is used to install the *netifaces* module using pip3, this module recovers the IP address (tun0) you obtain by connecting to the VPN using OPENVPN for example.
___

### II - [ NOTE-TAKING FILE ]

This file is based on an attack strategy. The attack strategy defines the different phases of attack, this strategy is inspired 
by the [Cyber Kill Chain](https://en.wikipedia.org/wiki/Kill_chain).﻿ In this strategy that I present to you is composed of 3 PHASES : 

- PHASE 1 [ _RECONNAISSANCE_ ] : Gather information about our target, such as which technologies are used ? What ports are open and what services are used ? What vulnerabilities and weaknesses can be exploited ? The greater the amount of information gathered, the more sophisticated the attack and the higher the probability of success.

- PHASE 2 [ _EXPLOITATION_ ] : Exploitation of the vulnerabilities identified in the reconnaissance phase. The aim of this phase is to gain initial access to the target's system.

- PHASE 3 [ _TOTAL CONTROL & EVASION_ ] : At this point we have restricted, unstable access which is likely to be detected. So to avoid losing access, we can open up other paths so that we can easily regain access in the event of problems. To do this, we need to obtain more privileges known as elevation of privileges which means moving from a restricted access level to a higher one. Once our mission is completed, we must erase all traces of our passage and leave the network.

**The example.txt file is a perfect example of how to use this strategy in a CTF challenge.**
