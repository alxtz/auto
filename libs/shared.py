import time
import pyautogui

# debug = True
debug = False

def is_img_on_screen(img_name, confidence = 0.7):
  if debug: print('[DEBUG] locating', img_name)

  target = pyautogui.locateOnScreen('images/' + img_name + '.png', confidence)

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

def locate_and_click_center_2(img_name, delay = 1, optional = True):
  if debug: print('[DEBUG] locating', img_name)

  target = pyautogui.locateOnScreen('images/' + img_name + '.png', confidence = 0.8)

  if debug: print('[DEBUG] located and try to click', target)

  if not optional:
    pyautogui.click(target.left + target.width/2, target.top + target.height/2)
  else:
    if target is not None:
      pyautogui.click(target.left + target.width/2, target.top + target.height/2)


  time.sleep(delay)

def wait_for_existance(img_name, interval = 5, max_loop = 6, dummy_click = False):
  count = 0

  while count < max_loop:
    count = count + 1
    print('[INFO] count', count)
    if dummy_click:
      opt_ref = pyautogui.locateOnScreen('images/opt_ref.png', confidence = 0.85)
      if opt_ref is not None:
        print('opt_ref', opt_ref)
        pyautogui.click(opt_ref.left - 100, opt_ref.top)
        print('try click before exist')
      else:
        print('opt_ref not found')

    check = pyautogui.locateOnScreen('images/' + img_name + '.png', confidence = 0.7)

    if check is not None:
      if debug: print('[DEBUG] exists', img_name)
      return
    else:
      time.sleep(interval)
      if debug: print('[DEBUG] waiting for existance', img_name)
      continue
  
  raise ValueError("never exist", img_name)
