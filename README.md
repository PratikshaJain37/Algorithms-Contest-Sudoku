# Solving Sudokus (Pygame)

```
v1.5: with Neural Network algorithm.
```

Made for the Algorithms Contest by ACM-W, 2021

Check out the Youtube [video](https://www.youtube.com/watch?v=LNeW8TpfCCg) for the algorithm and code explanations. 

It is a small Pygame simulation to solve sudokus. It shows how different algorithms behave  - you can see how various algorithms, like Backtracking, Graph-coloring and Deep Learning operate in real-time.


## Demo

Backtracking:
![Backtracking](https://github.com/PratikshaJain37/Algorithms-Contest-Sudoku/blob/master/media/backtracking.gif)

Graph-Coloring:
![Graph-Coloring](https://github.com/PratikshaJain37/Algorithms-Contest-Sudoku/blob/master/media/graph-color.gif)

Deep Learning:
![Deep Learning](https://github.com/PratikshaJain37/Algorithms-Contest-Sudoku/blob/master/media/neural-net.gif)

## Getting Started

Once you have pygame and the virtual environment setup, clone this repository, and install the requirements.
```
$ git clone https://github.com/PratikshaJain37/Algorithms-Contest-Sudoku 
$ pip3 install -r requirements. txt 
```
After making sure you are in the directory which contains the code, run the 'main' script using python3
```
$ cd Algorithms-Contest-Sudoku
$ python3 main.py
```
A pygame window will appear, with a sudoku grid. 

You can press:
- 'b': To solve with backtracking
- 'g': To solve with graph-coloring
- 'n': To solve with deep learning
- 'f': To toggle speed (default=Slow)
- 'spacebar': To reset the board

<hr>

## Run Your Own Sudoku

In helpers.py, there is a function called ```get_board()```, which holds the board to be solved. You can change the board there, but make sure to keep the board as a list of lists (9x9). 

## Bugs 
1. You cannot run graph-coloring twice in the same pygame :/

## Further Plans
1. Implement way to detect sudoku from image, and solve it.
2. Implement Stochastic search/optimazation [methods](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#Stochastic_search_/_optimization_methods)
3. Implement Constraint Programming [(CSP)](https://en.wikipedia.org/wiki/Sudoku_solving_algorithms#Constraint_programming)
4. Implement scanning (traditional methods)

<hr>


## Contributing

If you have some suggestions, feel free to raise an Issue and submit a pull request!

<hr>

## References and Acknowledgements

1. Altered the Pygame UI from TechWithTim's [project](https://github.com/techwithtim/Sudoku-GUI-Solver)
(His [video](https://www.youtube.com/watch?v=_Z9Mz2V-Mig&list=PLzMcBGfZo4-kE3aF6Y0wNBNih7hWRAU2o&index=3 
) was the one that actually inspired me to make this project!)
2. Graph connections - Ishaan Gupta. Check out his code [here](https://github.com/Ishaan97/Sudoku-Solver-Graph-Coloring) and his very thorough blog post [here](https://medium.com/code-science/sudoku-solver-graph-coloring-8f1b4df47072)
3. Neural Network Model - Shiva Verma. Check out his code [here](https://github.com/Ishaan97/Sudoku-Solver-Graph-Coloring), and his really well written blog [here](https://towardsdatascience.com/solving-sudoku-with-convolution-neural-network-keras-655ba4be3b11).

## License

This project is licensed under the MIT License.
