"""

The main.py file is the 'center' of all python file

"""

import Bash.bash as bash
import os


# get all python file in Script file and execute each
os.chdir('Script')
allScript = os.listdir()

for script in allScript:
    exec(open(script).read())

# infinite running the bash
while True:
    bash.run()
