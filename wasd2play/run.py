from wasd2play.wasd_lib import WasdLib
import subprocess
import argparse


def open_player(url, player, selected_stream=0, force_open_last_stream=False, download_stream=False):
    """ Open player with stream """
    try:
        wasd = WasdLib(url)

        print("[wasd2play] Got a stream playlist...")
        stream_info = wasd.get_stream(selected_stream)

        # Set to current url
        stream_url = stream_info['stream_m3u8']

        # If stream offline, open last
        if stream_info['stream_status'] == "STOPPED" or force_open_last_stream:
            print("[wasd2play] Open last archived stream...")
            stream_url = stream_info['archive_stream_m3u8']
        else:
            print("[wasd2play] Open current stream...")

        print(f"[wasd2play] {wasd.stream_name} in your {player} player!")

        tags = ", ".join(stream_info['stream_tags'])
        print(f"[wasd2play] Tags: {tags}")
    except KeyError:
        print("[wasd2play] Wrong url/streamer nickname. Stopping.")
        return 0
    except OSError:
        print("[wasd2play] OSError. Stopping.")
        return 0

    try:
        if download_stream:
            subprocess.run(f"ffmpeg -i {stream_url} -c copy -bsf:a aac_adtstoasc \"{wasd.stream_name}\".mp4")
        else:
            subprocess.run([player, stream_url], stdout=subprocess.PIPE, check=True)
    except FileNotFoundError:
        print("[wasd2play] Error: player or ffmpeg not found. Try use another player with -p flag. Stopping.")
    except KeyboardInterrupt:
        return 0


def show_streams(url, page=1):
    wasd = WasdLib(url)

    print("[wasd2play] Got a streams list...\n")

    streams_list = wasd.get_streams(page)
    count = (page * 10) - 10
    for stream_name in streams_list:
        count += 1
        print(count, stream_name)
    print(f"Page {page}/3")


def runner():
    """ Entry point """

    my_parser = argparse.ArgumentParser(prog='wasd2play',
                                        usage='%(prog)s [options] url',
                                        description='Open any stream in your favorite player!',
                                        epilog='Have a good time!')

    my_parser.add_argument('url',
                           help='stream url')

    # Optional args
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
                           action='store',
                           dest="page",
                           nargs='?',
                           const=1,
                           type=int,
                           help='Show recent streams page by page')

    # Download with ffmpeg
    my_parser.add_argument('-d', '--download',
                           action='store_true',
                           dest='download_stream',
                           help='Download stream with ffmpeg')

    args = my_parser.parse_args()

    welcome_message = "##\n## wasd2play\n##\n"
    print(welcome_message)

    if (args.page is not None) and (args.page >= 1):
        show_streams(args.url, args.page)
        return 0

    open_player(args.url, args.your_player, args.selected, args.last_stream, args.download_stream)
