# 🛠️ Debugging Hackathon: Crack the Code!

Welcome to the Debugging Hackathon! You have been provided with 5 faulty programs. Your task is to find the bugs (Logical, Runtime, or Syntax errors) and fix them.

## 🚨 Hackathon Rules (READ CAREFULLY)
1. **Language Lock:** You must choose **EITHER** C or Python 3, and use it for **ALL 5** questions. Mixing languages will result in an automatic 0.
2. **No Library Cheating:** Do not import external libraries to bypass the logic (e.g., `import math` in Python or `<stdlib.h>` in C, unless already provided).
3. **Hardcoding is Banned:** Using `if/else` blocks to simply print the exact sample outputs will be caught by our hidden test cases.
4. **Grading:** Each question is worth 50 marks (10 marks per sample test, 10 marks per hidden test). 

---

### Q1: Logic Gate Simulation
**The Concept:** Logic gates take binary inputs (0 or 1) and output a result based on simple rules (e.g., AND requires both inputs to be 1; OR requires at least one input to be 1).

**The Problem:** The code takes two binary inputs (A and B) and should evaluate them through 8 standard logic gates: Buffer (just A), NOT (opposite of A), AND, OR, NAND (opposite of AND), NOR (opposite of OR), XOR (1 if inputs are different), and XNOR (1 if inputs are the same).

* **Constraints:** Inputs A and B will only be `0` or `1`.
* **Input:** Two space-separated integers.
* **Output:** 8 lines showing the gate name and the result.

**Sample Input 1:**
```text
0 0
```
**Sample Output 1:**
```text
BUFFER: 0
NOT: 1
AND: 0
OR: 0
NAND: 1
NOR: 1
XOR: 0
XNOR: 1
```

---

### Q2: "W" Pattern Printing
**The Problem:** The code should print a visual "W" shape made of asterisks (`*`) and spaces. The height of the pattern is N, and the width is calculated as `4 * N - 3`.

* **Constraints:** 2 <= N <= 20
* **Input:** A single integer N.

**Sample Input 1:**
```text
3
```
**Sample Output 1:**
```text
*   *   *
 * * * *
  *   *
```

---

### Q3: University Student Searching
**The Problem:** You are given a list of student ID numbers. The code needs to sort these IDs from lowest to highest, and then use a "Binary Search" (cutting the list in half repeatedly) to find the exact position of a specific Target ID.

* **Constraints:** 1 <= N <= 10,000.
* **Input:** * Line 1: N (number of students)
  * Line 2: N space-separated IDs
  * Line 3: The Target ID to find
* **Output:** * Line 1: The sorted list of IDs.
  * Line 2: The index (position) of the target in the sorted list, starting from 0. (Print -1 if not found).

**Sample Input 1:**
```text
5
5 4 3 2 1
3
```
**Sample Output 1:**
```text
1 2 3 4 5
2
```

---

### Q4: Round-Robin Task Scheduling
**The Concept:** Imagine 3 people waiting to play a video game, but you only let them play for exactly 2 minutes at a time before forcing them to pass the controller to the next person in a circle. They keep passing the controller around until everyone has finished their game.

**The Problem:** Calculate the "Total Turnaround Time". A single task's turnaround time is the exact minute on the clock when that specific task is 100% completed. We need the sum of these finish times for all tasks combined.

* **Constraints:** 1 <= N <= 1000.
* **Input:** * Line 1: N (number of tasks)
  * Line 2: The total minutes each task requires to finish (space-separated)
  * Line 3: Q (The maximum minutes allowed per turn)
* **Output:** A single integer representing the sum of all completion times.

**Sample Input 1:**
```text
3
10 5 8
2
```
**Sample Output 1:**
```text
59
```

---

### Q5: Tower of Hanoi Analytics
**The Concept:** Tower of Hanoi is a famous puzzle where you move a stack of N disks from one peg to another without ever putting a larger disk on top of a smaller one. 

**The Problem:** You do *not* need to simulate the puzzle. You just need to fix the math! The mathematical formula for the minimum total moves required is `(2 to the power of N) - 1`. Also, the very first move of the game is *always* moving Disk 1.

* **Constraints:** 1 <= N <= 30.
* **Input:** A single integer N.
* **Output:** Two lines of text showing the total moves and the first disk moved.

**Sample Input 1:**
```text
3
```
**Sample Output 1:**
```text
Total Moves: 7
First move of Disk 1: 1
```
