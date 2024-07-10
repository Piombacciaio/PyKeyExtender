import darkdetect, pyautogui as pg, PySimpleGUI as PSG
from time import sleep
from threading import Thread

def theme_selection():
  "Detect either dark or light theme and generate the layout"

  if darkdetect.isDark(): 
    PSG.theme("DarkBlack")
  else:
    PSG.theme("LightBlue6")
  layout = [
    [PSG.Text("NumPad-Keys", tooltip="Will send a key as from the numpad after the duration\nNumbers can be chained")],
    [PSG.Push(), PSG.Button("1", key="-NUM-1-", size=(3,1)), PSG.Button("2", key="-NUM-2-", size=(3,1)), PSG.Button("3", key="-NUM-3-", size=(3,1)), PSG.Push()],
    [PSG.Push(), PSG.Button("4", key="-NUM-4-", size=(3,1)), PSG.Button("5", key="-NUM-5-", size=(3,1)), PSG.Button("6", key="-NUM-6-", size=(3,1)), PSG.Push()],
    [PSG.Push(), PSG.Button("7", key="-NUM-7-", size=(3,1)), PSG.Button("8", key="-NUM-8-", size=(3,1)), PSG.Button("9", key="-NUM-9-", size=(3,1)), PSG.Push()],
    [PSG.Push(), PSG.Button("0", key="-NUM-0-", size=(3,1)), PSG.Push()],
    [PSG.Text("")],
    [PSG.HorizontalSeparator()],
    [PSG.Text("F-Keys", tooltip="Will enable to press all the function keys missing from the standard keyboard\nKey presses can be chained")],
    [PSG.Push(), PSG.Button("F13", key="-F13-", size=(5,1)), PSG.Push(), PSG.Button("F14", key="-F14-", size=(5,1)), PSG.Push(), PSG.Button("F15", key="-F15-", size=(5,1)), PSG.Push(), PSG.Button("F16", key="-F16-", size=(5,1)), PSG.Push()],
    [PSG.Push(), PSG.Button("F17", key="-F17-", size=(5,1)), PSG.Push(), PSG.Button("F18", key="-F18-", size=(5,1)), PSG.Push(), PSG.Button("F19", key="-F19-", size=(5,1)), PSG.Push(), PSG.Button("F20", key="-F20-", size=(5,1)), PSG.Push()],
    [PSG.Push(), PSG.Button("F21", key="-F21-", size=(5,1)), PSG.Push(), PSG.Button("F22", key="-F22-", size=(5,1)), PSG.Push(), PSG.Button("F23", key="-F23-", size=(5,1)), PSG.Push(), PSG.Button("F24", key="-F24-", size=(5,1)), PSG.Push()],
    [PSG.Text("")],
    [PSG.HorizontalSeparator()],
    [PSG.Text("Modifier-Keys", tooltip="Standard modifier keys on a toggle for easier use")],
    [PSG.Checkbox("CTRL", key="-CTRL-", change_submits=True), PSG.Push(), PSG.Checkbox("SHIFT", key="-SHIFT-", change_submits=True), PSG.Push(), PSG.Checkbox("ESC", key="-ESC-", change_submits=True), PSG.Push(), PSG.Checkbox("ALT", key="-ALT-", change_submits=True)],
    [PSG.Text("")],
    [PSG.HorizontalSeparator()],
    [PSG.Text("Settings")],
    [PSG.Text("Delay (Seconds): ", tooltip="Delay, after which, the button will be pressed"), PSG.Input("2", key="-DELAY-INPUT-", size=(5,1))],
    [PSG.Text("Duration (ms): ", tooltip="Duration, during which, the button will be pressed"), PSG.Input("50", key="-DURATION-INPUT-", size=(5,1), pad=((22,0), 0))],
    [PSG.Checkbox("Keep Tool On Top", key="-KEEP-ON-TOP-", change_submits=True, default=True)],
    [PSG.Text("")],
    [PSG.HorizontalSeparator()],
    [PSG.Text("Status: "), PSG.Text("IDLE", key="-STATUS-")]
  ]
  return layout

def key_press(key:str, delay:float, duration:float, window:PSG.Window):
  """Send a key press after the delay and for the duration selected.
  Window parameter is used to update the status indicator"""

  window["-STATUS-"].update(f"Sending {key} in {delay}s")
  sleep(delay)
  window["-STATUS-"].update(f"Pressing {key}")
  pg.keyDown(key)
  sleep(duration)
  pg.keyUp(key)
  window["-STATUS-"].update("IDLE")

def main():
  layout = theme_selection()
  window = PSG.Window(f"PyKeyExtender | by Piombacciaio", layout, icon="icon.ico", finalize=True, keep_on_top=True, location=(0,0))
  while 1: 
    events, values = window.read()
    if events == PSG.WIN_CLOSED: break
    #Update KeepOnTop
    if events == "-KEEP-ON-TOP-":
      if values["-KEEP-ON-TOP-"]:
        window.keep_on_top_set()
      else:
        window.keep_on_top_clear()
    #CTRL Hold
    if events == "-CTRL-":
      if values["-CTRL-"]:
        pg.keyDown("ctrl")
      else:
        pg.keyUp("ctrl")
    #SHIFT Hold
    if events == "-SHIFT-":
      if values["-SHIFT-"]:
        pg.keyDown("shift")
      else:
        pg.keyUp("shift")
    #DEL Hold
    if events == "-ESC-":
      if values["-ESC-"]:
        pg.keyDown("esc")
      else:
        pg.keyUp("esc")
    #ALT Hold
    if events == "-ALT-":
      if values["-ALT-"]:
        pg.keyDown("alt")
      else:
        pg.keyUp("alt")
    #Keys Handler
    if events in [f"-NUM-{x}-" for x in range(0, 10)] or events in [f"-F{x}-" for x in range(13, 25)]:
      delay = float(values["-DELAY-INPUT-"])
      duration= float(values["-DURATION-INPUT-"])/1000
      key = events.replace("-", "")
      Thread(target=key_press, args=(key, delay, duration, window)).start()

if __name__ == '__main__': main()
