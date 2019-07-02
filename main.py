from cate import *



@on_start
def say_hi():
    say("Hello world!")

@on_key(Keys.K_p)
def void():
    say(3)
    pause(1)
    say(2)
    pause(1)
    say(1)
    pause(1)
    say("LIFT OFF")

@on_key(Keys.K_k)
def do():
    say("hay")

@on_key(Keys.K_ESCAPE)
def quit():
    say("Are you sure you wanna quit?")

    k = wait_for(Keys.K_y, Keys.K_n)

    if k == Keys.K_y:
        say("Goodbye!")
        pause(2)
        exit()
    else:
        say("Good choice :)")

@on_key_down(Keys.K_a)
def toggleaxis():
    toggle_axis()


start()
