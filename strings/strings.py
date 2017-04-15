# this is from the Coding interview book Chapter 1
class Unique:

    def __init__(self):
        pass

    def unique(self, string):
        """
            This is question 1:
            Implement an algorthmm to determine if a string has all unique characters. What if you cannot use
            additional data structures?
        """
        # ask it is an ASCII or Unicode string

        dictionary = {}

        # there are only 256 unique letters in the english alphabet, there for if you have a string with more than 256
        # then it will return false
        if len(string) > 256:
            print("[len of {string}] is [length]. returning false".format(string=string,length=len(string)))
            return False

        for char in string:
            if char in dictionary:
                print("[{char}] is in dictoniary!!".format(char=char))
                print("It is not unique. Returning False!!")
                print(dictionary)
                return False
            else:
                print("[{char}] not in dictoniary. Adding".format(char=char))
                dictionary[char] =1

        print("It is unique. Returning True!!")
        return True


class Reverse:
    """
        This is question 2 in chapters
    """

    def reverse(self, string):
        """
        This is question 2 in chapter 1:
        Implement a function void reverse(char* str in C or C++ which reverse a null-terminated string
        """
        if string is "":
            return string
        else:
            return string[-1] + self.reverse(string=string[:-1])


class Permutation:
    """
        This is question 3 of chapter 1
    """
    def __init__(self, string1, string2):
        """
        Given two strings, write a method to decide if one is a permutation of the other.
        """
        # questions to ask,
        # 1. is it cases synsitive
        # 2. is whitespace significant

        self.string1 = string1.lower()
        self.string2 = string2.lower()



    def permutation(self):
        # check if they are the same length, they can't be the same otherwise
        if len(self.string1) is not len(self.string2):
            return False

        reverse = Reverse()
        reverse_string = reverse.reverse(string=self.string1)
        print(reverse_string)

        if reverse_string == self.string2:
            return True
        else:
            return False

    def permuntation_two(self):
        # check if they are the same length, they can't be the same otherwise
        if len(self.string1) is not len(self.string2):
            return False












if __name__ =='__main__':

    unique = Unique()

    assert unique.unique(string="this") == True
    assert unique.unique(string="hadlhfljlkjaldfkjalsdkfjalsdkjflaskdjf;alskdjflkasjdflkajdflkjasdlfkjasdlkfj") == False

    reverse = Reverse()

    print("reverseing 'topping'")
    print(reverse.reverse(string="topping"))

    print("Checking 'stone' and 'lake' ")
    print(Permutation(string1='stong', string2='lake').permutation())

    print("Checking 'god' and 'dog' ")
    print(Permutation(string1='god', string2='dog').permutation())
