import random

class Game:
    def __init__(self):
        """
        Sets up a game of snakes and ladders. Snake and Ladder positions are hard-coded
        """
        self.state = "AtHome"
        self.roll_count = 0

        # Keep track if player was moved by a snake or ladder for printing output
        self.snaked = False
        self.laddered = False

        # setup game board
        self.position = 0
        self.end = 100
        self.ladders = dict([(5, 10), (18, 59), (79, 100)])
        self.snakes = dict([(11, 7), (27, 4), (82, 63)])
        # end game board setup

    def input(self):
        """
        Ask user for input and execute command
        """
        self.print_board()
        mode = input(f"Press 1 to roll a die and 2 to exit!! ")
        if mode == "1": # Roll dice
            # Output roll information
            print(f"Pressed 1, rolling a die")
            roll = self.move()
            print(f"Dice value: {roll}")
            print("")

            # Output new game state information after the roll
            print(f"After the dice is rolled:")
            print(f"CurrentPostion: {self.position}", end=" ")
            if self.snaked:
                print("(Since it is bit by a snake)", end=" ")
                self.snaked = False
            if self.laddered:
                print("(Since it gets a ladder)", end = " ")
                self.laddered = False
            print("")
            print(f"PlayerState: {self.state}")

            # Player wins as soon as position reaches the last position of the game board
            if self.position == self.end:
                print("Hurray you won!! Bye bye :)")
                exit()
            print("---------------------------------------------------------------")

        elif mode == "2": # Exit game
            print("Now exiting")
            exit()

        else:
            print("Invalid input, try again\n")


    def move(self):
        """
        Simulate a dice roll and update player position including any movement by snakes or ladders
        """
        roll = self.roll()

        # AtHome
        if not self.check_state():
            if roll == 6:
                self.state = "RoamFree"
        # RoamFree
        else:
            # Update player position with roll amount if less than or equal to 100
            self.position += roll if self.position + roll <= 100 else 0

            # Move up and down snakes and ladders until player is no longer on a space with snakes or ladders
            while self.position in self.ladders or self.position in self.snakes:
                if self.position in self.ladders:
                    self.position = self.ladders[self.position]
                    self.laddered = True
                elif self.position in self.snakes:
                    self.position = self.snakes[self.snakes]
                    self.snaked = True

        return roll

    def roll(self):
        """
        Returns a random intger from 1 to 6 and increments the roll count
        """
        self.roll_count += 1
        return random.randint(1, 6)

    def check_state(self):
        """
        Returns True if state is RoamFree
        """
        return True if self.state == "RoamFree" else False

    def print_board(self):
        """
        Outputs total number of dice rolls, ladder positions, snake positions, player position, and player state
        """
        print(f"----------------------------- Total Dice rolls before this: {self.roll_count} ----------------------------------")
        print(f"Ladders: {self.ladders}")
        print(f"Snakes: {self.snakes}")
        print(f"CurrentPostion: {self.position}")
        print(f"CurrentState: {self.state}")


def main():
    game = Game()
    while True:
        game.input()

if __name__ == "__main__":
    main()
