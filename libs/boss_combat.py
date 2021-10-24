from libs.combat import combat
from libs.shared import is_img_on_screen, locate_and_click_center, wait_for_existance

class boss_combat:
  @staticmethod
  def criteria():
    if not is_img_on_screen('enter_boss_stage'):
      raise ValueError("criteria mismatch: boss_combat.exec()")

  @staticmethod
  def exec():
    print('entering boss combat')
    wait_for_existance('enter_boss_stage')
    # boss_combat.criteria()
    locate_and_click_center('enter_boss_stage')
    wait_for_existance('combat_exist')
    combat.exec(boss_fight=True)

  @staticmethod
  def revert():
    return