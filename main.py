from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import Note

# Create the tables in the database (if they don't exist yet)
#Base.metadata.create_all(bind=engine)

app = FastAPI()

# What the user sends us
class NoteIn(BaseModel):
    title: str
    content: str
    category: str | None = None

class NoteOut(BaseModel):
    id: int
    title: str
    content: str
    category: str | None

    model_config = {"from_attributes": True}

# See all notes
@app.get("/notes", response_model=list[NoteOut])
def list_notes(db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    return notes

# Create a new note
@app.post("/notes", response_model=NoteOut)
def create_note(note: NoteIn, db: Session = Depends(get_db)):
    new_note = Note(title=note.title, content=note.content, category=note.category)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

# Get a specific note by ID
@app.get("/notes/{note_id}", response_model=NoteOut)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


# Update a note
@app.put("/notes/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note: NoteIn, db: Session = Depends(get_db)):
    existing_note = db.query(Note).filter(Note.id == note_id).first()
    if existing_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    existing_note.title = note.title
    existing_note.content = note.content
    existing_note.category = note.category
    db.commit()
    db.refresh(existing_note)
    return existing_note


# Delete a note
@app.delete("/notes/delete/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    # note = db.get(Note,note_id)
    note = db.query(Note).filter(Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}