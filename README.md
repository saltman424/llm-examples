# LLM Experiments

This repository showcases practical implementations of various LLM techniques, from simple text generation to more complex agentic systems with self-execution capabilities and persistent memory. Each project is designed to demonstrate specific architectural patterns in LLM application development.

All projects are built in Python with the use of [LangGraph](https://www.langchain.com/langgraph) and a local [Ollama](https://ollama.com/) LLM. See the README in each project for 

## Setup

Unless stated otherwise in the project's README, the setup for all projects is:
1. Install Ollama from https://ollama.com
2. Run `ollama pull llama3.2`
3. Install Poetry from https://python-poetry.org/docs/#installing-with-pipx
4. Run `poetry install`

To execute the project, simply run `poetry run start`

## Projects

### 1. Choose Your Own Adventure
**Path:** `choose-your-own-adventure/`

An interactive storytelling experience powered by LLMs that generates dynamic narratives based on user choices.

**Key Features:**
- Dynamic story generation with context preservation
- Adaptive narrative paths based on user input
- State management for consistent story progression

**Techniques Demonstrated:**
- Simple multi-step agentic workflows

---

### 2. Data Visualizer
**Path:** `data-visualizer/`

An intelligent data analysis tool that automatically generates Python code to analyze datasets and produces comprehensive HTML reports.

**Key Features:**
- Automatic file format detection and parsing
- LLM-generated Python code for custom analysis
- Self-execution of generated code with safety measures
- HTML report generation with visualizations

**Techniques Demonstrated:**
- Code generation and validation
- Sandboxed code execution
- Error handling and retry logic
- Multi-step agentic workflows

---

### 3. Mental Health RAG
**Path:** `mental-health-rag/`

A Retrieval-Augmented Generation (RAG) system that answers mental health questions using a curated knowledge base of mental health resources.

**Key Features:**
- Vector database integration for semantic search
- PDF document parsing and chunking
- Context-aware response generation

**Techniques Demonstrated:**
- Document embedding and indexing
- Vector similarity search (done under-the-hood by [Chroma](https://docs.trychroma.com/docs/overview/architecture#the-query-executor))
- RAG

## Potential Future Projects
1. Note-Taking Assistant - Demonstrates long-term memory management
2. TBD - Demonstrates Agent-to-Agent protocol using [Strands Agents](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/multi-agent/agent-to-agent/)
3. TBD - Demonstrates MCP using the official [modelcontextprotocol SDK](https://github.com/modelcontextprotocol/python-sdk)

---

*For questions or collaboration opportunities, please reach out via [LinkedIn](https://www.linkedin.com/in/sander-altman/).*