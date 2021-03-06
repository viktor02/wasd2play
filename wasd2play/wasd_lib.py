import requests
import json


class WasdLib:
    def __init__(self, stream_url):
        self.channel_id = self.get_channel_id_from_url(stream_url)
        self.stream_name = ""
        self.stream_status = "STOPPED"

        wasd_session = requests.session()
        wasd_session.get("https://wasd.tv/api/auth/anon-token")

    def get_json_of_stream_by_offset(self, limit=1, offset=0, status='INIT,IDLE,RUNNING,STOPPED'):
        payload = {
            'limit': limit,
            'offset': offset,
            'channel_id': self.channel_id,
            'media_container_type': 'SINGLE,COOP',
            'media_container_status': status,
            'order_direction': 'DESC'
        }

        api_url = "https://wasd.tv/api/v2/media-containers"
        result_json = requests.get(api_url, params=payload)
        result = json.loads(result_json.content)
        return result

    def get_stream(self, selected_stream=0) -> dict:
        """ Get playlist m3u8 for current stream """
        stream_json = self.get_json_of_stream_by_offset(1, selected_stream)

        tags = []
        for tag in stream_json['result'][0]['tags']:
            tags.append(tag['tag_name'])

        result = {
            'stream_name': stream_json['result'][0]['media_container_name'],
            'stream_status': stream_json['result'][0]['media_container_status'],
            'stream_m3u8':
                stream_json['result'][0]['media_container_streams'][0]['stream_media'][0]['media_meta']['media_url'],
            'archive_stream_m3u8':
                stream_json['result'][0]['media_container_streams'][0]['stream_media'][0]['media_meta'][
                    'media_archive_url'],
            'stream_tags':
                tags
        }

        self.stream_name = result['stream_name']
        self.stream_status = result['stream_name']
        return result

    def get_streams(self, page=1) -> tuple:
        """ Get tuple of streams
        Bugs: wasd.tv returns only up to 30 streams, regardless of the limit and offset. Also, if not point stream status, return only up to 15
        """

        limit = 10
        offset = (page * 10) - 10
        json_r = self.get_json_of_stream_by_offset(limit, offset)

        list_of_streams = []
        for i in json_r['result']:
            name = i['media_container_name']
            list_of_streams.append(name)
        return tuple(list_of_streams)

    @staticmethod
    def get_channel_id_from_url(stream_url) -> int:
        """ Convert streamer nickname to channel id """
        nickname = stream_url.split("/")[-1:][0]
        r = requests.get(f"https://wasd.tv/api/channels/nicknames/{nickname}")
        json_r = json.loads(r.content)
        channel_id = int(json_r['result']['channel_id'])
        return channel_id
