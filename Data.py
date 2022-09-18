from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
❣ ʜᴇʟʟᴏ {} ❣

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ꜰᴏʀᴄᴇꜱᴜʙ ʙᴏᴛ 💖

ɪ ᴄᴀɴ ꜰᴏʀᴄᴇ ʏᴏᴜʀ ɢʀᴜᴏᴘ'ꜱ ᴜꜱᴇʀꜱ ᴛᴏ ᴊᴏɪɴ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴄʜᴀᴛ❄️
ᴛʜᴇ ᴄʜᴀᴛ ᴄᴀɴ ʙᴇ ᴀ ɢʀᴏᴜᴘ ᴏʀ ᴀ ᴄʜᴀɴɴᴇʟ☘
ɪᴛ ᴄᴀɴ ʙᴇ ᴘʀɪᴠᴀᴛᴇ ᴏʀ ᴘᴜʙʟɪᴄ🍄

ᴜꜱᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ᴛᴏ ʟᴇᴀʀɴ ᴍᴏʀᴇ👻

ᴘᴏᴡᴇʀᴅ ʙʏ @EpicBotsSl 🇱🇰

    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏛️ Return Home 🏛️", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🤖 More Bots 🤖", url="https://t.me/EpicBotsSl")],
        [
            InlineKeyboardButton("❔ How to Use ❔", callback_data="help"),
            InlineKeyboardButton("♾️ About ♾️", callback_data="about")
        ],
        [InlineKeyboardButton("♻️ Owner ♻️", url="https://t.me/wisula4")],
        [InlineKeyboardButton("🛫 Support Group 🛫", url="https://t.me/Epicchats")],
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group👩‍💻

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private🤗

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub --1001620454933` or `/forcesubscribe -1001620454933`

4) [Optional] Use /settings to change settings! 🙄

5) You are good Leave the rest to me🥰

🤖 **Available Commands** 🤖

/fsub - See current force subscribe chat ☘️
/fsub chat_id/username - Force users to join the particular chat☘️
/settings - Change Group Settings☘️
/id - Get the chat id of any group or channel☘️
/about - About The Bot☘️
/help - This Message☘️
/start - Start the Bot☘️

**Note** - You can also use `/forcesubscribe` instead of `/fsub`😊
    """

    # About Message
    ABOUT = """
**About This Bot** 🤩

A telegram force subscribing bot by @EpicBotsSl 🇱🇰

Source Code : [wisula](https://github.com/wisula)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @ImDark_Empire
    """
