# SATSolver
SAT-based Sudoku solver. Uses minisat and walksat.<br />
Comprised of a basic implementation and some extended functionality as well.  

**Contributers:**<br />
Yuki Hayashi<br />
Spencer Vatrt-Watts<br />
Mohammed Abousaleh<br />
Zane Li<br />


**Files:**<br />
README<br />
Report<br />
sud2sat.py<br />
sat2sud.py<br />
test_puzzles.txt<br />
test_puzzles_script.py<br />
top95.txt<br />
top95_script.py<br />
test_puzzles_script_walksat.py<br />
top95_script_walksat.py<br />
<br />
**README**
This file describes the contents of every file in the repository. In addition to the general descriptions of files,
the Readme also includes details about our files that help people understand and use the code. Group member names are written in this file. 
<br />
<br />
**Report**
The report contains the description of two programs sat2sud and sud2sat as well as results of our experiments. The results of
our experiment are about 50 puzzles that were solved by our programs. In addition, we provided info about the running the puzzles, 
which includes the mean, median, variance, and standard deviation. 
<br />
<br />
**sud2sat.py**
This file is a python script that reads a unsolved Sudoku puzzle in a specified format in a txt file. This generated txt file will be used for the input to the miniSAT solver. 
To run the sud2sat: $ python sud2sat.py name_of_test_file.txt 
Afterwards, a txt file called "sud2satOutput" will be generated
To run this txt with miniSAT: $ minsat name_of_test_file.txt name_of_output_file.txt
<br />
<br />
Note: only one sudoku puzzle can be run in the test file. 
<br />
<br />
**sat2sud.py**
This file is a python script that reads the output generated from miniSAT and converts the output back into a sudoku puzzle encoded as an 81 character string.
Convert the output back to a sudoku: 	$ python sat2sud.py name_of_test_file_of_sudoku_in_CNF.txt
<br />
<br />
Note: the solved sudoku puzzle will be shown in a 9x9 grid in the terminal. 
<br />
<br />
**test_puzzles.txt**
This file contains 50 unsolved sudoku puzzles that come from <a href="https://projecteuler.net/project/resources/p096_sudoku.txt">https://projecteuler.net/project/resources/p096_sudoku.txt</a>. These puzzles were used to test our solution and we documented the results of the tests. 
<br />
<br />
**test_puzzles_script.py**
This file is an executable that runs unsolved sudoku puzzles from test_puzzles.txt and writes the results from miniSAT and 
puzzle solutions to two files. 
<br />
<br />
### First Extended Task
The first extended task consisted of testing the solver on hard inputs from 
<a href="http://magictour.free.fr/top95">http://magictour.free.fr/top95</a>.
<br />
<br />
**top95.txt**
This txt file includes the hard inputs from <a href="http://magictour.free.fr/top95">http://magictour.free.fr/top95</a>. This contents of the file will be run by top95_script.py.
<br />
<br />
**top95_script.py**
This file is an executable similar to test_puzzles_script.py, in which the program runs unsolved puzzles from top95.txt and writes the results from miniSAT and puzzle solutions to two files.
<br />
<br />
### Second Extended Task
The third extended task consisted of testing a different SAT-solver. For this task we chose to use walksat, available at <a href="https://www.cs.rochester.edu/u/kautz/walksat/">https://www.cs.rochester.edu/u/kautz/walksat/</a>. Walksat must be installed for the following script to work, this can be accomplished by running the makefile included in this repo.
<br />
<br />
**test_puzzles_script_walksat.py**
This file is an executable that runs unsolved sudoku puzzles from test_puzzles.txt and writes the results from walksat and 
puzzle solutions to two files.
<br />
<br />
**top95_script_walksat.py**
This file is an executable similar to test_puzzles_script_walksat.py, in which the program runs unsolved puzzles from top95.txt and writes the results from walksat and puzzle solutions to two files.
