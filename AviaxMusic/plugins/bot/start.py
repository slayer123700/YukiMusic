import asyncio
import time
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

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
    is_on_off,
)
from AviaxMusic.utils.decorators.language import LanguageStart
from AviaxMusic.utils.formatters import get_readable_time
from AviaxMusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS, OWNER_ID
from strings import get_string


@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)

    # Loading animation
    loading_1 = await message.reply_text("⚡")
    for dots in ["ʟᴏᴀᴅɪɴɢ", "ʟᴏᴀᴅɪɴɢ.", "ʟᴏᴀᴅɪɴɢ..", "ᴀʟᴍᴏsᴛ ʜᴇʀᴇ..."]:
        await asyncio.sleep(0.1)
        await loading_1.edit_text(f"<b>{dots}</b>")
    await loading_1.delete()

    # Reaction and message effect
    await message.react("🍓", big=True)

    # Temporary start animation
    started_msg = await message.reply_text(
        text="<b>sᴛᴀʀᴛᴇᴅ...<a href='https://files.catbox.moe/ck28qb.mp4' target='_blank'>ㅤ ㅤㅤㅤ</a></b>",
        invert_media=True,
        message_effect_id=5159385139981059251
    )
    await asyncio.sleep(0.4)
    await started_msg.delete()

    # Welcome message
    welcome_text = (
        f"❤️‍🩹 𝐖ᴇʟᴄᴏᴍᴇ {message.from_user.mention} (ID: <code>{message.from_user.id}</code>) 𝐓ᴏ\n\n"
        "🌙 ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ 🍇\n\n"
        "꩟ 𝐒ᴛᴜᴅɪᴏ 𝐌ᴀsᴛᴇʀ 𝐀ᴜᴅɪᴏ 𝐐ᴜᴀʟɪᴛʏ 🍇\n"
        "꩟ 𝐙ᴇʀᴏ-𝐋ᴀᴛᴇɴᴄʏ 𝐒ᴛʀᴇᴀᴍɪɴɢ 🍇\n"
        "꩟ 𝟐𝟒/𝟕 𝐀ᴄᴛɪᴠᴇ & 𝐑ᴇsᴘᴏɴsɪᴠᴇ 🍇\n"
        "꩟ 𝐒ᴍᴀʀᴛ 𝐀𝐈-𝐏ᴏᴡᴇʀᴇᴅ 𝐏ʟᴀʏʟɪsᴛs 🍇\n"
        "꩟ 𝐋ɪɡʜᴛɴɪɴɢ-𝐅ᴀsᴛ 𝐒ᴇᴀʀᴄʜᴇs 🍇\n"
        "꩟ 𝐘ᴏᴜʀ 𝐏ʀᴏғɪʟᴇ 🍇\n\n"
        "꩟ 𝐍ᴀᴍᴇ :- \n"
        "꩟ 𝐈'𝐃 :-\n\n"
        "🎧 𝐑ᴇᴀᴅʏ 𝐓ᴏ 𝐄xᴘᴇʀɪᴇɴᴄᴇ 𝐌ᴜsɪᴄ 𝐋ɪᴋᴇ 𝐍ᴇᴠᴇʀ 𝐁ᴇғᴏʀᴇ? 💃🏼\n\n"
        "𝐉ᴏɪɴ 𝐎ᴜʀ 𝐌ᴜsɪᴄ 𝐑ᴇᴠᴏʟᴜᴛɪᴏɴ 𝐓ᴏᴅᴀʏ! 🎸"
    )

    # FIXED: help_pannel already returns InlineKeyboardMarkup
    await message.reply_text(
        text=welcome_text,
        reply_markup=help_pannel(_),
        invert_media=True,
        message_effect_id=5159385139981059251
    )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)  # returns a list
    uptime = int(time.time() - _boot_)

    await message.react("🍓", big=True)

    welcome_text = (
        f"❤️‍🩹 𝐖ᴇʟᴄᴏᴍᴇ {message.from_user.mention} (ID: <code>{message.from_user.id}</code>) 𝐓ᴏ\n\n"
        "🌙 ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴍᴜsɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ 🍇\n\n"
        "꩟ 𝐒ᴛᴜᴅɪᴏ 𝐌ᴀsᴛᴇʀ 𝐀ᴜᴅɪᴏ 𝐐ᴜᴀʟɪᴛʏ 🍇\n"
        "꩟ 𝐙ᴇʀᴏ-𝐋ᴀᴛᴇɴᴄʏ 𝐒ᴛʀᴇᴀᴍɪɴɢ 🍇\n"
        "꩟ 𝟐𝟒/𝟕 𝐀ᴄᴛɪᴠᴇ & 𝐑ᴇsᴘᴏɴsɪᴠᴇ 🍇\n"
        "꩟ 𝐒ᴍᴀʀᴛ 𝐀𝐈-𝐏ᴏᴡᴇʀᴇᴅ 𝐏ʟᴀʏʟɪsᴛs 🍇\n"
        "꩟ 𝐋ɪɡʜᴛɴɪɴɢ-𝐅ᴀsᴛ 𝐒ᴇᴀʀᴄʜᴇs 🍇\n"
        "꩟ 𝐘ᴏᴜʀ 𝐏ʀᴏғɪʟᴇ 🍇\n\n"
        "꩟ 𝐍ᴀᴍᴇ :- \n"
        "꩟ 𝐈'𝐃 :-\n\n"
        "🎧 𝐑ᴇᴀᴅʏ 𝐓ᴏ 𝐄xᴘᴇʀɪᴇɴᴄᴇ 𝐌ᴜsɪᴄ 𝐋ɪᴋᴇ 𝐍ᴇᴠᴇʀ 𝐁ᴇғᴏʀᴇ? 💃🏼\n\n"
        "𝐉ᴏɪɴ 𝐎ᴜʀ 𝐌ᴜsɪᴄ 𝐑ᴇᴠᴏʟᴜᴛɪᴏɴ 𝐓ᴏᴅᴀʏ! 🎸"
    )

    # FIXED: start_panel returns a list, so wrap in InlineKeyboardMarkup
    await message.reply_text(
        text=welcome_text,
        reply_markup=InlineKeyboardMarkup(out),
        invert_media=True,
        message_effect_id=5159385139981059251
    )

    await add_served_chat(message.chat.id)


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

                out = start_panel(_)
                await message.reply_text(
                    _["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out)
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
