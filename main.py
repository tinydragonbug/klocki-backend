from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Zezwalamy na połączenia z naszego frontendu w React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "Serwer Klocków działa!"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Nowy klient połączony!")
    try:
        while True:
            # Oczekujemy na wiadomość od klienta
            data = await websocket.receive_text()
            print(f"Otrzymano wiadomość: {data}")
            # Odsyłamy echo w celach testowych
            await websocket.send_text(f"Serwer potwierdza: {data}")
    except WebSocketDisconnect:
        print("Klient rozłączony")