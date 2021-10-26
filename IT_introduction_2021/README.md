## About this course

- Title: Introduction to IT
- Lecturers: Marco Rocchetto (marco@v-research.it) & Mattia Pacchin (mattia@v-research.it)
- Students: ITS 1st year (@311Verona)
- When: October 2021 
- Office hours: you can always drop us an email to schedule a 1 on 1 meeting.

## Learning Outcomes
This course provides an overview on the problems and challenges related to the foundations of programming. We'll discuss basic concepts such as the concept of algorithm and programs, how the computers work, how to program in C, and the relation between C and Assembly. 

### Textbook
jon Erickson, Hacking: The Art of Exploitation (2nd edition)... it is a great book but we'll only focus on chapter 0x200

## Lessons
### L0. 21-October-2021 (Thursday) [14.00-18.00]
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
- Exercises ([pdf](material/first_exercises.pdf))
- Ubuntu terminal instruction ([pdf](material/terminal_instruction.pdf))
- C notes ([pdf](material/Appunti_teoria_C.pdf))
- firstprog.c ([c](material/draft/firstprog.c))

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
