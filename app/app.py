from llm.engine import load_llm
from llm.chat import ChatSystem

def main():
    llm = load_llm()               # load your Llama model
    chat_system = ChatSystem(llm)  # wrap it in ChatSystem
    chat_system.chat_display()     # call method on the ChatSystem instance

if __name__ == "__main__":
    main()
