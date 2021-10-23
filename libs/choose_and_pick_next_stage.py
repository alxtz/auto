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

    if already_has_battle:
      locate_and_click_center('select_stage_battle')
      wait_for_existance('combat_exist')
    else:
      click_ref = pyautogui.locateOnScreen('images/empty_next_stage.png', confidence = 0.8)

      count = 0
      while True:
        pyautogui.click(click_ref.left - 125 * count, click_ref.top + click_ref.height/2 + 100)
        pyautogui.mouseUp()
        count = count + 1
        time.sleep(1)

        has_battle = is_img_on_screen('select_stage_battle')
        # has_revive = is_img_on_screen('has_stage_revive')

        if has_battle:
          locate_and_click_center('select_stage_battle')
          wait_for_existance('combat_exist')
          break

  @staticmethod
  def revert():
    return