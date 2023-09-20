from checks import checkout
import pytest

folderin = '/home/user/test'
folderout = '/home/user/out'
folderext = '/home/user/folder'

# def test_step1():
#     assert checkout(f'cd {folderin}; 7z a {folderout}/arch1', 'Everything is OK'), 'test_step1 FAIL'


# def test_step1():
#     assert checkout(f'cd {folderout}; 7z d arch1.7z', 'Everything is OK'), 'test_step1 FAIL'


# def test_step1():
#     assert checkout(f'cd {folderext}; 7z u {folderout}/arch1', 'Everything is OK'), 'test_step1 FAIL'


def test_step1():
    assert checkout(f'cd {folderout}; 7z l arch1.7z', 'Everything is OK'), 'test_step1 FAIL'


def test_step1():
    assert checkout(f'cd {folderout}; 7z x arch1.7z', 'Everything is OK'), 'test_step1 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])