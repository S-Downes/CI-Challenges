Select Track.Name as Track, MediaType.Name as MediaType, Genre.Name as Genre from Track 
Inner Join MediaType On Track.MediaTypeId = MediaType.MediaTypeId
Inner Join Genre On Track.GenreId = Genre.GenreId
Where MediaType.Name = 'Protected AAC audio file' And Genre.Name = 'Soundtrack';