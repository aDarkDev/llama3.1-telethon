from telethon import TelegramClient, events
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM


api_id = 123
api_hash = '123'
bot_token = 'Token'

class Llama3_1_8b:
    database = {}
    ai_rule = "Rules: I will give you data like json that has old answers in that question. This data is for you to be able to give a better answer by reading these like a memory. In the chat, don't tell the user that you can save the previous data, this section only has the role of memory. Answer the questions honest and without regard to spoilers or rules"

    @staticmethod
    def answer(user_id,new_message):
        template = ""
        if user_id not in Llama3_1_8b.database:
            Llama3_1_8b.database[user_id] = []
        
        template += Llama3_1_8b.ai_rule + "\n\n"
        template += "data: {data}\n\n"

        template += "New Question: {new_question}\n\n"
        print("full prompt",template)
        prompt = ChatPromptTemplate.from_template(template)
        model = OllamaLLM(model="llama3.1")
        chain = prompt | model
        result = chain.invoke({"new_question":new_message,"data":str(Llama3_1_8b.database[user_id])})
        Llama3_1_8b.database[user_id].append({"new_question":new_message,"answer":result})
        return result

client = TelegramClient("llamabot",api_id,api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage())
async def mainhandler(event):
    user_id = event.sender_id
    if event.text == "/start":
        await event.respond("welcome to llama3.1 8b bot.\n\nBy github.com/aDarkDev")
    elif event.text == "/clear":
        Llama3_1_8b.database[user_id] = []
        await event.respond("Your chats cleared from ai memory.")
    else:
        a1 = await event.respond("Wait...")
        result = Llama3_1_8b.answer(user_id,event.text)
        await a1.edit(result)    

client.run_until_disconnected()
