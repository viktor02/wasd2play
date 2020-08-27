from wasd2play.wasd_lib import WasdLib
import subprocess
import argparse


def open_player(url, player='mpv'):
    wasd = WasdLib(url)
    s = wasd.get_last_stream_info()
    subprocess.run([player, s['stream_m3u8']])


my_parser = argparse.ArgumentParser(prog='wasd2play',
                                    usage='%(prog)s [options] url',
                                    description='Open wasd.tv stream in your player')

my_parser.add_argument('-p',
                       help='point your player',
                       default='mpv',
                       dest='open_player')
my_parser.add_argument('url',
                       help='stream url')

args = my_parser.parse_args()

open_player(args.url, args.open_player)
