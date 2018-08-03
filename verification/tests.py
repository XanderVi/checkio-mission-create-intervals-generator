"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [1, 2, 3, 4, 5, 7, 8, 12],
            "answer": [[1, 5], [7, 8], [12, 12]]
        },
        {
            "input": [1, 2, 3, 6, 7, 8, 4, 5],
            "answer": [[1, 8]]
        }
    ],
    "Extra": [
        {
            "input": [1, 3, 7],
            "answer": [[1,1], [3, 3], [7, 7]]
        },
        {
            "input": [7, 9, 10, 11, 12],
            "answer": [[7, 7], [9, 12]]
        },
        {
            "input": [1, 3, 5, 7],
            "answer": [[1, 1], [3, 3], [5, 5], [7, 7]]
        },
        {
            "input": [],
            "answer": []
        },
        {
            "input": [1],
            "answer": [[1, 1]]
        },
        {
            "input": [8,7],
            "answer": [[7,8]]
        },
        {
            "input": [6, 9, 1, 7],
            "answer": [[1, 1], [6, 7], [9, 9]]
        },
        {
            "input": [8, 9, 6, 7],
            "answer": [[6, 9]]
        }
    ]
}
