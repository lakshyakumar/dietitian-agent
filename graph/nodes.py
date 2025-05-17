
from langchain_core.messages import  AIMessage, HumanMessage

from graph.agents import query_selector_agent
from common.type import DietitianState, Sentiment, DietitianDependency
from db.db_handler import DatabaseHandler


def init_node(state: DietitianState):

    print("Initializing node...")
    crud = DatabaseHandler(db_name="chat_database")
    chat_id = None
    summary = None
    sentiment = Sentiment.NEUTRAL
    if state["chat_id"] is not None: 
        print(f"Chat ID: {state["chat_id"]} already exists")
        chat_id = state["chat_id"]
        chat = crud.get_chat_by_id(chat_id)
        sentiment = chat.sentiment
        summary = chat.summary
    else:
        chat_id = crud.create_chat()
        print(f"Chat ID: {chat_id} created")
        state["chat_id"] = chat_id
        state["summary"] = ""
        state["sentiment"] = Sentiment.NEUTRAL
    
    

    return { "crud": crud , "chat_id": chat_id, "summary": summary , "sentiment": sentiment }

def chat_node(state: DietitianState):
    print("Chat node...")
    result = query_selector_agent.run_sync(state["query"], deps=DietitianDependency( sentiment=state["sentiment"], summary=state["summary"]))
    # print("summary generated: ", result.output.summary)
    return { "messages": [AIMessage(content=result.output.answer)], "summary": result.output.summary, "sentiment": result.output.sentiment }

def updation_node(state: DietitianState):
    
    print("Updating node...")
    crud = state["crud"]
    chat_id = state["chat_id"]
    summary = state["summary"]
    sentiment = state["sentiment"]
    
    if chat_id is not None:
        crud.update_chat(chat_id, summary=summary, sentiment=sentiment.value)
        print(f"Chat ID: {chat_id} updated")