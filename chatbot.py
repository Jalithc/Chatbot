import tkinter as tk
from nltk.chat.util import Chat, reflections

class ChatInterface(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.chatbot = Chat(patterns, reflections)

        self.title("Chatbot")
        self.geometry("400x500")

        self.chat_history = tk.Text(self)
        self.chat_history.config(state=tk.DISABLED)
        self.chat_history.pack(expand=True, fill=tk.BOTH)

        self.input_field = tk.Entry(self)
        self.input_field.pack(expand=True, fill=tk.X)
        self.input_field.bind("<Return>", self.on_enter_pressed)

    def on_enter_pressed(self, event):
        user_input = self.input_field.get()
        self.input_field.delete(0, tk.END)

        response = self.chatbot.respond(user_input)
        self.add_to_chat_history(user_input, "You")
        self.add_to_chat_history(response, "Chatbot")

    def add_to_chat_history(self, message, sender):
        self.chat_history.config(state=tk.NORMAL)
        self.chat_history.insert(tk.END, f"{sender}: {message}\n")
        self.chat_history.config(state=tk.DISABLED)

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you', ["I'm doing well, thank you!", "I'm fine, thanks!"]),
    (r'quit', ['Bye, take care!', 'Goodbye!']),
]

if __name__ == "__main__":
    app = ChatInterface()
    app.mainloop()
