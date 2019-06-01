-- Make sure Album is inserted first before Tracks are added

-- Insert Into Album(Title, ArtistId)
-- Values("Boy", 150);

Insert Into Track(Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice) 
Values("Twilight", 348, 2, 1, "U2", 4220, 1235, 0.99),
Values("An Cat Dubh", 348, 2, 1, "U2", 4460, 1236, 0.99);