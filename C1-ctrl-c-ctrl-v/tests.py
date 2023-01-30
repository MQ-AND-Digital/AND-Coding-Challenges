from strings import *
from pytest import *
from main import *

def test_answer_1():
    assert modifyString(stringsList[0]) == "the big red fox jumps over the big red lazy dog."

def test_answer_2():
    assert modifyString(stringsList[1]) == "the tall oak tree towers over the lush green meadow."

def test_answer_3():
    assert modifyString(stringsList[2]) == "the sun shines down on the sun shines down the busy the sun shines down on the sun shines down."

def test_answer_4():
    assert modifyString(stringsList[3]) == "the tall oak tree towers over the lush green meadow."

def test_answer_5():
    assert modifyString(stringsList[4]) == "a majestic lion searches for a majestic lion in the tall grass."
    
def test_answer_6():
    assert modifyString(stringsList[5]) == "Twinkling in the dark, the shimmering star shines bright."
    
def test_answer_7():
    assert modifyString(stringsList[6]) == "a fluffy white cloud drifts across the sky, a fluffy white cloud drifts"