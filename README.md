# Bowling Challenge

In this exercise you're going to be challenged to write a program to score a bowling game. Just in case it's been a while since you've last bowled, here is how you keep score:

1. A game has 10 frames(rounds)
2. For each frame a player has two chances to knock 10 pins down.
3. The score for the frame is the total number of pins knocked down.
4. A spare is when the player knocks down all 10 pins in *two* tries.
  * A player will receive a bonus for that frame plus however many pins they knock down in the next roll.
    ~EX: If the score is 10 (total num knocked down) plus a bonus of 5 (num of pins knocked down in the next roll) then the score for the previous frame would be 15.
5. A strike is when a player knocks down all 10 pins in the first try.
  * The bonus in this situation is the value of the next two balls rolled
6. In the 10th frame a player who rolls a spare or a strike is allowed to roll the extra balls.
  * There is a hard cap at three balls in the 10th frame though.

Before starting make sure you understand the nuances of the game studying this example of a game. Walk through each frame making sure the score makes sense as you understand the rolls.

![alt text](http://slocums.homestead.com/files/scrsheet.gif "bowling game frame")

## Purpose

This exercise is an object oriented exercise focusing on *form*. The goal isn't just to make your program work, but instead should focus on a step by step, TDD driven approach. Write your most basic test case first and slowly work your way up.
