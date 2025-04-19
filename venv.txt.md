source venv/bin/activate
(sudo lsof -i :8765)
python3 server.py


ngrok config add-authtoken xxxx-xxx-xxx-xxx
ngrok http 8765

"wss://xxxx-xxx-xxx-xxx.ngrok-free.app"; // ← ngrok URL に更新



source venv/bin/activate
python3 server.py
python -m http.server 8000
ngrok http 8000
http://localhost:8000/index.html



http://192.168.1.10:8000/index.html

ngrok.yml
tunnels:
  http:
    proto: http
    addr: 8000
  websocket:
    proto: http
    addr: 8765
ngrok start --all

