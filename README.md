# Snake_Game
Classic Snake Game. Collect food pieces and keep your snake growing! The program also keeps the record of the highest score. Use W,A,S,D for controlling your snake.

The game is made using Python. 

The snake itself is created in the "Snake" class (snake.py). The snake is an list containing the "Turtle" (turtle library) class objects. Thus, the snake is an list of multiple squared Turtle objects. 
    The "create_snake" function creates an original snake, containing 3 squares.
    The "grow" function gets coordinates of the last snake's square (its tail) and sends them to the function "add_segment". This function creates a new Turtle object, adds it to "snake list" and sends it to the tail position.
    The "move" function makes the snake move. It starts with the last square and sends it to the position of the square in front of it. Thus, each square moves forward, replacing the next one, reaching the head of the snake. The head then moves forward by 20px. 
    The "go_through_wall" function checks if the first square (snake's head) hits the wall. If snake hits its head, then the first square gets send to the opposite side of the field, thereby it "goes through the walls".
    The "right"/"left"/"up"/"down" functions change the direction of moving by setting the direction (the angle) of the first square's heading. 
    The "tail_hit" function check the distance between the head and each of the "snake list" elements. If it is too small, it considers this situation as a hit and returns "True"
    The "reset" function deletes the existing snake from the interface, then it clears the "snake list" and creates a new snake by triggering the "create_snake" function.
    
The food pieces for the snake are created in the class Food (food.py). The food piece is the turtle circle object. The "refresh" function sends this object to some random coordinates.

This game also contains the scoreboard, which is created in the Score class (scoreboard.py). It reads the recorded highest crose from the file "highest_score.txt". 
    The "update" function creates a writing containing the information about the highest score and current score. 
    The "reset" function checks, if the current final score (at the moment when a user loses) is higher than the highest score. If it's the case, it updates the "highest_score.txt", sets current score equal to 0 and calls an "update" function.
    The "add_score" function adds one point to the current score. 
   
   
   
The "main.py" file merges all of this classes with their function. It creates the inteface by using turtle library's Screen class. This screen listens to the users key commands (W,A,S,D) changing the direction of the snake movement. 
The while loop makes snake move by triggering "move" command from the "Snake" class. It breaks when the snake hits its tail.
