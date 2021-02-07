import dict_inteterdiff as di

def test_1():
    d1 = {1:30, 2:20, 3:30, 5:80}
    d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

    
    expected = ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
    actual = di.dict_interdiff(d1, d2)

    assert expected == actual
