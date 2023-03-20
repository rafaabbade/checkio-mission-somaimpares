"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[1, 2, 3, 4, 5]],
            "answer": 9
        },
        {
            "input": [[2,4,6,8]],
            "answer": 0
        },
        {
            "input": [[]],
            "answer": 0
        }
    ],
    "Extra": [
        {
            "input": [[10,11,12,13,14,15]],
            "answer": 39
        },
    ]
}
