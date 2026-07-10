
    const ws = new WebSocket("ws://localhost:8000/ws");
    ws.onopen = () => {
        console.log("Connected to WebSocket server");
    };

    const sendButton = document.getElementById("sendButton");
    sendButton.addEventListener("click", () => {
        const messageInput = document.getElementById("messageInput");
        const message = messageInput.value;
        ws.send(message);
        messageInput.value = "";
    });

    ws.onmessage = (event) => {
        const message = event.data;
        console.log("Received message:", message);
        const messagediv = document.getElementById("messages");
        messagediv.innerHTML += "<p>" + message + "</p>";
    };
