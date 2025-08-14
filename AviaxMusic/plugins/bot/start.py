import asyncio
import time
import random
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
)
from AviaxMusic.utils.decorators.language import LanguageStart
from AviaxMusic.utils.formatters import get_readable_time
from AviaxMusic.utils.inline import help_pannel, start_panel
from config import BANNED_USERS
from strings import get_string

STICKER_FILE_ID = random.choice(config.START_STICKER_FILE_ID)

# Generate welcome text with blockquotes
def get_welcome_text(user):
    return (
        "🌟✨ WELCOME TO ˹ Shizuka ꭙ Music ˼ ✨🌟\n\n"
        "```\n"
        "> 🎧 THE ULTIMATE MUSIC EXPERIENCE 🎶\n"
        "> ✨ Studio Master Audio Quality\n"
        "> 🚀 Zero-Latency Streaming\n"
        "> 🌙 24/7 Active & Responsive\n"
        "> 💫 Smart AI-Powered Playlists\n"
        "> 🔥 Lightning-Fast Searches\n"
        "> 👤 YOUR PROFILE 👑\n"
        f"💖 Name: {user.first_name}\n"
        f"🔐 ID: {user.id}\n"
        "> ⚡ JOIN OUR MUSIC REVOLUTION TODAY! 🎉\n"
        "Ready to experience music like never before?\n"
        "```"
    )

# Private start command
@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)

    # 🍓 Reaction
    await message.react("🍓", big=True)

    # Sticker
    await message.reply_cached_media(file_id=STICKER_FILE_ID)

    # Video + blockquote text in the same message
    out_buttons = start_panel(_)  # Buttons
    await message.reply_video(
        video="https://files.catbox.moe/0v9dyq.mp4",
        caption=get_welcome_text(message.from_user),
        parse_mode=None,  # No parse mode to avoid errors
        supports_streaming=True,
        reply_markup=InlineKeyboardMarkup(out_buttons)
    )

    # Handle /start arguments
    if len(message.text.split()) > 1:
        arg = message.text.split(None, 1)[1]
        if arg.startswith("help"):
            keyboard = help_pannel(_)
            await message.reply_text(
                "Here’s how you can use me ⬇️",
                reply_markup=keyboard
            )
        elif arg.startswith("sud"):
            await sudoers_list(client=client, message=message, _=_)
        elif arg.startswith("inf"):
            m = await message.reply_text("⚡️ Searching...")
            query = arg.replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            next_result = await results.next()
            if isinstance(next_result, dict) and "result" in next_result:
                for result in next_result["result"]:
                    title = result["title"]
                    duration = result["duration"]
                    views = result["viewCount"]["short"]
                    thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                    channel = result["channel"]["name"]
                    link = result["link"]
                    published = result["publishedTime"]
                    key = InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="ʏᴏᴜᴛᴜʙᴇ", url=link)]]
                    )
                await m.delete()
                await app.send_photo(
                    chat_id=message.chat.id,
                    photo=thumbnail,
                    caption=f"{title}\nDuration: {duration}\nViews: {views}\nPublished: {published}\nChannel: {channel}",
                    reply_markup=key,
                )

# Group start command
@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_text(
        text=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    await add_served_chat(message.chat.id)


# Welcome new chat members
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
                            config.SUPPORT_GROUP,
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
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
