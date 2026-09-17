from pydantic import BaseModel
from pydantic import Field
from typing import Optional


class Media(BaseModel):
    #
    language: str = Field(..., min_length=4, max_length=20, description="Language of the song")
    title: str = Field(..., min_length=6, max_length=30, description="Title of the song")
    genre: str = Field(..., min_length=3, max_length=20, description="Genre of the song")

class CreateMedia(Media):
    # When creating a media item, all fields are required. 
    # The fields are inherited from the Media class.
    # language: str = Field(..., min_length=4, max_length=20, description="Language of the song")
    # title: str = Field(..., min_length=6, max_length=30, description="Title of the song")
    # genre: str = Field(..., min_length=3, max_length=20, description="Genre of the song")
    pass

class UpdateMedia(BaseModel):
    # When updating a media item, all fields are optional
    language: Optional[str] = Field(None, min_length=4, max_length=20, description="Language of the song")
    title: Optional[str] = Field(None, min_length=6, max_length=30, description="Title of the song")
    genre: Optional[str] = Field(None, min_length=3, max_length=20, description="Genre of the song")

class MediaMetaData(Media):
    # Metadata for the media item, including its unique ID.
    # Rest of the fields are inherited from the Media class.
    id: int = Field(..., description="ID of the media item")