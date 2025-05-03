from typing import Annotated, Union
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from dataclasses import dataclass
from enum import Enum

from db.db_handler import DatabaseHandler

class Sentiment(Enum):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"
    NEUTRAL = "Neutral"


class DietitianState(TypedDict):
    """
    State object to be used in the agent
    """
    chat_id: Union[str, None] 
    crud: DatabaseHandler
    query: str
    sentiment: Sentiment
    summary: str
    messages: Annotated[list, add_messages]
    
    
@dataclass
class DietitianOutput:
    """
    object to be used in the agent 
    """
    summary: Union[str, None]
    sentiment: Union[Sentiment, None]
    answer: str
    
@dataclass
class DietitianDependency:
    """
    object to be used in the agent 
    """
    sentiment: Union[str, None]
    summary: Union[Sentiment, None]
    
