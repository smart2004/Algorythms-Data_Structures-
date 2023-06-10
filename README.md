# algorythms-data_structures- by smart200481 <Mikhail Sutormin>

## deque.py  
### Brief Task Description

Gosh implemented the Dec data structure, the maximum size of which is determined by a given number. Methods push_back(x), push_front(x), pop_back(), pop_front() worked correctly. But, if there were many elements in the deck, the program worked for a very long time. The fact is that not all operations were performed in O(1). Help Gosh! Write an efficient implementation.

###### Attention: when implementing, use a ring buffer.

### Input Format
  
The first line contains the number of commands n — an integer not exceeding 100000. 
The second line contains the number m — the maximum deque size. It does not exceed 50000. 
The next n lines contain one of the commands:
```
push_back(value) - add an element to the end of the deque. If the deque already contains the maximum number of elements, print "error".
push_front(value) - add an element to the front of the deque. If the deque already contains the maximum number of elements, print "error".
pop_front() - Display the first element of the deque and remove it. If deque was empty, print "error".
pop_back() - print the last element of the deque and remove it. If deque was empty, print "error".
```
Value is an integer, modulo not exceeding 1000.

### Output Format
  
Print the result of each command on a separate line. No output is required for successful push_back(x) and push_front(x) requests.


### How to launch the project:
  
##### Clone repository:

```
git clone git@github.com:smart2004/Algorythms-Data_Structures-.git
```

##### Switch to the folder:

```
cd algorythms-data_structures-
```

##### Launch python task:

```
python deque.py
```
###### NOTE: better use IDE and start task @ the place
  
##### Example for input:
```
8
11
push_front -860
push_front 29
pop_back
pop_back
push_back 850
pop_back
pop_back
pop_front
```
  
##### Example for output:
```
-860
29
850
error
error
```
  

## polski_note.py
### Brief Task Description

The task is related to reverse Polish notation. It is used to parse arithmetic expressions. It is also sometimes called postfix notation.

In postfix notation, the operands are placed before the operator signs.

Example 1:
```
3 4 +
means 3 + 4 and equals 7
```
Example 2:
```
12 5 /
Since the division is integer, the result is 2.
```
Example 3:
```
10 2 4 * -
means 10 - 2 * 4 and equals 2
```
Let's take a closer look at the last example:

The * sign is immediately after the numbers 2 and 4, which means that you need to apply the operation that this sign denotes to them, that is, multiply these two numbers. As a result, we get 8.

After that, the expression will take the form:
```
10 8 -
```
The minus operation must be applied to the two numbers preceding it, that is, 10 and 8. As a result, we get 2.

Let's consider the algorithm in more detail. To implement it, we will use the stack.

To calculate the value of an expression written in reverse Polish notation, you need to read the expression from left to right and follow these steps:

Input character processing:
If an operand is given as input, it is pushed onto the top of the stack.
If an operation sign is given to the input, then this operation is performed on the required number of values taken from the stack in the order of addition. The result of the performed operation is placed on the top of the stack.
If the input character set is not fully processed, go to step 1.
After the input character set has been completely processed, the result of the expression evaluation is at the top of the stack. If there are several numbers left on the stack, then only the top element should be displayed.
A note about negative numbers and division: in this problem, division refers to mathematical integer division. This means that it always rounds down. Namely: if a / b = c, then b ⋅ c is the largest number that does not exceed a and is simultaneously divisible by b without remainder.

In the current problem, it is guaranteed that there is no division by a negative number.
  
### Input Format
  
The single line contains an expression written in reverse Polish notation. Numbers and arithmetic operations are written with a space.
Operations can be given as input: +, -, *, / and numbers, modulo not exceeding 10000.
It is guaranteed that the value of intermediate expressions in the test data modulo is not more than 50000.

### Output Format
  
Output a single number — the value of the expression

### How to launch the project:
  
##### Clone repository:

```
git clone git@github.com:smart2004/Algorythms-Data_Structures-.git
```

##### Switch to the folder:

```
cd algorythms-data_structures-
```

##### Launch python task:

```
python polski_note.py
```
###### NOTE: better use IDE and start task @ the place
  
##### Example for input:
```
4 8 + 6 * 7 / 9 -
```
  
##### Example for output:
```
1
```  
