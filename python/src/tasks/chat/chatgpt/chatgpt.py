from tasks.chat.chat import Chat
import os
import openai
import logging
openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatGPT(Chat):

    def __init__(self, actuators: list, sensors: list):
        super().__init__(actuators, sensors)
        self.model = "gpt-3.5-turbo"
        self.messages = []

    def chat(self):
        self.speaker.speak("How may I assist you today?")
        while True:
            logging.info("Awaiting user's key press...")
            self.await_key_press()

            # Get user question / statement
            logging.info("Getting user's input...")
            query = self.listener.listen()

            logging.info("Checking special conditions on user entry...")
            if self.check_exit_condition(query):
                self.speaker.speak("Exiting conversation...")
                break
            elif self.check_skip_condition(query):
                continue
            elif self.check_reset_condition(query):
                self.reset_messages()
                self.speaker.speak("Resetting conversation...")
                continue

            # Say that it is thinking
            logging.info("Letting user know that it's thinking...")
            self.speaker.speak("Hmmm... thinking...")

            # Get ChatGPT reply
            logging.info("Waiting for ChatGPT reply...")
            reply = self.chatgpt_reply(query)

            # Speak
            logging.info("Speaking reply...")
            self.speaker.speak(reply)

    @staticmethod
    def await_key_press():
        response = input("\nPress the Enter key to ask another question: ")

    @staticmethod
    def check_exit_condition(query: str) -> bool:
        qlower = query.lower()
        if qlower == 'x':
            return True
        elif 'exit' in qlower:
            return True
        elif 'stop' == qlower:
            return True
        return False

    @staticmethod
    def check_skip_condition(query: str) -> bool:
        return query == ""

    @staticmethod
    def check_reset_condition(query: str) -> bool:
        return query == "reset"

    def chatgpt_reply(self, query: str) -> str:
        self.messages.append({"role": "user", "content": query})
        return self.__chat_completion()

    def reset_messages(self):
        self.messages = []

    def __chat_completion(self):
        """
        Makes API call
        """
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        reply = completion['choices'][0]['message']
        self.messages.append(reply)
        return reply['content']
