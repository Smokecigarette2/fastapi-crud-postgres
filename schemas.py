from pydantic import BaseModel, EmailStr

# User Schema (Pydantic Model)
class UserCreate(BaseModel):
    email: EmailStr
    name: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str

    class Config:
        from_attributes = True  # Allows SQLAlchemy models to be converted to Pydantic

class NoteCreate(BaseModel):
    title: str
    content: str

# Note Schema for Response
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int  # Include user ID for reference

    class Config:
        from_attributes = True