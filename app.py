# U5 学员骨架：最小可运行的接口服务
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "fde-demo"})


@app.get("/devices")
def devices():
    items = [
        {"id": "PB-001", "type": "喷浆机器人", "status": "running"},
        {"id": "PB-002", "type": "喷浆机器人", "status": "idle"},
    ]
    return jsonify({"items": items, "total": len(items)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
