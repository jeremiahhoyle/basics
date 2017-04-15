from strings import Unique

def test_string():

    unique = Unique()

    assert unique.unique(string="this") == True

    assert unique.unique(string="hadlhfljlkjaldfkjalsdkfjalsdkjflaskdjf;alskdjflkasjdflkajdflkjasdlfkjasdlkfj") == False