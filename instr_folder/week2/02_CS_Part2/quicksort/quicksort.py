def quicksort(list):


def assertion(actualAnswer, expectedAnswer):
    print("Your answer:    " + str(actualAnswer))
    print("Expcted answer: " + str(expectedAnswer))
    print(actualAnswer == expectedAnswer)

assertion(quicksort([4, 2, 5, 8, 6]), [2, 4, 5, 6, 8])
