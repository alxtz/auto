from libs.shared import is_img_on_screen, locate_and_click_center, wait_for_existance

class click_and_enter_combat:
  @staticmethod
  def criteria():
    if not is_img_on_screen('enter_combat_crit'):
      raise ValueError("criteria mismatch: click_and_enter_combat.exec()")

  @staticmethod
  def exec():
    click_and_enter_combat.criteria()
    locate_and_click_center('enter_combat_crit')
    wait_for_existance('combat_exist')

  @staticmethod
  def revert():
    return