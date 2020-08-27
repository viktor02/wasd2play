import requests
import json


class WasdLib:
    def __init__(self, stream_url):
        self.channel_id = self.get_channelid_from_url(stream_url)
        pass

    def get_last_stream_info(self):
        """ Get playlist m3u8 for current stream """

        payload = {
            'limit': '1',
            'offset': '0',
            'channel_id': self.channel_id,
            'media_container_type': 'SINGLE,COOP',
        }

        api_url = "https://wasd.tv/api/media-containers"
        r = requests.get(api_url, params=payload)

        json_r = json.loads(r.content)

        user_id = json_r['result'][0]['user_id']

        result = {
            'stream_name': json_r['result'][0]['media_container_name'],
            'stream_m3u8': "https://cdn.wasd.tv/live/{}/index.m3u8".format(user_id),
            'archive_stream_m3u8':
                json_r['result'][0]['media_container_streams'][0]['stream_media'][0]['media_meta']['media_archive_url'],
            'stream_fps': json_r['result'][0]['media_container_streams'][0]['stream_current_fps']
        }
        return result

    @staticmethod
    def get_channelid_from_url(stream_url):
        """ Get channel id from url """
        # https://wasd.tv/api/channels/nicknames/thedrzj
        nickname = stream_url.split("/")[-1:][0]
        r = requests.get("https://wasd.tv/api/channels/nicknames/{}".format(nickname))
        json_r = json.loads(r.content)
        channel_id = json_r['result']['channel_id']
        return channel_id

