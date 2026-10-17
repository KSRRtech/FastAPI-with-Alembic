from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app= FastAPI()

class NoteIn(BaseModel):
    title: str
    content: str


notes=[]
next_id=1

@app.get("/notes")
def list_notes():
    return notes

@app.post("/notes")
def create_note(note: NoteIn):
    global next_id
    note = {"id": next_id, "title": note.title, "content": note.content}
    notes.append(note)
    next_id += 1
    return note

@app.get("/notes/{note_id}")
def get_note(note_id: int):
    for note in notes:
        if note["id"] == note_id:
            return note
    raise HTTPException(status_code=404, detail="Note not found")


@app.put("/notes/{note_id}")
def update_note(note_id: int, note: NoteIn):
    for existing_note in notes:
        if existing_note["id"] == note_id:
            existing_note["title"] = note.title
            existing_note["content"] = note.content
            return existing_note
    raise HTTPException(status_code=404, detail="Note not found")


@app.delete("/notes/delete/{note_id}")
def delete_note(note_id:int):
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            return {"message": "Note deleted successfully"}
    raise HTTPException(status_code=404, detail="Note not found")

