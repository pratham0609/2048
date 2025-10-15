# 2048
2048 game
2048 GAME

Download application from /dist/main.exe



Python + Tkinter 


•	Combine tiles containing same numbers till we reach 2048

•	Tiles contain only power of 2 [2,4, 8…]

•	Ideally board is 4x4, but we need to have configurable dimensions

•	Score tracking in GUI too

•	Game restart button

Functional programming


•	Functions for each move [up, down, left, right], function for merging tiles, generating new tiles

•	Separation of logic and UI

•	No global state [only passed explicitly]

•	As dimensions are variable, need to consider that and hard code dimensionss


Components
1.	Board 
a.	2D array
b.	Empty cells represented by “0”
c.	Non-empty = power of 2
d.	Eg: board = 
[[2, 0, 0, 2],
[4, 4, 0, 0],
[0, 0, 0, 0],
[0, 0, 0, 0]].


2.	Moves – After each move, we
   
    i.	Compress – Slide tiles to a side [UDLR]
  	
    ii.	Merge – combine equal sides after a move
  	
    iii.	Compress – after merge, need to slide tiles to recent direction
  	
    iv.	Spawn random 2/4 at empty spot
  	
	These actions will be in 4 move functions, each returning a new board and score gained

    i.	move_left(board)
    
    ii.	move_right(board)
    
    iii.move_up(board)
    
    iv.	move_down(board)

3.	End Game:
   
    a.	Win – when any cell is 2048
  	
    b.	Lose – when board is full and no valid moves

4.	GUI:
   
    a.	Grid displaying tiles
  	
    b.	Score
  	
    c.	Restart button
  	
    d.	Keyboard listeners [UDLR]

5.	File (Logic) Separation
   
    a.	main – starts GUI, initialize game

    b.	logic – functions for game logic
  	
    c.	gui – Tkinter for UI
  	
    d.	utils – helper functions 

6.	 Score calculation
    a.	When merging, score += merged_val [i.e., sum of 2 equal merged tile]

7.	At start, ask user for the board configurations
