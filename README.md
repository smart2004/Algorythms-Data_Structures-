# algorythms-data_structures- by smart200481 <Mikhail Sutormin>

## deque.py  
### Brief Task Description

Gosha implemented the Dec data structure, the maximum size of which is determined by a given number. Methods push_back(x), push_front(x), pop_back(), pop_front() worked correctly. But, if there were many elements in the deck, the program worked for a very long time. The fact is that not all operations were performed in O(1). Help Gosh! Write an efficient implementation.

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

The "Speed Typing Trainer" is a sixteen-key 4x4 square keyboard. Each key can display either a dot or a number from 1 to 9.
The exercise on the simulator is divided into rounds:
- each round consists of several games;
- in different rounds, the number of games may be different;
- the number of each game in the round is indicated by the counter t.
  
For each round, certain values are set on the keys, which remain unchanged during all the games of the round.
The value of the game counter t cannot exceed the value of the largest number displayed on the keyboard in the current round.
Two players take part in the exercise on the simulator, they play together on the same keyboard. For each round, the maximum number of keys that one player can press is set (it is denoted by the variable k and does not change during the round).
In each individual game, the participants must press the keys together, on which the number corresponding to the number of the game t is displayed. For example, in the second game of a round, players must press all those keys that show a deuce.
There may be games in the round where you do not need to press buttons: for example, in the above version of the round in games from t = 4 to t = 8, you do not need to press buttons: there are no numbers from 4 to 8 on the keyboard.
If in the next game the participants have the opportunity to press all the necessary keys, they press them and get 1 point.
Let's assume that for the round a set of buttons is given, as in the picture, and k = 3 (each of the participants can press no more than three buttons). Then in the second game (t = 2), where twos must be pressed, two players can only press 6 keys together (k * 2 = 6). But there are seven twos on the keyboard; participants will not be able to click all of them and will not receive a point.
  
Write a program that will receive data for a specific round:
- k value,
- values for buttons,
and calculate the number of points that will be earned in this round.
  
### Input Format
  
The first line contains an integer k (1 ≤ k ≤ 5).

The next four lines set the values for the buttons—4 characters per line. Each character is either a dot or a number from 1 to 9. The characters on the same line are consecutive and are not separated by spaces.

### Output Format
  
Print a single integer, the number of points the players will score in the round.

### How to launch the project:
  
##### Clone repository:

```
git clone git@github.com:smart2004/Algorythms-Basics-.git
```

##### Switch to the folder:

```
cd algorythms-basics-
```

##### Launch python task:

```
python hands_agility.py
```
###### NOTE: better use IDE and start task @ the place
  
##### Example for input:
```
3
1231
2..2
2..2
2..2
```
  
##### Example for output:
```
2
```  
