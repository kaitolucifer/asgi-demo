function WebSocketTest() {
    const ws = new WebSocket("ws://127.0.0.1:5000/ws");
    ws.onopen = function() {
        const send = "hello from ws client"
        ws.send(send);
        console.log(`send "${send}"`);
    }
    ws.onmessage = function (event) {
        const recv = event.data
        console.log(`receive "${recv}"`);
    }
    ws.onclose = function() {
        console.log("websocket connection closed")
    }
}