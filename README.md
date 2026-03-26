# 🛠️ Debugging Hackathon: Crack the Code!

Welcome to the Debugging Hackathon! You have been provided with 5 faulty programs. Your task is to find the bugs (Logical, Runtime, or Syntax errors) and fix them.

## 🚨 Hackathon Rules (READ CAREFULLY)
1. **Language Lock:** You must choose **EITHER** C or Python 3, and use it for **ALL 5** questions. Mixing languages will result in an automatic 0.
2. **No Library Cheating:** Do not import external libraries to bypass the logic. We have strict anti-import checkers. (e.g., `import math` or `itertools` in Python, or `<stdlib.h>` bypasses in C are forbidden unless already provided).
3. **Hardcoding is Banned:** Using `if/else` blocks to simply print the sample outputs will be caught by our 3 hidden test cases per question.
4. **Grading:** Each question is worth 50 marks (10 marks per sample test, 10 marks per hidden test). 

---

### Q1: Logic Gate Simulation
**Problem:** The code should take two binary inputs (A and B) and evaluate them through a Buffer (A), NOT (A), AND, OR, NAND, NOR, XOR, and XNOR gate.
* **Constraints:** Inputs A and B will only be `0` or `1`.
* **Input:** Two space-separated integers.
* **Output:** 8 lines showing the gate name and the result.
* **Sample 1:** Input: `0 0` | Output: `BUFFER: 0`, `NOT: 1`, `AND: 0`, `OR: 0`, `NAND: 1`, `NOR: 1`, `XOR: 0`, `XNOR: 1`
* **Sample 2:** Input: `1 0` | Output: `BUFFER: 1`, `NOT: 0`, `AND: 0`, `OR: 1`, `NAND: 1`, `NOR: 0`, `XOR: 1`, `XNOR: 0`

### Q2: "W" Pattern Printing
**Problem:** The code should print a W-shaped asterisk pattern of height N and width 4N-3.
* **Constraints:** 2 <= N <= 20
* **Input:** A single integer N.
* **Output:** The pattern using `*` and spaces.
* **Sample 1:** Input: `2` 
    * Output: 
        ```text
        * * *
         * * 

### Q3: University Student Searching
**Problem:** The code takes an array of student IDs, sorts them in ascending order, and uses Binary Search to find a target ID.
* **Constraints:** 1 <= N <= 10^4.
* **Input:** N (number of students), followed by N space-separated IDs, followed by the Target ID.
* **Output:** Line 1: The sorted array. Line 2: The index of the target (or -1 if not found).
* **Sample 1:** Input: `5 5 4 3 2 1 3` | Output: `1 2 3 4 5 2`

### Q4: Round-Robin CPU Scheduling
**Problem:** Simulate a Round-Robin CPU scheduler and output the total turnaround time of all processes combined.
* **Constraints:** 1 <= N <= 1000.
* **Input:** N (number of processes), followed by N burst times, followed by the time quantum Q.
* **Output:** A single integer (Total turnaround time).
* **Sample 1:** Input: `3 \n 10 5 8 \n 2` | Output: `61`

### Q5: Tower of Hanoi Analytics
**Problem:** Mathematically compute the total number of moves for N disks, and print the disk moved on the first step.
* **Constraints:** 1 <= N <= 30.
* **Input:** A single integer N.
* **Output:** "Total Moves: <M>" and "First move of Disk 1: <D>".
* **Sample 1:** Input: `3` | Output: `Total Moves: 7 \n First move of Disk 1: 1`
