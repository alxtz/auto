import sys
from libs.choose_deck_and_enter import choose_deck_and_enter
from libs.choose_stage_and_enter import choose_stage_and_enter
from libs.click_and_enter_combat import click_and_enter_combat
from libs.combat import combat

combat.exec()
sys.exit()

choose_stage_and_enter.exec()

choose_deck_and_enter.exec()

# check_and_memorize_myst_location()

# scroll_back_select_stage_1()


for i in range(1, 6):
  # expect a state where combat had ended, also combat reward had been selected, just waiting to click the combat/event button
  print('loop', i)

  if (i == 1):
    # redundant
    click_and_enter_combat.exec()
    print(0)
  else:
    print(0)
# click_and_wait_revive()
# click_and_wait_buff()
# click_choose_and_close_buff()

# combat(max_round = -1)
  # play_heros()
  # end_turn()
  # wait_for_battle_end(timeout = 20)
  # check_win(timeout = 5)
  # use_ablities()
  # end_turn()
  # wait_for_battle_end()
  # check_win()

# select_and_confirm_battle_rewards()
# choose_and_pick_next_stage()

# click_and_enter_combat()
# click_and_wait_revive()
# click_and_wait_buff()
# click_choose_and_close_buff()

# check_if_last_round()
  # concede()
  # skip_concede_reward()

# ...loop again
