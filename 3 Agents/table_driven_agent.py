A = "A"
B = "B"
percepts = []
table = {
    ((A, "Clean"),): "Right",
    ((A, "Dirty"),): "Suck",
    ((B, "Clean"),): "Left",
    ((B, "Dirty"),): "Suck",

    ((A, "Clean"), (A, "Clean")): "Right",
    ((A, "Clean"), (A, "Dirty")): "Suck",
    ((A, "Dirty"), (B, "Clean")): "Left",
    ((A, "Clean"), (B, "Dirty")): "Suck",

    ((B, "Clean"), (B, "Clean")): "Left",
    ((B, "Clean"), (B, "Dirty")): "Suck",
    ((B, "Dirty"), (A, "Clean")): "Right",
    ((B, "Clean"), (A, "Dirty")): "Suck",

    #...
    ((A, "Clean"), (A, "Clean"), (A, "Clean")): "Right",
    ((A, "Clean"), (A, "Clean"), (A, "Dirty")): "Suck",
    ((A, "Clean"), (A, "Dirty"), (B, "Clean")): "Left",

    ((B, "Clean"), (B, "Clean"), (B, "Clean")): "Left",
    ((B, "Clean"), (B, "Clean"), (B, "Dirty")): "Suck",
    ((B, "Clean"), (A, "Dirty"), (B, "Clean")): "Left",
    ((B, "Clean"), (B, "Clean"), (A, "Dirty")): "Suck"

    #...

}


def LOOKUP(percepts, table): # Lookup appropiate action for percepts
    action = table.get(tuple(percepts))
    return action


def TABLE_DRIVEN_AGENT(percept): # Determine action based on table and percepts
    percepts.append(percept) # Add percept
    action = LOOKUP(percepts, table) # Lookup appropiate action for percepts
    return action


def run():  # run agent on several sequential percepts
    print("Action\tPercepts")
    print(TABLE_DRIVEN_AGENT((A, "Dirty")), "\t", percepts)

    print(TABLE_DRIVEN_AGENT((B, "Clean")), "\t", percepts)


run()