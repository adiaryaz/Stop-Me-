# Stop-Me!

A mysterious looping program where the final output is the factorial of the input count until 'stop' is entered.

## 📝 Description

This is a mysterious app that continues to run until you provide the magic word: "stop". For every input given, the application prints "RUN" and increases a counter. When "stop" is entered, it calculates the factorial of the counter to produce a final "Total runs" value.

The core mathematical principle is the factorial, where the total is the result of n! (n being the number of times "RUN" was printed).

## 🎯 Problem Statement

**Input:** 
- The program will repeatedly ask for a string input from the user.

**Output:** 
- The program will print "RUN" for every input that is not "stop".

- When the user inputs "stop" (case-insensitive), the program will cease looping and display the total result based on the factorial of the run count.

**Rules:**
- The loop terminates only when the input is "stop".
- The final calculation is (number of RUNs)!.
- The comparison for "stop" is case-insensitive.

## 💡 Examples

### Example 1
```
Input:
apple
stop

Output:
RUN
Total 1 runs
```
Explanation: 1 input before "stop", so 1! = 1

### Example 2
```
Input:
apple
grape
snakefruit
stop

Output:
RUN
RUN
RUN
Total 6 runs
```
Explanation: 3 inputs before "stop", so 3! = 6

### Example 3
```
Input:
apple
mango
grape
snakefruit
melon
stop

Output:
RUN
RUN
RUN
RUN
RUN
Total 120 runs
```
Explanation: 5 inputs before "stop", so 5! = 120

### Example 4
```
Input:
APPLE
MaNGO
StOP

Output:
RUN
RUN
Total 2 runs
```
Explanation: 2 inputs before "StOP", so 2! = 2

## 🚀 How to Use

1. Clone this repository
```bash
git clone https://github.com/adiaryaz/stop-me.git
cd calculate-circle-area
```

2. Run the program
```bash
python stop_me.py
```

3. Enter any word to continue the loop or type stop to end it.
