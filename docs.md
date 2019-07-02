# Decorators (events)

* `@on_start`:
Same as Scratch's `On Start` block. Runs the functions when the program starts. The order is the same as the order the functions were declared in.

* `@on_key(Keys.key)`
This adds an event handler for a key. `Keys` contains all the keys `pygame` offers.

* `@on_key_down(Keys.key)`
This event handler fires when a key is down.


Note: `on_key_down` only fires once, even if the key is held. `on_key` will keep firing until the key is released.


# Built-in functions

* `say(msg)`
Same as Scratch's  `say`. Show `msg` on screen.

* `exit()`
Quit the program.

* `start()`
Start the program. It will run until `exit()` is called.

* `pause(time)`
Sleep the execution of the program for `time` amount of seconds.

* `wait_for(*keys)`
Wait for a key in `keys` to be pressed. Return the pressed key.

* `set_text_color(color)`
Set the text color.

* `toggle_axis`
Toggle axis visibility.

* `show_axis(bool)`
Set the axis visibility to `bool`.

# To do:
Input, move functions, sound functions, make it look nicer, wait, print for x seconds.

* `ask()`
Allows user input, blocking.
