**IMPORTANT**: the development of this project was stalled for a bit because i had more important stuff to do, i am going to start development again, but with news about microsoft aquiring github i will be moving the project to https://gitlab.com/bluetechgirl/raspi-watch

# raspi-watch
a simple interface for a raspberry pi zero based smart watch built with python 3 and tkinter. it is built with the raspberry pi zero wh and the adafruit pitft - 2.8" touchscreen display in mind. Keep in mind that this is in very early stages of development and is not complete and will contain quite a few bugs. If you are interested in helping you can submit a pull request with proposed changes, add an issue explaining what problems there are, or contact me at @bluetechgirl on twitter. 

## planned features
- notifications with smart phone (will need a seperate app and is planned for later)
- clock with alarm/stopwatch/timer functions (obviously)
- a status bar with indicators visible at all times
- file manager with text file viewer and photo viewer
- an option to have a seperate encrypted file storage accessable via file manager with a key
- a settings app to control themes, wifi and bluetooth connectivity, brightness, autosleep, audio, time/date, encrypted storage key, and the pin to lock some apps
- calandar
- calculator
- music player
- optional nmap scanner (planned for later and meant for cyber security enthusiasts)

(note, these may change)

## not currently planned
- fitness tracker (i do not have a gryrometer module or the knoledge to get it right. if you can develop this feel free to make a pull request)
- heartrate monitor (same reason as fitness tracker)
- calorie counter (this may be implemented in the future)
- messaging/emailing directly on device (screen would be too small for a full keyboard to be practical)
- contact manager (don't see much of a point since the device won't be messaging anyone, just simply showing notifications)
