class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5934011554"
    sudo_users = "7142432455", "5934011554"
    GROUP_ID = -1002090005496
    TOKEN = "6936772405:AAGLpttd9DAYPr75yCFphf1AbmiStbNub-8"
    mongo_url = "mongodb+srv://honey:honey@honey.mf1aofb.mongodb.net/?retryWrites=true&w=majority&appName=honey"
    PHOTO_URL = ["https://graph.org/file/d5a2374e6027b72e92ae1.jpg", "https://graph.org/file/42cc1a7769dab55cbfa49.jpg"]
    SUPPORT_CHAT = "honey_suppoort"
    UPDATE_CHAT = "Honey_networks"
    BOT_USERNAME = "DbhsgGbot"
    CHARA_CHANNEL_ID = "-1002136697049"
    api_id = 29044160
    api_hash = "b93797389eab3cec8c697ae4f2418466"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
