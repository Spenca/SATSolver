# SATSolver
SAT-based Sudoku solver for CSC320.
We finished the basic task and the three extended tasks.  

**Members:**<br />
-Yuki Hayashi <br />
-Spencer Vatrt-Watts <br />
-Mohammed Abousaleh<br />
-Zane Li <br />


**Files in Submission:**<br />
-README.md<br />
-Report<br />
-sud2sat.py<br />
-sat2sud.py<br />
-test_puzzles.txt<br />
-test_puzzles_script.py<br />
-top95.txt<br />
-top95_script.py<br />

**README.md**
This file describes the contents of every file in the zip folder. In addition to the general descriptions of files,
the Readme also includes details about our files that help people understand and use the code. Group member names and IDs
are written in this file. 
<br />
<br />
**Report**
The report contains the description of two programs sat2sud and sud2sat as well as results of our experiments. The results of
our experiment are about 50 puzzles that were solved by our programs. In addition, we provided info about the running the puzzles, 
which include the mean, median, variance, and standard deviation. 

<br />
**sud2sat.py**
This file is an executable that reads a unsolved Sudoku puzzle in a specified format in a txt file. This generated txt file will be used for the input to the miniSAT solver. 
To run the sud2say: $ python sud2sat.py < name of test files>.txt 
Afterwards, a txt file called "sud2satOutput" will be generated
To run this txt with miniSAT: $ minsat < name of testfile>.txt < name of output file>.txt
<br />
Note: only one sudoku puzzle can be run in the testfile. 
<br />
**sat2sud.py**

<br />

**test_puzzles.txt**
<br />
**test_puzzles_script.py**
<br />

## Extended Tasks
<br />
**top95.txt**
<br />
**top95_script.py**
<br />


