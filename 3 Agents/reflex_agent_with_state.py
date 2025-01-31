A = "A"
B = "B"
state = {}
action = None
model = {A: None, B: None} #initially ignorant


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


def UPDATE_STATE(state, action, percept):
    (location, status) = percept
    state = percept
    if model[A] == model[B] == "Clean":
        state = (A, B, "Clean")
    model[location] = status
    return state


def REFLEX_AGENT_WITH_STATE(percept):
    global state, action #fetches variables out of method
    state = UPDATE_STATE(state, action, percept)
    rule = RULE_MATCH(state, rules)
    action = Rule_Action[rule]
    return action


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


run(10, REFLEX_AGENT_WITH_STATE)