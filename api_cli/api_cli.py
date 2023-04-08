from options import args_parser


def main():
    args = args_parser()
    res = args.func(args)
    print(res)


if __name__ == '__main__':
    main()
