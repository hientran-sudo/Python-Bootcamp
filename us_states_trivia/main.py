import turtle

import pandas

screen = turtle.Screen()

screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)

 

turtle.shape(image)

 

#def get_mouse_click_coor(x,y):

#    print(x,y)

#

#turtle.onscreenclick(get_mouse_click_coor)

#turtle.mainloop()

data = pandas.read_csv(r"50_states.csv")

state_dict = data.to_dict()

guess_state = []

#game_is_on = True

 

while len(guess_state)<50:

    answer = screen.textinput(title=f"{len(guess_state)}/50 States Correct", prompt="What is another state name?")

    for i in range(0,49):

        if answer == state_dict["state"][i].lower():

            guess_state.append(answer)

            tim = turtle.Turtle()

            tim.hideturtle()

            tim.penup()

            tim.goto(state_dict["x"][i],state_dict["y"][i])

            tim.write(state_dict["state"][i], font=("Verdana", 10, "normal"))

 

#screen.exitonclick()

 
