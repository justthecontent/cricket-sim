# Cricket Simulation Code

This project is a simulation of a cricket game, implemented in Python. The `main.py` script is the entry point for the simulation.

## Sample Run

```
South Africa won the toss and elected to ball first
Over 0.1: A1 faces B11 - WKT
A1 is out!
Over 0.2: A3 faces B11 - 4
Over 0.3: A3 faces B11 - 5
Over 0.4: A3 faces B11 - NB
Over 0.4: A3 faces B11 - 1
A3 scores 1 run(s)
Over 0.5: A2 faces B11 - 5
Over 0.6: A2 faces B11 - 3
A2 scores 3 run(s)
End of over 0: {'A1': 'Bat', 'A2': 'Bat', 'A3': 'Bat', 'A4': 'Bat', 'A5': 'Bat', 'A6': 'All', 'A7': 'Ball', 'A8': 'Ball', 'A9': 'Ball', 'A10': 'Ball', 'A11': 'Ball'} - 19/1
Over 1.1: A2 faces B6 - 2
Over 1.2: A2 faces B6 - WD
Over 1.2: A2 faces B6 - WKT
A2 is out!
Over 1.3: A4 faces B6 - 5
Over 1.4: A4 faces B6 - 5
Over 1.5: A4 faces B6 - 6
Over 1.6: A4 faces B6 - 1
A4 scores 1 run(s)
End of over 1: {'A1': 'Bat', 'A2': 'Bat', 'A3': 'Bat', 'A4': 'Bat', 'A5': 'Bat', 'A6': 'All', 'A7': 'Ball', 'A8': 'Ball', 'A9': 'Ball', 'A10': 'Ball', 'A11': 'Ball'} - 39/2
Over 2.1: A4 faces B9 - 0
Over 2.2: A4 faces B9 - NB
Over 2.2: A4 faces B9 - 2
Over 2.3: A4 faces B9 - 5
Over 2.4: A4 faces B9 - 0
Over 2.5: A4 faces B9 - 6
Over 2.6: A4 faces B9 - WD
Over 2.6: A4 faces B9 - NB
Over 2.6: A4 faces B9 - 0
End of over 2: {'A1': 'Bat', 'A2': 'Bat', 'A3': 'Bat', 'A4': 'Bat', 'A5': 'Bat', 'A6': 'All', 'A7': 'Ball', 'A8': 'Ball', 'A9': 'Ball', 'A10': 'Ball', 'A11': 'Ball'} - 55/2
Over 3.1: A3 faces B6 - NB
Over 3.1: A3 faces B6 - 2
Over 3.2: A3 faces B6 - 0
Over 3.3: A3 faces B6 - 2
Over 3.4: A3 faces B6 - 1
A3 scores 1 run(s)
Over 3.5: A4 faces B6 - NB
Over 3.5: A4 faces B6 - 3
A4 scores 3 run(s)
Over 3.6: A3 faces B6 - 0
End of over 3: {'A1': 'Bat', 'A2': 'Bat', 'A3': 'Bat', 'A4': 'Bat', 'A5': 'Bat', 'A6': 'All', 'A7': 'Ball', 'A8': 'Ball', 'A9': 'Ball', 'A10': 'Ball', 'A11': 'Ball'} - 65/2
Over 4.1: A4 faces B8 - 4
Over 4.2: A4 faces B8 - 2
Over 4.3: A4 faces B8 - 6
Over 4.4: A4 faces B8 - 1
A4 scores 1 run(s)
Over 4.5: A3 faces B8 - WD
Over 4.5: A3 faces B8 - 1
A3 scores 1 run(s)
Over 4.6: A4 faces B8 - 6
End of over 4: {'A1': 'Bat', 'A2': 'Bat', 'A3': 'Bat', 'A4': 'Bat', 'A5': 'Bat', 'A6': 'All', 'A7': 'Ball', 'A8': 'Ball', 'A9': 'Ball', 'A10': 'Ball', 'A11': 'Ball'} - 86/2
After 5 overs, Bangladesh scored 86 (Extras: 8)

Bangladesh batting Timeline: 
     Runs  Balls
A1      0      1
A2     10      4
A3     16      9
A4     52     16
A5      0      0
A6      0      0
A7      0      0
A8      0      0
A9      0      0
A10     0      0
A11     0      0

South Africa bowling Timeline: 
         B6  B7  B8  B9  B10  B11
Overs     2   0   1   1    0    1
Wickets   1   0   0   0    0    1
Now South Africa needs 87 runs to win

Over 0.1: B1 faces A9 - NB
Over 0.1: B1 faces A9 - 4
Over 0.2: B1 faces A9 - NB
Over 0.2: B1 faces A9 - 2
Over 0.3: B1 faces A9 - NB
Over 0.3: B1 faces A9 - 3
B1 scores 3 run(s)
Over 0.4: B2 faces A9 - 6
Over 0.5: B2 faces A9 - 6
Over 0.6: B2 faces A9 - 4
End of over 0: {'B1': 'Bat', 'B2': 'Bat', 'B3': 'Bat', 'B4': 'Bat', 'B5': 'Bat', 'B6': 'All', 'B7': 'Ball', 'B8': 'Ball', 'B9': 'Ball', 'B10': 'Ball', 'B11': 'Ball'} - 28/0
Over 1.1: B1 faces A10 - 4
Over 1.2: B1 faces A10 - 2
Over 1.3: B1 faces A10 - 3
B1 scores 3 run(s)
Over 1.4: B2 faces A10 - WKT
B2 is out!
Over 1.5: B3 faces A10 - 0
Over 1.6: B3 faces A10 - 1
B3 scores 1 run(s)
End of over 1: {'B1': 'Bat', 'B2': 'Bat', 'B3': 'Bat', 'B4': 'Bat', 'B5': 'Bat', 'B6': 'All', 'B7': 'Ball', 'B8': 'Ball', 'B9': 'Ball', 'B10': 'Ball', 'B11': 'Ball'} - 38/1
Over 2.1: B3 faces A8 - 2
Over 2.2: B3 faces A8 - 5
Over 2.3: B3 faces A8 - 5
Over 2.4: B3 faces A8 - 5
Over 2.5: B3 faces A8 - 0
Over 2.6: B3 faces A8 - WKT
B3 is out!
End of over 2: {'B1': 'Bat', 'B2': 'Bat', 'B3': 'Bat', 'B4': 'Bat', 'B5': 'Bat', 'B6': 'All', 'B7': 'Ball', 'B8': 'Ball', 'B9': 'Ball', 'B10': 'Ball', 'B11': 'Ball'} - 55/2
Over 3.1: B1 faces A6 - NB
Over 3.1: B1 faces A6 - WD
Over 3.1: B1 faces A6 - WKT
B1 is out!
Over 3.2: B5 faces A6 - 3
B5 scores 3 run(s)
Over 3.3: B4 faces A6 - 5
Over 3.4: B4 faces A6 - WKT
B4 is out!
Over 3.5: B6 faces A6 - 5
Over 3.6: B6 faces A6 - 3
B6 scores 3 run(s)
End of over 3: {'B1': 'Bat', 'B2': 'Bat', 'B3': 'Bat', 'B4': 'Bat', 'B5': 'Bat', 'B6': 'All', 'B7': 'Ball', 'B8': 'Ball', 'B9': 'Ball', 'B10': 'Ball', 'B11': 'Ball'} - 73/4
Over 4.1: B6 faces A10 - WKT
B6 is out!
Over 4.2: B7 faces A10 - 2
Over 4.3: B7 faces A10 - WD
Over 4.3: B7 faces A10 - NB
Over 4.3: B7 faces A10 - 0
Over 4.4: B7 faces A10 - 3
B7 scores 3 run(s)
Over 4.5: B5 faces A10 - NB
Over 4.5: B5 faces A10 - NB
Over 4.5: B5 faces A10 - WD
Over 4.5: B5 faces A10 - WD
Over 4.5: B5 faces A10 - 6
Target of 87 achieved by {'B1': 'Bat', 'B2': 'Bat', 'B3': 'Bat', 'B4': 'Bat', 'B5': 'Bat', 'B6': 'All', 'B7': 'Ball', 'B8': 'Ball', 'B9': 'Ball', 'B10': 'Ball', 'B11': 'Ball'}
After 5 overs, South Africa scored 90 (Extras: 11)

South Africa batting Timeline: 
     Runs  Balls
B1     18      7
B2     16      4
B3     18      8
B4      5      2
B5      9      2
B6      8      3
B7      5      3
B8      0      0
B9      0      0
B10     0      0
B11     0      0

Bangladesh bowling Timeline: 
         A6  A7  A8  A9  A10  A11
Overs     1   0   1   1    1    0
Wickets   2   0   1   0    2    0

# -------------------- Bangladesh VS South Africa -------------------- #

South Africa won


```
