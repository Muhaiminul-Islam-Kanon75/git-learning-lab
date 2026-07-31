from app.web import run_server
import webbrowser


def main():
    url = "http://127.0.0.1:8000"
    webbrowser.open(url)
    run_server()


if __name__ == "__main__":
    main()