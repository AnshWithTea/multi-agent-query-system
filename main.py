# main.py

import uvicorn
import shutil
import os
from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

# Import all agent functions
from agents.web_agent import search_web
from agents.arxiv_agent import search_arxiv
from agents.pdf_rag_agent import process_pdf_and_store, query_rag_store
from agents.controller_agent import route_query, synthesize_answer

load_dotenv()
app = FastAPI()

# --- Serve Static Files and Templates ---
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# --- Simple In-Memory State ---
app.state.last_collection_name = None

# --- UI Endpoint ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# --- API Endpoints ---

@app.post("/api/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    temp_pdf_path = f"temp_{file.filename}"
    with open(temp_pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    collection_name = os.path.splitext(file.filename)[0].replace(" ", "_")
    process_pdf_and_store(temp_pdf_path, collection_name)
    os.remove(temp_pdf_path)

    app.state.last_collection_name = collection_name
    print(f"Updated app state: last_collection_name = {app.state.last_collection_name}")

    return {"filename": file.filename, "collection_name": collection_name, "status": "processed"}

@app.post("/api/ask")
async def ask_question(query: str = Form(...)):
    print(f"\n--- New Query Received: '{query}' ---")
    
    collection_name = app.state.last_collection_name
    collection_exists = collection_name is not None
    
    agent_choice, rationale = route_query(query, collection_exists)
    
    context = ""
    if agent_choice == "WEB_SEARCH":
        context = search_web(query)
    elif agent_choice == "ARXIV":
        context = search_arxiv(query)
    elif agent_choice == "PDF_RAG":
        if collection_exists:
            context = query_rag_store(query, collection_name)
        else:
            context = "Error: Tried to query PDF, but no document has been uploaded."
            rationale += " (Error: No PDF uploaded)"
            
    final_answer = synthesize_answer(query, context)
    
    return {
        "query": query,
        "answer": final_answer,
        "agents_used": [agent_choice],
        "rationale": rationale,
    }

@app.get("/api/logs")
async def get_logs():
    # As per spec, this doesn't need to be fully implemented
    return {"logs": "Logging to file is handled via server-side print statements for this demo."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)