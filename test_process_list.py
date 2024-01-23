import pytest
from process_list import process_list

def test_normal_case():
    assert process_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 5, 7]

def test_error_on_wrong_length():
    with pytest.raises(ValueError):
        process_list([1, 2, 3])

def test_empty_list():
    assert process_list([]) == []


