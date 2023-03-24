from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5880231538:AAGBtF4mJwh2WUoxprX4AJxCuE34cOcSjdI"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001455456913]# List of chat id's to forward messages from.
    TO_CHATS = [-1001716237919,-1001709087053,-1001751021009,-1001741161728,-1001189750195,-1001688416622,-1001419102324,-1001767529378]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 16
   
    
