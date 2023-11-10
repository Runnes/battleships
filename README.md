# battleship-python-Runnes
Tasks

Placement phase
Implement the placement phase of the battleship program where players can place ships on a board.

Row (as character), column (as number) and direction (horizontal/vertical) for placement are asked from the user as user input.

A 5x5 board is shown after each placement, similar to the following example, where 0 indicates an empty space and X indicates a ship part.

1 2 3 4 5
A 0 0 0 0 0
B X X 0 0 0
C 0 0 0 0 0
D 0 0 0 0 0
E 0 0 0 0 0
If the user input is invalid (outside range), the Invalid input! error message is displayed and the program asks for input again.

Ships can be at least two different sizes (such as 1-block long and 2-blocks long).

The program keeps asking for input until all ships are placed.

When trying to place two ships next to each other (touching corners are okay), the Ships are too close!error message is displayed and the program asks again for an input

After one player is finished with the placement phase, a waiting screen is displayed with no boards, with the Next player's placement phase message.

When pressing any button on the waiting screen, the second player's placement phase begins.

CRITERIA
Shooting phase
Implement the shooting phase of the battleship program where players have to sink each other's ships.

The game asks for a row (as a letter) and a column (as a number) as user input for shooting.

Both players' 5x5 board is shown after each shooting, similar to the following example, where 0 indicates an undiscovered tile, M indicates a missed shot, H indicates a hit ship part, and S indicates a sunk ship part.

Player 1 Player 2
1 2 3 4 5 1 2 3 4 5
A 0 0 0 0 M A 0 0 0 0 M
B S S M 0 0 B 0 0 0 0 0
C 0 0 0 0 0 C H M 0 0 0
D 0 0 0 0 0 D 0 0 0 0 0
E 0 0 0 0 0 E 0 0 S 0 0
Players change turns after each shot

Player turns are clearly indicated.

If invalid input is entered (outside range), the Invalid input! error message is displayed and the program asks for input again (shooting twice at the same spot is a valid but unnecessary move).

Hitting, missing and sinking ship (parts) results in displaying as message, such as You've hit a ship!, You've missed!, and You've sunk a ship! respectively.

If one of the players sinks all ships of the other player, the Player <n> wins! message is displayed, where is the number of the winning player. Then the game ends.

CRITERIA
OPTIONAL TASK: Custom board size
Extend the game so that the user can choose a custom board size at the beginning.

Before the placement phase, the game asks for the size of the board as user input.

If the given board size is out of range (5-10) the Invalid input! (must be between 5-10) error message is displayed.

The board size is used and displayed during the placement phase, with characters between A-J indicating rows and numbers between 1-10 indicating columns.

The board size is used and displayed during shooting phase, with characters between A-J indicating rows and numbers between 1-10 indicating columns.

CRITERIA
OPTIONAL TASK: Turn limit
Extend the game so there is a turn limit in the game, after which the game results in a draw.

Before the placement phase, the game asks for the turn limit as user input.

If the turn limit is out of range (5-50) the Invalid input! (must be between 5-50) error message is displayed.

The number of remaining turns is constantly displayed above the boards, such as Turns left: 18.

The number of remaining turns is decreased after each player has a shot.

If the number of remaining turns reaches zero, the No more turns, it's a draw! message is displayed, and the game ends.

CRITERIA
OPTIONAL TASK: AI can play
Extend the game so that there is a single player mode, where the user can play against the computer.

Before the placement phase, the game asks for the game mode as user input by printing a menu with two items (1. Single player, 2. Multiplayer).

If the choice is out of range (1-2), the Invalid input! error message is displayed.

If multiplayer is chosen as the game mode, the game works with two players, as in the above tasks.

If single player is chosen as the game mode, Player 2 is the computer. The AI generates its moves during the placement and shooting phases.

CRITERIA
General requirements
Variable names in the program are meaningful, non-abbreviated nouns.

Function names in the program are meaningful, non-abbreviated verbs.

There are no unnecessary (dead) code or comments in the program.

There are no duplicate code parts, or code parts doing the same thing differently in the program.

There are no functions doing more than one thing in the program.
