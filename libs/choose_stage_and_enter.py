from libs.shared import is_img_on_screen, locate_and_click_center

class choose_stage_and_enter:
  @staticmethod
  def criteria():
    if not is_img_on_screen('felwood_title'):
      raise ValueError("criteria mismatch: choose_stage_and_enter.exec()")

  @staticmethod
  def exec():
    choose_stage_and_enter.criteria()
    locate_and_click_center('felwood_5')
    locate_and_click_center('stage_select', 3)

  @staticmethod
  def revert():
    # locate_and_click_center('choose_deck_back', 3)
    return