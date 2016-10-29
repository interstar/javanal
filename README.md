# Javanal (Java Analysis)

I needed a very quick and dirty way to look at a few Java files and see the class hierarchy and the interfaces.

I didn't need much detail. I didn't need UML. I didn't need the arrows to go the right way or the right sort of boxes. (I didn't know graphviz / dot well enough to get that right, and didn't want to spend the time looking it up.) 

I just wanted to grep the source code for all the *extends* and *implements* statements and to see what it looked like.

Here's how I use it

    cat *pde | egrep 'extends|implements' | javanal.py > test.dot
    xdot test.dot
    
Yeah, I'm looking at Processing files. That's why they have the .pde suffix and I'm not using an IDE that already has this built-in.

Also, my program is small ... only 30 or so classes and interfaces. Big enough to get lost in, but small enough to scroll around a single diagram. Anything larger and you probably want a different tool.



