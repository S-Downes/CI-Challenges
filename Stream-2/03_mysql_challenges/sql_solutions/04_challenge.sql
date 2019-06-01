Select Track.Name as Track, Genre.Name as Genre from Track Inner Join Genre On Track.GenreId = Genre.GenreId
Where Genre.GenreId = 2;