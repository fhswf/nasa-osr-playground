import mpg123

import os

file = "file.mp3"
os.system("mpg123 " + file)




# import winsound
# Play Windows exit sound.
# winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

# Probably play Windows default sound, if any is registered (because
# "*" probably isn't the registered name of any sound).
# winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
