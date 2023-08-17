years_of_exp = c(7,5,1,3)
salary_in_lakhs = c(21,13,6,8)
employee.data = data.frame(years_of_exp ,salary_in_lakhs)
employee.data
model = lm(salary_in_lakhs ~ years_of_exp, data= employee.data)
summary(model)
plot(salary_in_lakhs ~ years_of_exp, data = employee.data)
abline(model)