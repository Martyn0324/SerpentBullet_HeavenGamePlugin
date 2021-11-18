SerpentAI Game Plugin for Bullet Heaven 2, a Bullet Hell game that allows for using the mouse as controller.
Good way to test SerpentAI for mouse commands, something that it seems not many people have done so far.


# The input mapping

To be able to make SerpentAI use the mouse, it was necessary to map my whole pc screen(1920x1080) and pass each pixel into the `MouseEvents(MouseEvent.MOVE, x = X, y = Y)` function with its position in X and Y. However, the result was a .py file with about 5 million lines and 140 Mb. Unfortunately, I couldn't think about any other way to avoid creating this monster.

The best I could do was to reduced those inputs based on the probability someone would click on each point of the screen.

## Take a look at this screenshot

![bullet_heaven_reduced](https://user-images.githubusercontent.com/28028007/142492235-a8eeda00-f108-40bd-988d-a2ca894e90b4.png)

The red boxes indicates screen regions that have been removed from the input mapping, which resulted in the file input_reduced.py. The explanation for this removal is simple: since the game is a bullet hell, there's no reason for someone to move the cursor into the boxes at each side of the screen, where one will find only visual information.

At the same time, why would someone place its mouse(the character) at the top of the screen? To risk being hit by incoming opponents and projectiles?

Using this logic, I could remove many lines of the code, which gave result to an input_reduced containing about 3 million lines and 80 Mb, which is quite a good reduction, even if it's stills far from good or perfection.

If anyone have an idea on how to make the coordinate mapping process more effective, please tell me. I'll really appreaciate the help.
