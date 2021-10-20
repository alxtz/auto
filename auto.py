import pyautogui, sys, time, cv2

print('Program started.')
input('Move mouse over bot window and press Enter.')
botWindow = pyautogui.position()
print('window', botWindow)

# window = pyautogui.locateOnScreen('images/boss.png')
# if window is None:
#     sys.exit('Could not find game on screen. Is the game visible?')

# print('pve', window)

# winLeft = window[0]
# winTop = window[1]

# print('Found game window at:', winLeft, winTop)

"""
bossImg = pyautogui.locateOnScreen('images/boss.png')
print('bs', bossImg)
pyautogui.click(bossImg.left -400, bossImg.top)

time.sleep(1.5)

time.sleep(1.5)

repeat = True
img = None

while repeat:
    img = pyautogui.locateOnScreen('images/deck.png')
    if img is not None:
        pyautogui.click(img.left + img.width/2, img.top + img.height/2)
        break
    else:
        print('error in select deck')

time.sleep(1.5)
"""


def playCards():
    should_retry = False
    rag = pyautogui.locateOnScreen('images/rag.png', confidence = 0.5)
    if rag is not None:
        print('rag located')
        pyautogui.moveTo(rag.left + rag.width/2, rag.top + rag.height/2)
        time.sleep(3)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.moveTo(rag.left + rag.width/2, rag.top + rag.height/2 - 500)
        time.sleep(3)
        pyautogui.mouseUp(button='left')
        time.sleep(5)
    else:
        print('rag not located')
        should_retry = True

    mage = pyautogui.locateOnScreen('images/mage.png', confidence = 0.5)
    if mage is not None:
        print('mage located')
        pyautogui.moveTo(mage.left + mage.width/2, mage.top + mage.height/2)
        time.sleep(3)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.moveTo(mage.left + mage.width/2, mage.top + mage.height/2 - 500)
        time.sleep(3)
        pyautogui.mouseUp(button='left')
        time.sleep(5)
    else:
        print('mage not located')
        should_retry = True

    dia = pyautogui.locateOnScreen('images/dia.png', confidence = 0.5)
    if dia is not None:
        print('dia located')
        pyautogui.moveTo(dia.left + dia.width/2, dia.top + dia.height/2)
        time.sleep(3)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.moveTo(dia.left + dia.width/2, dia.top + dia.height/2 - 500)
        time.sleep(3)
        pyautogui.mouseUp(button='left')
        time.sleep(5)
    else:
        print('dia not located')
        should_retry = True
    return should_retry

def combat():
    print('call combat')
    img = pyautogui.locateOnScreen('images/handref.png')
    if img is not None:
        time.sleep(5)
        retry = playCards()
        if retry is True:
            playCards()

        # finish
        time.sleep(5)
        pyautogui.click(img.left + 920, img.top + 355)
        time.sleep(5)

        # ab
        pyautogui.click(img.left + 350, img.top + 365)
        time.sleep(3)
        pyautogui.click(img.left + 475, img.top + 365)
        time.sleep(3)

        # finish
        pyautogui.click(img.left + 920, img.top + 355)
        time.sleep(18) # r1 battle

        # r2
        pyautogui.click(img.left + 350, img.top + 365)
        time.sleep(3)
        pyautogui.click(img.left + 475, img.top + 365)
        time.sleep(3)
        pyautogui.click(img.left + 475, img.top + 365)
        time.sleep(3)

        # dup
        pyautogui.click(img.left + 475, img.top + 365)
        time.sleep(2)

        pyautogui.click(img.left + 920, img.top + 355)
        time.sleep(20)

        pyautogui.click(img.left + 920, img.top + 355)
        time.sleep(5)
        pyautogui.click(img.left + 920, img.top + 355)
        time.sleep(12)
        pyautogui.click(img.left + 920, img.top + 355)
        time.sleep(4)
        pyautogui.click(img.left + 650, img.top + 655)
        time.sleep(6)
        # done selecting trea
        pyautogui.mouseUp()
        print('combat ended')
    else:
        print('handref missing')

def chooseStg2Task():
    img = pyautogui.locateOnScreen('images/tsk.png', confidence=0.8)
    print('choose stg2tsk', img)
    if img is None:
        print('tsk img not found')
    elif img.left > 950:
        print('its a right task')
        pyautogui.click(img.left - 50, img.top + 250)
        time.sleep(1)
        pyautogui.click(img.left + 50, img.top + 250)
        time.sleep(1)
        pyautogui.mouseUp()
    elif img.left < 750:
        print('its a left task')
        pyautogui.click(img.left - 60, img.top + 250)
        time.sleep(1)
        pyautogui.click(img.left - 50, img.top + 250)
        time.sleep(1)
        pyautogui.click(img.left + 50, img.top + 250)
        time.sleep(1)
        pyautogui.click(img.left + 115, img.top + 250)
        time.sleep(1)
        pyautogui.mouseUp()
    else:
        print('its a middle task')
        pyautogui.click(img.left + 170, img.top + 250)
        time.sleep(1)
        pyautogui.click(img.left + 150, img.top + 250)
        time.sleep(1)
        pyautogui.click(img.left + 100, img.top + 250)
        time.sleep(1)
        pyautogui.click(img.left + 50, img.top + 250)
        time.sleep(1)
        pyautogui.click(img.left - 50, img.top + 250)
        time.sleep(1)
        pyautogui.click(img.left - 100, img.top + 250)
        time.sleep(1)
        pyautogui.click(img.left - 135, img.top + 250)
        time.sleep(1)
        pyautogui.mouseUp()

def postStgTaskSelect():
    print('post select')
    # img = pyautogui.locateOnScreen('images/combatbtn.png')
    img = pyautogui.locateOnScreen('images/combatbtn.png', confidence=0.8)
    if img is not None:
        pyautogui.click(img.left+50, img.top+50)
        print('click start combat')
        time.sleep(20)
        combat()
    else:
        print('pick something')
        img = pyautogui.locateOnScreen('images/event.png', confidence=0.8)
        if img is not None:
            print('click buff')
            pyautogui.click(img.left+50, img.top+50)
            time.sleep(3)
            pyautogui.click(img.left+50, img.top+50)
        else:
            print('click revive')
            img = pyautogui.locateOnScreen('images/revive.png', confidence=0.8)
            pyautogui.click(img.left+50, img.top+50)
            time.sleep(3)
            pyautogui.click(img.left+50, img.top+50)
            time.sleep(3)

def pickReward():
    img = pyautogui.locateOnScreen('images/reward.png', confidence=0.8)
    if img is not None:
        pyautogui.click(img.left+50, img.top+50)
        time.sleep(2)
    img = pyautogui.locateOnScreen('images/revive.png', confidence=0.8)
    if img is not None:
        print('mis prize')
        pyautogui.click(img.left+50, img.top+50)
        time.sleep(2)
        img = pyautogui.locateOnScreen('images/unselect.png', confidence=0.8)
        if img is not None:
            pyautogui.click(img.left+50, img.top - 250)
            time.sleep(2)
            # img = pyautogui.locateOnScreen('images/select.png', confidence=0.8)
            pyautogui.click(img.left+20, img.top +20)
            time.sleep(2)

def sur():
    print('sur')
    img = pyautogui.locateOnScreen('images/team.png', confidence=0.5)
    if img is not None:
        pyautogui.click(img.left+100, img.top+30)
    time.sleep(4)
    img = pyautogui.locateOnScreen('images/end.png', confidence=0.8)
    if img is None:
        img = pyautogui.locateOnScreen('images/team.png', confidence=0.5)
        if img is not None:
            pyautogui.click(img.left+100, img.top+30)
        time.sleep(4)
        img = pyautogui.locateOnScreen('images/end.png', confidence=0.8)
        if img is not None:
            pyautogui.click(img.left+10, img.top+10)
            time.sleep(2)
        else:
            img = pyautogui.locateOnScreen('images/team.png', confidence=0.5)
            pyautogui.click(img.left+100, img.top+30)
            time.sleep(4)
            img = pyautogui.locateOnScreen('images/end.png', confidence=0.8)
            if img is not None:
                pyautogui.click(img.left+10, img.top+10)
            time.sleep(2)

    else:
        pyautogui.click(img.left+10, img.top+10)
        time.sleep(2)
    img = pyautogui.locateOnScreen('images/endok.png', confidence=0.8)
    pyautogui.click(img.left+10, img.top+10)
    time.sleep(2)
    pyautogui.click(img.left+10, img.top+10)
    time.sleep(3)
    pyautogui.click(img.left+10, img.top+10)
    time.sleep(3)
    pyautogui.click(img.left+10, img.top+10)
    time.sleep(3)

def start():
    time.sleep(5)
    img = pyautogui.locateOnScreen('images/boss.png', confidence=0.8)
    if img is None:
        img = pyautogui.locateOnScreen('images/left.png', confidence=0.8)
        if img is not None:
            pyautogui.click(img.left+10, img.top+10)
            time.sleep(3)
        img = pyautogui.locateOnScreen('images/boss.png', confidence=0.8)
        pyautogui.click(img.left+10, img.top+10)
    else:
        pyautogui.click(img.left+50, img.top+50)
        time.sleep(2)
    img = pyautogui.locateOnScreen('images/bossselect.png', confidence=0.8)
    pyautogui.click(img.left+50, img.top+10)
    time.sleep(4)
    img = pyautogui.locateOnScreen('images/bossselect.png', confidence=0.8)
    pyautogui.click(img.left+50, img.top+10)
    time.sleep(10)

err_count = 0

def wait_for_visible():
    return

def find_and_click_center():
    return

while True:
    try:
        time.sleep(4)
        postStgTaskSelect()
        print('combat end sleep')
        time.sleep(5)
        print('before choose stg 2 task')
        chooseStg2Task()
        time.sleep(5)
        postStgTaskSelect()
        time.sleep(5)
        pickReward()
        sur()
        start()

        err_count = 0
        print('[try] err_count', err_count)
    except Exception as e:
        err_count = err_count + 1
        print('[e] err_count', err_count)
        print('err in loop', e)
        if err_count > 10 and err_count < 100:
            check = pyautogui.locateOnScreen('images/me.png', confidence=0.8)
            print('check', check)
            time.sleep(3)
            if check is not None:
                opt = pyautogui.locateOnScreen('images/opt.png', confidence=0.8)
                print('opt', opt)
                pyautogui.click(opt.left +10, opt.top+10)
                time.sleep(3)
                surgame = pyautogui.locateOnScreen('images/surgame.png', confidence=0.8)
                pyautogui.click(surgame.left +10, surgame.top+10)
                time.sleep(3)
                start()
                err_count = 0
                print('restarted')
        elif err_count > 20:
            print('too many err')
            break


