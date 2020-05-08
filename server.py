#!/usr/bin/env python3


import os
import posixpath
from http.server import SimpleHTTPRequestHandler, test


class HtmlHTTPRequestHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = super().translate_path(path)
        trailing_slash = path.rstrip().endswith('/')
        base, ext = posixpath.splitext(path)
        # 解决路径不带html的转发
        if not trailing_slash and ext == "" and not os.path.exists(path):
            path += '.html'
        return path


if __name__ == '__main__':
    import argparse
    from functools import partial

    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('--directory', '-d', default=os.getcwd(),
                        help='Specify alternative directory '
                        '[default:current directory]')
    parser.add_argument('port', action='store',
                        default=8000, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8000]')
    args = parser.parse_args()
    handler_class = partial(HtmlHTTPRequestHandler,
                            directory=args.directory)
    test(HandlerClass=handler_class, port=args.port, bind=args.bind)