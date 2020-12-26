from wasd2play.wasd_lib import WasdLib
import subprocess
import argparse


def open_player(url, player, selected_stream=0, force_open_last_stream=False):
    """ Open player with stream """

    wasd = WasdLib(url)

    print("[wasd2play] Got a stream playlist...")
    stream_info = wasd.get_stream(selected_stream)

    # Set to current url
    stream_url = stream_info['stream_m3u8']

    # If stream offline, open last
    if stream_info['stream_status'] == "STOPPED" or force_open_last_stream:
        print("[wasd2play] Open last archived stream...")
        print("[wasd2play] {} in your {} player!".format(wasd.stream_name, player))
        stream_url = stream_info['archive_stream_m3u8']
    else:
        print("[wasd2play] Open current stream...")
        print("[wasd2play] {} in your {} player!".format(wasd.stream_name, player))

    tags = ", ".join(stream_info['stream_tags'])
    print("[wasd2play] {}".format(tags))

    try:
        subprocess.run([player, stream_url], stdout=subprocess.PIPE, check=True)
    except FileNotFoundError:
        print("Error: vlc not found. Try use another player with -p flag")


def show_streams(url):
    wasd = WasdLib(url)

    print("[wasd2play] Got a streams list...\n")

    streams_list = wasd.get_streams()
    for stream_name in streams_list:
        print(streams_list.index(stream_name), stream_name)


def runner():
    """ Entry point """

    my_parser = argparse.ArgumentParser(prog='wasd2play',
                                        usage='%(prog)s [options] url',
                                        description='Open any stream in your favorite player!',
                                        epilog='Have a good time!')

    my_parser.add_argument('url',
                           help='stream url')
    my_parser.add_argument('-p', '--player',
                           help='Point your player',
                           default='vlc',
                           dest='your_player')
    my_parser.add_argument('-l', '--last',
                           action='store_true',
                           dest="last_stream",
                           help='Open last stream')

    # Show and select streams
    my_parser.add_argument('-s', '--select',
                           action='store',
                           dest="selected",
                           type=int,
                           help='Select stream')
    my_parser.add_argument('-ls', '--list',
                           action='store_true',
                           dest="show_list_of_streams",
                           help='Show recent streams')

    args = my_parser.parse_args()

    welcome_message = "##\n## wasd2play\n##\n"
    print(welcome_message)

    if args.show_list_of_streams:
        show_streams(args.url)
        return 0

    open_player(args.url, args.your_player, args.selected, args.last_stream)
