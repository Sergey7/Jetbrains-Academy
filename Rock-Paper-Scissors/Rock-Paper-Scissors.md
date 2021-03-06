## **Description**
How about some brand new rules? The original game has a fairly small choice of options.

Extended versions of the game are decreasing the probability of draw, so it could be cool to play them.
Now, your program should be able to accept alternative lists of options, like Rock, Paper, Scissors, Lizard, Spock, or even a list like this:



At this stage, before the start of the game, the user will be able to choose the options that will be used. After entering his/her name, the user should provide a list of options separated by a comma. For example,

***rock,paper,scissors,lizard,spock***

If the user inputs an empty line, your program should start the game with default options: rock. paper and scissors.

After the game options are defined, your program should output ***Okay, let's start***

Whatever list of options the user chooses, your program, obviously, should be able to identify which option beats which, that is, the relationships between different options. First, every option is equal to itself (causing a draw if both user and computer choose the same option). Secondly, every option wins over one half of the other options of the list and gets defeated by another half. How to determine which options are stronger or weaker than the option you're currently looking at? Well, you can try to do it this way: take the list of options (provided by the user or the default one). Find the option for which you want to know its relationships with other options. Take all the options that follow this chosen option in the list. Add to them the list of options that precede the chosen option. Now you have another list of options that doesn't include the "chosen" option and has the different order of elements in it (first go the options following the chosen one in the original list, after them are the ones that precede it). So, in this "new" list, the first half of the options will be defeating the "chosen" option, and the second half will get beaten by it.

For example, the user's list of options is ***rock,paper,scissors,lizard,spock.*** You want to know what options are weaker than ***lizard***. By looking at the list ***spock,rock,paper,scissors*** you realize that ***spock*** and ***rock*** will be beating the lizard, and ***paper*** and scissors will get defeated by it. For spock it'll be almost the same, but it'll get beaten by ***rock*** and ***paper***, and prevail over ***scissors*** and ***lizard***. For the version of the game with 15 options, you can look at the picture above to understand the relationships between options.

Of course, this is not the most efficient way to determine which option prevails over which. You are welcome to try to develop some other methods of tackling this problem.

## **Objectives**
Your program should:

Output a line ***Enter your name:*** . Note that the user should enter his/her name on the same line (not the one following the output!)
Read input specifying the user's name and output a new line ***Hello, <name>***
Read a file named ***rating.txt*** and check if there's a record for the user with the same name; if yes, use the score specified in the ***rating.txt*** for this user as a starting point for calculating the score in the current game. If no, start counting user's score from 0.
Read input specifying the list of options that will be used for playing the game (options are separated by comma). If the input is an empty line, play with default options.
Output a line ***Okay, let's start***
Play the game by the rules defined on the previous stages:
Read user's input
If the input is ***!exit***, output ***Bye!*** and stop the game
If the input is the name of the option, then:
Pick a random option
Output a line with the result of the game in the following format (***<option>*** is the name of the option chosen by the program):
Lose -> ***Sorry, but computer chose <option>***
Draw -> ***There is a draw (<option>)***
Win -> ***Well done. Computer chose <option> and failed***
For each draw, add 50 points to the score. For each user's win, add 100 to his/her score. In case the user loses, don't change the score.
If the input corresponds to anything else, output ***Invalid input***
Play the game again (with the same options that were defined before the start of the game)
## Example
The greater-than symbol followed by space ***(> )*** represents the user input. Notice that it's not the part of the input.
### Example 1:
```
Enter your name: > Tim
Hello, Tim
> rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
Okay, let's start
> rock
Sorry, but computer chose air
> !rating
Your rating: 0
> rock
Well done. Computer chose sponge and failed
> !rating
Your rating: 100
> !exit
Bye!
```
### Example 2:
```
Enter your name: > Tim
Hello, Tim
> 
Okay, let's start
> rock
Well done. Computer chose scissors and failed
> paper
Well done. Computer chose rock and failed
> paper
There is a draw (paper)
> scissors
Sorry, but computer chose rock
> !exit
Bye!
```
## Solution
    
```
import random

name = input('Enter your name: ')
print(f'Hello, {name}')
score = 0

with open('rating.txt', 'r') as file:
    for line in file:
        player_name, player_score = line.split()
        if name == player_name:
            score = int(player_score)
            break

options = input().split(',')
if options == ['']:
    options = ['rock', 'paper', 'scissors']
print("Okay, let's start")

while True:
    player = input()
    if player == '!exit':
        print('Bye')
        break
    if player == '!rating':
        print(f'Your rating: {score}')
        continue
    if player not in options:
        print('Invalid input')
        continue
    computer = random.choice(options)
    if computer == player:
        score += 50
        print(f'There is a draw ({computer})')
    else:
        offset = (options.index(computer) - options.index(player)) % len(options)
        if offset > len(options) // 2:
            score += 100
            print(f'Well done. Computer chose {computer} and failed')
        else:
            print(f'Sorry, but computer chose {computer}')
```
