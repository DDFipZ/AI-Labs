A = "A"
B = "B"
Rule_Action = {
    1: "Suck",
    2: "Right",
    3: "Left",
    4: "NoOp"
}
rules = {
    (A, "Dirty"): 1,
    (B, "Dirty"): 1,
    (A, "Clean"): 2,
    (B, "Clean"): 3,
    (A, B, "Clean"): 4
}
Environment = {
    A: "Dirty",
    B: "Dirty",
    "Current": A
}


def INTERPRET_INPUT(input):
    return input


def RULE_MATCH(state, rules):
    rule = rules.get(tuple(state))
    return rule


def SIMPLE_REFLEX_AGENT(percept): #Gets percept from Sensors, in this case its current location and if it is dirty or clean
    state = INTERPRET_INPUT(percept) #Interprets the input
    rule = RULE_MATCH(state, rules) #finds the rule that goes with the state
    action = Rule_Action[rule] #from the rule, it finds the action


def Sensors():  #Sense Environment
    location = Environment["Current"]
    return location, Environment[location]


def Actuators(action):  #Modify Environment
    location = Environment["Current"]
    if action == "Suck":
        Environment[location] = "Clean"
    elif action == "Right" and location == A:
        Environment["Current"] = B
    elif action == "Left" and location == B:
        Environment["Current"] = A


def run(n, make_agent):  #Run the agent through n steps
    print("Current \tNew")
    print("location status action location status")
    for i in range(1, n):
        (location, status) = Sensors() #Sense Environment before action
        print("{:12s}{:8s}".format(location, status), end = "")
        action = make_agent(Sensors())
        Actuators(action)
        (location, status) = Sensors() #Senses the Environment after action
        print("{:8s}{:12s}{:8s}".format(action, location, status))


run(10, SIMPLE_REFLEX_AGENT)