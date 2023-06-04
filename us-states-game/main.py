import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
# image = "blank_states_img.gif"

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
data = pandas.read_csv('50_states.csv')
all_states = data["state"].to_list()
Guessed_states = []
while len(Guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in Guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        Guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
