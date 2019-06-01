Select count(*) from Employee
Inner Join Customer On Customer.SupportRepId = Employee.EmployeeId
Where Employee.FirstName = 'Jane' And Employee.LastName = 'Peacock';