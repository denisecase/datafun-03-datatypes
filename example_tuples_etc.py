"""
Purpose: Illustrate tuples, sets, and dictionaries in Python.

Tuples, sets, and dictionaries are all iterable objects. 
That means that they can be used in a for loop.
And with filter() and map() functions (better!)
And with comprehension syntax (the best!)

Here are some examples for tuples, sets, and dictionaries.

"""

# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)


def illustrate_tuples():
    """This function illustrates tuples in Python."""

    """
    TUPLES .......................................................

    In Python, a tuple is a immutable sequence type. 
    This means that once you create a tuple, 
    you cannot change the values it contains: 
    you can't add, remove, or change the values of any of the elements 
        in the tuple.
    Tuples are created using parentheses.

    You can access the elements of a tuple using indexing, like a list.
    The first index is 0 and the last index is -1.

    Since a tuple (like a list) is ordered, you can use slicing to get a
    range of elements from the tuple. [start:end:step]

    Tuples support concatenation, repetition, and membership testing.

    Tuples enable a function to return multiple values, for example:
    (slope, intercept) = statistics.linear_regression(xlist, ylist)
    (host, port) = get_host_and_port()

    Tuples are often used as keys in dictionaries.
    """

    # Create some tuples
    tupleA = (1, 2, 3, 4, 5)
    tupleB = (4, 5, 6, 7, 8)

    logger.info(f"tupleA = {tupleA}")
    logger.info(f"tupleB = {tupleB}")

    # tuple concatenation
    tupleCat = tupleA + tupleB

    # tuple repetition
    tupleAThrice = tupleA * 3

    # TODO: Start using this f-string "syntactic sugar" for quick ouptut
    # just add space = space inside the curly braces
    # it will print the name of the variable and the value
    logger.info(f"{tupleA = }")
    logger.info(f"{tupleB = }")
    logger.info(f"{tupleCat = }")
    logger.info(f"{tupleAThrice = }")

    # tuple membership testing

    tupleD = (1, 2, 3)
    hasOne = 1 in tupleD  # True
    hasFour = 4 in tupleD  # False

    # tuple indexing (0 is first, -1 is last, or 1 less than the length)

    my_tuple = (1, 2, 3)
    first = my_tuple[0]
    second = my_tuple[1]
    third = my_tuple[2]
    last = my_tuple[-1]

    # Use tuples to return multiple values from a function

    def divide_and_remainder(dividend, divisor):
        quotient = dividend // divisor
        remainder = dividend % divisor
        return quotient, remainder

    q, r = divide_and_remainder(10, 3)
    logger.info(f"Quotient: {q}, Remainder: {r}")


def illustrate_sets():
    """This function illustrates sets in Python."""

    """
    SETS .......................................................    

    A set is an unordered collection of unique elements.
    A set is created using curly braces.
    Sets can use the same methods as lists and tuples.
    Sets support the following operations:

    Membership testing (using the in and not in operators)
    Element addition (using the add method)
    Element removal (using the remove and discard methods)
    Set union (using the union method or the | operator)
    Set intersection (using the intersection method or the & operator)
    Set difference (using the difference method or the - operator)
    Set symmetric difference (using the symmetric_difference method or ^ operator)


    """

    setA = {1, 2, 3, 4, 5}
    setB = {4, 5, 6, 7, 8}

    logger.info(f"setA = {setA}")
    logger.info(f"setB = {setB}")

    # set union
    setC = setA | setB

    # set intersection
    setD = setA & setB

    # set difference
    setE = setA - setB

    # sets are often used to remove duplicates from a list
    # after gettin the set, convert it back to a list with list() or []
    listWords = ["apple", "banana", "apple", "pear", "banana", "orange"]
    setWords = set(listWords)
    listWordsNoDuplicates = list(setWords)
    listWordsNoDuplicates = [setWords]  # same as above


def illustrate_dictionaries():
    """This function illustrates dictionaries in Python."""

    """
    DICTIONARIES .......................................................    

    A dictionary is an unordered collection of key-value pairs.
    A dictionary is created using curly braces.
    A dictionary is accessed using keys, not indexes.
    A dictionary is mutable, so you can add, remove, and change values.
    A dictionary is iterable, so you can use it in a for loop.
    A dictionary is not ordered, so you can't slice to access a range of values.

    Dictionaries support the following operations:

    Indexing: access the value associated with a key in the dictionary. 
    For example: dogA['name'].

    Membership testing: use 'in' and 'not in' operators 
    to test whether a key is in the dictionary. 
    For example: 'name' in dogA.

    Adding and updating items: use indexing to add a new key-value pair,
    or to update the value associated with an existing key. 
    For example: dogA['age'] = 2.

    Removing items: Use the del statement to remove a key-value pair. 
    For example: del dogA['weight_kg'].

    Iteration: You can use a for loop to iterate over the 
    keys, values, or key-value pairs in a dictionary. 
    For example: for key in dogA: print(key)

    Dictionaries are a lot like 
    JSON objects - a common data format used in web development.

    """

    dogA_dict = {"name": "Rex", "age": 2, "weight_kg": 13.4}
    dogB_dict = {"name": "Fido", "age": 3, "weight_kg": 15.2}

    logger.info(f"dogA_dict = {dogA_dict}")
    logger.info(f"dogB_dict = {dogB_dict}")

    assessment_dict = {"low": 0, "medium": 1, "high": 2}
    logger.info(f"assessment_dict = {assessment_dict}")

    data_dict = {
        "name": ["Alice", "Bob", "Charlie", "David"],
        "age": [25, 30, 35, 40],
        "income": [50000, 60000, 70000, 80000],
    }
    logger.info(f"data_dict = {data_dict}")

    # In data anlytics, dictionaries may be used to store and manipulate
    # tabular data, e.g. from database records or Excel rows.

    # Dictionaries can be used to store and aggregate statistical data,
    # such as counts or sums. For example, a dictionary of word-count pairs.

    with open("text_simple.txt") as file_object:
        word_list = file_object.read().split()

    word_counts_dict = {}
    for word in word_list:
        if word in word_counts_dict:
            word_counts_dict[word] += 1
        else:
            word_counts_dict[word] = 1

    logger.info("Word count is a good way to begin processing text.")
    logger.info(f"Given text_simple.txt, the word_counts_dict = {word_counts_dict}")

    # IMPORTANT: Dictionary comprehesions - the preferred approach

    # Create a dictionary of word counts from a list of words
    # A dictionary is always key:value pairs
    # Say "I want word:count for each word in word_list"
    # Cast the result to a dictionary by using curly braces {}
    word_counts_dict2 = {word: word_list.count(word) for word in word_list}

    # Spend most of your practice on comprehensions - they are
    # key to transforming data in Python.

    logger.info("Given text_simple.txt and comprehensions,")
    logger.info(f"the the word_counts_dict2 = {word_counts_dict2}")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here
    illustrate_tuples()
    illustrate_sets()
    illustrate_dictionaries()

    logger.info("Add more logging statements to the code to see what happens.")
    logger.info("Explore enough to understand.")
    logger.info("Apply these skills to your own topic domain.")
    show_log()
