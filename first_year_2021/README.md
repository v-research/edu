## About this course

- Title: Introduction to Web Cybersecurity
- Lecturers: Marco Rocchetto (marco@v-research.it) & Mattia Pacchin (mattia@v-research.it)
- Students: ITS 1nd year (@311Verona)
- When: January-February 2021
- Office hours: you can always drop us an email to schedule a 1 on 1 meeting. 

## Learning Outcomes
This course provides an overview on the problems and challenges related to
software security in the context of Web applications, focusing on the main
current solutions (namely, testing techniques). The student will familiarize
with general cybersecurity principles (such as cryptography and security
properties as confidentiality, integrity, and availability) and with the main
cybersecurity issues in the Web (such as the OWASP top 10 web app security
risks, and the main knowledge bases such as the CWE, CVE, NVD, CAPEC). The
student will be asked to critically analyze the security of Web applications
and ultimately to provide evidences of cyber-insecurities in Web applications
(using learning platforms such as the OWASP Juice Shop). Alongside the "hacking
her way to cybersecurity" approach, the student will be made aware of the
current unfalsifiability of necessary security claims, and subsequent lack of
clear understanding of what a cybersecure web application should look like.

No specific skill is required but the basic understanding of programming is presupposed. 
Within the course, an introduction to the basic concepts of HTML, JavaScript, SQL will be provided.

## Course Material

### Learning Platforms
- [OWASP WebGoat](https://owasp.org/www-project-webgoat/) as the reference learning platform
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) as a "playground" where the students will test their cybersecurity skills and understanding
- [XSS Game](https://xss-game.appspot.com/) as a "playground" for testing XSS skills

### Software Used in the Course
- [ZAP](https://www.zaproxy.org/)

## Lessons

### L0. 19-January-2021 (Tuesday) [14.00-18.00]
0. *An introduction to Cybersecurity* [theory 1h]
    - #whoami & course overview
    - Beliefs on Cybersecurity
    - Infosec and the CIA-triad evolution (1970-today)
    - Attacker vs Hacker, Blue and Red Teams, ...
    - Hacker Ethics and Laws against Attackers
    - Cybersecurity Resources: CVE, CWE, CAPEC, WASC, NVD
    - Cybersecurity Resources: OWASP, DEFCON, PHRAK, IEEE S&P 
1. Coffee break [10m]
2. *Lab Configuration* [lab 1h] 
3. *Hacking the HTTP* [theory 30m + lab 1h30m]
    - The WebGoat platform [15m]
    - The HTTP protocol and the Client-Server architecture [15m]
    - Webgoat lesson (General->HTTPBasic) [1h30m]
      - ZAP HUD Tutorial [OPTIONAL]

##### Lesson 0 - Material
- Slide ([pdf](lesson_0/l0_slide.pdf), [odp](lesson_0/l0_slide.odp))
- WebGoat & ZAP [installation](lesson_0/webgoat_zap_installation.odt)
 

### L1. 26-January-2021 (Tuesday) [14.00-18.00]
0. *Cybersecurity Topic #1 - SQL-injection*  [theory 30m + lab 2h]
    - Intro to Databases and DBMS [15m]
    - WebGoat lesson (A1 - Injection, path traversal excluded) [2h]
1. Coffee break [10m] 
2. Open Discussion [30m]

##### Lesson 1 - Material
- Slide ([pdf](lesson_1/l1_slide.pdf), [odp]( lesson_1/l1_slide.odp))


### L2. 1-February-2021 (Monday) [14.00-18.00]
0. *Intro to JavaScript & HTML* [30m]
1. *Cybersecurity Topic #3 - XSS*
    - XSS short intro [15m]
    - WebGoat exercises (A7 - Cross-site Scripting) [1h]
2. Cofee break [10m]
3. *[XSS Game](https://xss-game.appspot.com/)* [1h30m]

##### Lesson 2 - Material
- Slide ([pdf](lesson_2/l2_slide.pdf), [odp]( lesson_2/l2_slide.odp))


### L3. 9-February-2021 (Tuesday) [14.00-18.00]
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

##### Lesson 3 - Material
- Slide ([pdf](lesson_3/l3_slide.pdf), [odp]( lesson_3/l3_slide.odp))


### L4. 16-February-2021 (Tuesday) [14.00-18.00]
0. *[OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)* [2h50m]
1. Coffee break [10m]
2. *Results Review & Discussion* [1h]

##### Lesson 4 - Material
- Slide ([pdf](lesson_4/l4_slide.pdf), [odp]( lesson_4/l4_slide.odp))
