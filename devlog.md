# Dev log

Since the exercise asks for explanation of ideas as well. So this file is to log ideas and thoughts

### 31-05-2018

Why is the max board width 7 - and not used when setting the range - and why is 7 passed to range when the doc says the upper bound of range is exclusive.

Need to check if changing the tests is allowed in the exercise? (would assume so)

...

Idea - pieces should probably inherit from an abstract base class.

...

Reading docs on unit tests - apparently should use assertEqual rather than assert ... == so can produce reports

...

Python has no switch statement apparently, Googling suggests using a dictionary of functions. However, both enums only have 2 values which means a series of if else staements is likely *more* performant than a lookup table

...

why does the chessboard add method set piece_color when this is a property of the pieces. I don't like setting it in 2 places

...

More thought 

- do we actually need capture and move as 2 separate move types, I'm not too sure of the rules of chess but can't you just compute what pieces are captured by if you move a piece on top of the other one.
- Also is it theoretically possible for a pawn to capture 2 pieces at once by en passant or whatever it is.
- SHould the move validator check if the move fails to get the player out of check

(this all might be out of scope for the exercise though...)