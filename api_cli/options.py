import argparse

from user import list_user, create_user, update_user, get_user, delete_user


def args_parser():
    global_parser = argparse.ArgumentParser(prog="api-cli")
    global_parser.add_argument(
        '-H',
        '--host',
        type=str,
        default='127.0.0.1',
        help='api server ip address'
    )
    global_parser.add_argument(
        '-p',
        '--port',
        type=str,
        default='5000',
        help='api server port'
    )

    global_sub_parsers = global_parser.add_subparsers(
        title="user subcommands", help="sub operations"
    )
    add_user_parser(global_sub_parsers)

    args = global_parser.parse_args()
    return args


def add_user_parser(global_sub_parsers):
    user_sub_parsers = global_sub_parsers. \
        add_parser("user", help="user operations").add_subparsers()

    # create user subcommand
    add_create_parser(user_sub_parsers)

    # list user subcommand
    add_list_parser(user_sub_parsers)

    # get user subcommand
    add_get_parser(user_sub_parsers)

    # update user subcommand
    add_update_parser(user_sub_parsers)

    # delete user subcommand
    add_delete_parser(user_sub_parsers)


def add_create_parser(user_sub_parsers):
    create_user_parser = user_sub_parsers.add_parser("create", help="create user")
    create_user_parser.add_argument(
        '-f',
        '--user_file',
        type=str,
        required=True,
        help='user definition yaml file'
    )
    create_user_parser.set_defaults(func=create_user)


def add_list_parser(user_sub_parsers):
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


def add_get_parser(user_sub_parsers):
    get_user_parser = user_sub_parsers.add_parser("get", help="get user")
    get_user_parser.add_argument(
        '-U',
        '--user_id',
        type=int,
        required=True,
        help='user ID'
    )
    get_user_parser.set_defaults(func=get_user)


def add_update_parser(user_sub_parsers):
    update_user_parser = user_sub_parsers.add_parser("update", help="update user")
    update_user_parser.add_argument(
        '-f',
        '--user_file',
        type=str,
        required=True,
        help='user definition yaml file'
    )

    update_user_parser.add_argument(
        '-U',
        '--user_id',
        type=int,
        required=True,
        help='user ID'
    )
    update_user_parser.set_defaults(func=update_user)


def add_delete_parser(user_sub_parsers):
    delete_user_parser = user_sub_parsers.add_parser("delete", help="delete user")
    delete_user_parser.add_argument(
        '-U',
        '--user_id',
        type=int,
        required=True,
        help='user ID'
    )
    delete_user_parser.set_defaults(func=delete_user)
