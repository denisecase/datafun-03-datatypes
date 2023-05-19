"""

Purpose: Illustrate options for working with numeric lists in Python.

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules and a local logger module.

"""

# import from standard library
import statistics
import math

# import from local files
from util_datafun_logger import setup_logger

# Set up logging .............................................

# Call the setup_logger function
logger, logname = setup_logger(__file__)

# Define shared data ..........................................

# define a variable with some univariant data
# (one varabile, many readings)
score_list = [
    105,
    129,
    87,
    86,
    111,
    111,
    89,
    81,
    108,
    92,
    110,
    100,
    75,
    105,
    103,
    109,
    76,
    119,
    99,
    91,
    103,
    129,
    106,
    101,
    84,
    111,
    74,
    87,
    86,
    103,
    103,
    106,
    86,
    111,
    75,
    87,
    102,
    121,
    111,
    88,
    89,
    101,
    106,
    95,
    103,
    107,
    101,
    81,
    109,
    104,
]

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
xtimes_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
yvalues_list = [2, 5, 8, 20, 21, 23, 24, 27, 30, 31, 31, 32]

# Define functions ........................................


def illustrate_list_statistics():
    """This function illustrates descriptive statistics for a numric list."""

    logger.info(f"score_list: {score_list}")

    # Descriptive: Averages and measures of central tendency
    # Use statisttics module to get mean, median, mode
    # for a values list

    mean = statistics.mean(score_list)
    median = statistics.median(score_list)
    mode = statistics.mode(score_list)

    logger.info(f"mean: {mean}")
    logger.info(f"median: {median}")
    logger.info(f"mode: {mode}")

    stdev = statistics.stdev(score_list)
    variance = statistics.variance(score_list)

    logger.info(f"stdev: {stdev}")
    logger.info(f"variance: {variance}")


def illustrate_list_correlation_and_prediction():
    """This function illustrates correlation and prediction for a numric list."""

    logger.info(f"xtimes_list: {xtimes_list}")
    logger.info(f"yvalues_list: {yvalues_list}")

    # Descriptive: Measures of correlation
    # Use two numerical lists of the same size
    # Use statisttics module to get correlation between list1 and list2

    correlationxy = statistics.correlation(xtimes_list, yvalues_list)
    logger.info(f"correlation between x and y: {correlationxy}")

    # Predictive: Machine Learning - Linear Regression
    # If the corrlation is close to 1.0, then the data is linearly related
    # If so, use statistics module to get linear regression for list1 and list2
    # This is a form of supervised machine learning - it uses all known data
    # Use the slope and intercept and an unknown (future) x to predict a y value
    # Python functions can return multiple values

    slope, intercept = statistics.linear_regression(xtimes_list, yvalues_list)
    logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")

    # Once we have learned the slope and intercept
    # of the best-fit straight line through the data,
    # we can use it to make predictions

    # Predict the y value for a given x value outside the range of the data

    x_max = max(xtimes_list)
    newx = x_max * 1.5  # predict for a future x value

    # Use the slope and intercept to predict a y value for the future x value
    # y = mx + b

    newy = slope * newx + intercept

    logger.info("We predict that when x = {newx}, y will be about {newy}")


def illustrate_list_built_in_functions():
    # BUILT-IN FUNCTIONS ......................................
    # Many built-in functions work on lists
    # try min(), max(), len(), sum(), sorted(), reversed()

    # Using the score list provided above, do the following:
    # Calcuate the max and min scores
    max_value = max(score_list)
    min_value = min(score_list)

    logger.info(f"Given score list: {score_list}")
    logger.info(f"The max() is {max_value}")
    logger.info(f"The min() is {min_value}")

    # Calculate the length of the list
    len_list = len(score_list)
    logger.info(f"The len() is {len_list}")

    # Calculate the sum of the list
    sum_list = sum(score_list)
    logger.info(f"The sum() is {sum_list}")

    # Calculate the average of the list
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list}")

    logger.info(f"Given score list: {score_list}")
    # Return a new list soreted in ascending order
    asc_scores = sorted(score_list)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_scores}")

    # Return a new list soreted in descending order
    desc_scores = sorted(score_list, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_scores}"
    )


def illustrate_list_methods():
    """This function illustrates methods that can be called on a list"""

    """

     LIST METHODS ............................................... 

     Here are some common methods that operate on an instance of a list.

     append(x): Add an item to the end of the list.
     extend(iterable): Add all the items from an iterable (such as another list)
          to the end of the list.
     insert(i, x): Insert an item at a given position.
     remove(x): Remove the first occurrence of an item.
     pop([i]): Remove the item at the given position in the list, 
     and return it. If no index is specified, 
     removes and returns the last item in the list.
     clear(): Remove all items from the list.
     index(x[, start[, end]]): Return the index of the first occurrence of
          an item.
     count(x): Return the number of occurrences of an item.
     sort(key=None, reverse=False): Sort the items in the list 
          in ascending order.
     reverse(): Reverse the order of the items in the list.
     copy(): Return a shallow copy of the list.

     """

    # append an item to the end of the list
    lst = [1, 2, 3]
    lst.append(4)

    # extend the list with another list
    lst.extend([4, 5, 6])

    # insert an item at a given position (0 = first item)
    i = 0
    newvalue = 42
    lst.insert(i, newvalue)

    # remove an item
    item_to_remove = 42
    lst.remove(item_to_remove)

    # Count how many times 111 appears in the list
    ct_of_111 = score_list.count(111)

    # Sort the list in ascending order using the sort() method
    asc_scores2 = score_list.sort()

    # Sort the list in descending order using the sort() method
    desc_scores2 = score_list.sort(reverse=True)

    # Copy the list to a new list
    new_scores = score_list.copy()
    logger.info(f"new_scores is: {new_scores}")

    # Remove the first item from the new list
    # The first item in a list is at index 0
    # Think of it as an offset from the beginning of the list
    first = new_scores.pop(0)
    logger.info(
        f"Popped the first (index=0): {first} and now, new_scores is: {new_scores}"
    )

    # Remove the last item from the new list
    # The last item in a list is at index -1
    last = new_scores.pop(-1)
    logger.info(
        f"Popped the last (index=-1): {last} and now, new_scores is: {new_scores}"
    )

    # Remove the item at index 3 from the new list
    fourth = new_scores.pop(3)
    logger.info(
        f"Popped the fourth (index=3): {fourth} and now, new_scores is: {new_scores}"
    )


def illustrate_list_transformations():
    """This function illustrates transformations that can be applied to a list"""

    logger.info("Score list: {score_list}")

    # TRANFORMATIONS ............................

    # FILTER and MAP are critical tranformations in big data applications

    # Use the built-in function filter() anywhere you need to filter a list
    # Filter the new list to only include scores greater than 100
    # You could pass in a named function, but honestly this is easier
    # Say "KEEP x such that x > 100 is True" given score_list
    # Cast the result using square brackets to get back a list
    scores_over_100 = [filter(lambda x: x > 100, score_list)]
    logger.info(f"Scores over 100: {scores_over_100}")

    # Use the built-in function map() anywhere you need to transform a list

    # Map each element to its square
    # Say "map x to x squared" given score_list
    # Cast the result using square brackets to get a list
    doubled_scores = [map(lambda x: x * 2, score_list)]
    logger.info(f"Doubled scores: {doubled_scores}")

    # Map each element to its square root
    # Say "map x to the square root of x" given score_list
    # remember to cast the result to a list (using square brackets)
    sqrt_scores = map(lambda x: math.sqrt(x), score_list)
    logger.info(f"Square root of scores: {sqrt_scores}")

    # Map each element (radius) to its area
    radius_list = [1, 2, 3, 4, 5]
    logger.info(f"Radius list: {radius_list}")
    # Say "map r to pi r squared" given radius_list
    # cast the result to a list using square brackets
    area_list = [map(lambda r: math.pi * r * r, radius_list)]
    logger.info(f"Area of circles: {area_list}")


def illustrate_list_comprehensions():
    """This function illustrates list comprehensions"""

    logger.info("Score list: {score_list}")

    # TRANFORMATIONS - Using List Comprehensions
    # List comprehensions are a concise way to create lists
    # They work like map and filter, but are more concise
    # They are the preferred "pythonic" way to do transformations
    # They are faster than map / filter - it's quite impressive when you master them!

    # With comprehensions, we start with what we WANT
    # Filter the new list to only include scores greater than 100
    # Say "KEEP x (for each x in score_list) IF  x > 100"
    # Cast the result to a list using square brackets

    scores_over_100 = [x for x in score_list if x > 100]
    logger.info("Scores over 100 (using list comprehensions!): {scores_over_100}")

    # Try again "keep x (for each x in score_list) IF  x < 42"
    scores_under_42 = [x for x in score_list if x < 42]
    logger.info("Scores under 42 (using list comprehensions!): {scores_under_42}")

    # Map each element to its square
    # Say "give me x squared (for each x in score_list)"
    # Cast the result to a list using square brackets

    doubled_scores = [x * 2 for x in score_list]
    logger.info("Doubled scores (using list comprehensions!): {doubled_scores}")

    # Map each element to its square root
    # Say "give me the square root of x (for each x in score_list)"
    # Cast the result to a list using square brackets
    sqrt_scores = [math.sqrt(x) for x in score_list]

    radius_list = [1, 2, 3, 4, 5]
    logger.info(f"Given radius_list: {radius_list}")

    # Map each element (radius) to its area
    # Say "give me pi r squared (for each r in radius_list)"
    # Cast the result to a list using square brackets
    area_list = [math.pi * r * r for r in radius_list]
    logger.info(f"Area of circles: {area_list}")

    # Map each element (radius) to its circumference
    # Say "give me 2 pi r (for each r in radius_list)"
    # Cast the result to a list using square brackets
    circumference_list = [2 * math.pi * r for r in radius_list]
    logger.info(f"Circumference of circles: {circumference_list}")

    logger.info("Mastering comprehesions is a valuable skill for data scientists.")
    numbers = [1, 2, 3, 4]
    squares = [x**2 for x in numbers]
    logger.info(f"Given numbers: {numbers}")
    logger.info(f"Squares of numbers using [x ** 2 for x in numbers] is {squares}")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here (see instructions)
    illustrate_list_statistics()
    illustrate_list_correlation_and_prediction()
    illustrate_list_built_in_functions()
    illustrate_list_methods()
    illustrate_list_transformations()
    illustrate_list_comprehensions()

    logger.info("Add more logging statements to the code to see what happens.")
    logger.info("Explore enough to understand.")
    logger.info("Apply these skills to your own topic domain.")

    show_log()


# Why do we wrap parts of our code into functions?
# Because when you write good functions, you can reuse them in other scripts.
# Just like we import our logger and reuse the setup_logger() function.
# You can easily build a set of resuable functions to support your topic domain.

# For example, if your topic domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a lists of favorite artists.

# When you write reusable functions for your domain, you can
# import the module with your utility functions into other scripts
# and use them for free.
# This is excellent practice.
