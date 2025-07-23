const form = document.getElementById("chat-form")
form.addEventListener("submit", (e) => {
  e.preventDefault()
  const input = document.getElementById("chat-input")
  if (input.value && selectedUser) {
    ws.send(
      JSON.stringify({
        type: "send_message",
        user_id: selectedUser,
        message: input.value,
      })
    )
    appendMessage(input.value, false)
    input.value = ""
  }
})
