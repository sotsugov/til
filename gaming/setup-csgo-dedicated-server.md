# Counter-Strike: Global Offensive Dedicated Servers

## Windows Azure VM Setup
* New Compute > Virtual Machine > From Gallery > Windows Server
* Enable endpoints

You need to forward the ports to the ip address the server is running on. You only need to forward `udp 27015` for gaming. If you want to use rcon from outside too you also need to forward `tcp 27015`. No other ports are needed.
Also you need to make sure none of the ports is blocked by any kind of firewall on your router or server.

```
CSGO TCP        TCP 27015   27015
CSGO UDP        UDP 27015   27015
PowerShell      TCP 5986    5986
Remote Desktop  TCP 56421   3389
```

## Windows
* Create a folder for SteamCMD.
For example
`C:\steamcmd`
* Download SteamCMD for Windows: https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip
* Extract the contents of the zip to the folder.

## SteamCMD
* Start SteamCMD. At the `Steam>` prompt, set your CS:GO Dedicated Server install directory.
```
force_install_dir c:\csgo-ds\
force_install_dir .\csgo-ds\
```
Steam may require a login
`login anonymous`

* Install or Update CS:GO. If this is your first time installing or if you are trying to verify the integrity of the server files:
`app_update 740 validate`

It will take some time to install it since its little big at the end we are installing a game server.
* Once finished, type `quit` at the `Steam>` prompt to properly log off of the Steam servers.

## Server Config
* You can choose not to edit the new files for server settings, if you'll not use any mods or workshop items.
Now lets go inside the csgo folder. You need to create two files. Duplicate `gamemodes_server.txt.example` and rename it to `gamemodes_server.txt`. Duplicate `gamerulescvars.txt.example` and modify it to `gamerulescvars.txt`

* The server settings will need to be specified in the new config file created in the `csgo/cfg` folder.
`C:\csgo_ds\csgo\cfg` folder and create a file `server.cfg` with same method of notepad.
Inside of it you can put some settings lines like this:

```
hostname "dgen tactics"
rcon_password "prettypassword"
sv_password ""

mp_freezetime 5
mp_join_grace_time 15
mp_match_end_restart 0
sv_cheats 0
sv_lan 0
sv_allow_lobby_connect_only 0
sv_dc_friends_reqd 0
sv_hibernate_when_empty 0

bot_difficulty 1
bot_chatter "off"
bot_join_after_player 0
bot_quota 10
bot_quota_mode "fill"
```

## Running srcds.exe
You can create a bat file to run the server, however, as a cmd line it will look something like this:
`PS C:\csgo_ds\steamcmd\csgo_ds> .\srcds.exe -game csgo -console -usercon +game_type 0 +game_mode 0 +mapgroup mg_active +map de_dust2  +sv_setsteamaccount A***6A53E6 -tickrate 128`

## Connecting in the game
You'll need to get the public IP address of the server or DNS name, in Azure, for example it's located in Dashboard > Quick Glance > Public virtual IP (VIP) address.

```
connect **.cloudapp.net
connect 52.**.**.130:27015
```

## Registering Game Server Login Token
To create your GSLTs, visit the GSLT creation utility and follow the instructions here: http://steamcommunity.com/dev/managegameservers

Each GSLT is restricted for use on one dedicated server instance only, and should be passed on command line with `+sv_setsteamaccount THISGSLTHERE`. You can also use command line setting `-net_port_try 1` to avoid instances from reusing the same GSLT by accident.


### Compiled from:
* https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Dedicated_Servers
* http://blog.counter-strike.net/index.php/server_guidelines/
* https://developer.valvesoftware.com/wiki/Source_Dedicated_Server
