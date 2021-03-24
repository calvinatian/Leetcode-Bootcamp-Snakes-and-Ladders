# How to use

Game is setup using the `Game` class with no parameters. Ask for user input using the `input()` method inside the `Game` class. The `game.py` file can be run directly for the below example.

Example setup that continuously runs until the user either wins or quits the program.
```python
game = Game()
while True:
    game.input()

```

* Ladder and snake positions are hard-coded in the `Game` class.

## Project Description
1. We have just 1 player in the game.
2. The player starts at 0 and wins the game on reaching 100.
3. There should be at least 3 ladders in the game. 
4. There should be at least 3 snakes in the game. 
5. You can define (start, end)  points of the snakes and ladders on your own. 
6. You will roll a dice that should produce an integer value in the range [1, 6]. The produced integer value should be random. (Use random function to generate the output)
7. Your player can have 2 states -(i) AtHome (ii) RoamFree. 
8. When the game begins, the player is at position 0 and its state is AtHome.
9. The player can only move forward once its state turns to RoamFree. For the state to turn to RoamFree, it is necessary for the dice to show a value of 6. 
10. Once the state of the player is RoamFree, the player is eligible to move forward. Thus, any time the dice is rolled and the state of the player is RoamFree, the player will move forward. For eg.,
    1. if the current position of the player is 0 and 
    2. the current state is RoamFree, 
    3. And the dice shows 3
    4. The new position will become old position + new position i.e. 0 + 3 = 3
11. Once the player reaches a new position that is the lower point of the ladder, the player’s position will automatically be changed to the higher point of the ladder. For eg., 
    1. if the current position of the player is 3 and
    2. the current state is RoamFree, and
    3. The dice shows 2
    4. The position will become 5 and 
    5. If this position i.e. 5 is the starting point of a ladder that ends at 10,
    6. The final position of the player would become 10.
12. Similarly, once the player reaches a new position that is the mouth of the snake, the player’s position will automatically be changed to the tail of the snake.
13. To win the game the player should exactly reach 100. In case the player is at 98, there are just 2 valid moves that the player can make. 
    1. If the dice shows 1, the player shifts to 99 and the game is still on.
    2. If the dice shows 2, the player shifts to 100 and wins the game.
    3. For any value of dice >= 3 the player can’t move and will remain at its own position while the game is still on.
