
# Serious Sam: Next Encounter Weapon Binds for Dolphin
An external tool which hooks into Dolphin, similar to the [Dolphin Mouse Injector](https://github.com/garungorp/MouseInjectorDolphinDuck), and allows for custom weapon binds for Serious Sam: Next Encounter to help the game play more like the PC games. 

This only works on Dolphin and the Gamecube version of Serious Sam: Next Encounter.

Works of Windows and maybe Linux, but most likely does not work on Mac as of this moment. 

This program will work for ``Serious Sam - Next Encounter (USA) (Rev 1).ciso`` and ``Serious Sam - Next Encounter (USA) (Rev 1).nkit.iso``. Other versions have not been tested.

## How To Use

1) Open your emulator and start Serious Sam: The Next Encounter

    - Optional but recommended: Before opening the game, right click on your game and select ``Add Shortcut to Desktop``. Find that shortcut and right click on it. Select ``Properties``. Find where it says ``Target`` and select the text box next to it. Go to the end of the text, where there will likely be a quotation mark and add ``--debug`` AFTER the quotations.
      
		 - Your new "Target" should look something like ``"path\to\Dolphin\folder\Dolphin.exe" -e "path/to/Serious/Sam/rom" --debug``
       
		 - This will  help you in being able to manually clear Dolphin's JIT cache, which may be important for you.
       
     - If you are using Linux, you can enable debug mode for Dolphin through opening the emulator through the terminal with the ``-d`` flag. Altogether, it should look like ``dolphin-emu -d`` or ``flatpak run org.DolphinEmu.dolphin-emu -d`` if you installed via a flatpak.

<br>

2) Assuming that you plan to use the Dolphin Mouse Injector (which is extremely likely), download [my barebones fork](https://github.com/GrouganDev/MouseInjectorDolphinDuckChangedInput) in order to ensure that any of the keybinds for that program do not conflict with this one's.

<br>

3) You should see a file called ``Serious Sam Weapon Binds.ini``. This is a Dolphin Gamecube controller profile tailor-made for use with both this program and the Dolphin Mouse Injector. Place the file in the folder which contains all Gamecube controller profiles for your installation of Dolphin. 
	- On Windows the default location is generally 'C:\Users\yourusername\AppData\Roaming\Dolphin Emulator\Config\Profiles\GCPad'
	
	- For Linux, it may vary depending on distro and method of installation, but it may be in '~/.config/dolphin-emu/Config/Profiles/GCPad'
	
		- If you cannot find the necessary folder, open Dolphin, hit the 'Controllers' button near the top of the window, go to your Gamecube controller port and press 'Configure' to the right of the window. You should see a down arrow near the top right of the newly popped up window. Press it and then press 'Open Folder'. That will take you to where the program reads all of its controller profiles. 
	- Now select your new profile from the drop down menu to the left of that arrow. Once you have selected the correct profile, click 'Load' to set up all of your inputs for custom weapon bindings. 

<br>

4) Open the ``NE Weapon Injector`` executable which matches your operating system. The program will automatically hook itself onto Dolphin so long as the game is already open before you run this executable.  
	- If you wish to unhook or rehook after the executable is already running, you will need to clear Dolphin's JIT cache before doing so.

		- Assuming you are running on the debug version of Dolphin, which the directions for doing so has already been given above, go to the top of Dolphin's window where all of the drop down menus are. Click on the one called ``JIT``. Then click ``Clear Cache``. Now, you can press right shift (by default) in your program to successfully toggle whether or not it is hooking to Dolphin.

<br>

5) So long as the program is hooked to Dolphin, the weapon binds should work out of the box. If you wish to change them, you can edit the ``main.py`` file to manually edit weapon bindings. 
	- If you do edit your bindings and wish to compile the new version of your ``main.py`` script into a new executable, run the ``python_setup.bat`` file if you're on Windows or ``python_setup.sh`` if you're on Linux. This should ensure that you have all of the files necessary along with a proper virtual environment. Then, run the ``compile_python`` script that suits your OS to compile your script into an executable.

		- Note: You must have [Python](https://www.python.org/downloads/) installed on your computer in order to do this. This program was created with Python 3.12.4, but later versions also work. If you do not have Python installed on your computer, these scripts will not work. 



## Default Weapon Bindings
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
