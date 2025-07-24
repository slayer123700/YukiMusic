import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "26249286"))
API_HASH = getenv("API_HASH", "4e3bf0b014fda4ac752e8f4ab854279b")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8040764357:AAG25PTTdaM6rmJZO-WhAWLHjgs4u5w6KWs")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://musicbotxd:musicbotxd@cluster0.6thyk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1700))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", -1002745123292))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6018803920"))

#YOUTUBE API's 
API_URL = getenv("API_URL", 'https://www.googleapis.com/youtube/v3/search?part=snippet&q=your_search_query&key=AIzaSyD_iwN3MADFGdp4xCZFo4G-e04BPyFORms') #youtube song url
API_KEY = getenv("API_KEY", 'AIzaSyD_iwN3MADFGdp4xCZFo4G-e04BPyFORms')

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/slayer123700/YukiMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/eldian_bot_update")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+vuzPm5BpV3Y0NTVl")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://telegra.ph/file/d3d80cd8cc0a6363eb21d.jpg")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION1", "AQFH6C0AKkxz-IBQU1Myfb_53E7vnRvk3OVmYrQVVSxuT4HebUGsmEznymVrgSPncqJhGKb086AyD-EuwyqebV6lAST3eD-l2kWKDCjRcxrirCsow84pyybWmPMsOmsuETJuMFVI-wiuItVa5zmEdv-KNSEva4Xs9142_N8KJ76FjXSXieDB5HJU_bWBE5mbR9L7I6by5KmdRG94pq04hLLlW1yE6HEKjtwANqWcetk0KK30Lu_K-DZ9u3zQ4DrCMpFdefcp31SMKk3pL6H36dzpIEMEw_verhYLUxJ-PFXgfHWxg93fFcDvVUWQ1slMAai688gFKBLyBDffCdrrOuBFn75qvAAAAAHKOI5UAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/v9assw.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/2rahxv.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/0t6grx.jpg"
STATS_IMG_URL = "https://files.catbox.moe/2rahxv.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/v9assw.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/v9assw.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/uv2r88.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
