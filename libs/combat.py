import time
import pyautogui
from libs.shared import is_img_on_screen, locate_and_click_center, locate_and_click_center_2, wait_for_existance

class combat:
  @staticmethod
  def criteria():
    if not is_img_on_screen('combat_exist'):
      raise ValueError("criteria mismatch: combat.exec()")

  @staticmethod
  def exec(boss_fight = False):
    combat.criteria()
    combat.play_hand()
    combat.end_turn()

    while True:
      # expect loop to start for every ability selection state
      choose_abilities.wait_criteria()
      choose_abilities.exec()
      combat.end_turn()

      # trigger battle ~~

      ended = combat.has_combat_ended()
      if ended:
        print('combat ended!')

        if boss_fight:
          print('do boss rewards')

          print('time to click on rewards')

          ref = pyautogui.locateOnScreen('images/opt_ref.png', confidence = 0.9)

          # skip dummies
          time.sleep(3)
          pyautogui.click(ref.left - 100, ref.top)
          time.sleep(3)
          pyautogui.click(ref.left - 100, ref.top)
          time.sleep(3)
          pyautogui.click(ref.left - 100, ref.top)

          time.sleep(15)

          print('ref', ref)

          pyautogui.click(ref.left - 300, ref.top - 100)
          time.sleep(1.5)
          pyautogui.click(ref.left - 600, ref.top - 100)
          time.sleep(1.5)
          pyautogui.click(ref.left - 700, ref.top - 400)
          time.sleep(1.5)
          pyautogui.click(ref.left - 200, ref.top - 400)
          time.sleep(1.5)
          pyautogui.click(ref.left - 400, ref.top - 550)
          time.sleep(1.5)
          pyautogui.click(ref.left - 400, ref.top - 310)
          time.sleep(5)

          print('click completed')

          pyautogui.moveTo(ref.left - 100, ref.top)

          wait_for_existance('complete_ok')
          locate_and_click_center('complete_ok')
          wait_for_existance('felwood_title')

        else:
          wait_for_existance('combat_reward', dummy_click=True)

        break
      else:
        print('fight temp ended, wait for another round')
        continue

  @staticmethod
  def revert():
    locate_and_click_center_2('opt_ref')
    print('opened ref')
    time.sleep(5)
    locate_and_click_center('sur')
    print('clicked sur')
    wait_for_existance('felwood_title', dummy_click=True)
    return

  @staticmethod
  def play_hand():
    combat.play_rag()
    combat.play_baron()
    combat.play_anton()

  @staticmethod
  def play_rag():
    rag = pyautogui.locateOnScreen('images/hand_rag.png', confidence = 0.6)

    if rag is None:
      raise ValueError("rag hero died in combat")

    pyautogui.moveTo(rag.left + rag.width/2, rag.top + rag.height/2)
    time.sleep(2)
    pyautogui.mouseDown(button='left')
    time.sleep(2)
    pyautogui.moveTo(rag.left + rag.width/2, rag.top + rag.height/2 - 500)
    time.sleep(2)
    pyautogui.mouseUp(button='left')
    time.sleep(3)

    wait_for_existance('board_rag')
    

  @staticmethod
  def play_baron():
    target = pyautogui.locateOnScreen('images/hand_baron.png', confidence = 0.7)

    pyautogui.moveTo(target.left + target.width/2, target.top + target.height/2)
    time.sleep(2)
    pyautogui.mouseDown(button='left')
    time.sleep(2)
    pyautogui.moveTo(target.left + target.width/2, target.top + target.height/2 - 500)
    time.sleep(2)
    pyautogui.mouseUp(button='left')
    time.sleep(3)

    wait_for_existance('board_baron')

  @staticmethod
  def play_anton():
    target = pyautogui.locateOnScreen('images/hand_anton.png', confidence = 0.7)

    if target is None:
      raise ValueError("anton hero died in combat")

    pyautogui.moveTo(target.left + target.width/2, target.top + target.height/2)
    time.sleep(2)
    pyautogui.mouseDown(button='left')
    time.sleep(2)
    pyautogui.moveTo(target.left + target.width/2, target.top + target.height/2 - 500)
    time.sleep(2)
    pyautogui.mouseUp(button='left')
    time.sleep(3)

    wait_for_existance('board_anton')

  @staticmethod
  def has_combat_ended():
    loop_count = 0

    while True:
      loop_count = loop_count + 1
      time.sleep(5)
      still_in_combat = pyautogui.locateOnScreen('images/ab_2_ok_baron.png', confidence = 0.7)
      combat_won = pyautogui.locateOnScreen('images/combat_won.png', confidence = 0.7)
      someone_died = pyautogui.locateOnScreen('images/someone_died.png', confidence = 0.7)


      if still_in_combat:
        return False
      elif combat_won:
        return True
      elif someone_died:
        raise ValueError("hero died in combat")
      else:
        if loop_count > 10:
          raise ValueError("has_combat_ended() unexpected state")
        else:
          continue


  @staticmethod
  def end_turn():
    time.sleep(2)
    wait_for_existance('end_turn')
    locate_and_click_center('end_turn')

class choose_abilities:
  @staticmethod
  def wait_criteria():
    wait_for_existance('ab_2_ok_baron')

  @staticmethod
  def exec():
    wait_for_existance('ab_2_ok_baron')
    locate_and_click_center('ab_2_ok_baron')

    wait_for_existance('ab_2_ok_rag')
    locate_and_click_center('ab_2_ok_rag')

    wait_for_existance('ab_1_ok_anton')
    anton_target = pyautogui.locateOnScreen('images/ab_1_ok_anton.png', confidence = 0.7)
    locate_and_click_center('ab_1_ok_anton')
    pyautogui.click(anton_target.left + anton_target.width/2 + 120, anton_target.top - 95) 

    print('try to see if bomb exist')

    time.sleep(3)
    if is_img_on_screen('bomb', confidence=0.5):
      print('trigger bomb')
      locate_and_click_center('bomb')
    else:
      print('bomb not exist')

    
  