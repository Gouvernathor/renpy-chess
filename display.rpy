# board must be a chess.Board object
# the colors are the colors of the squares
# action_function is a function that takes a square as argument and returns an action, or None
# it can be passed a dict.get bound method, for example
# it can also be passed Return, or functools.partial(SetScreenVariable, "clickedonsquare"), or functools.partial(functools.partial(renpy.notify))
# properties_function is a function that takes a square as argument and returns a dict of properties to be passed to the buttons, or None
# the dicts' keys and values must be valid style property names and values taken by buttons
# the dict may contain the "action" key, in which case it will override the action_function's result (it will still be called though)
screen chess_board(board=chess.Board.empty,
    white_board_color=chess.WHITE_BOARD_COLOR, black_board_color=chess.BLACK_BOARD_COLOR,
    action_function={}.get,
    properties_function={}.get,
    ):
    grid 8 8:
        align (.5, .5)
        at transform:
            fit "contain"
        for square, rownbr, colnbr, piece in board.enumerate():
            fixed:
                xysize (100, 100) # arbitrary, will be scaled by fit contain
                if (rownbr+colnbr)%2:
                    add white_board_color
                else:
                    add black_board_color

                button:
                    xysize (1., 1.)
                    style "default"
                    if piece is not None:
                        add piece.displayable() align (.5, .5) fit "contain"
                    action action_function(square)
                    properties properties_function(square)
