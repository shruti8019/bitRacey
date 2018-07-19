

import cx_Freeze



executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={'build_exe': {'packages':["pygame"],
                           "include_files":['mycar.png','car.png','crash.wav','Broadway.mp3']}},
    executables = executables

    )
