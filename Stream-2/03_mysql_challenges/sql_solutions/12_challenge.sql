Select count(*) from Employee
Inner Join Customer On Customer.SupportRepId = Employee.EmployeeId
Where Employee.EmployeeId = 4;