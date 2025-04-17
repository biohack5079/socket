source venv/bin/activate
python3 server.py


ngrok config add-authtoken xxxx-xxx-xxx-xxx
ngrok http 8765

"wss://xxxx-xxx-xxx-xxx.ngrok-free.app"; // ← ngrok URL に更新

python -m http.server 8000

http://localhost:8000/index.html
