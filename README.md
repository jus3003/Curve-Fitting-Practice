# 2022Fall_assignment3_template
2022Fall_assignment3_template (made by TA: Pohan Wang)

## Problem sets
Please refer to the Google doc: [LINK][link1]

[link1]: https://docs.google.com/document/d/10euL-y7H6sgnh8wDQmvrPkQ_3vAhCfFAVXoH03uU1_U/edit

=====================================================
## PROBLEM 1 & PROBLEM 3 Writing Portions :star:

### Problem 1 Honor Statement:
Please complete the tutorials linked in the assignment doc and then fill out the statement below.
NOTE: Elements from these tutorials will likely appear on the quiz.

`I, Justin Lam (UT EID: JHL2965), have personally completed the first two matplotlib tutorials and have taken any necessary additional actions to understand the material.`

### Problem 3 Writing Response:

Adding extra points would create a line with a better fit to the data. This would increase the r^2 value until r^2 reaches close to 1. The a and b values will get closer to each other with each iteration until the a and b values are unchanging for further iterations.

Sidenote: Hello Pohan it's Justin. I had success with predicting the equations and graphing the line on the animation. However, I had problems removing the lines from previous iterations so they are just overlaying over each other as the points are added. The lines have the correct equations and still stay within the X values of the  points in the frame.   



=====================================================
## Files
- `assignment3.py` : This is an empty framework of the code template. Please follow the structure of the pre-defined functions below:
    - Q2:

        Required output:
        1. problem2.gif
    - Q3:

        Required output:
        1. problem3.gif
        2. Writing section
        3. Print equation output to console
    - Q4:

        Required output:
        1. problem4.gif
        2. Print equation output to console


- `*.csv`: data files for each question
- `test_files`: folder with the sample output gif files.

- `test_assignment3.py` : A test script written with pytest. It is not necessary to run these tests to earn full credit on this assignment, but it is for your benefit as they are similar to how you will be graded.
  - test use command: `!python -m pytest test_assignment3.py` (in spyder's terminal)
  - The way to specify file path depends on OS: L12, 13 provides the format for linux/MacOS, and Windows (just leave the right path format for your python running OS)

    ```python

    path  = os.getcwd() + '/' + 'assignment1.py' #linux, mac user
    # path  = os.getcwd() + '\\' + 'assignment1.py' #windows user

    ```

## Reminders
- Make sure that your submitted code is compilable
- You may import any packages for processing this assignment but do not use any exactly same functions to do the regression. (e.g. use `numpy.polyfit(different_order`), but the matrix operations are allowed (math operations, inverse, any other linear algebras ...etc).
- Please make sure the gif generate function of Q2/3/4 is working, the grading script will call the function and check the result of those gif files been created by calling it. (i.e. DO NOT only upload final gifs on Github, but leave the real function inside not working.)
- We have pre-sprcified the gif file names in the template, you should not have to change those file save lines.
