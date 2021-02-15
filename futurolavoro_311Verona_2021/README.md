## About this course

- Title: Mini-course on Secure Webapp Engineering
- Lecturers: Marco Rocchetto (marco@v-research.it)
- Students: Futurolavoro (@311Verona)
- When: February 2021
- Slides: [pdf](./futurolavoro_slides.pdf), [odp](./futurolavoro_slides.odp)

## Learning Outcomes
This mini-course gives an overview on the concepts of **confidentiality**, **integrity**, and **authentication**; along with a short introduction to **cryptography** (both symmetric and asymmetric), **hashing**, and **encoding**. Those concepts will then be implemented to guarantee the security of data (at-rest and in-transit) of an ad-hoc web application. Finally, we will study and implement state-of-the-art password policies.

## Agenda
0. *An introduction to Cybersecurity* [theory]
	- #whoami
	- weakness (CWE), vulnerability (CVE), and Attacks
	- CIA-triad and authentication
	- information security, at-rest and in-transit
	- challenge **C1: authentication and trust**
1. *Secure Design 1* [lab]
	- challenge **C2: which property (confidentiality, integrity, authentication) and requirement shall hold in which part of your app?**
	- focus first on user registration and login
	- testing/showing the obvious insecurities
2. *Security Procedures* [theory]
	- ~Steganography and~ Encoding
	- Cryptographic Hash Functions
	- challenge **C3: how do we use hash functions?**
	- Symmetric and Asymmetric Encryption (and Signing)
3. *Secure Design 2* [lab]
	- **challenge C3: propose techniques to preserve security properties**
4. *Security Algorithms* [theory]
	- openssl\_encrypt
	- openssl_public\_encrypt (RSA)
4. *Secure Coding* [lab]
	- implement requirements
5. *Security Testing* [theory]
	- hashing passwords without salting?
	- is there a known vulnerability in the algorithm you chose? (cve.mitre.org)
	- no password policies?
	- decrypt with lookup tables & brute force passwords after a db leak (john the ripper)
	- ~is there a flaw in the logic of your authentication process?~
6. *Security Mitigations* [theory]
	- salting, peppering, and password policies
7. *After-school*
	- use an external identity service provider (Google/Facebook)
	- Use strong authentication (2FA, telegram bot)
	- Availabilty & Denial of Service
	- implement a "I'm not a bot"
	- Accountability & OCSP (Online Certificate Status Protocol)

### Resources
- [AGID Security Guidelines (ITA)](https://www.agid.gov.it/sites/default/files/repository_files/allegato_4_-_linee_guida_per_la_modellazione_delle_minacce-dlt.pdf)
- [AGID TLS & Ciphersuite (ITA)](https://www.agid.gov.it/it/sicurezza/tls-e-cipher-suite)
