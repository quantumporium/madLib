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
    [ ] Have 5 multiples stories
        -> Each story have is unique ammount of part of speech (noun, verb, etc)
        -> Make the story comme up at random
    [ ] Get the input (part of speech) from the user
        -> stored them in an list/array
        -> Tell how much noun he will need to give (You will need to enter 3 nouns ...)
    [ ] Add the input(part of speech) to the predefined story
        -> Each input need to get use

    -=-=-=- testing -=-=-=-
    [ ] ????

    -=-=-=- note -=-=-=-
    - Each story will need to be its own function (can't find another way)
    - Testing function might be difficult (a lot of them will be non-pure function)
    - I should maybe do this in another file 

"""
# data structure
class story:
    def __init__(self, nbNoun, nbAdj, nbVerb, nbAdv, storyFunction):
        self.nbNoun = nbNoun
        self.nbAdj  = nbAdj
        self.nbVerb = nbVerb
        self.nbAdv = nbAdv
        self.storyFunction = storyFunction
        
        return

## function
### once upon a time story
def once_time(noun, adj, verb, adv):
    """
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

## initialising story object


class foo:
    def __init__(self, name):
        self.name = name
        print(self.name)

s = foo(once_time)

# s = once_time
s.name(noun = [1,2, 3] , adj = [1,2,3] , verb = [1], adv = [1]) 
## main Program loop
