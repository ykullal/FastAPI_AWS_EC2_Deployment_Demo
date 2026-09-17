from models import MediaMetaData


# The list of media items stored as MediaMetaData objects
# Instead of storing them as dictionaries, we store them as MediaMetaData objects. 
# For simplicity, we are not using the actual database and are storing the media items in memory.
MEDIA = [
    MediaMetaData(id=1, language="Kannada", title="Naavaduava Nudiye kannada nudi", genre="movie"),
    MediaMetaData(id=2, language="Hindi", title="Kabhi Kabhi Mere Dil Me", genre="movie"),
    MediaMetaData(id=3, language="English", title="Dangerous", genre="Pop"),
    MediaMetaData(id=4, language="English", title="Let's break-it", genre="Pop"),
    MediaMetaData(id=5, language="Hindi", title="Yaad Aa Rahahe Tera Pyar", genre="movie"),
    MediaMetaData(id=6, language="Hindi", title="Dil Ke tukde", genre="movie"),
    MediaMetaData(id=7, language="Hindi", title="Dil Dhadakne Do", genre="movie"),
    MediaMetaData(id=8, language="Hindi", title="Tera Yaar Hoon Main", genre="movie"),
    MediaMetaData(id=9, language="Kannada", title="Krishan nee begane baaro", genre="devotional"),
    MediaMetaData(id=10, language="Kannada", title="Bhagyada Balegara", genre="folk"),
    MediaMetaData(id=11, language="English", title="Shape of You", genre="Pop"),
    MediaMetaData(id=12, language="Hindi", title="Tum Hi Ho", genre="movie"),
    MediaMetaData(id=13, language="Kannada", title="Anisutide", genre="movie"),
    MediaMetaData(id=14, language="English", title="Blinding Lights", genre="Pop"),
    MediaMetaData(id=15, language="Hindi", title="Channa Mereya", genre="movie"),
    MediaMetaData(id=16, language="Tamil", title="Chinna Chinna Aasai", genre="movie"),
    MediaMetaData(id=17, language="Telugu", title="Bangaru Kodipetta", genre="movie"),
    MediaMetaData(id=18, language="Malayalam", title="Entammede Jimikki Kammal", genre="movie"),
    MediaMetaData(id=19, language="Punjabi", title="Lamberghini", genre="Pop"),
    MediaMetaData(id=20, language="Bengali", title="Tomake Chai", genre="movie"),
]