from fastapi import APIRouter, Query
from graph.graph import GraphBuilder

# Create a router instance
router = APIRouter()

mongo_graph = GraphBuilder()
mongo_graph.compile()

# Define the /aidiate route
@router.get("/")
def diet_chat(
    query: str = Query(..., description="What is your aidiate query?"),
    chat_id: str = Query(None, description="Optional chat ID for the conversation")
):
    result = mongo_graph.invoke_graph(query, chat_id=chat_id)
    return {"message": result["messages"][-1].content, "chat_id": str(result["chat_id"])}