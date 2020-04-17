import pytest
from Servidor.src.softdes import lambda_handler

def test_lambda_NoFunction():
    args = {'ndes': '1', 'code': '', 'args': [[1], [2], [3]], 'resp': [0, 0, 0], 'diag': ['a', 'b', 'c']}
    feedback = lambda_handler(args, '')
    assert (len(feedback) != 0)

def test_lambda_OK_1():
    args = {'ndes': '1', 'code': 'def desafio1(des):\n    return (0)\n\n', 'args': [[1], [2], [3]], 'resp': [0, 0, 0], 'diag': ['a', 'b', 'c']}
    feedback = lambda_handler(args, '')
    assert (len(feedback) == 0) 
    
def test_lambda_OK_2():
    args = {'ndes': '1', 'code': 'def desafio1(des):\n    return (des)\n\n', 'args': [[2], [2], [2]], 'resp': [2, 2, 2], 'diag': ['a', 'b', 'c']}
    feedback = lambda_handler(args, '')
    assert (len(feedback) == 0) 

def test_lambda_OK_3():
    args = {'ndes': '1', 'code': 'def desafio1(des):\n    return (50)\n\n', 'args': [[1], [2], [3]], 'resp': [50, 50, 50], 'diag': ['a', 'b', 'c']}
    feedback = lambda_handler(args, '')
    assert (len(feedback) == 0) 

def test_lambda_Wrong_Result_1():
    args = {'ndes': '1', 'code': 'def desafio1(des):\n    return (des)\n\n', 'args': [[1], [2], [3]], 'resp': [1, 2, 0], 'diag': ['a', 'b', 'c']}
    feedback = lambda_handler(args, '')
    assert (len(feedback) != 0) 
    
def test_lambda_Wrong_Result_2():
    args = {'ndes': '1', 'code': 'def desafio1(des):\n    a=1+1\n    return (a)\n\n', 'args': [[1], [2], [3]], 'resp': [0, 0, 0], 'diag': ['a', 'b', 'c']}
    feedback = lambda_handler(args, '')
    assert (len(feedback) != 0) 


