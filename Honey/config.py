class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "OWNER_ID"
    sudo_users = "7142432455", "5934011554"
    GROUP_ID = -1002090005496
    TOKEN = "BOT_TOKEN"
    mongo_url = "MONGO_DB_URL"
    PHOTO_URL = ["https://graph.org/file/d5a2374e6027b72e92ae1.jpg", "https://graph.org/file/42cc1a7769dab55cbfa49.jpg"]
    SUPPORT_CHAT = "SUPPORT_CHAT"
    UPDATE_CHAT = "Honey_networks"
    BOT_USERNAME = "BOT_USERNAME"
    CHARA_CHANNEL_ID = "-1002136697049"
    api_id = 29044160
    api_hash = "API_HASH"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
