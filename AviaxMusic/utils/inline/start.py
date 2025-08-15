# AviaxMusic/utils/inline/start.py

from pyrogram.types import InlineKeyboardButton
import config
from AviaxMusic import app

# Buttons for when the bot is in a group
def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


# Buttons for private chat with the bot
def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP),
        ],
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ɪɴ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="ᴜᴛɪʟɪᴛʏ ᴄᴏᴍᴍᴀɴᴅs", callback_data="settings_back_helper"),
        ]
    ]
    return buttons
