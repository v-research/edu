## About this course
- Title: Security Engineering in Practice
- Lecturers: Marco Rocchetto (marco@v-research.it) & Mattia Pacchin (mattia@v-research.it)
- Students: ITS 2nd year (@311Verona)
- When: November 2021 - February 2022
- Office hours: you can always drop us an email to schedule a 1 on 1 meeting.

## Learning Outcomes
In this course the students will be divided in groups and they will develop a cybersecure login following an engineering process.
Then they will try to attack other group's login system and they will understand the weaknesses.  
Shortly: **the students become hackers!**

# Welcome to the Club of the Practical Men,
[those who live their lives and then think about it](https://www.knowledgezero.com/finding-cybersecure)

From the RFC 1392, an **hacker** is
>a person who delights in having an intimate understanding of the
>internal workings of a system, computers and computer networks in
>particular.  The term is often misused in a pejorative context,
>where "cracker" would be the correct term.

## The Im-practical Society
In the world there are 3 types of people: 
* (Un)Practical men, like you
* Captains, who created this game and will help you and defend you from
* Pirates, who will attack your solutions

## There are 3 types of Practical Men:
* *Scientist*, the real science expert. His strong point is the theory, he really loves to study and his job is to detail the problem statement, to define the requirements and justify them.
* *Engineer*, he knows how to make it work. He makes an use case analysis, then an activity diagram and finally he describes the implementation. 
* *Programmer*, the one who translates the theory into practice. First of all, he has to setup a development environment which easily allows to his team to collaborate in an efficient way, so he starts to code together with the scientist and the engineer.

## Lessons
### L0. 26-November-2021 (Friday) [9.00-13.00]
1. *Q&A* [30m]
    - #whoami & course overview
    - Q&A
	- What is a computer?
	- What is a number?
	- What is an algorithm?
	- What is programming?
2. *Intro to programming* [1h30m]
	- Explanation from page 5 to 19 (stop before book section 0x250)
	- Linux WSL and ubuntu installation, VSCode useful extensions
3. Coffee break [10m]
4. *Excercises* [1h50m]
  - First C program -> explanation of book example
	- First exercise in C
	- Some more exercises
	- Induction (if (time>0))

##### Lesson 0 - Resources
- Slide ([pdf](material/introduction.pdf))
- GitHub SSH key generation guide ([link](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent))

### L1. 22-October-2021 (Friday) [14.00-18.00]
1. *ASM intro* [30m]
    - x86 processor (book section 0x252)
    - GDB basics
	- Breakpoint
    - Registers info
2. *ASM language* [1h]
	- Disassembly
	- Registers
	- Inspect program (ASM vs C, registers and gdb)
3. Coffee break [10m]
4. *Exercises* [2h20m]
	- Do it with your arch. What does it change? (32bit vs 64bit)

### L2. 26-October-2021 (Tuesday) [14.00-18.00]
0. [README](material/ex1_solutions.txt): instructions on how to inspect code with gdb
1. Ex. 1: use gdb to inspect code ([ex1.c](material/raw_var.c))
2. Ex. 2: use gdb to inspect code with ASCII ([ex2.c](material/raw_hello.c))
3. DYI: Can you inspect the code in ([firstprog.c](material/draft/firstprog.c))
2. Coffee break [10m]
3. *Exercises* [1h]
	- super secret club ex. ([file.c](material/supersecretclub.c))

### L3. 26-October-2021 (Monday) [14.00-18.00]
1. *C basics* [4h]
	- String
	- Array
	- Types
	- Pointers
	- Format strings
	- Command line
	- Variable scoping
2. Coffee break [10m]
	- Basic exercises 
		- ([es1.c](material/basic_exercises/es1.c))
		- ([es2.c](material/basic_exercises/es2.c))
		- ([es3.c](material/basic_exercises/es3.c))
		- ([es4.c](material/basic_exercises/es4.c))
		- ([es5.c](material/basic_exercises/es5.c))
		- ([es6.c](material/basic_exercises/es6.c))
		- ([numeroPrimo.c](material/basic_exercises/numeroPrimo.c))
		- ([randint.c](material/basic_exercises/randint.c))
	- Some more exercises ([pdf](material/other_exercises.pdf))

### L4. 27-October-2021 (Wednesday) [14.00-18.00]
1. *Exercises* [4h]
	- isolaDeserta.c
2. Coffee break [10m]

##### Lesson 4 - Resources
- Exercises ([pdf](material/last_exercises.pdf))
- isolaDeserta.c ([c](material/draft/isolaDeserta.c))
