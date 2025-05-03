from langgraph.graph import END, START, StateGraph
from langchain_core.messages import  AIMessage, HumanMessage

from common.type import DietitianState
from graph.nodes import chat_node, init_node, updation_node


class GraphBuilder:
    compiled_graph = None
    def __init__(self):
        # Initialize the StateGraph with the State class
        self.graph_builder = StateGraph(DietitianState)

        # Add all the nodes
        self.graph_builder.add_node("init_node", init_node)
        self.graph_builder.add_node("updation_node", updation_node)
        self.graph_builder.add_node("chat_node", chat_node)

        # Add the edges
        self.graph_builder.set_entry_point("init_node")
        self.graph_builder.add_edge("init_node", "chat_node")
        self.graph_builder.add_edge("chat_node", "updation_node")
        self.graph_builder.add_edge("updation_node", END)
       
    def compile(self):
        """
        Compile the graph and return the compiled graph.
        """
        self.compiled_graph =  self.graph_builder.compile()

    def invoke_graph(self, query, chat_id=None):
        """
        Take a query and create initial parameters for the graph.
        """
        if not self.compiled_graph:
            raise ValueError("Graph has not been compiled. Please call `compile` before invoking.")

        # Example of creating initial parameters based on the query
        initial_state = {"messages": [HumanMessage(content=query)], "query": query, "chat_id": chat_id}

        # Invoke the compiled graph with the initial state
        return self.compiled_graph.invoke(initial_state)