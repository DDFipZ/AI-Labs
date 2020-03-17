A = "A"
B = "B"

Environment = {
    A: "Dirty",
    B: "Dirty",
    "Current": A
}


def REFLEX_VACUUM_AGENT(loc_st):  #Determine Action
    if loc_st[1] == "Dirty":
        return "Suck"
    if loc_st[0] == A:
        return "Right"
    if loc_st[0] == B:
        return "Left"


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
    print("Current\tNew")
    print("location status action location status")
    for i in range(1, n):
        (location, status) = Sensors()