import asyncio
import time
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from AviaxMusic import app
from AviaxMusic.misc import _boot_
from AviaxMusic.plugins.sudo.sudoers import sudoers_list
from AviaxMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
)
from AviaxMusic.utils.decorators.language import LanguageStart
from AviaxMusic.utils.inline import help_pannel, start_panel
from config import BANNED_USERS
from strings import get_string


WELCOME_VIDEO = "https://files.catbox.moe/ck28qb.mp4"

# Private /start
@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)

    # Loading animation
    loading_msg = await message.reply_text("⚡")
    for dots in ["ʟᴏᴀᴅɪɴɢ", "ʟᴏᴀᴅɪɴɢ.", "ʟᴏᴀᴅɪɴɢ..", "ᴀʟᴍᴏsᴛ ʜᴇʀᴇ..."]:
        await asyncio.sleep(0.1)
        await loading_msg.edit_text(f"<b>{dots}</b>")
    await loading_msg.delete()

    # Reaction
    await message.react("🍓", big=True)

    # Welcome text
    welcome_text = (
        f"❤️‍🩹 𝐖ᴇʟᴄᴏᴍᴇ {message.from_user.mention} "
        f"(ID: <code>{message.from_user.id}</code>) 𝐓ᴏ\n\n"
        "🌙 ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ 🍇\n\n"
        "꩟ 𝐒ᴛᴜᴅɪᴏ 𝐌ᴀsᴛᴇʀ 𝐀ᴜᴅɪᴏ 𝐐ᴜᴀʟɪᴛʏ 🍇\n"
        "꩟ 𝐙ᴇʀᴏ-𝐋ᴀᴛᴇɴᴄʏ 𝐒ᴛʀᴇᴀᴍɪɴɢ 🍇\n"
        "꩟ 𝟐𝟒/𝟕 𝐀ᴄᴛɪᴠᴇ & 𝐑ᴇsᴘᴏɴsɪᴠᴇ 🍇\n"
        "꩟ 𝐒ᴍᴀʀᴛ 𝐀𝐈-𝐏ᴏᴡᴇʀᴇᴅ 𝐏ʟᴀʏʟɪsᴛs 🍇\n"
        "꩟ 𝐋ɪɡʜᴛɴɪɴɢ-𝐅ᴀsᴛ 𝐒ᴇᴀʀᴄʜᴇs 🍇\n\n"
        f"꩟ 𝐘ᴏᴜʀ 𝐏ʀᴏғɪʟᴇ 🍇\n"
        f"꩟ 𝐍ᴀᴍᴇ :- {message.from_user.first_name}\n"
        f"꩟ 𝐈'𝐃 :- {message.from_user.id}\n\n"
        "🎧 𝐑ᴇᴀᴅʏ 𝐓ᴏ 𝐄xᴘᴇʀɪᴇɴᴄᴇ 𝐌ᴜsɪᴄ 𝐋ɪᴋᴇ 𝐍ᴇᴠᴇʀ 𝐁ᴇғᴏʀᴇ? 💃🏼\n\n"
        "𝐉ᴏɪɴ 𝐎ᴜʀ 𝐌ᴜsɪᴄ 𝐑ᴇᴠᴏʟᴜᴛɪᴏɴ 𝐓ᴏᴅᴀʏ! 🎸"
    )

    # Send video + welcome text + buttons in one message
    await message.reply_video(
        video=WELCOME_VIDEO,
        caption=welcome_text,
        reply_markup=help_pannel(_)
    )


# Group /start
@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    await message.react("🍓", big=True)
    await add_served_chat(message.chat.id)

    welcome_text = (
        f"❤️‍🩹 𝐖ᴇʟᴄᴏᴍᴇ {message.from_user.mention} "
        f"(ID: <code>{message.from_user.id}</code>) 𝐓ᴏ\n\n"
        "🌙 ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ 🍇\n\n"
        "꩟ 𝐒ᴛᴜᴅɪᴏ 𝐌ᴀsᴛᴇʀ 𝐀ᴜᴅɪᴏ 𝐐ᴜᴀʟɪᴛʏ 🍇\n"
        "꩟ 𝐙ᴇʀᴏ-𝐋ᴀᴛᴇɴᴄʏ 𝐒ᴛʀᴇᴀᴍɪɴɢ 🍇\n"
        "꩟ 𝟐𝟒/𝟕 𝐀ᴄᴛɪᴠᴇ & 𝐑ᴇsᴘᴏɴsɪᴠᴇ 🍇\n"
        "꩟ 𝐒ᴍᴀʀᴛ 𝐀𝐈-𝐏ᴏᴡᴇʀᴇᴅ 𝐏ʟᴀʏʟɪsᴛs 🍇\n"
        "꩟ 𝐋ɪɡʜᴛɴɪɴɢ-𝐅ᴀsᴛ 𝐒ᴇᴀʀᴄʜᴇs 🍇\n\n"
        f"꩟ 𝐘ᴏᴜʀ 𝐏ʀᴏғɪʟᴇ 🍇\n"
        f"꩟ 𝐍ᴀᴍᴇ :- {message.from_user.first_name}\n"
        f"꩟ 𝐈'𝐃 :- {message.from_user.id}\n\n"
        "🎧 𝐑ᴇᴀᴅʏ 𝐓ᴏ 𝐄xᴘᴇʀɪᴇɴᴄᴇ 𝐌ᴜsɪᴄ 𝐋ɪᴋᴇ 𝐍ᴇᴠᴇʀ 𝐁ᴇғᴏʀᴇ? 💃🏼\n\n"
        "𝐉ᴏɪɴ 𝐎ᴜʀ 𝐌ᴜsɪᴄ 𝐑ᴇᴠᴏʟᴜᴛɪᴏɴ 𝐓ᴏᴅᴀʏ! 🎸"
    )

    await message.reply_video(
        video=WELCOME_VIDEO,
        caption=welcome_text,
        reply_markup=InlineKeyboardMarkup(start_panel(_))
    )


# Auto-welcome when bot joins a group
@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)

            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass

            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)

                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                await message.reply_video(
                    video=WELCOME_VIDEO,
                    caption=_["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(start_panel(_))
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()

        except Exception as ex:
            print(ex)
