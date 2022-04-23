
import random
import pytest
def test_always_pass():
    assert True == bool(1)

def test_no_param():
    import time
    assert int(time.time())%2 == 0

# a fixture in same file
@pytest.fixture
def rand_squre():
    return random.choice([i*i for i in range(0, 50)])

# rand_squre is local fixture
def test_local_fixture(rand_squre):
    assert rand_squre % 2 == 0

# rand is a fixture in conftest.py
def test_global_fixture(rand):
    assert(rand % 2 ==0)

@pytest.mark.skip # pytest will skip this
# @pytest.mark.xfail : python will still execute just for information,when failure (xfailed), when pass (xpassed)
def test_always_fail():
    assert 1 == 2

# put test into math group
@pytest.mark.math
def test_add():
    assert 1+2 == 3