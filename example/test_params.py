# content of test_indirect_list.py

import pytest


@pytest.fixture(scope="function")
def test_x(request):
    print(f"Param is:{request.param}")
    return request.param * 3


@pytest.fixture(params=[1, 2])
def test_with_params(request):
    return request.param

@pytest.fixture(scope="function")
def y(request, test_with_params):
    return request.param * 2


@pytest.mark.parametrize("test_x, y", [("a", "b")], indirect=["y"])
def test_indirect(test_x, y):
    assert y == "bb"
    assert test_x == "a"

