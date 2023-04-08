import argparse

from user import list_user, create_user


def args_parser():
    global_parser = argparse.ArgumentParser(prog="api-cli")

    global_parser.add_argument(
        '--host',
        type=str,
        default='127.0.0.1',
        help='api server ip address'
    )
    global_parser.add_argument(
        '--port',
        type=str,
        default='5000',
        help='api server port'
    )

    global_sub_parsers = global_parser.add_subparsers(
        title="user subcommands", help="sub operations"
    )
    user_sub_parsers = global_sub_parsers. \
        add_parser("user", help="user operations").add_subparsers()

    # list user subcommand
    list_user_parser = user_sub_parsers.add_parser("list", help="list users")
    list_user_parser.add_argument(
        '-fn',
        '--first_name',
        type=str,
        help="first_name of user"
    )
    list_user_parser.add_argument(
        '-ln',
        '--last_name',
        type=str,
        help="last_name of user"
    )
    list_user_parser.add_argument(
        '-s',
        '--start',
        type=int,
        default=0,
        help="start of list"
    )
    list_user_parser.add_argument(
        '-o',
        '--offset',
        type=int,
        default=10,
        help="total items of list"
    )
    list_user_parser.set_defaults(func=list_user)

    # create user subcommand
    create_user_parser = user_sub_parsers.add_parser("create", help="create user")
    create_user_parser.add_argument(
        '-f',
        '--user_file',
        type=str,
        required=True,
        help='user definition yaml file'
    )
    create_user_parser.set_defaults(func=create_user)

    args = global_parser.parse_args()
    return args
