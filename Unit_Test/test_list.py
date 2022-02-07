import pdb
import unittest.mock
import List
import pytest

ll_alpha = ['l','o','n','d','o','n']

data = [([ll_alpha], [1]), ([ll_alpha], [2]), ([ll_alpha], [3])]


@pytest.fixture()
def setup_list():  # Pytest Fixtures

    ll_alpha.clear()
    print("Inside Fixture")


def test_list_empty(setup_list):
    assert len(ll_alpha) == 0


def test_add_items():
    global ll_alpha
    List.AddToList(ll_alpha, 'b')
    List.AddToList(ll_alpha, 'c')
    List.AddToList(ll_alpha, 'd')
    assert len(ll_alpha) == 3


def test_del_items():
    global ll_alpha
    List.DelFromList(ll_alpha)
    List.DelFromList(ll_alpha)
    assert len(ll_alpha) == 1


def test_len_list():
    global ll_alpha
    assert len(ll_alpha) == 1


def test_add_z():
    global ll_alpha
    num_items = len(ll_alpha)
    List.AddToList(ll_alpha, 'z')
    assert num_items == len(ll_alpha)


'''Some parameterized tests
    pass the arguments to the test_001 function
   This will make multiple calls to test_001 with args from the list
   Note: The actual arguments passed are not modified. ll_alpha remains unchanged after this test.
'''


@pytest.mark.parametrize('test_input1,test_input2', data)
def test_001(test_input1, test_input2):
    num = len(test_input1)
    List.AddToList(test_input1, test_input2)
    assert len(test_input1) == num + 1
    print(test_input1)


def test_002():
    num = len(ll_alpha)
    List.AddToList(ll_alpha, 'c')
    assert len(ll_alpha) == num + 1
    print(ll_alpha)


def test_cleanup():
    print(ll_alpha)
    print("Cleaning up")
