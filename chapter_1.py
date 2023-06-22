import helper_methods as hm
import os
import chapter_2 as c2


def ToC():
    print(
        """Intro 
        \nChapter 1: The Meeting 
        \nChapter 2: An unfortunate situation (?) 
        \n\nStairs: 
        \n\n--Sticks 
        \n--Outhouse: 
        \n----Bar 
        \n----Museum 
        \n----Mall 
        \n--Fireman's Den 
        \n\nDoor: 
        \n\n--Run 
        \n--Fight 
        \n--Give up 
        \n\nChapter 3: Presidential Affairs 
        \nChapter 4: title 
        \nChapter 5: title
        """
    )

    chapters = [
        "intro",
        "1",
        "chapter 1",
        "the meeting",
        "2",
        "chapter 2",
        "an unfortunate situation (?)",
        "stairs",
        "sticks",
        "outhouse",
        "fireman's den",
        "door",
        "run",
        "fight",
        "give up",
        "3",
        "chapter 3",
        "presidential affairs",
        "4",
        "chapter 4",
        "title",
        "5",
        "chapter 5",
        "title",
    ]

    cs = input("\nJump to chapter: ")

    if cs.lower() in chapters:
        print("\n")
        return cs
    else:
        os.system("cls")
        return ToC()


def intro():
    print(
        "Welcome to Bigby's Adventure! \n\nThis is an interactive journey in which you, the user, will be able to decide what Bigby does and alter the story in many ways! \n\nMake sure to follow all instructions and, most importantly, have fun!"
    )

    input("Press Enter to continue")

    return chapter_1()


def chapter_1():
    os.system("cls")

    text = [
        "Chapter 1: The Meeting",
        "Bigy was roaming around the plaza one day when he suddenly felt the urge to have a pizza.",
        "He went into a nearby pizzeria and ordered.",
        "As he was waiting, he saw this beautiful woman sitting by the window.",
        "The woman had flowing, blonde, hair and gorgeous, blue, eyes; Bigby was in love.",
        "He knew he had to go and talk to her, but he never gained the self-confidence he needed to approach women.",
        "He knew this to be true, so he had to come up with a different strategy.",
        "He saw the woman was eating a unique looking dish. He asked the cashier:",
        "'Excuse me madam, but the dish that that woman over there is eating looks quite delicious. Might I get her name so I can go over there and ask her what the dish is?'",
        "The cashier responded with 'I think she said her name was Sarah, but I'm not 100 percent sure.'",
        "That was good enough for Bigby. He went to the woman and said:",
        "'Excuse me, Sarah, what is that dish you are eating?'",
        "'Oh, it's squid-ink pasta.'",
        "Bigby said thank you and left in a hurry.",
    ]

    hm.pauser(text)

    input("Press enter to continue to the next chapter")

    return c2.chapter_2()
