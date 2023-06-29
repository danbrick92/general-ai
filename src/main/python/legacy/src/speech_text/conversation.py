import chat as c
import text_to_speech

class Conversation:

    def __init__(self):
        pass

    def begin_conversation(self):
        print("Starting conversation. Hit x to exit. Type r to repeat.")
        chat = c.Chat('gpt-3.5-turbo')
        spk = text_to_speech.Speak()
        
        while True:
            question = input("Type your question here. Hit x to exit. Type r to repeat: ")
            if question.lower().replace(' ', '') == "x":
                print("Exiting...")
                break
            elif question.lower().replace(' ', '') == "r":
                spk.speak(reply)
                continue
            
            reply = chat.continue_conversation(question)
            print(f"Reply: {reply}")
            spk.speak(reply)

conv = Conversation()
conv.begin_conversation()