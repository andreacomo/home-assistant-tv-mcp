import requests
import json
from mcp.server.fastmcp import FastMCP
from typing import TypeVar
import os

config = {
    'hass_url': os.environ.get('HASS_URL', 'http://homeassistant.local:8123'),
    'hass_token': os.environ.get('HASS_TOKEN', '')
}

T = TypeVar("T")
mcp = FastMCP(name="Samsung TV Remote Service Tool")

@mcp.tool()
def send_remote_command(entity_id: str, command_keys: list[str]) -> list[dict[str, T]]:
    """
    Send a remote command to the Samsung TV.

    :param entity_id: The entity ID of the Samsung TV. The format supported must be 'remote.tv_<model_identifier>', so the entity ID must be of the "remote" domain
    :param command_keys: A list of command keys to send to the TV. Allowed keys are:
        Number keys and channel keys:
        Key	        Description
        KEY_1	    1
        KEY_2	    2
        KEY_3	    3
        KEY_4	    4
        KEY_5	    5
        KEY_6	    6
        KEY_7	    7
        KEY_8	    8
        KEY_9	    9
        KEY_0	    0
        KEY_CHUP	ChannelUp
        KEY_CHDOWN	ChannelDown
        KEY_PRECH	PreviousChannel
        KEY_FAVCH	FavoriteChannels
        KEY_CH_LIST	ChannelList

        Volume keys:
        Key	        Description
        KEY_VOLUP	VolumeUp
        KEY_VOLDOWN	VolumeDown
        KEY_MUTE	Mute/Unmute

    :return: A list of dictionaries with the result of the command.
    """
    url = config['hass_url'] + '/api/services/remote/send_command'
    headers = {
        'Authorization': f"Bearer {config['hass_token']}",
        'Content-Type': 'application/json'
    }
    body = {
        'entity_id': entity_id,
        'command': command_keys
    }
    response = requests.post(url, headers=headers, data=json.dumps(body))
    return response.json()

def main():
    """Entry point for the direct execution server."""
    mcp.run()


if __name__ == "__main__":
    main()