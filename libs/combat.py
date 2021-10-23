from libs.shared import is_img_on_screen, locate_and_click_center, wait_for_existance

class combat:
  @staticmethod
  def criteria():
    if not is_img_on_screen('enter_combat_crit'):
      raise ValueError("criteria mismatch: combat.exec()")

  @staticmethod
  def exec():
    combat.criteria()
    combat.play_hand()

    combat.end_turn()

    return

    while True():
      # expect loop to start for every ability selection state
      choose_abilities.wait_criteria()
      choose_abilities.exec()
      combat.end_turn()

      # trigger battle ~~

      # wait for at least 20 seconds, or til
      # 1. ablities are shown
      # 2. win icon has shown
      # oh oh, actually shouldn't wait for any of those
      ended = combat.has_combat_ended()
      if ended:
        break
      else:
        continue

  @staticmethod
  def revert():
    return

  @staticmethod
  def play_hand():
    combat.play_rag()
    combat.play_baron()
    combat.play_anton()

  @staticmethod
  def play_rag():
    return

  @staticmethod
  def play_baron():
    return

  @staticmethod
  def play_anton():
    return

  @staticmethod
  def has_combat_ended():
    return

class choose_abilities:
  @staticmethod
  def wait_criteria():
    # will wait til ability can select
    return

  @staticmethod
  def exec():
    return
  