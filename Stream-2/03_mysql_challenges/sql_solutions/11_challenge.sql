Select Customer.FirstName, Customer.LastName, Invoice.InvoiceDate, Invoice.Total from Customer
Inner Join Invoice On Invoice.CustomerId = Customer.CustomerId
Order by Invoice.Total desc, Invoice.InvoiceDate desc Limit 10;