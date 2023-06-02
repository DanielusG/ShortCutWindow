from pynput import keyboard
import platform
class ShortCutManager():
  cmb = []
  
  current = set()

  def __init__(self, execute, cmbstr: list[str]):
    self.execute = execute
    self._convertStrCombinationToKeyCombination(cmbstr)
    listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release,name=str(self.cmb))
    listener.start()
  
  def _convertStrCombinationToKeyCombination(self, cmbstr: list[str]):
    localcmb = set()
    for comb in cmbstr:
      if comb == "ctrl":
        if platform.system() == "Windows":
          localcmb.add(keyboard.Key.ctrl_l)
        else:
          localcmb.add(keyboard.Key.ctrl)
      elif comb == "alt":
        localcmb.add(keyboard.Key.alt)
      elif comb == "shift":
        localcmb.add(keyboard.Key.shift)
      elif comb == "f1":
        localcmb.add(keyboard.Key.f1)
      elif comb == "f2":
        localcmb.add(keyboard.Key.f2)
      elif comb == "f3":
        localcmb.add(keyboard.Key.f3)
      elif comb == "f4":
        localcmb.add(keyboard.Key.f4)
      elif comb == "q":
        localcmb.add(keyboard.KeyCode(char='q'))
    self.cmb = [localcmb]

  def on_press(self, key):
    if any([key in z for z in self.cmb]):
      self.current.add(key)
      if any(all(k in self.current for k in z) for z in self.cmb):
        print("Shortcut pressed: " + str(self.cmb))
        self.execute()
  
  def on_release(self, key):
    try:
      if any([key in z for z in self.cmb]):
        self.current.remove(key)
    except KeyError:
      pass