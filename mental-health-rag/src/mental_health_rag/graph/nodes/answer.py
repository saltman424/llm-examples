import multiprocessing
from ...db import collection
from ...llm import llm
from ...state import State
from .node import Node

RAG_N_RESULTS = 2

class Answer(Node):
  def __call__(self, state: State) -> State:
    """Uses RAG to help answer the queries."""
    original_query = state["original_query"]
    expanded_queries = state["expanded_queries"]
    queries = [original_query] + expanded_queries
    print(f"Coming up with {len(queries)} possible answers...")
    global num_answered
    with multiprocessing.Pool(initializer=worker_init, initargs=(multiprocessing.Value('i', 0),)) as pool:
      state["answers"] = pool.map(answer, queries)
    return state

def worker_init(_num_answered):
    global num_answered
    num_answered = _num_answered

def answer(query: str) -> str:
  rag_result = collection.query(query_texts=[query], n_results=RAG_N_RESULTS)
  answer_sep = ("\n---\n")
  prompt = f"""You are a mental health professional answering everyday people's questions about mental health.

You remember this from the literature:
{answer_sep.join(rag_result["documents"][0]).strip()}

You have received this question:
{query}

Provide a thoughtful, compassionate, accurate, and precise response. Remember your professional duties. Be helpful, but be very careful not to mislead anyone with your response.

You know nothing about this person other than the question they have provided."""
  response = llm.invoke(prompt).content
  global num_answered
  with num_answered.get_lock():
    num_answered.value += 1
    print(f"Came up with {num_answered.value} possible answer(s)")
  return response