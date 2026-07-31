import json
import mimetypes
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from app.quiz import QUESTIONS
from app.simulator import get_git_command

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"


def get_questions_payload():
    return {
        "questions": [
            {"question": item["question"], "answer": item["answer"]}
            for item in QUESTIONS
        ]
    }


def evaluate_quiz(answers):
    results = []
    score = 0

    for index, item in enumerate(QUESTIONS):
        user_answer = answers[index] if index < len(answers) else ""
        is_correct = False

        if isinstance(user_answer, bool):
            is_correct = user_answer
        else:
            is_correct = str(user_answer).strip() == item["answer"]

        if is_correct:
            score += 1

        results.append(
            {
                "question": item["question"],
                "user_answer": user_answer,
                "correct": is_correct,
                "expected": item["answer"],
            }
        )

    return {"score": score, "total": len(QUESTIONS), "results": results}


def simulate_command_payload(command: str):
    return {"command": command, "result": get_git_command(command)}


class GitLearningRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        route = parsed_path.path

        if route == "/api/questions":
            self._send_json(get_questions_payload())
            return

        if route == "/api/health":
            self._send_json({"status": "ok"})
            return

        if route == "/":
            file_path = STATIC_DIR / "index.html"
        else:
            file_path = STATIC_DIR / route.lstrip("/")

        if file_path.exists() and file_path.is_file():
            self._send_file(file_path)
            return

        self._send_file(STATIC_DIR / "index.html")

    def do_POST(self):
        parsed_path = urlparse(self.path)
        route = parsed_path.path

        content_length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(content_length).decode("utf-8") if content_length else "{}"

        try:
            payload = json.loads(body) if body else {}
        except json.JSONDecodeError:
            payload = {}

        if route == "/api/quiz":
            answers = payload.get("answers", [])
            self._send_json(evaluate_quiz(answers))
            return

        if route == "/api/simulate":
            command = payload.get("command", "")
            self._send_json(simulate_command_payload(command))
            return

        self._send_json({"error": "Not found"}, status_code=404)

    def log_message(self, format, *args):
        return

    def _send_json(self, data, status_code=200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, file_path: Path):
        content_type, _ = mimetypes.guess_type(str(file_path))
        if content_type is None:
            content_type = "application/octet-stream"

        body = file_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def run_server(host: str = "127.0.0.1", port: int = 8000):
    server = ThreadingHTTPServer((host, port), GitLearningRequestHandler)
    print(f"Starting frontend at http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Frontend stopped.")
    finally:
        server.server_close()
