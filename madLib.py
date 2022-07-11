#!/usr/bin/python3
""" -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    | author:           quantumporium   |
    | email:            quantum@email   |
    | name software:    madLib (for py) |
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

    -> Example usage
    choose a noun:
    choose a verb:
    choose an adjective: 

    ***** Here you mad lib! *****
    There were some time an {noun} who was
    {verb} and he like a really {adjective} object.
    He like is so much that .......

    -=-=-=- functinality -=-=-=-
    [ ] Have 4 multiples stories
        -> Each story have is unique ammount of part of speech (noun, verb, etc)
        -> Make the story comme up at random
    [+] Get the input (part of speech) from the user
        -> stored them in an list/array
        -> Tell how much noun he will need to give (You will need to enter 3 nouns ...)
    [+] Add the input(part of speech) to the predefined story
        -> Each input need to get use

    -=-=-=- testing -=-=-=-
    [ ] ????

    -=-=-=- note -=-=-=-
    - Each story will need to be its own function (can't find another way)
    - Testing function might be difficult (a lot of them will be non-pure function)
    - I should maybe do this in another file 

"""
# Import library
import random as rd

# data structure
class story:
    def __init__(self, nbNoun, nbAdj, nbVerb, nbAdv, storyFunction):
        self.nbNoun = nbNoun
        self.nbAdj  = nbAdj
        self.nbVerb = nbVerb
        self.nbAdv = nbAdv
        self.storyFunction = storyFunction
        # first the value represent the nb of item for each part of speech then it contain the actual nb 
        # of item for each part of speech

    def create_story(self):
        self.storyFunction( noun = self.nbNoun, adj = self.nbAdj, verb = self.nbVerb, adv = self.nbAdv)
        return

## function
### once upon a time story
def once_time(noun, adj, verb, adv):
    """
    name: once_upon_time
    number noun = 3 
    number adj = 3
    number verb = 1
    number adv = 1

    """

    story = """
Once upon a time, there was a {noun[0]}. The {noun[0]} was very {adj[0]}. He lived in a {adj[1]} town named {noun[1]}. Legend is said that no one was more {adj[0]} and {adj[2]} then {noun[0]} in is town. {noun[0]} add an {noun[2]} and together they go on a {adv[0]} {verb[0]}.
    """
    print( story.format(noun = noun, adj = adj, verb = verb, adv = adv) )
    return

once_upon_time = story( nbNoun = 3, nbAdj = 3, nbVerb = 1, nbAdv = 1, storyFunction = once_time)
def since_dawn(noun, adj, verb, adv):
    """
    name: since the dawn of time
    nb noun: 4
    nb adj : 1
    nv verb: 1
    nb adv : 
    """
    
    story = """
Since the dawn of {noun[0]}, the clan of {noun[1]} was in a war with the clan of {noun[2]}. Because they  they didn't like them. This dislike started begin  when two member of the clan of {noun[1]} {verb[0]} a really important item from the leader of the other clan. This item was an {adj[0]} {noun[3]} and was the most precious item of the clan of {noun[2]}. """
    
    print( story.format(noun = noun, adj = adj, verb = verb, adv = adv) )
    return

since_the_dawn = story( nbNoun = 4, nbAdj = 1, nbVerb = 1, nbAdv = 0, storyFunction = since_dawn )
def yesterday( noun, adj, verb, adv):
    """
    name   : Yesterday
    nb noun: 3
    nb adj : 1
    nb verb: 1
    nb adv : 2
    """

    story = """
Yesterday , {noun[0]} and is {adj[0]} {noun[1]} went on a {verb[0]}. They decided to go for a {verb[0]} because they weren't feeling well. They failed their {noun[2]} exam and felt {adv[0]} bad because of it. But they weren't still totaly defeated by it. They decided that they will work very hard to the next exam in order to {adv[1]} pass it.
"""

    print( story.format(noun = noun, adj = adj, verb = verb, adv = adv) )
    return
## initialising story object
yesterday_they_did = story( nbNoun = 3, nbAdj = 1, nbVerb = 1, nbAdv = 2, storyFunction = yesterday )

def it_was_day( noun, adj, verb, adv):
    """
    noun: it was a day
    nb noun: 1
    nb adj : 1
    nb verb: 1
    nb adv : 1

    """

    story = """
It was a {adj[0]} day when I decied to go for a {verb[0]}. I decided to go for a {verb[0]} because I was tired of not feeling good. I know that taking a {verb[0]} cheer me. I saw {noun[0]} during my {verb[0]} and it made me {adv[0]} happy.
    
    """
    print( story.format(noun = noun, adj = adj, verb = verb, adv = adv) )
    return

it_was_a_day = story( nbNoun = 1, nbAdj = 1, nbVerb = 1, nbAdv = 1, storyFunction = it_was_day)

## array to store the object of the story
library_story = [ once_upon_time, it_was_a_day, yesterday_they_did, since_the_dawn]
## other function - mostly utilities
def get_part_speech(storyObject):
    userNoun, userAdj, userVerb, userAdv = [], [], [], []

    print("-=-=-=- Noun -=-=-=-")
    print(f"[INFO] you will need to enter {len(range(storyObject.nbNoun))} nouns")
    for item in range(storyObject.nbNoun):
        userNoun.append(input("Enter a noun: "))

    print("-=-=-=- Adj  -=-=-=-")
    print(f"[INFO] you will need to enter {len(range(storyObject.nbAdj))} adjectives")
    for item in range(storyObject.nbAdj):
        userAdj.append(input("Enter a adjective: "))

    print("-=-=-=- Verb -=-=-=-")
    print(f"[INFO] you will need to enter {len(range(storyObject.nbVerb))} verbs")
    for item in range(storyObject.nbVerb):
        userVerb.append(input("Enter a verb: "))

    print("-=-=-=- Adv  -=-=-=-")
    print(f"[INFO] you will need to enter {len(range(storyObject.nbAdv))} adverbs")
    for item in range(storyObject.nbAdv):
        userAdv.append(input("Enter a adverb: "))
        

    return userNoun, userAdj, userVerb, userAdv

def choose_rd_story(library_story):
    rd_index = rd.randint(0, len(library_story) - 1)
    return library_story[rd_index]

## main Program loop
if __name__ == "__main__":
    print("********** WELCOME TO MADLIBS PYTHON **********")
    
    random_story = choose_rd_story(library_story)
    part_speech = get_part_speech( storyObject = random_story )

    random_story.nbNoun = part_speech[0] 
    random_story.nbAdj = part_speech[1]
    random_story.nbVerb = part_speech[2]
    random_story.nbAdv = part_speech[3]

    random_story.create_story()

