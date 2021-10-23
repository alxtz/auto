import time
import pyautogui

debug = True

def is_img_on_screen(img_name):
  if debug: print('[DEBUG] locating', img_name)

  target = pyautogui.locateOnScreen('images/' + img_name + '.png', confidence = 0.7)

  result = target is not None

  if debug: print('[DEBUG] locate result', result)

  return result

def locate_and_click_center(img_name, delay = 1, optional = True):
  if debug: print('[DEBUG] locating', img_name)

  target = pyautogui.locateOnScreen('images/' + img_name + '.png', confidence = 0.7)

  if debug: print('[DEBUG] located and try to click', target)

  if not optional:
    pyautogui.click(target.left + target.width/2, target.top + target.height/2)
  else:
    if target is not None:
      pyautogui.click(target.left + target.width/2, target.top + target.height/2)


  time.sleep(delay)

def wait_for_existance(img_name, interval = 5, max_loop = 6):
  count = 0

  while count < max_loop:
    check = pyautogui.locateOnScreen('images/' + img_name + '.png', confidence = 0.7)

    if check is not None:
      if debug: print('[DEBUG] exists', img_name)
      break
    else:
      time.sleep(interval)
      if debug: print('[DEBUG] waiting for existance', img_name)
      continue

