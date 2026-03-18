LangGraph, LangChain & Groq Whisper AI Projects

Project Overview This repository contains practical implementations of
Generative AI applications using LangChain, LangGraph, Groq APIs, and
Large Language Models (LLMs). The projects demonstrate how to build
conversational AI agents, stateful workflows, and speech-to-text
applications.

Technologies Used - Python - LangChain - LangGraph - Groq API - Whisper
Speech Model - Jupyter Notebook - VS Code - IPython Display - TypedDict
(Python typing)

Main Topics Covered - LangChain Framework - LangGraph Stateful
Workflows - Multi-node AI pipelines - Chatbot using Groq LLM -
Speech-to-Text using Whisper - Graph-based AI agents - LLM integration
with Python

About LangChain LangChain is a framework designed for building
applications powered by Large Language Models (LLMs). It allows
developers to connect language models with external data sources, APIs,
and tools to create intelligent applications.

Common LangChain Components - Models (LLMs) - Prompts - Chains -
Agents - Memory - Indexes

About LangGraph LangGraph is a Python framework built on top of
LangChain for building stateful, multi-step workflows for AI agents.

Key Concepts in LangGraph

StateGraph Defines the structure of the workflow.

State Stores shared memory or context between nodes.

Node A function that performs a task such as calling an LLM.

Edge Defines the flow of execution between nodes.

START Starting point of the graph.

END Marks the end of graph execution.

Project 1 – Simple LangGraph Workflow This project demonstrates how to
build a simple workflow using LangGraph.

Steps: 1. Define the State using TypedDict 2. Create nodes (functions)
3. Define graph edges 4. Compile the graph 5. Execute the graph

Example workflow:

Start Node -> Process Node -> End Node

Example Code:

pip install langgraph

from langgraph.graph import StateGraph, END from typing import TypedDict

class MyState(TypedDict): message: str

Project 2 – LangGraph Chatbot with Groq LLM

This project builds a chatbot using:

-   LangGraph workflow
-   Groq LLM (Gemma2-9b-It)
-   LangChain integration

The chatbot processes user messages through a graph node that calls the
language model.

Libraries Used

pip install langchain langchain_groq langchain_community

Example Node:

def chatbot(state): return {“messages”: llm.invoke(state[‘messages’])}

Project 3 – Multi Node LangGraph Pipeline

This workflow demonstrates multiple nodes in a graph.

Pipeline Flow:

START ↓ Preprocess Message ↓ Sentiment Analysis ↓ Chatbot Response ↓
Logger ↓ END

Each node performs a specific task before passing the state to the next
node.

Example Tasks: - Clean user input - Detect sentiment - Generate AI
response - Log outputs

Project 4 – Speech to Text using Groq Whisper

This project demonstrates speech recognition using Groq’s Whisper model.

Model Used: whisper-large-v3

Example Code:

from groq import Groq

client = Groq(api_key=“YOUR_API_KEY”)

with open(“audio.m4a”, “rb”) as file: transcription =
client.audio.transcriptions.create( file=(file.name, file.read()),
model=“whisper-large-v3” )

print(transcription.text)

Applications

-   AI Chatbots
-   Conversational Agents
-   Multi-agent AI systems
-   Voice assistants
-   Speech-to-text applications
-   Intelligent workflow automation

LangChain Ecosystem

LangChain – Framework for LLM applications LangGraph – Workflow engine
for AI agents LangFlow – Visual builder for AI apps LangSmith –
Monitoring and debugging platform

Project Goals

-   Understand LangChain ecosystem
-   Build stateful AI workflows
-   Create LLM powered chatbots
-   Integrate Groq APIs with Python
-   Implement speech recognition using AI

Useful Resources

LangChain Documentation https://python.langchain.com/docs

LangGraph Documentation https://langchain-ai.github.io/langgraph

Groq Documentation https://console.groq.com/docs
