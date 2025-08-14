import asyncio
import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
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

# ----------------- MENU SYSTEM ----------------- #
LOADED_MODULES = {}
STICKER_FILE_ID = random.choices(config.START_STICKER_FILE_ID, weights=[1, 1])[0]

def get_paginated_buttons(page=1, items_per_page=15):
    modules = sorted(LOADED_MODULES.keys())
    total_pages = (len(modules) + items_per_page - 1) // items_per_page
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page
    current_modules = modules[start_idx:end_idx]

    buttons = [
        InlineKeyboardButton(mod, callback_data=f"help_{i}_{page}")
        for i, mod in enumerate(current_modules, start=start_idx)
    ]
    button_rows = [buttons[i:i + 3] for i in range(0, len(buttons), 3)]

    if page == 1:
        button_rows.append([InlineKeyboardButton("➡️", callback_data=f"area_{page + 1}")])
        button_rows.append([InlineKeyboardButton("🗑️", callback_data="delete")])
        button_rows.append([InlineKeyboardButton("Bᴀᴄᴋ", callback_data="st_back")])
    elif page == total_pages:
        button_rows.append([InlineKeyboardButton("⬅️", callback_data=f"area_{page - 1}")])
        button_rows.append([InlineKeyboardButton("🗑️", callback_data="delete")])
        button_rows.append([InlineKeyboardButton("Bᴀᴄᴋ", callback_data="st_back")])
    else:
        button_rows.append([
            InlineKeyboardButton("⬅️", callback_data=f"area_{page - 1}"),
            InlineKeyboardButton("🗑️", callback_data="delete"),
            InlineKeyboardButton("➡️", callback_data=f"area_{page + 1}"),
        ])
        button_rows.append([InlineKeyboardButton("Bᴀᴄᴋ", callback_data="st_back")])

    return InlineKeyboardMarkup(button_rows)

def get_main_menu_buttons():
    buttons = [
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.me.username}?startgroup=true")],
        [InlineKeyboardButton("🤝 Sᴜᴘᴘᴏʀᴛ", url=config.SUPPORT_GROUP),
         InlineKeyboardButton("👤 ᴏᴡɴᴇʀ", user_id=OWNER_ID)],
        [InlineKeyboardButton("Cᴏᴍᴍᴀɴᴅs", callback_data="yumeko_help")]
    ]
    return InlineKeyboardMarkup(buttons)

# ----------------- START COMMAND ----------------- #
@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)

    # Reaction
    await message.react("🍓", big=True)

    # Fancy loading animation
    loading_1 = await message.reply_text("⚡")  # ✅ fixed indentation
    for text in ["<b>ʟᴏᴀᴅɪɴɢ</b>", "<b>ʟᴏᴀᴅɪɴɢ.</b>", "<b>ʟᴏᴀᴅɪɴɢ..</b>", "<b>ᴀʟᴍᴏsᴛ ʜᴇʀᴇ...</b>"]:
        await asyncio.sleep(0.1)
        await loading_1.edit_text(text)
    await asyncio.sleep(0.1)
    await loading_1.delete()

    # Sticker before greeting
    await message.reply_cached_media(file_id=STICKER_FILE_ID)

    started_msg = await message.reply_text(
        text="<b>sᴛᴀʀᴛᴇᴅ...<a href='https://files.catbox.moe/0v9dyq.mp4'>ㅤ</a></b>"
    )
    await asyncio.sleep(0.4)
    await started_msg.delete()

    # If /start has arguments
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name.startswith("help"):
            await message.reply_text(
                "**📚 Available Commands & Modules:**",
                reply_markup=get_paginated_buttons()
            )
            return
        if name.startswith("sud"):
            await sudoers_list(client=client, message=message, _=_)
            return
        if name.startswith("inf"):
            pass
    else:
        await message.reply(
            text=(
                f"**ʜᴇʏ, {message.from_user.mention} 🎀**\n"
                f"**ɪ'ᴍ  {app.mention} ♡💫, ʏᴏᴜʀ ᴍᴜʟᴛɪᴛᴀsᴋɪɴɢ ᴀssɪsᴛᴀɴᴛ ʙᴏᴛ, ʙᴜɪʟᴛ ᴛᴏ sᴛʀᴇᴀᴍʟɪɴᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ᴡɪᴛʜ ᴀᴅᴠᴀɴᴄᴇᴅ ᴛᴏᴏʟs ᴀɴᴅ ғᴇᴀᴛᴜʀᴇs! 🌸**\n\n"
                f"[✨]({config.START_IMG_URL}) **✨ ʜᴇʀᴇ's ᴡʜᴀᴛ ɪ ᴄᴀɴ ᴅᴏ:**\n"
                f" • ᴇғғɪᴄɪᴇɴᴛ ɢʀᴏᴜᴘ sᴜᴘᴇʀᴠɪsɪᴏɴ🛠\n"
                f" • ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ ᴏᴘᴛɪᴏɴs🚫\n"
                f" • ᴇɴᴛᴇʀᴛᴀɪɴɪɴɢ ᴀɴᴅ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ ᴍᴏᴅᴜʟᴇs🎮\n\n"
                f"📚 **Need help? Click the button below! 💬**"
            ),
            reply_markup=get_main_menu_buttons(),
            invert_media=True,
            message_effect_id=5159385139981059251
        )

# ----------------- HELP MENU HANDLERS ----------------- #
@app.on_message(filters.command("help") & filters.private & ~BANNED_USERS)
async def help_command(client, message: Message):
    await message.reply(
        "**📚 All Available Modules:**",
        reply_markup=get_paginated_buttons(),
        invert_media=True
    )

@app.on_callback_query(filters.regex(r"^yumeko_help$"))
async def show_help_menu(client, query: CallbackQuery):
    await query.message.edit(
        "**📚 All Available Modules:**",
        reply_markup=get_paginated_buttons(),
        invert_media=True
    )

@app.on_callback_query(filters.regex(r"^help_\d+_\d+$"))
async def handle_help_callback(client, query: CallbackQuery):
    data = query.data.split("_")
    module_index = int(data[1])
    current_page = int(data[2])
    modules = sorted(LOADED_MODULES.keys())
    module_name = modules[module_index]
    help_text = LOADED_MODULES.get(module_name, "No help available for this module.")
    await query.message.edit(
        text=help_text,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data=f"area_{current_page}")]])
    )

@app.on_callback_query(filters.regex(r"^area_\d+$"))
async def handle_pagination_callback(client, query: CallbackQuery):
    page = int(query.data[5:])
    await query.message.edit(
        "**📚 All Available Modules:**",
        reply_markup=get_paginated_buttons(page),
        invert_media=True
    )

@app.on_callback_query(filters.regex("st_back"))
async def start_back(client, query: CallbackQuery):
    await query.message.edit(
        f"**Welcome back, {query.from_user.mention}**",
        reply_markup=get_main_menu_buttons(),
        invert_media=True
    )

# ----------------- GROUP START ----------------- #
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

# ----------------- WELCOME HANDLER ----------------- #
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
