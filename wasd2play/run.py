from wasd2play.wasd_lib import WasdLib
import subprocess
import argparse


def open_player(url, player):
    wasd = WasdLib(url)
    s = wasd.get_last_stream_info()
    print("[wasd2play] Got a stream playlist...")
    print("[wasd2play] {} in your {} player!".format(wasd.stream_name, player))
    subprocess.run([player, s['stream_m3u8']], stdout=subprocess.PIPE)


def runner():
    my_parser = argparse.ArgumentParser(prog='wasd2play',
                                        usage='%(prog)s [options] url',
                                        description='Open any stream in your favorite player!')
    my_parser.add_argument('-p',
                           help='point your player',
                           default='vlc',
                           dest='your_player')
    my_parser.add_argument('url',
                           help='stream url')
    args = my_parser.parse_args()

    welcome_message = "##\n## wasd2play\n##\n"
    print(welcome_message)

    open_player(args.url, args.your_player)
