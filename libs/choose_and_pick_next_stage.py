import time
import pyautogui
from libs.shared import is_img_on_screen, locate_and_click_center, wait_for_existance

class choose_and_pick_next_stage:
  @staticmethod
  def criteria():
    if not is_img_on_screen('empty_next_stage'):
      raise ValueError("criteria mismatch: choose_and_pick_next_stage.exec()")

  @staticmethod
  def exec():
    choose_and_pick_next_stage.criteria()

    already_has_battle = is_img_on_screen('select_stage_battle')

    # todo, fix all screen
    already_has_revive = is_img_on_screen('has_stage_revive') and is_img_on_screen('select_stage_revive')

    already_has_buff = is_img_on_screen('has_stage_buff')
    has_buff_btn = is_img_on_screen('select_stage_buff')

    already_has_myst_bomb = is_img_on_screen('has_stage_bomb') and is_img_on_screen('select_stage_bomb')
    already_has_myst_dest = is_img_on_screen('has_stage_dest') and is_img_on_screen('select_stage_dest')

    print('alb', already_has_battle)
    print('alr', already_has_revive)
    print('albu', already_has_buff and has_buff_btn)

    if already_has_battle:
      locate_and_click_center('select_stage_battle')
      wait_for_existance('combat_exist')
      return "battle"
    elif already_has_revive:
      locate_and_click_center('select_stage_revive')
      time.sleep(5)
      return "revive"
    elif already_has_myst_dest:
      locate_and_click_center('select_stage_dest')
      time.sleep(5)
      return "revive"
    elif already_has_buff and has_buff_btn:
      dummy = pyautogui.locateOnScreen('images/has_stage_buff.png', confidence = 0.8)
      print('dummy', dummy)
      locate_and_click_center('select_stage_buff')
      time.sleep(3)
      pyautogui.click(dummy.left, dummy.top)
      time.sleep(3)
      return "buff"
    elif already_has_myst_bomb:
      dummy = pyautogui.locateOnScreen('images/has_stage_bomb.png', confidence = 0.8)
      locate_and_click_center('select_stage_bomb')
      time.sleep(3)
      pyautogui.click(dummy.left, dummy.top)
      time.sleep(3)
      return "myst"
    else:
      click_ref = pyautogui.locateOnScreen('images/empty_next_stage.png', confidence = 0.8)

      count = 0
      while True:
        pyautogui.click(click_ref.left - 150 - 50 * count, click_ref.top + click_ref.height/2 - 50)
        pyautogui.mouseUp()
        count = count + 1
        time.sleep(1)

        has_battle = is_img_on_screen('select_stage_battle')
        has_revive = is_img_on_screen('has_stage_revive')and is_img_on_screen('select_stage_revive')

        has_buff = is_img_on_screen('has_stage_buff') and is_img_on_screen('select_stage_buff')
        has_myst_bomb = is_img_on_screen('has_stage_bomb') and is_img_on_screen('select_stage_bomb')
        has_myst_dest = is_img_on_screen('has_stage_dest') and is_img_on_screen('select_stage_dest')

        print('has', has_battle, has_revive, has_buff)

        if has_battle:
          locate_and_click_center('select_stage_battle')
          wait_for_existance('combat_exist')
          return "battle"
        elif has_revive:
          locate_and_click_center('select_stage_revive')
          time.sleep(5)
          return "revive"
        elif has_myst_dest:
          locate_and_click_center('select_stage_dest')
          time.sleep(5)
          return "revive"
        elif has_buff:
          dummy = pyautogui.locateOnScreen('images/has_stage_buff_full.png', confidence = 0.8)
          locate_and_click_center('select_stage_buff')
          time.sleep(3)
          pyautogui.click(dummy.left, dummy.top)
          time.sleep(3)
          return "buff"
        elif has_myst_bomb:
          dummy = pyautogui.locateOnScreen('images/has_stage_bomb.png', confidence = 0.8)
          locate_and_click_center('select_stage_bomb')
          time.sleep(3)
          pyautogui.click(dummy.left, dummy.top)
          time.sleep(3)
          return "myst"


  @staticmethod
  def revert():
    return