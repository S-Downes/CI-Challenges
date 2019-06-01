Select Album.Title as Album, Track.Name as Track, Playlist.Name as Playlist from Album
Inner Join Track On Track.AlbumId = Album.AlbumId
Inner Join PlaylistTrack On PlaylistTrack.TrackId = Track.TrackId
Inner Join Playlist On Playlist.PlaylistId = PlaylistTrack.PlaylistId
Where Playlist.Name = 'On-The-Go 1';