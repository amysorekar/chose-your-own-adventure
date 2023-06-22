import time


def pauser(text):
    """Prints out the line every X seconds

    Args:
        text (list): The story
    """
    for line in text:
        print(line)
        last_enter_time = time.time()

        while True:
            if time.time() - last_enter_time > 0.1:
                print("")
                break

    return


def go_back_prompt(function):
    """Asks the user if they want to go back to the previous choice

    Args:
        function: the go back function to be called

    Returns:
        the go back function if the user chooses to go back,
        nothing if the user chooses to continue
    """
    print("\nDo you wish to choose another path? Y/N")
    choice = input("Choice: ")

    if choice.lower() == "y":
        return function()

    return


def make_choice(dictionary, choice_function):
    """Calls the choice function of the given choice
    and calls that choice's function

    Args:
        dictionary: A dictionary of choices and their functions
        choice_function: the choice function to be called

    Returns:
        The function of the choice that was called
    """
    c = (
        choice_function()
    )  # saves the result to c everytime it's called. shouldn't be doing that

    if c in dictionary:
        return dictionary[c]()


def run_choice(go_back_function, choice, text, dictionary):
    """Runs the choice function and returns the
    function of the choice that was called

    Args:
        go_back_function: the go back function
        choice: the choice function
        text: the story

    Returns:
        The choice function of the choice given
    """
    go_back_prompt(go_back_function)
    pauser(text)

    return make_choice(dictionary, choice)


def ending(go_back_function, text):
    """For when a choice ends the story. Prompts the user
    to return to the menu

    Args:
        go_back_function: a go back function
        text: the story

    Returns:
        a number for the main method.
    """
    go_back_prompt(go_back_function)

    pauser(text)

    input("Press enter to continue to the menu")

    return restart()


def restart():
    return "story over"


def next_chapter(go_back, text, chapter):
    go_back_prompt(go_back)
    pauser(text)

    input("Press enter to continue to the next chapter")
    return chapter()


def two_options(one, two):
    while True:
        choice = input(one + " or " + two + ": ")

        if choice.lower() == str(one):
            return one

        elif choice.lower() == str(two):
            return two


def three_options(one, two, three):
    while True:
        choice = input(one + ", " + two + ", or " + three + ": ")

        if choice.lower() == str(one):
            return one

        elif choice.lower() == str(two):
            return two

        elif choice.lower() == str(three):
            return three
