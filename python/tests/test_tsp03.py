from tsp03_spacefilling import quicksort

def test_quicksort():
    assert quicksort([1,2,3,4,5]) == [1,2,3,4,5]
    assert quicksort([1,3,6,8,2]) == [1,2,3,6,8]
    assert quicksort([1,3,6,3,2]) == [1,2,3,3,6]
    assert quicksort([1,3,6,3,2], key=lambda s: s * -1) == [6,3,3,2,1]
