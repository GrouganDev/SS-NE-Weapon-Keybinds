import dolphin_memory_engine
import os
import sys

hooked = False

currentWeapon = 0x00000000
altWeapon = 0xFFFFFFFF

wantsHook = False




async def injectCode():
    try:
        dolphin_memory_engine.write_word(0x800c5aa0, 0x49712D95) #bl 0x817d8834
        dolphin_memory_engine.write_word(0x817d8834, 0x3DE0817D) #lis r15, 0x817D 
        dolphin_memory_engine.write_word(0x817d8838, 0x61EF885C) #ori r15, r15, 0x885C 
        dolphin_memory_engine.write_word(0x817d883c, 0x83CF0000) #lwz r30, 0x00(r15) 
        dolphin_memory_engine.write_word(0x817d8840, 0x4e800020) #blr


        #branch if the game plans to swap weapons
        dolphin_memory_engine.write_word(0x800c5afc, 0x49712D95) #bl 0x817d8890 

        #load current weapon index into r16
        dolphin_memory_engine.write_word(0x817d8890, 0x3DE0817D) #lis r15, 0x817D 
        dolphin_memory_engine.write_word(0x817d8894, 0x61EF8860) #ori r15, r15, 0x8860 
        dolphin_memory_engine.write_word(0x817d8898, 0x820F0000) #lwz r16, 0x00(r15) 

        #Compare r30 to r16 and swap to new weapon if equal. Check alt weapon otherwise
        dolphin_memory_engine.write_word(0x817d889c, 0x7C10F000) #cmpw r16, r30 
        dolphin_memory_engine.write_word(0x817d88a0, 0x4082000C) #bne 0x817d88a8 
        dolphin_memory_engine.write_word(0x817d88a4, 0x93DF05F8) #stw r30, 0x05F8(r31) 
        dolphin_memory_engine.write_word(0x817d88a8, 0x4e800020) #blr

        #check alt weapon (address 0x817D8868)
        dolphin_memory_engine.write_word(0x817d88ac, 0x3DE0817D) #lis r15, 0x817D 
        dolphin_memory_engine.write_word(0x817D88b0, 0x61EF8868) #ori r15, r15, 0x8868 
        dolphin_memory_engine.write_word(0x817d88b4, 0x820F0000) #lwz r16, 0x00(r15) 
        dolphin_memory_engine.write_word(0x817d88b8, 0x7C10F000) #cmpw r16, r30 
        dolphin_memory_engine.write_word(0x817d88bc, 0x40820008) #bne 0x817d88a8 
        dolphin_memory_engine.write_word(0x817d88c0, 0x921F05F8) #stw r16, 0x05F8(r31) 
        dolphin_memory_engine.write_word(0x817d88c4, 0x4e800020) #blr
    except RuntimeError:
        pass


async def deinjectCode():
    try:
        dolphin_memory_engine.write_word(0x800c5aa0, 0x83df05f8)
        dolphin_memory_engine.write_word(0x800c5afc, 0x93df05f8)
    except RuntimeError:
        pass



async def hookToDolphin():
    try:
        dolphin_memory_engine.hook()
        await injectCode()
    
    except RuntimeError:
        pass

    return dolphin_memory_engine.is_hooked()


async def unhookToDolphin():
    try:
        await deinjectCode()
        dolphin_memory_engine.un_hook()
    
    except RuntimeError:
        pass

    return not dolphin_memory_engine.is_hooked()



def updateWeaponWord(currentWeapon, altWeapon):
    currentWeaponBelow = (currentWeapon - 1) % 12
    try:
        #Updates memory to be the weapon index minus one mod 12
        dolphin_memory_engine.write_word(0x817D885C, currentWeaponBelow)

        #Updates neighboring memory to be actual currentWeapon index
        dolphin_memory_engine.write_word(0x817D8860, currentWeapon)

        #Updates alt weapon index that is checked if the currentWeaponBelow cannot be accessed
        dolphin_memory_engine.write_word(0x817D8868, altWeapon)
    except RuntimeError:
        pass


#Only two weapons can be in any given "group"
def assignWeaponGroup(first, second, currentWeapon):
    current = 0
    alt = 0

    if currentWeapon == first:
        current = second
        alt = first
    else:
        current = first
        alt = second

    return current, alt 
     


"""
WEAPON INDICES:

0x00000000 - Chainsaw
0x00000001 - Pistol(s)
0x00000002 - Uzis
0x00000003 - Shotgun
0x00000004 - Minigun
0x00000005 - Grenade Launcher
0x00000006 - Rocket Launcher
0x00000007 - Flamethrower
0x00000008 - Sniper Rifle
0x00000009 - Sirian Powergun
0x0000000A - Cannon
0x0000000B - Serious Bomb
"""


## Both keyboard and mouse monitoring is done through pynput
## Doumentation can be found here: https://pynput.readthedocs.io/en/latest/


## READING KEYBOARD INPUT
import asyncio
import threading
from pynput import keyboard
from pynput.keyboard import Key

def on_press(key):    
    global currentWeapon
    global altWeapon 
    try:
        #Normal keys which can be turned into chars
        k = key.char
        match key.char:
            case '1':
                currentWeapon = 0x00000000

                #0xFFFFFFFF is used if this "group" only contains one weapon
                altWeapon = 0xFFFFFFFF

            case '2':
                currentWeapon = 0x00000001
                altWeapon = 0xFFFFFFFF

            case '3':
                currentWeapon = 0x00000003
                altWeapon = 0xFFFFFFFF

            case '4':
                currentWeapon, altWeapon = assignWeaponGroup(0x00000002, 0x00000004, currentWeapon=currentWeapon)

            case 'f':
                currentWeapon, altWeapon = assignWeaponGroup(0x00000006, 0x00000005, currentWeapon=currentWeapon)

            case 'x':
                currentWeapon, altWeapon = assignWeaponGroup(0x00000007, 0x00000008, currentWeapon=currentWeapon)

            case 'c':
                currentWeapon, altWeapon = assignWeaponGroup(0x0000000A, 0x00000009, currentWeapon=currentWeapon)

    except AttributeError:
        #Special keys such as shift, alt, esc, etc.
        match key:
            case Key.alt_l:
                currentWeapon = 0x0000000B
                altWeapon = 0xFFFFFFFF

            case Key.shift_r:
                global wantsHook
                wantsHook = True


    updateWeaponWord(currentWeapon=currentWeapon, altWeapon=altWeapon)
   

def start_async_keyboard():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()


keyboard_thread = threading.Thread(target=start_async_keyboard)
keyboard_thread.daemon = True  
keyboard_thread.start()








## READING MOUSE INPUT
from pynput import mouse
from pynput.mouse import Button

def on_click(x, y, button, pressed):
    global currentWeapon
    global altWeapon

    if pressed:
        if os.name == 'nt':
            match button:
                case Button.x2:
                    currentWeapon, altWeapon = assignWeaponGroup(0x00000007, 0x00000008, currentWeapon=currentWeapon)

                case Button.x1:
                    currentWeapon, altWeapon = assignWeaponGroup(0x0000000A, 0x00000009, currentWeapon=currentWeapon)
        else:
            match button:
                case Button.button9:
                    currentWeapon, altWeapon = assignWeaponGroup(0x00000007, 0x00000008, currentWeapon=currentWeapon)

                case Button.button9:
                    currentWeapon, altWeapon = assignWeaponGroup(0x0000000A, 0x00000009, currentWeapon=currentWeapon)

        updateWeaponWord(currentWeapon=currentWeapon, altWeapon=altWeapon)

def start_async_mouse():
    listener = mouse.Listener(on_click=on_click)
    listener.start()

mouse_thread = threading.Thread(target=start_async_mouse)
mouse_thread.daemon = True  
mouse_thread.start()






async def printMenu():
    global hooked
    os.system('cls' if os.name == 'nt' else 'clear')
    lineOne = "Serious Sam: Next Encounter Weapon Binds for Dolphin"
    longLine = "----------------------------------------------------------"
    status = ("Connected" if hooked else "Not Connected") + " - Press Right Shift to Toggle Connection"

    print(lineOne + "\n" + longLine + "\n" + status)




async def main():
    global hooked
    global wantsHook

    os.system('cls' if os.name == 'nt' else 'clear')

    hooked = await hookToDolphin()

    
    if not hooked:
        print("Game not loaded. Closing shortly...")
        await asyncio.sleep(3)
        sys.exit(0)
    

    await printMenu()


    while True:
        if wantsHook:
            hooked = not await unhookToDolphin() if hooked else await hookToDolphin()
            wantsHook = False
            await printMenu()
            print("\n\nNote: In order for changes to take effect, you may need to clear the JIT cache in Dolphin before switching.")
            print("You'll need to enable Dolphin's debug mode in order to access this option.")

        await asyncio.sleep(0.01)

asyncio.run(main())