#import os
#import webbrowser
#
#from app.web import run_server
#
#
#def main():
#    host = os.getenv("HOST", "127.0.0.1")
#    port = int(os.getenv("PORT", "8000"))
#
#    if os.getenv("OPEN_BROWSER", "1") == "1":
#        webbrowser.open(f"http://{host}:{port}")
#
#    run_server(host=host, port=port)
#
#
#if __name__ == "__main__":
#    main()

from app.web import run_server


HOST = "0.0.0.0"
PORT = 8000


def main():
    run_server(host=HOST, port=PORT)


if __name__ == "__main__":
    main()
