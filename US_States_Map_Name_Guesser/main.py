import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Map")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state_names = data["state"]
all_states = state_names.to_list()
print(all_states)
crt_state=[]

while len(crt_state)<len(all_states):
    guess = screen.textinput(f"{len(crt_state)}/50 States Correct", "Enter a State Name?").title()
    print(guess)
    if guess == "Exit":
        unknown_states = []
        for state in state_names:
            if state not in crt_state:
                unknown_states.append(state)
        new_data=pandas.DataFrame(unknown_states)
        new_data.to_csv("unknown_states.csv")
        break
    if guess in all_states:
        crt_state.append(guess)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_info = data[data["state"] == guess]
        t.goto(state_info.x.item(), state_info.y.item())
        t.write(guess)
        print(len(crt_state))
print(f"You answered {crt_state} States correctly")




