# Multi-Game-Of-Life
Multiplayer version of Conway's Game of Life

This follows all the same rules as Conway's Game of Life, but adds a new extra rules

If a living cell is surrounded by 4+ cells of a different faction, it gets killed

If a living cell is surrounded by 2-3 cells of a different faction, it converts to that faction if it does not have an equivelent amount of cells of its own faction nearby
- If multiple factions attempt to convert the same cell, the cell simply dies.

If a dead cell is surrounded by exactly 3 cells of 1 faction (and < 3 for all other factions), it becomes living for that faction. 
