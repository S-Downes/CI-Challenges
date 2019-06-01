Select MediaType.Name, count(Track.Name) from MediaType
Inner Join Track On MediaType.MediaTypeId = Track.MediaTypeId
Group by MediaType.Name
Order by count(Track.Name) desc;