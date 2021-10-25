import sys
import time

import pyautogui
from libs.boss_combat import boss_combat
from libs.choose_and_pick_next_stage import choose_and_pick_next_stage
from libs.choose_deck_and_enter import choose_deck_and_enter
from libs.choose_stage_and_enter import choose_stage_and_enter
from libs.click_and_enter_combat import click_and_enter_combat
from libs.combat import combat
from libs.select_and_confirm_battle_rewards import select_and_confirm_battle_rewards
from libs.shared import is_img_on_screen, locate_and_click_center, wait_for_existance

# print('do boss rewards')
# time.sleep(10)
# ref = pyautogui.locateOnScreen('images/opt_ref.png', confidence = 0.9)
# pyautogui.click(ref.left - 300, ref.top - 100)
# time.sleep(1.5)
# pyautogui.click(ref.left - 600, ref.top - 100)
# time.sleep(1.5)
# pyautogui.click(ref.left - 700, ref.top - 400)
# time.sleep(1.5)
# pyautogui.click(ref.left - 200, ref.top - 400)
# time.sleep(1.5)
# pyautogui.click(ref.left - 400, ref.top - 550)
# time.sleep(1.5)
# pyautogui.click(ref.left - 400, ref.top - 310)
# time.sleep(1.5)
# locate_and_click_center('complete_ok')
# wait_for_existance('felwood_title')


# combat.exec()
# choose_and_pick_next_stage.exec()
# target = pyautogui.locateOnScreen('images/hand_anton.png', confidence = 0.7)
# print('t', target)

# print('try to see if bomb exist')

# time.sleep(2)
# if is_img_on_screen('bomb', confidence=0.7):
#   print('trigger bomb')
#   locate_and_click_center('bomb')
# else:
#   print('bomb not exist')

# locate_and_click_center('select_stage_myst')
# time.sleep(1)
# target = pyautogui.locateOnScreen('images/myst_select.png', confidence=0.9)
# pyautogui.click(target.left, target.top - 200)
# time.sleep(2)
# pyautogui.click(target.left, target.top)
# time.sleep(3)
# pyautogui.click(target.left, target.top)
# time.sleep(3)
# print('try to see if bomb exist')

# time.sleep(3)
# if is_img_on_screen('bomb', confidence=0.5):
#   print('trigger bomb')
#   locate_and_click_center('bomb')
# else:
#   print('bomb not exist')
# combat.revert()
# sys.exit()


# check_and_memorize_myst_location()
# scroll_back_select_stage_1()

# battle, revive, buff, myst

while True:
  print('[INFO] starting another adventure')

  choose_stage_and_enter.exec()
  choose_deck_and_enter.exec()

  for i in range(1, 8):
    print('[INFO] round', i)

    if (i == 1): # redundant
      click_and_enter_combat.exec()
      try:
        combat.exec()
      except ValueError:
        print('error in combat, trying to revert')
        combat.revert()
        break
      select_and_confirm_battle_rewards.exec()
      # choose_and_pick_next_stage.exec()
    elif (i == 7):
      # boss fight
      print('boss fight')
      try:
        boss_combat.exec()
      except ValueError:
        print('error in boss combat, trying to revert')
        combat.revert()
        break
    else:
      choose_result = choose_and_pick_next_stage.exec()
      print('choose result', choose_result)
      if choose_result == "battle":
        try:
          combat.exec()
        except ValueError:
          print('error in combat, trying to revert')
          combat.revert()
          break

        select_and_confirm_battle_rewards.exec()
      elif choose_result == "revive":
        print('chose revive, skip')
        continue
      elif choose_result == "myst":
        print('chose myst, skip')
        continue
      elif choose_result == "portal":
        print('chose portal')
        # boss fight
        print('boss fight')
        try:
          boss_combat.exec()
        except ValueError:
          print('error in boss combat, trying to revert')
          combat.revert()
          break
      # if last_round == "battle":
      #   combat.exec()
      #   select_and_confirm_battle_rewards.exec()
      #   last_round = choose_and_pick_next_stage.exec()
      #   print('[INFO] round', i, 'ended, its a', last_round)
      # elif last_round == "revive":
      #   last_round = choose_and_pick_next_stage.exec()

# click_and_wait_revive()
# click_and_wait_buff()
# click_choose_and_close_buff()


# click_and_enter_combat()
# click_and_wait_revive()
# click_and_wait_buff()
# click_choose_and_close_buff()

# check_if_last_round()
  # concede()
  # skip_concede_reward()

# ...loop again
