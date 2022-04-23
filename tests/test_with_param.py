import math
import pytest

# pass parameters to current function
@pytest.mark.parametrize('x,v' ,[
    (2, 1.41),(2, 1.42),
    (5, 2.23),(5,2.24),
    (6, 2.45),(6, 2.44)
    ])
def test_pass_param(x, v):
    assert round(math.sqrt(x),2) == v

# pass n to fixture
@pytest.mark.parametrize('n', [3, 4, 5])
def test_pass_param_to_fixture(rand_div):
    assert rand_div % 2 == 0 or rand_div % 5 == 0

# pass x to current function
# pass n to fixture
@pytest.mark.parametrize('x,n', [[1,2], [3,4],[5,6]])
def test_pass_param_to_both(x, rand_div):
    assert rand_div % x == 0

# pass n1, n2 to global fixture: <triangle>
# pass v to current function
@pytest.mark.parametrize('n1,n2,v', [[3, 4, 5], [6, 8, 10], [1,2,2.3]])
@pytest.mark.math # put into math category
def test_pass_multiple_param_fixture(triangle, v):
    assert v == triangle

# will generate combinations :
# n1=3, n2=4, v=5; 
# n1=3, n2=4, v=10; 
# n1=6, n2=8, v=5; 
# n1=6, n2=8, v=10
@pytest.mark.parametrize('n1, n2', [[3,4], [6,8]])
@pytest.mark.parametrize('v', [5, 10])
def test_pass_multiple_another_way(triangle, v):
    assert v == triangle
