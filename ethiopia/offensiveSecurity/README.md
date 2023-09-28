# Cybersecurity
This is a [git repository](https://en.wikipedia.org/wiki/Git) which is hosted
on GitHub; a beautiful place where we learn together cybersecurity and what
faith will bring us. In this README I write my notes of the course but some of
the content may be provided as a link to external resources (so, check the links pls). 
If you have any
suggestion to improve this text or the course, please open an
[issue](https://github.com/v-research/pascal/issues/new/choose).

For any doubt, curiosity or anything else, feel free to drop me an email (marco@v-research.it).

### Objective of the Course
1. Understand general penetration testing phases. Apply critical thinking to creatively and systematically defend from future attacks
2. Implement penetration testing phases Understand the process and toolchain for a structured penetration testing
3. Practice different attacking techniques for network penetration testing. Apply vulnerability assessment technologies (e.g. nmap) to identify vulnerabilities in a network Infrastructure, and search for exploits on major web repositories (e.g., CVE, NVD) and tools (e.g., metasploit).
5. Practice different attacking techniques for web application penetration testing. Apply offensive technologies to exploit web-based attacks such as SQL-injection, XSS, XSRF, etc.
6. Reporting attacks and vulnerabilities identified during network or web app penetration tests. Analyze and document security tests and report to the end user (customer).

**Table of Content**
* [Intro](#intro)
* [Penetration Testing](#penetration-testing)
* Password Cracking (Brute Force and Dictionary Attack)
* Network Protocols and Man-in-the-Middle Attack
* Web Attacks: SQL Injection
* Web Attacks: XSS
* Web Attacks: XSRF

## Intro

### Requisite (because it is a logical AND between all the following) to attend this course:
1. Use the *pen-and-paper* approach to take notes during each lecture! This is the most important part of the whole course. If you don't take notes, it is likely that you won't remember what we have done. Mis-understanding will pile up in time and we won't be speaking the same language very very soon (as you won't understand what I'm saying).
2. *Study*! If you don't invest time in reading and **reason** on your notes (something like: "wait! I wrote "integrity" but what was the definition? Let's look on [wikipedia](https://en.wikipedia.org/wiki/Information_security)) you can spare the effort of keeping notes in the first place. You *have to* spend your time in reasoning on your notes or you won't understand what we are doing. At the beginning, you may feel you can remember the whole blablabla of each lesson, but it is going to become difficult in a few lessons. The difference between listening and understanding determines the distance that you have to walk in this course: 
   1. listen,
   2. draft notes,
   3. review note with a critical mind (wikipedia, duckduckgo, google and **marco@v-research.it** are your best [friends](https://www.amazon.it/Lamicizia-latino-fronte-Tullio-Cicerone/dp/8817067008/ref=sr_1_1?crid=3DVEA9A01CN98&keywords=cicerone+amicizia&qid=1646997948&sprefix=cicerone+amicizia%2Caps%2C156&sr=8-1)... Cicero too), 
   4. believe you have understood something, 
   5. test your believed understanding until you find a counter-example (how? talk to your [best friend](https://en.wikipedia.org/wiki/Rubber_duck_debugging), and 
   6. be vigilant forever after.
4. Create a [study group](https://en.wikipedia.org/wiki/Study_group) and study together because "When students study in groups, they can motivate and encourage each other and lessen procrastination". Consider investing time (e.g., a couple of hours) after each lesson to review together the notes. Tell each other (even if it seems trivial) what we've done during the last lesson(s) and if it is all clear then:
5. *Relax*. Take your time, stay away from your notes. Let them ripe. Go back to 1.

>We read and write poetry because we are members of the human race. And the human race is filled with passion. And medicine, law, business, engineering, these are noble pursuits and necessary to sustain life. But poetry, beauty, romance, love, these are what we stay alive for.
>John Keating, "Dead Poets Society"

### What is Cybersecurity?
What is something? What does it even mean to understand *what* something *is*? This is too long to be discussed in this course but there's a friend who is willing to tell you... well, unfortunately he's dead but he left you a [precious book](https://www.amazon.it/scoperta-scientifica-carattere-autocorrettivo-scienza/dp/8806203924/ref=sr_1_1?keywords=popper+la+logica+della+scoperta+scientifica&qid=1646999719&sprefix=popper+la+logica%2Caps%2C85&sr=8-1). We know that ideas on what a phenomenon is (or hypothesis) should be *invented* and **not** defined by observing the phenomenon. 
> "[…] and I think (like you, by the way) that theory cannot be fabricated out of the results of observation, but that it can only be invented." Albert Einstein writing to Karl Popper.

So, cybersecurity cannot be understood out of the results of observation but, in this course, we are going to understand cybersecurity out of the results of observation anyway! Why? Because how could we even conceive to ask ourselves "what is cybersecurity?" if we didn't stumble upon some "observation" or some situation in which cyber-insecurity was evident?

### Ok, WAT?
For us cybersecurity is the [CIA-triad](https://en.wikipedia.org/wiki/Information_security) (Confidentiality, Integrity, Availability), meaning that any system in which the CIA-triad holds is (for us) secure (enough). For simplicity, suppose a component of a system (e.g., a web-server) is talking to you (e.g., to your browser) by sending you some *messages*.

* Confidentiality holds if only the trusted peers (e.g., the web-server and your browser) can *understand* the content of the messages. Of course, it would be "more confidential" if not even the very peers of a conversation would be able to understand the content of the messages... but it would be pretty useless :)
* Integrity holds when the trusted parties can understand if the message has been corrupted (accidentally) or altered (e.g., maliciously by an attacker).
* Availability holds when we are able to understand if a service (e.g., the web-server or a web-site) is "down" or not available.

#### Did you say attacker?
An *attacker* is what is usually, mistakenly called hacker. In this course we want to learn how to protect our system from a malicious cracker, someone who mainly wants to break the CIA triad and we call him/her attacker.
An *hacker*, instead, is "a person who delights in having an intimate understanding of the internal workings of a system, computers and computer networks in particular. The term is often misused in a pejorative context, where cracker would be the correct term". [RFC-1392](https://tools.ietf.org/html/rfc1392).

#### How do we guarantee the CIA-triad holds in a system?
Using the so-called [Alice-and-Bob notation](https://en.wikipedia.org/wiki/Security_protocol_notation) where Alice (A) and Bob (B) are honest and Eve (E) is the malicious attacker, let us suppose that Alice wants to send "ciao bob" to Bob.

To preserve confidentiality, Alice can agree with Bob upon using a specific transformation over each message. Let's say, they will substitute each letter in the message by a letter at some fixed number of positions (which we call `k`) down the alphabet (aka [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher)). So, the message "ciao bob" is transformed into "dlbp cpc" if `k=1` and `A->B:dlbp cpc` will only be understood from Bob (since he's the only one who knows how to translate the message back into its meaning - and we assume, for simplicity, that Eve is not so clever to figure out we are doing this "trick").

MUHAHAHAHA! This does not preserve confidentiality as soon as I employ a [frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis).
Long story short, letters in a sentence are bound to be used with a fixed frequency (which may vary from language to language). In English we have the following frequencies

![](./English_letter_frequency.png)

and if we see a message like "dlbp cpc" we may *not* know how to decipher it but what if listened to a whole conversation?
Let's try! Go to: [cryptii/Caesar cipher](https://cryptii.com/pipes/caesar-cipher) and encode a message (e.g. in Italian).
My message encoded was:
Jphv Ivi, zvuv Thyjv. Cvslcv zvsv kpyap jol xbhukv buv zwvzah buh ivyzh, sh ivyzh zp zwvzah wlyjoé buv sh zwvzah l uvu ps jvuayhypv. Xbpukp uvu wvzzphtv kpyl jol buv zwvzah buh ivyzh wlyjoé sh ivyzh zp zwvzah th zvsv jol sh ivyzh zp zwvzah wlyjoé xbhsjbuv sh zwvzah. Ps wypujpwpv jhbzhsl è jvzh zlyph l s'ptwspjhgpvul mbugpvuh pu bu clyzv th uvu uljlzzhyphtlual hujol ulss'hsayv.

We can surely go to some tools like [this](https://www.dcode.fr/frequency-analysis) and analyze the frequency and quite easily decrypt the message.
We can also try all possible decryption with tools such as [md5decrypt.net](https://md5decrypt.net/en/Caesar/) and, by clicking on "bruteforce" you will easily spot what I wanted to say.

- How can we guarantee integrity or availability? We'll look into this in the following lessons.

# Penetration Testing
* Why? Penetration Testing and the Engineering Model
* White/Black/box Penetration testing Phases
* Terminology. Threat (weak password), Vulnerability (password guessing), Attack (dictionary), Exploit (implementation)

The process of penetration testing may be simplified into the following five phases (see [Wiki](https://en.wikipedia.org/wiki/Penetration_test)]:
1. Reconnaissance: The act of gathering important information on a target system. This information can be used to better attack the target. For example, open source search engines can be used to find data that can be used in a social engineering attack.
2. Scanning & Vulnerability Assessment: Uses technical tools to further the attacker's knowledge of the system. For example, Nmap can be used to scan for open ports.
3. Exploitation: Using the data gathered in the reconnaissance and scanning phases, the attacker can use a payload to exploit the targeted system. For example, Metasploit can be used to automate attacks on known vulnerabilities.
5. Reporting: Once the exploitation phase is complete, the tester prepares a report documenting the penetration test's findings. The report generated in this final penetration testing phase can be used to fix any vulnerabilities found in the system and improve the organization's security posture.

### Do you speak techy?
0. have a decent computer (we can give you one if your is "old" or "tired")
1. Install a virtual machine (e.g. [VirtualBox](https://www.virtualbox.org/) with [Ubuntu 20.04](https://ubuntu.com/download/desktop/thank-you?version=20.04.4&architecture=amd64) - Why? Because you don't want to "try" something on your computer. You are going to make a mess (we are explorers! and sometimes wanderers) and you don't like re-installing the OS on your computer.
   1. A [Virtual Machines](https://www.virtualbox.org/manual/ch01.html) (VM) is a *software* virtualization of a computer. You create a new "virtual computer" inside your real computer. So you can trash the virtual computer if you mess up and your real computer won't even notice.
   2. You can take a [snapshot](https://www.virtualbox.org/manual/ch01.html) of a VM and you can go back to that snapshot (e.g., if you mess up). So, take a snapshot right after having installed Ubuntu and you can go back to a clean Ubuntu installation whenever you want.
2. Install [PostgreSQL](https://www.postgresql.org/) on the VM.
   1. `sudo apt update` updates the links from which Ubuntu will search for software
   2. `sudo apt install postgresql` will install the latest version of PostgreSQL supported by the OS (on Ubuntu 20.04 is v12)
   3. `sudo systemctl status postgresql` you can check the status of the PostgreSQL process (it should be active and running)
   4. `sudo systemctl stop postgresql` you stop the PostgreSQL process (guess what happens substituting start or restart to stop)

