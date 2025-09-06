async function sendMessage() {
  const input = document.getElementById("userInput");
  const lang = document.getElementById("langSelect").value;
  const message = input.value.trim();
  if (!message) return;

  const chatbox = document.getElementById("chatbox");
  appendMessage("You", message, "user-msg");

  // Send to backend
  const res = await fetch("/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message, lang})
  });

  const data = await res.json();
  appendMessage("Bot", data.reply, "bot-msg");

  input.value = "";
  chatbox.scrollTop = chatbox.scrollHeight;
}

function appendMessage(sender, text, className) {
  const chatbox = document.getElementById("chatbox");
  const msg = document.createElement("div");
  msg.className = `message ${className}`;
  msg.innerHTML = `<b>${sender}:</b> ${text}`;
  chatbox.appendChild(msg);
}
