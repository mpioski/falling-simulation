# falling-simulation
A particles falling simulation using cellular automaton and pygame. Pygame is used only for graphics purposes, since the
algorithm is independent of the graphics library.

![sand](media/sand.gif)

## Features
- Falling sand

## TODO
- Add water
- Add gas
- Add oil
- Add fire
- Switch to [ModernGL](https://github.com/moderngl/moderngl)
- Multithreading for each row of the grid

## Optimizations

Largers screen sizes, like 800x800, can not be handled by the current branch implementation. However, there is a branch 
called `numpy` which is used to speed up the simulation using numpy array as "minimap" to store the current state of the screen.


## Installation
```
pip install -r requirements.txt
```