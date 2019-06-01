Select Track.Name, Round(Sum(InvoiceLine.UnitPrice * Quantity), 2) from Track
Inner Join InvoiceLine On InvoiceLine.TrackId = Track.TrackId
Where Track.Name = 'The Woman King';