import time
import pyautogui
from libs.shared import is_img_on_screen, locate_and_click_center, wait_for_existance

class select_and_confirm_battle_rewards:
  @staticmethod
  def criteria():
    if not is_img_on_screen('combat_reward'):
      raise ValueError("criteria mismatch: select_and_confirm_battle_rewards.exec()")

  @staticmethod
  def exec():
    select_and_confirm_battle_rewards.criteria()
    get_btn = pyautogui.locateOnScreen('images/get_reward.png', confidence = 0.7)
    pyautogui.click(get_btn.left + get_btn.width/2, get_btn.top - 275)
    time.sleep(1)
    pyautogui.click(get_btn.left + get_btn.width/2, get_btn.top + get_btn.height/2)
    wait_for_existance('empty_next_stage')

  @staticmethod
  def revert():
    return