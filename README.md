**Changelog**

19.05
- further steps towards code compatibility with PEP8
- the higher animal's trait rank, the bigger its movement cost


12.05
- some steps towards code compatibility with PEP8
- if an animal die, a herb will appear on the field it died on


11.05
- new HUD
- the animals can only have 2 shades of red/green now:
      fair if they are hungry,
      dark if they are ready to breed


08.05
- implemented a better movement method


07.05
- color of the animal depends on its DNA sum now - the higher the darker
- animals won't go to the last tile they were on now
- added legs length trait


06.05
_"New traits"_
- fixed critical birth bug 
- added bowel length trait
- added fat limit trait


05.05
- chunks update planning (optimization attempt - failed)


04.05
_"Inheritance"_
- fixed pause+clean bug
- added inheritance of genes
- added possibility of mutation


-break-


28.08
_"Tempo"_
- modified delta_t time regulation to fit the task better
- added tempo regulation through buttons
- minor interface changes
- fixed cleaning issue


27.04
_"Buttons I"_
- created a few button sprites and added them
- added plus, minus, start, pause and clean buttons
- start, pause and clean buttons work


26.04
- fixed herbs not spawning on some fields


25.04
_"Optimization II"_
- optimized eating and breeding for both carnivores and herbivores
- color of animals depends on their energy level
- new layout design changes


24.04
_"Optimization I"_
- limited amount of herbs to 1 per field
- extraction of main settings to the begginning of the program
- started working on optimization of breeding process
- added logo


23.04
_"Carni&herbi"_
- divided animals into carnivores and herbivores
- carnivores eat herbivores
- preliminary balancing
- preliminary preparations for regulation of the speed of the simulation


22.04
_"Herbs, breeding, energy"_
- added herbs class
- herbs spawn every X frames now
- animals can eat herbs now
- added movement energy cost
- added breeding

21.04
- adding new objects by key
- added coding of the traits using "DNA"
- increased grid size from 13x13 to 43x43

20.04
- created animal class
- calling objects from objects list
- animals can move now
- fixed irregular speeds problem, which was caused by dividing max_counter not by its divider

19.04
- setting intervals for particular objects
- added function creating a square moving randomly around the grid
- the square bounces off the edges now
- three squares moving randomly around the grid with different speeds, bouncing off the edges

18.04
- delta_t application test

17.04
- research about classes and its uses
- research about different methods to make events occur every X time: delta_t

16.04
- added 2 fields long "snake" walking through the grid
- created code to make events occur every X frames

15.04
- created four-dimensional list representing a grid with its content
- added coloring certain fields
- did research about using loops inside of the main PyGame loop
- added code that iterates over the fields and colors one at the time

14.04
- designed interface of SERG

