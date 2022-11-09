##
## Unit tests for ME369P/396P Spring 2022 Assignment 1
##

import pytest
import importlib
import os
import io
import sys
import re
import traceback

# path  = os.getcwd() + '/' + 'assignment3.py' #linux, mac user
path  = os.getcwd() + '\\' + 'assignment3.py' #windows user
spec = importlib.util.spec_from_file_location("assignment3", path)
my_script = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(my_script)
    print("PASS: SCRIPT IS EXECUTABLE")
except Exception as ex:
    print('\n\nFAIL: EXCEPTION THROWN WHILE RUNNING FUNCTION:')
    print(type(ex).__name__,': ',ex, end='\n\n', sep='')
except:
    print('\n\nFAIL: NON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n') 


def test_problem3CurveFitting():
    # redirect student stdout
    test_file = open('test_files/test_format_p3.txt').read()
    my_output = io.StringIO()
    old_stdout = sys.stdout            
    sys.stdout = my_output

    try:
        my_script.problem3CurveFitting('data_3_3.csv')
    except Exception as ex:
        print('\n\nEXCEPTION THROWN WHILE RUNNING FUNCTION:')
        # print(type(ex).__name__,': ',ex, end='\n\n', sep='')
        print(traceback.format_exc())
    except:            
        print('\n\nNON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n') 


    #stdout is to console again
    sys.stdout = old_stdout
    my_output = my_output.getvalue().replace("+",'').replace("-",'')
    cleaned_output = re.sub("\\d", "?", my_output)
    print(cleaned_output)

    assert test_file in cleaned_output

def test_problem4WhichCurve():
    test_file = open('test_files/test_format_p4.txt').read()
    my_output = io.StringIO()
    old_stdout = sys.stdout            
    sys.stdout = my_output

    try:
        my_script.problem4WhichCurve('data_3_4.csv')
    except Exception as ex:
        print('\n\nEXCEPTION THROWN WHILE RUNNING FUNCTION:')
        # print(type(ex).__name__,': ',ex, end='\n\n', sep='')
        print(traceback.format_exc())
    except:            
        print('\n\nNON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n') 


    #stdout is to console again
    sys.stdout = old_stdout
    my_output = my_output.getvalue().replace("+",'').replace("-",'')
    cleaned_output = re.sub("\\d", "?", my_output)
    print(cleaned_output)

    assert test_file in cleaned_output

