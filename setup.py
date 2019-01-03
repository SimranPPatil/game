import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="Echo and Narcissisus",
    options={"build_exe": {"packages":["pygame", "time"],
                           "include_files":["1.jpg", "2.jpg", "b3.jpg", "b4.jpg","cb.png", "chatbubble.png", "e1.png", "e2.png", "e3.png", "e4.png", "e5.png", "echo.png", "m2.jpg", "m3.jpg", "mountains.jpeg"],
                           }
                           },
    executables = executables
    )
