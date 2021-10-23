import time
from libs.shared import is_img_on_screen, locate_and_click_center

class choose_deck_and_enter:
  @staticmethod
  def criteria():
    if not is_img_on_screen('deck_title'):
      raise ValueError("criteria mismatch: choose_deck_and_enter.exec()")

  @staticmethod
  def exec():
    choose_deck_and_enter.criteria()
    locate_and_click_center('deck_2_5')
    locate_and_click_center('deck_select')
    locate_and_click_center('dialog_confirm')
    time.sleep(10)

  @staticmethod
  def revert():
    # locate_and_click_center('choose_deck_back', 3)
    return