import requests
import json


class WasdLib:
    def __init__(self, stream_url):
        self.channel_id = self.get_channelid_from_url(stream_url)
        self.stream_name = None

    def get_last_stream_info(self):
        """ Get playlist m3u8 for current stream """

        payload = {
            'limit': '1',
            'offset': '0',
            'channel_id': self.channel_id,
            'media_container_type': 'SINGLE,COOP',
        }

        s = requests.session()
        s.get("https://wasd.tv/api/auth/anon-token")

        api_url = "https://wasd.tv/api/media-containers"
        r = requests.get(api_url, params=payload)

        json_r = json.loads(r.content)

        result = {
            'stream_name': json_r['result'][0]['media_container_name'],
            'stream_m3u8':
                json_r['result'][0]['media_container_streams'][0]['stream_media'][0]['media_meta']['media_url'],
            'archive_stream_m3u8':
                json_r['result'][0]['media_container_streams'][0]['stream_media'][0]['media_meta']['media_archive_url']
        }

        self.stream_name = result['stream_name']
        return result

    @staticmethod
    def get_channelid_from_url(stream_url):
        """ Get channel id from url """
        nickname = stream_url.split("/")[-1:][0]
        r = requests.get("https://wasd.tv/api/channels/nicknames/{}".format(nickname))
        json_r = json.loads(r.content)
        channel_id = json_r['result']['channel_id']
        return channel_id

