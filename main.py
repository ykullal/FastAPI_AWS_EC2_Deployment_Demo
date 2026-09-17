from fastapi import FastAPI
from fastapi import HTTPException
from models import MediaMetaData
from models import UpdateMedia
from models import CreateMedia
from database import MEDIA
from typing import List, Optional

# FastAPI application instance
app = FastAPI()

@app.get("/songs", response_model=List[MediaMetaData])
async def songs(limit: Optional[int] = None) -> List[MediaMetaData]:
    """Get the list of songs with an optional limit on the number of songs returned.
    If limit is not specified, it defaults to first 5 songs details. 
    Here, limit is sent as a query parameter in the URL.
    Example: 
        /songs?limit=3

    Returns:
        List[MediaMetaData]: List of song objects containing details of songs.
    """
    return MEDIA[:limit] if limit is not None else MEDIA


# The media_id path variable for retrieving a specific song by its ID
@app.get("/songs/{media_id}", response_model=MediaMetaData)
async def get_song(media_id: int) -> MediaMetaData:
    """Get details of a specific song by its ID.

    Args:
        media_id (int): The ID of the song to retrieve.

    Returns:
        MediaMetaData: The song object containing details of the song.
    """
    for media in MEDIA:
        if media.id == media_id:
            return media
    raise HTTPException(status_code=404, detail=f"Media with id {media_id} not found")


# The media_id path variable for retrieving a specific song by its ID
# then updating the song details. New values are provided in the request body.
@app.put("/songs/{media_id}", response_model=MediaMetaData)
async def update_song(media_id: int, media_data: UpdateMedia) -> MediaMetaData:
    """Update details of a specific song by its ID.

    Args:
        media_id (int): The ID of the song to update.
        media_data (UpdateMedia): The updated data for the song.

    Returns:
        MediaMetaData: The song object containing details of the song.
    """
    for media in MEDIA:
        if media.id == media_id:
            if media_data.title is not None:
                media.title = media_data.title
            if media_data.language is not None:
                media.language = media_data.language
            if media_data.genre is not None:
                media.genre = media_data.genre
            return media
    raise HTTPException(status_code=404, detail=f"Media with id {media_id} not found")


@app.post("/songs", response_model=MediaMetaData)
async def create_song(media_data: CreateMedia) -> MediaMetaData:
    """Create a new song with the provided details.

    Args:
        media_data (CreateMedia): The data for the new song.

    Returns:
        MediaMetaData: The song object containing details of the song.
    """
    new_id = max(media.id for media in MEDIA) + 1 if MEDIA else 1
    new_media_data = MediaMetaData(id=new_id, 
                                   title=media_data.title,
                                   language=media_data.language,
                                   genre=media_data.genre) 
    
    MEDIA.append(new_media_data)
    return new_media_data

# The media_id path variable for retrieving a specific song by its ID
# then deleting the song with the specified ID.
@app.delete("/songs/{media_id}", response_model=MediaMetaData)
async def delete_song(media_id: int) -> MediaMetaData:
    """Delete a specific song by its ID.

    Args:
        media_id (int): The ID of the song to delete.

    Returns:
        MediaMetaData: The song object containing details of the deleted song.
    """
    for media in MEDIA:
        if media.id == media_id:
            MEDIA.remove(media)
            return media
    raise HTTPException(status_code=404, detail=f"Media with id {media_id} not found")
