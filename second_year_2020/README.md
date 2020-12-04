## About this course

- Title: Introduction to Web Cybersecurity
- Lecturers: Marco Rocchetto (marco@v-research.it) & Mattia Pacchin (mattia@v-research.it)
- Students: ITS 2nd year (@311Verona)
- When: December 2020 
- Office hours: you can always drop us an email or just pass by our office (311Verona, 2nd floor, door on the left with "V-Research" printed on it) to talk about cybersecurity (or "the ultimate question of life, the Universe, and everything") but we'll be online at [this virtual room](https://teams.microsoft.com/l/meetup-join/19%3ameeting_NmYxMzYzOGYtYWUxZi00OGI5LWI1NzYtZWFiZGIzZmVjNjM4%40thread.v2/0?context=%7b%22Tid%22%3a%22210f6a61-e517-4752-a4f1-ba8e00e939f2%22%2c%22Oid%22%3a%2218e4ff36-8bbb-44e3-8611-2af7dbb48ef0%22%7d) (via MS Teams) every Friday (4/11/18/25-December-2020 9.00-11.00) where you can just join and ask us some questions.

## Learning Outcomes
This course provides an overview on the problems and challenges related to software security in the context of Web applications, focusing on the main current solutions (namely, testing techniques). The student will familiarize with general cybersecurity principles (such as cryptography and security properties as confidentiality, integrity, and availability) and with the main cybersecurity issues in the Web (such as the OWASP top 10 web app security risks, and the main knowledge bases such as the CWE, CVE, NVD, CAPEC). The student will be asked to critically analyze the security of Web applications and ultimately to provide evidences of cyber-insecurities in Web applications (using learning platforms such as the OWASP Juice Shop). Alongside the "hacking her way to cybersecurity" approach, the student will be made aware of the current unfalsifiability of necessary security claims, and subsequent lack of clear understanding of what a cybersecure web application should look like.

No specific skill is required but the basic understanding of programming is presupposed. 
Within the course, an introduction to the basic concepts of HTML, JavaScript, SQL will be provided.

## Course Material
### Learning Platforms
- [OWASP WebGoat](https://owasp.org/www-project-webgoat/) as the reference learning platform
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) as a "playground" where the students will test their cybersecurity skills and understanding
- [XSS Game](https://xss-game.appspot.com/) as a "playground" for testing XSS skills
- [Hacker101 CTF](https://ctf.hacker101.com/) as a first step towards CTFs
### Main Testing Tools Presented in the Course
- [ZAP](https://www.zaproxy.org/)
- [SQL-map](http://sqlmap.org/)

## Lessons
### [L0. 02-December-2020](./lesson_0) (Wednesday) [9.15-13.15]
0. *An introduction to Cybersecurity* [theory 1h]
    - #whoami & course overview
    - Beliefs on Cybersecurity
    - Infosec and the CIA-triad evolution (1970-today)
    - Attacker vs Hacker, Blue and Red Teams, ...
    - Hacker Ethics and Laws against Attackers
    - Cybersecurity Resources: CVE, CWE, CAPEC, WASC, NVD
    - Cybersecurity Resources: OWASP, DEFCON, PHRAK, IEEE S&P 
1. *Brainstorming session - what is a cybersecure web app?* [lab 1h] 
    - Students
      - (if) working individually, propose up to 10 keywords related to cybersecurity [15m]
      - (elif) working in group, propose (duckduckgo is your friend) a definition of cybersecurity (in the context of web apps) [30m]
    - Proposals Review & Open Discussion [45/30m]
2. Coffee break [10m]
3. *Hacking the HTTP* [theory 30m + lab 1h30m]
    - The WebGoat platform [15m]
    - The HTTP protocol and the Client-Server architecture [15m]
    - Webgoat lesson (General->HTTPBasic) [1h30m]
      - ZAP HUD Tutorial
 
### [L1. 09-December-2020](./lesson_1) (Wednesday) [9.15-13.15]
0. *Cybersecurity Topic #1 - SQL-injection*  [theory 30m + lab 2h]
    - Intro to Databases and DBMS [15m]
    - Introduction to [SQLmap with examples](https://www.youtube.com/user/inquisb/videos) [15m]
    - WebGoat lesson (A1 - Injection, path traversal excluded) [2h]
1. Coffee break [10m] 
2. Open Discussion [30m]
3. *Cybersecurity Topic #2 - Path Traversal* [lab 30m]
    - WebGoat lesson (A1 - Injection -> Path Traversal) [30m]

### [L2. 14-December-2020](./lesson_2) (Wednesday) [9.15-13.15]
0. *Intro to JavaScript & HTML* [30m]
1. *Cybersecurity Topic #3 - XSS*
    - XSS short intro [15m]
    - WebGoat exercises [1h]
2. Cofee break [10m]
3. *[XSS Game](https://xss-game.appspot.com/)* [1h30m]

### [L3. 16-December-2020](./lesson_3) (Monday) [9.15-13.15]
0. *Crypto Overview & Integrity Deep Dive* [1h30m]
    - Steganography, Encryption & Decryption
    - Symmetric and Asymmetric Encryption
    - Overview of Major Cryptographic Algorithms (RSA, AES, ...)
    - Attacks on Protocol Logic (man-in-the-middle, reflection, ...)
    - Authenticated Key Agreement
    - Trust, authentication, non-repudiation
    - Are quantum channels & protocols of any help?
1. Coffee break [10m]
2. *Cybersecurity Topic #4 - CSRF*
    - WebGoat lesson (A8:2013 Request Forgery) [1h]
3. *Cybersecurity Topic #5 - Broken Authentication*
    - WebGoat exercises [1h]

### [L4. 21-December-2020](./lesson_4) (Wednesday) [9.15-13.15]
0. *[OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)* [2h50m]
1. Coffee break [10m]
2. *Results Review & Discussion* [1h]

### Extra
0. *CTF & Bug Bounty Programs*
1. *[Hacker101 CTF](https://ctf.hacker101.com/)* [3h]
2. *Open Discussion* [1h]
