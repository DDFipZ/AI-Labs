A = "A"
B = "B"
C = "C"
D = "D"

Environment = {
    A: "Dirty",
    B: "Dirty",
    C: "Dirty",
    D: "Dirty",
    "Current": A
}


def REFLEX_VACUUM_AGENT(loc_st):  #Determine Action
    if loc_st[1] == "Dirty":
        return "Suck"
    if loc_st[0] == A:
        return "Right"
    if loc_st[0] == B:
        return "Down"
    if loc_st[0] == D:
        return "Left"
    if loc_st[0] == C:
        return "Up"


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
    elif action == "Right" and location == C:
        Environment["Current"] = D
    elif action == "Left" and location == D:
        Environment["Current"] = C
    elif action == "Up" and location == D:
        Environment["Current"] = B
    elif action == "Up" and location == C:
        Environment["Current"] = A
    elif action == "Down" and location == A:
        Environment["Current"] = C
    elif action == "Down" and location == B:
        Environment["Current"] = D


def run(n, make_agent):  #Run the agent through n steps
    print("Current \tNew")
    print("location status action location status")
    for i in range(1, n):
        (location, status) = Sensors() #Sense Environment before action
        print("{:12s}{:8s}".format(location, status), end = "")
        action = make_agent(Sensors())
        Actuators(action)
        (location, status) = Sensors() #Senses the Environment before action
        print("{:8s}{:12s}{:8s}".format(action, location, status))


run(20, REFLEX_VACUUM_AGENT)