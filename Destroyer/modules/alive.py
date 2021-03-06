import time

from telethon import version
from uniborg.util import Destroyer_on_cmd, sudo_cmd

from Destroyer import ALIVE_NAME, CMD_HELP, Lastupdate
from Destroyer.Configs import Config
from Destroyer.modules import currentversion


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "firebot"
PM_IMG = Config.ALIVE_IMAGE
pm_caption = "  __**๐ ๐ป๐ผ๐๐โ๐๐๐ผโ ๐๐ โ๐โโ๐โ๐พ ๐๐โ๐ผ๐๐๐ฝ๐๐๐๐ ๐**__\n\n"

pm_caption += f"**โโโโโโโ|โโโโโ|โโโโโโ**\n\n"
pm_caption += f"                 โโฟ แดแดsแดแดส โฟโ\n  **{DEFAULTUSER}**\n\n"
pm_caption += f"โโโโโโโโษชษดาแดโโโโโโโโ\n"
pm_caption += f"โฃโขโณโ  `แดแดสแดแดสแดษด:` `{version.__version__}` \n"
pm_caption += f"โฃโขโณโ  `แด แดสsษชแดษด:` `{currentversion}`\n"
pm_caption += f"โฃโขโณโ  `แดแดแดษชแดแด:` `{uptime}`\n"
pm_caption += f"โฃโขโณโ  `แดสแดษดษดแดส:` [แดแดษชษด](https://t.me/DESTROYER_USERBOT)\n"
pm_caption += f"โโโโโโโโโโโโโโโโโโโโ\n"
pm_caption += f" ||โข|| ๐๐ผโ๐โ๐๐๐ ๐น๐ ๐ป๐ผ๐๐โ๐๐๐ผโ ๐๐๐ผโ๐น๐๐ ||โข||\n"
pm_caption += " [ษขษชแดสแดส](https://github.com/rahulchoudhary17/DESTROYER-USERBOT) โข [ษขสแดแดแด](https://t.me/TEAM_DESTROYER_ON_STRICK)"


@fire.on(Destroyer_on_cmd(pattern=r"alive"))
@fire.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def chris(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if firebot UserBot is Alive"
    }
)
