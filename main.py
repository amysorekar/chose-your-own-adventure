import os
import chapter_1 as c1
import chapter_2 as c2
import chapter_3 as c3
import helper_methods as hm


def Choose_your_own_adventure(chapters):
    os.system("cls")
    ToC = c1.ToC()

    if ToC.lower() in chapters:
        os.system("cls")
        chapters[ToC]()

    if hm.restart() == "story over":
        Choose_your_own_adventure(chapters_dict)


chapters_dict = {
    "intro": c1.intro,
    "chapter 1": c1.chapter_1,
    "1": c1.chapter_1,
    "the meeting": c1.chapter_1,
    "chapter 2": c2.chapter_2,
    "2": c2.chapter_2,
    "an unfortunate situation (?)": c2.chapter_2,
    "stairs": c2.stairs,
    "sticks": c2.sticks,
    "outhouse": c2.outhouse,
    "bar": c2.bar,
    "museum": c2.museum,
    "fireman's den": c2.fireman_den,
    "door": c2.door,
    "run": c2.run,
    "fight": c2.fight,
    "give up": c2.give_up,
    "chapter 3": c3.chapter_3,
    "3": c3.chapter_3,
    "presidential affairs": c3.chapter_3,
}

Choose_your_own_adventure(chapters_dict)
