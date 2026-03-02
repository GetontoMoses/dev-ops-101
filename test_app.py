from app import Sum

def test_sum():
    assert (
        Sum(2,3) == 5
    )  # assert means - I expect this to be true. If it's not true, fail immediately.
    
# for pytest to work: 
#      test files must begin with test_.py  and test functions must begin with test_
