import ku
import pytest

def test_count_func():
    assert ku.count_func("123Python *$$$*Is        Better") == 3
    assert ku.count_func("123python *$$$*is        better") == 0

def test_count_func_1():
    assert ku.count_func_1("123Python *$$$*Is        Better") == 3
    assert ku.count_func_1("123python *$$$*is        better") == 0 

def test_count_func_2():
    assert ku.count_func_2("123Python *$$$*Is        Better") == ["Python", "Is", "Better"]
    assert ku.count_func_2("123python *$$$*is        better") == ["python", "is", "better"]

def test_checker_func():
    assert ku.checker_func("no", "no", "no", "yes", "no") == True
    assert ku.checker_func("no", "no", "no", "no", "yes") == True
    assert ku.checker_func("no", "yes", "no", "no", "yes") == False
    assert ku.checker_func("no", "no", "no", "yes", "yes") == True
    assert ku.checker_func("no", "no", "no", "no", "no") == False

def test_dispatcher():
    assert ku.dispatcher("") == "view_all_tasks"
    assert ku.dispatcher("saturday/") == "view_day_tasks"
    assert ku.dispatcher("sunday/") == "view_day_tasks"
    assert ku.dispatcher("sunday/morning/") == "view_specific_task"
    assert ku.dispatcher("sunday/noon/") == "view_specific_task"
    assert ku.dispatcher("saturday/evening/") == "view_specific_task"
    with pytest.raises(ValueError):
        ku.dispatcher("123")
        ku.dispatcher("*$$$*")
        ku.dispatcher("keta_99")
        ku.dispatcher("tako-99")


def test_cyrc_area():
    assert ku.cyrc_area("1") == 3.14

def test_sqr_area():
    assert ku.sqr_area("2") == 4

def test_l_func():
    assert ku.l_func(2, 1, 1, 2, 1, 1) == 3
    with pytest.raises(ValueError):
        ku.l_func(1, 1, 1, 1, 1, 1)
    