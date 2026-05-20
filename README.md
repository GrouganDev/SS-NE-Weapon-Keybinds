\# Serious Sam: Next Encounter Weapon Binds for Dolphin

An external tool which hooks into Dolphin, similar to the \[Dolphin Mouse Injector](https://github.com/garungorp/MouseInjectorDolphinDuck), and allows for custom weapon binds for Serious Sam: Next Encounter to help the game play more like the PC games. 



This only works on Dolphin and the Gamecube version of Serious Sam: Next Encounter.



Works of Windows and maybe Linux, but most likely does not work on Mac as of this moment.





\## How To Use



1\) Open your emulator and start Serious Sam: The Next Encounter



&#x20;   - Optional but recommended: Before opening the game, right click on your game and select ``Add Shortcut to Desktop``. Find that shortcut and right click on it. Select ``Properties``. Find where it says ``Target`` and select the text box next to it. Go to the end of the text, where there will likely be a quotation mark and add ``--debug`` AFTER the quotations.

&#x09;	 - Your new "Target" should look something like ``"path\\to\\Dolphin\\folder\\Dolphin.exe" -e "path/to/Serious/Sam/rom" --debug``

&#x09;	 - This will  help you in being able to manually clear Dolphin's JIT cache, which may be important for you.



2\) Open the ``NE Weapon Injector`` executable which matches your operating system. The program will automatically hook itself onto Dolphin so long as the game is already open before you run this executable.  

&#x09;- If you wish to unhook or rehook after the executable is already running, you will need to clear Dolphin's JIT cache before doing so. 

&#x09;	- Assuming you are running on the debug version of Dolphin, which the directions for doing so has already been given above, go to the top of Dolphin's window where all of the drop down menus are. Click on the one called ``JIT``. Then click ``Clear Cache``. Now, you can press right shift (by default) in your program to successfully toggle whether or not it is hooking to Dolphin.

&#x09;	

3\) So long as the program is hooked to Dolphin, the weapon binds should work out of the box. If you wish to change them, you can edit the ``main.py`` file to manually edit weapon bindings. 

&#x09;- If you do edit your bindings and wish to compile the new version of your ``main.py`` script into a new executable, simple run the ``compile\_python.bat`` file if you're on Windows or ``compile\_python.sh`` if you're on Linux.

&#x09;	- Note: You must have \[Python](https://www.python.org/downloads/) installed on your computer in order to do this. This program was created with Python 3.12.4, but later versions may work as well. If you do not have Python installed on your computer, this program will not work. 





\## Default Weapon Bindings

| Key          | Weapon(s)                 |

| :------------: | :-------------------------: |

| 1            | Chainsaw                  |

| 2            | Pistol(s)                 |

| 3            | Shotgun                   |

| 4            | Uzis/Minigun              |

| F            | Rocket/Grenade Launcher   |

| X or Mouse 5 | Flamethrower/Sniper Rifle |

| C or Mouse 4 | Cannon/Sirian Powergun    |

| Left Alt     | Serious Bomb              |



