from wasd2play.wasd_lib import WasdLib
import subprocess
import argparse


def open_player(url, player):
    wasd = WasdLib(url)
    s = wasd.get_last_stream_info()
    print("[wasd2play] Got a stream playlist...")
    subprocess.run([player, s['stream_m3u8']], stdout=subprocess.PIPE)
    print("[wasd2play] {} in your {} player!".format(wasd.stream_name, player))


if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(prog='wasd2play',
                                        usage='%(prog)s [options] url',
                                        description='Open wasd.tv stream in your player')
    my_parser.add_argument('-p',
                           help='point your player',
                           default='vlc',
                           dest='open_player')
    my_parser.add_argument('url',
                           help='stream url')
    args = my_parser.parse_args()

    welcome_message = "##\n## wasd2play\n##\n" % args.url
    print(welcome_message)

    open_player(args.url, args.open_player)
