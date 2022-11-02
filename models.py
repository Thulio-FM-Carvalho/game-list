from pydantic import BaseModel


class GameForm(BaseModel):
    id: str = None
    name: str = None
    category: str = None
    console: str = None
