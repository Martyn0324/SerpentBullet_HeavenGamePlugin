SerpentAI Game Plugin for Bullet Heaven 2, a Bullet Hell game that allows for using the mouse as controller.
Good way to test SerpentAI for mouse commands, something that it seems not many people have done so far.


# The input mapping

~~To be able to make SerpentAI use the mouse, it was necessary to map my whole pc screen(1920x1080) and pass each pixel into the `MouseEvents(MouseEvent.MOVE, x = X, y = Y)` function with its position in X and Y. However, the result was a .py file with about 5 million lines and 140 Mb. Unfortunately, I couldn't think about any other way to avoid creating this monster.~~

~~The best I could do was to reduced those inputs based on the probability someone would click on each point of the screen.~~

140 Mb, or even its reduced version with 80 Mb of code, demanded more than 200 Gb of a GPU's memory. Considering that the NVidia Tesla T4 GPUs, the most common one in AWS and a quite good one used by Google Cloud, has 16 Gb in its memory, using 200 Gb is impracticable. Only an enterprise like OpenAI would be able to withstand the costs caused by something as bizarre as this.

Because of this, a new way of getting move functions for the mouse was mandatory. Fortunately, this time I managed to think about something.

Instead of mapping each coordinate (X,Y) of my screen and giving them as options for the AI to choose, it was better to create a single dictionary with possible values for the highest dimension(mostly the width). From that, the AI can choose a value for X, and, then, choose a value for Y(with adaptions to match the screen height). After that, a specific function will generate the MOVE command using this X and Y as arguments.

That way, the inputs_mapping files can be discarded.

We went from this

![help](https://user-images.githubusercontent.com/28028007/142612331-044f42d9-5f44-412e-ada8-67be5f6e4509.png)

to this

![yes](https://user-images.githubusercontent.com/28028007/142612372-7ed82ccd-1252-4915-b4cc-98340984041c.png)

Looks like my poor GeForce GTX 1650 still can't handle it. However, probably someone with a more powerful GPU will be able to enjoy using all the 1920x1080 possible coordinates...or even more, you just need to change the `range(0,1920)` in the api.py

For me...I'll stick to my idea of reducing the possible inputs, which is the next section.

## Take a look at this screenshot

![bullet_heaven_reduced](https://user-images.githubusercontent.com/28028007/142492235-a8eeda00-f108-40bd-988d-a2ca894e90b4.png)

The red boxes indicates screen regions that have been removed from the input mapping, which results ~~in the file input_reduced.py~~ in a smaller input, thus requiring less memory from the GPU. The explanation for this removal is simple: since the game is a bullet hell, there's no reason for someone to move the cursor into the boxes at each side of the screen, where one will find only visual information.

At the same time, why would someone place its mouse(the character) at the top of the screen? To risk being hit by incoming opponents and projectiles?

Using this logic, I can reduce the range of options for the mouse input, which gives result to ~~an input_reduced containing about 3 million lines and 80 Mb, which is quite a good reduction, even if it's stills far from good or perfection.~~ a list and a dictionary that my GPU can read and continue clicking on many parts of the game screen...to the point that my AI even quitted the game during training...this sucks.

If anyone have an idea on how to make the coordinate mapping process more effective, please tell me. I'll really appreciate the help.
