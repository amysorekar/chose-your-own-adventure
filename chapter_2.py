import os
import choices as c
import chapter_3
import helper_methods as hm


def chapter_2():
    os.system("cls")

    text = [
        "Chapter 2: An unfortunate situation (?)",
        "Bigby left the store kicking himself.",
        "'Why?' he kept asking himself.",
        "'Why must you be such an incompetent loser? Can't you do anything right?'",
        " He got mad and kicked a can in the road off into an alley.",
        "A few seconds later he heard a loud crashing noise and stopped in his tracks.",
        "'That's weird', he thought, 'the can was not big enough to make a crashing noise like that'.",
        "He went to go investigate.",
        "He slowly crept down the dark alley, wary of any danger that might be lurking.",
        "At the end of the alley, there was a staircase leading down and an open door to the right.",
        "Does he go through the DOOR or down the STAIRS?",
    ]

    hm.pauser(text)

    hm.make_choice(choice_dict, c.stairs_door)


def stairs():
    text = [
        "\nYou chose stairs.",
        "Bigby heads down the stairs and hits his head hard on the hidden overhang.",
        "A few minutes later he woke up, dazed. He got his bearings and continued on."
        "He got to a tunnel and followed it.",
        "The tunnel ends up turning into a canal about 15ft wide and very long.",
        "In the canal was a man sitting in a small raft. The man sees Bigby and says:",
        "'Hello my child. What brings you to my canal?'",
        "Bigby was confused.",
        "'Your canal? I didn't even know there was a canal that ran under the city! What are you doing down here?",
        "'I am the ruler of these grounds. Ask me to take you to a destination or kindly leave.'",
        "'Um, well. What destinations are there?'\n\n"
        "'You may visit the STICKS, the OUTHOUSE, or the FIREMAN'S DEN. You decide.'",
    ]

    return hm.run_choice(
        stair_door_go_back, c.sticks_outhouse_fireman_den, text, choice_dict
    )


def sticks():
    text = [
        "\n'So you have chosen the sticks. Please step into my gondola.",
        "Bigby proceeded to step onto the craft.",
        "'What is the 'sticks' anyway?'",
        "'A place of plenty. A cornucopia. All your wishes may be granted in the sticks.'",
        "'Wow, sounds pretty cool. What are you doing down here?'",
        "'I was banished here as a teenager. My father told me if I didn't marry the Princess by the time I was 16, he would send me to the canals for life.",
        "To marry the Princess, I needed the Ring of Ceylon. The ring was located in the Hills of Heaven; only accessible by completing the 'Hierarchy of 3'.",
        "'What's that?'",
        "'WELL IF YOU WOULD SILENCE YOURSELF FOR MORE THAN FOUR SECONDS I WOULD TELL YOU!'",
        "'...'",
        "'Thank you. Now, as I was saying:'",
        "'The Hierarchy of 3 is a coveted quest. Only the skilled of the skilled, the masters of the masterful, and sharpest of the sharp can even attempt this quest. I was at the top of my class in intelligence, fitness, and strength.",
        "'To start the quest, I first had to solve a puzzle to get the key to the entrance to the Hills of Heaven. Once there, I had to finish step 1: answer the question: What do you seek?",
        "'What was the answer?'",
        "'What also seeks me.'",
        "'Sounds fancy.'",
        "'Yes.'",
        "'What's the next part of the Hierarchy of 3?'",
        "'Step 2 was to defeat the monster they call Barnaby.'",
        "'Barnaby was an angel, tasked with protecting the world.'",
        "'He was stellar at his job, for a while, until the darkness came.'",
        "'Asmodel, a newer angel, was getting a lot of attention from the gods.'",
        "'He got more responsibility, more credit, and more exposure. Barnaby was furious.'",
        "'He tried to ignore his anger and continue carrying out his duty, but overtime his anger festered. The gods viewed Asmodel with more and more admiration by the day.'",
        "'One night, a demon named Norma visited Barnaby. She promised him immense power and control, but only if he released himself to the darkness.'",
        "'Normally, Barnaby would have said no immediately and banished Norma from the heavens. But after feeling the way he had been, he accepted Norma's offer with ease.'",
        "'Now Barnaby is one of the most powerful demons and few can even try to stop him.'",
        "Bigby asked, inquisitively:",
        "'Did you defeat him?'",
        "The man responded with a smirk:",
        "'I'm rowing this boat, aren't I?'",
        "'That's amazing! Wait, what was the final step?'",
        "'The final step was to choose between several chalices. One contained the ring, the others nothing. I chose poorly. A voice above told me I chose the wrong chalice and that the correct answer is found inside. I only got one chance to select a chalice, so my quest was over.'",
        "'What?? What does 'the correct answer is found inside' even mean?'",
        "'I didn't know for so long, but many years later, I realized 'inside' meant inside of me: my brain. Only the most special man is worthy of the Princess, and part of that worthiness is wanting to devote their lives to her. Truly wanting to be with her in their core. I didn't want that. I was only doing the quest because of the ultimatum my father gave me. And so, I failed the quest...and now I'm here.'",
        "'Wow. I'm sorry.'",
        "'Sit down ... We're here.'",
        "'WOAH! This place is beautiful! Has this always been down here?'",
        "'Of course. People have been thriving in the sticks for ages. You have never heard of it because it is only available to those who are enlightened. I brought you here with me, so you're able to see it, else it would be more canal.'",
        "'Wait, why did you bring me here? You don't even know me.'",
        "'I know all about you, Bigby Smallbum. We have been expecting you for quite some time.'",
        "'Who's we-'",
        "At that moment the trumpets played from the heavens a fanfare so beautiful it brought Bigby to tears. A group of beautiful women surrounded Bigby, offering him a special lotus fruit.",
        "He ate the fruit graciously and became entranced. The whole world was tinted in a golden shimmer. Bigby was in awe.",
        "After eating the fruit, he started to float up to the heavens and disappeared into the sun.",
        "You have reached the end of Bigby's story. ",
    ]

    return hm.ending(sticks_outhouse_fireman_den_go_back, text)


def outhouse():
    text = [
        "\n'So you have chosen the outhouse'",
        "'The outhouse is not a place for the weak. Are you sure?'",
        "'Yes. Take me to the outhouse.'",
        "'Very well. Please step into my gondola'",
        "Bigby proceeded to step onto the craft.",
        "'So what is the 'outhouse' anyway?'",
        "'The outhouse is a confluence of the fallen soldiers of heaven.'",
        "''Fallen soldiers'... what does that mean?'",
        "'The fallen soldiers are those who used to be guardians of heaven, but because of negligence, malfeasance, or politics, were banished from heaven. They all congregate in the outhouse because it's the only place where people understand what they've been through. Since the knowledge of their fall is public, everyone in the city treats them like dirt.'",
        "'Man that's terrible. I never knew about them. I don't think I've even met one'",
        "'That's because they hide from you. They know they won't be accepted, so they pretend to be someone else.'",
        "'Wow, sounds like a sad life. Anyway, what will we do in the outhouse?'",
        "'That is your decision. Though mostly the fallen congregate in the outhouse, it's open for everyone. There is plenty for one to do there. You can visit the main bar & pub, go see the museum, or visit the mall.'",
        "'Sweet. Have you ever been here before?'",
        "Many times. Many of the fallen are my friends. I met them in my quest for the Ring of Ceylon.'",
        "'What's the Ring of Ceylon?'",
        "'That's a story for another time ... Sit down, we're here.'",
        "The canal opened up into a large plot of land, fit with a park, a river, and numerous buildings; an underground city.",
        "Bigby exclaimed 'WOW! This place is amazing!'",
        "'Would you like to go to the BAR, MUSEUM, or MALL?'",
    ]

    return hm.run_choice(
        sticks_outhouse_fireman_den_go_back, c.bar_museum_mall, text, choice_dict
    )


def fireman_den():
    text = [
        "\nThe man said 'wrong choice you fool' and fireboarded Bigby.",
        "\n\nYou have reached the end of Bigby's journey.",
    ]

    return hm.ending(sticks_outhouse_fireman_den_go_back, text)


def museum():
    return


def mall():
    return


def bar():
    text = [
        "\n'I'm kind of fancying a drink. Let's go to the bar.'",
        "'Are you sure? It's only for the toughest of the tough; some of them eat nails for breakfast'",
        "'Nails for breakfast, that's not that tough.'",
        "'... without any milk.'",
        "Bigby was speechless. He gulped loudly and told the man he wanted to go anyway.",
        "Bigby was let off next to the bar. He stepped one foot inside and was hit in the head by a stray bullet.",
        "You have reached the end of Bigby's story. ",
    ]

    return hm.ending(bar_museum_mall_go_back, text)


def door():
    text = [
        "\nBigby opened the door and walked into an enormous party.",
        "It was like walking into the fifth grade classroom as a third grader.",
        "Bigby walked around amazed; he'd never been to a party so big.",
        "He walked around looking for something familiar and noticed the bar.",
        "He went over and ordered a drink.",
        "As he was waiting he noticed Sarah sitting a few seats over.",
        "Bigby received his drink and saw in the corner of his eye that Sarah was no longer sitting there.",
        "To his terror, he heard:",
        "'I know you, don't I?'",
        "Bigby was frozen in fear.",
        "He managed to mumble:",
        "'No, I don't think so.'",
        "'No, I do! You were that guy at the pizzeria earlier!'",
        "Bigby responded, embarrassed, 'Oh yeah, that's right.'",
        "'Why did you leave right after you asked me what I was eating? I wanted to talk to you more.'",
        "'I was ashamed. You were so beautiful with your blonde hair and blue eyes. I knew I didn't stand a chance.'",
        "'Oh stop that. You have as much of a chance as any other guy!'",
        "'Really?'",
        "'Yes!! Now, what are you doing here? I didn't take you for the party type.'",
        "'It's a funny story actually. I was in this weird canal thing and there was this guy an-'",
        "'HAHA! What are you talking about?? Canal?? There aren't any canals in this area.'",
        "'What do you mean? I was just in there. There was a guy and a gondola and sticks and stuff!'",
        "'You must've hit your head or something. I have lived here my entire life, I promise you there is not a single canal around here. It wouldn't even be possible, we live on a desert fault: any canal dug would be full of sand.'",
        "'But then what did I walk into?'",
        "Right at that moment, four armed guards burst through the door.",
        "'EVERYBODY GET ON THE GROUND! WE ARE LOOKING FOR BIGBY SMALLBUM!'",
        "Bigby stood up.",
        "'Yeah, that's me. What is all this about??'",
        "One of the officers shouted out:",
        "'You are under arrest for the murder of the president. Witnesses placed you at the scene and time of death.'"
        "'What?! This can't be!'",
        "He looked to Sarah:",
        "'I didn't do this, I swear'",
        "The officers started advancing. Bigby had to make a decision",
        "Does Bigby RUN, GIVE UP, or FIGHT?",
    ]

    hm.run_choice(
        stair_door_go_back,
        c.run_fight_give_up,
        text,
        choice_dict,
    )


def run():
    text = [
        "\nBigby scrambled for an exit.",
        "He saw an exit door across the room.",
        "'Sarah, come with me!'",
        "The two made a break for the exit. The officers chased after them but Bigby's and Sarah's weaving skills were unimaginable, and they promptly lost their pursuers.",
        "After they were safely outside, Sarah exclaimed 'Bigby oh my god! What's going on??'",
        "'I think I'm being framed. Come with me, we gotta get out of here. We can't go back to my apartment, they'll probably be waiting for me.'",
        "'Come to my place. I live around the corner.'",
        "----- a few minutes later -----",
        "Sarah exasperatedly said 'Ok, at least we're safe now. But, Bigby, what the hell is going on?!'",
        "'I couldn't tell you. 'Killed the president'?? I've never even seen the president. They must have gotten me confused with someone else.'",
        "'But you have a unique name, how could they mess that up?'",
        "Sarah and Bigby resorted to the internet.",
        "'What the fuck?' Bigby cursed, 'The man-who-killed-the-president's name is BIGBY BIGBUM!'",
        "'God that is unfortunate. What are you going to do?'",
        "'I think you mean what are WE going to do; and I'll tell you what: we're going to clear my name.'",
        "'That sounds good and all, but how are we supposed to do that?'",
        "'I'm not sure, but we'll figure it out. Come on, let's go.'",
    ]

    hm.next_chapter(run_fight_give_up_go_back, text, chapter_3.chapter_3)


def fight():
    text = [
        "\nBigby squared his stance.",
        "He knew that the officers were much more trained than him and wearing protective gear.",
        "He looked around for anything he could use as a weapon.",
        "He grabbed a beer bottle next to him and smashed in on the bar to make a dagger.",
        "The officers started to advance and Bigby prepared himself.",
        "The first officer lunged at him and Bigby weaved it and stabbed the officer in the side.",
        "The next officer came charging and Bigby dodged him and pushed him over the bar.",
        "The final two officers both swung at Bigby at the same time, but he ducked and they hit each other.",
        "'Bigby oh my god! What's going on??', Sarah exclaimed.",
        "'I think I'm being framed. Come with me, we gotta get out of here.'",
        "The two scurried out of the party and into the street.",
        "Bigby told Sarah 'We can't go back to my apartment, they'll probably be waiting for me.'",
        "'Come to my place. I live around the corner.'",
        "----- a few minutes later -----",
        "Sarah exasperatedly said 'Ok, at least we're safe now. But, Bigby, what the hell is going on?!'",
        "'I couldn't tell you. 'Killed the president'?? I've never even seen the president. They must have gotten me confused with someone else.'",
        "'But you have a unique name, how could they mess that up?'",
        "Sarah and Bigby resorted to the internet.",
        "'What the fuck?' Bigby cursed, 'The man-who-killed-the-president's name is BIGBY BIGBUM!'",
        "'God that is unfortunate. What are you going to do?'",
        "'I think you mean what are WE going to do; and I'll tell you what: we're going to clear my name.'",
        "'That sounds good and all, but how are we supposed to do that?'",
        "'I'm not sure, but we'll figure it out. Come on, let's go.'",
        "Just as the two stepped outside, 13 squad cars and a military jet pulled up right in front of Sarah's apartment.",
        "'Bigby Smallbum, you are under arrest for the murder of 4 special forces officers and the president.'",
        "You have reached the end of Bigby's story.",
    ]

    hm.ending(run_fight_give_up_go_back, text)


def give_up():
    text = [
        "\nBigby quietly put his hands up",
        "The officers came to put cuffs on him.",
        "He looked at Sarah, 'I didn't do this'.",
        "'Bigby please! Fight back!'",
        "'There's no point. I'm outmanned and outgunned.'",
        "The officers came and arrested Bigby.",
        "You have reached the end of Bigby's story.",
    ]

    hm.ending(run_fight_give_up_go_back, text)


def stair_door_go_back():
    hm.make_choice(choice_dict, c.stairs_door)


def sticks_outhouse_fireman_den_go_back():
    hm.make_choice(choice_dict, c.sticks_outhouse_fireman_den)


def bar_museum_mall_go_back():
    hm.make_choice(choice_dict, c.bar_museum_mall)


def run_fight_give_up_go_back():
    hm.make_choice(choice_dict, c.run_fight_give_up)


choice_dict = {
    "stairs": stairs,
    "door": door,
    "sticks": sticks,
    "outhouse": outhouse,
    "fireman's den": fireman_den,
    "bar": bar,
    "museum": museum,
    "mall": mall,
    "run": run,
    "fight": fight,
    "give up": give_up,
}
