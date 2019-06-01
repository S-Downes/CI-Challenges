Select Artist.Name, Count(Track.Name) from Artist
Inner Join Album On Album.ArtistId = Artist.ArtistId
Inner Join Track On Track.AlbumId = Album.AlbumId
Group by Artist.Name
Order by Count(Track.Name) desc Limit 5;