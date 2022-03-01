# plexus_water_overflow

Runs on python 3.7.11

To run on the command line, type
`python main.py`

To run on the command line with arguments, type
```
python main.py <arg_liters> <arg_i> <arg_j>

arg_liters is the amount of liquid to be poured (in liters)
arg_i is the ith row to be checked
arg_j is the jth position to be checked

example:
python main.py 2.5 2 2
```

Assumptions:
All inputs are correct and no i/j position is out of bounds. Out of bounds happen for negative index or positions outside of used glasses. 
If there are no / incomplete inputs, the program will run with the default values


To run tests, type
`python -m unittest`