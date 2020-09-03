from wasd2play.wasd_lib import WasdLib
import subprocess
import argparse


def open_player(url, player, last_stream):
    """ Open player with stream"""
    wasd = WasdLib(url)
    s = wasd.get_last_stream_info()
    print("[wasd2play] Got a stream playlist...")
    print("[wasd2play] {} in your {} player!".format(wasd.stream_name, player))

    if last_stream:
        subprocess.run([player, s['archive_stream_m3u8']], stdout=subprocess.PIPE)
    else:
        subprocess.run([player, s['stream_m3u8']], stdout=subprocess.PIPE)


def runner():
    """ Entry point """
    my_parser = argparse.ArgumentParser(prog='wasd2play',
                                        usage='%(prog)s [options] url',
                                        description='Open any stream in your favorite player!')

    my_parser.add_argument('url',
                           help='stream url')
    my_parser.add_argument('-p', '--player',
                           help='point your player',
                           default='vlc',
                           dest='your_player')
    my_parser.add_argument('-l', '--last',
                           action='store_true',
                           dest="last_stream",
                           help='open last stream')

    args = my_parser.parse_args()

    welcome_message = "##\n## wasd2play\n##\n"
    print(welcome_message)

    open_player(args.url, args.your_player, args.last_stream)
