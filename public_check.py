import os
import subprocess
import platform

QUESTIONS = ["Q1_LogicGates", "Q2_WPattern", "Q3_StudentSearch", "Q4_RoundRobin", "Q5_TowerOFHanoi"]
IS_WINDOWS = platform.system() == "Windows"
PYTHON_CMD = "python" if IS_WINDOWS else "python3"

# Only the visible Sample Test Cases
TESTS = {
    "Q1_LogicGates": [("0 0", "BUFFER: 0\nNOT: 1\nAND: 0\nOR: 0\nNAND: 1\nNOR: 1\nXOR: 0\nXNOR: 1"), 
           ("1 0", "BUFFER: 1\nNOT: 0\nAND: 0\nOR: 1\nNAND: 1\nNOR: 0\nXOR: 1\nXNOR: 0")],
    "Q2_WPattern": [("2", "* * *\n * *"), ("3", "* * *\n * * * *\n  * *")],
    "Q3_StudentSearch": [("5\n5 4 3 2 1\n3", "1 2 3 4 5\n2"), ("4\n10 20 30 40\n50", "10 20 30 40\n-1")],
    "Q4_RoundRobin": [("3\n10 5 8\n2", "61"), ("2\n4 4\n2", "12")],
    "Q5_TowerOFHanoi": [("3", "Total Moves: 7\nFirst move of Disk 1: 1"), ("4", "Total Moves: 15\nFirst move of Disk 1: 1")]
}

def run_test(cmd, stdin_data):
    try:
        res = subprocess.run(cmd, input=stdin_data, text=True, capture_output=True, timeout=2)
        return res.stdout.strip()
    except subprocess.TimeoutExpired:
        return "TIMEOUT"

for q in QUESTIONS:
    c_path = f"{q}_solution.c"
    py_path = f"{q}_solution.py"
    
    if os.path.exists(c_path):
        exec_name = f"{q}_exec.exe" if IS_WINDOWS else f"{q}_exec"
        subprocess.run(["gcc", c_path, "-o", exec_name])
        cmd = [f"{exec_name}"] if IS_WINDOWS else [f"./{exec_name}"]
    elif os.path.exists(py_path):
        cmd = [PYTHON_CMD, py_path]
    else:
        print(f"[{q}] No code found.")
        continue

    passed = 0
    for i, (inp, exp) in enumerate(TESTS[q]):
        out = run_test(cmd, inp)
        if out == exp:
            passed += 1
    print(f"[{q}] Sample Tests Passed: {passed}/2")
