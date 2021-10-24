import sys

import pyautogui
from libs.boss_combat import boss_combat
from libs.choose_and_pick_next_stage import choose_and_pick_next_stage
from libs.choose_deck_and_enter import choose_deck_and_enter
from libs.choose_stage_and_enter import choose_stage_and_enter
from libs.click_and_enter_combat import click_and_enter_combat
from libs.combat import combat
from libs.select_and_confirm_battle_rewards import select_and_confirm_battle_rewards


# combat.exec()
# choose_and_pick_next_stage.exec()
# target = pyautogui.locateOnScreen('images/hand_anton.png', confidence = 0.7)
# print('t', target)
# sys.exit()

choose_stage_and_enter.exec()
choose_deck_and_enter.exec()

# check_and_memorize_myst_location()
# scroll_back_select_stage_1()

# battle, revive, buff, myst

for i in range(1, 8):
  print('[INFO] round', i)

  if (i == 1): # redundant
    click_and_enter_combat.exec()
    combat.exec()
    select_and_confirm_battle_rewards.exec()
    # choose_and_pick_next_stage.exec()
  elif (i == 7):
    # boss fight
    print('boss fight')
    boss_combat.exec()
  else:
    choose_result = choose_and_pick_next_stage.exec()
    print('choose result', choose_result)
    if choose_result == "battle":
      combat.exec()
      select_and_confirm_battle_rewards.exec()
    elif choose_result == "revive":
      print('chose revive, skip')
      continue
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
