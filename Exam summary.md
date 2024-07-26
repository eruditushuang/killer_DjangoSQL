# Exam summary
### time: 10:00-11:00, 60 min in total.
### provider: ****killer
### Format (7 tasks): 2* Quiz (Choices), 4* Code Gaps, 1* Coding. After finishing each section, you cannot come back.

## Quiz 1, 2
basic selection in SQL and (... I forgot it ...) 
## Quiz 3, 4, 5, 6 and likely answers, not 100% sure
Part of the code is missing.
* Having an orders table with a timestamp ordered_at column, fill in the gaps in the PostgreSQL query to extract a day, a month and a year into separate columns (integer-based).

Missing: __EXTRACT__ and __DAY__, __MONTH__, __YEAR__ and.
```SQL
SELECT 
  EXTRACT(DAY FROM ordered_at)::integer as order_day, 
  EXTRACT(MONTH FROM ordered_at)::integer as order_month, 
  EXTRACT(YEAR FROM ordered_at)::integer as  order_year
FROM orders
```

* You have a Pandas' DataFrame with age and salary columns. Please select age of three people with the highest salary.

Q: __sort_values( = "age")__ and __iloc[]__.
```python
top_3_salaries = df.sort_values(by="age").iloc[:3]
```

* Check with a conditional statement whether the data frame df contains nonnumeric values using the appropriate function from the apply() collection in R.
If so, display a relevant message. Put this code inside the trycatch function with a parameter that will return a message if an error occurs while executing the code.

Q: missing __sapply()__ and __tryCatch()__ and __!all__. 
A: should use __sapply()__.
```R
tryCatch(
  expr = {
    if(!all(sapply(df, is.numeric))){
      print("The dataframe contains non-numeric values.")
    }else{
      print("The dataframe has only numeric values.")
    }
  },
  error = function(e){
    print(paste("An error occurred: ", e))
  }
)
```
* Forgot... about PostGreSQL with __CASE__

## Quiz 7: Coding 1
* Clone it from Git
* Use the master branch (new branch not allowed)
* Implement the empty functions
* Run existing tests to see the new functions works
* Push it back to the repository __regularly__
* The exam repository is closed automatically when the exam ends.

# experience
## Overall
* We got maybe 60% correct.
* I prepared a lot, but the time is __too tight__ for thinking properly: It is almost an automatic-reflection test, not a reasoning test. 
* It requires advanced SQL knowledge and good __instinct__ for SQLAlchemy.

## Quiz
* Great help from the team and AI.

## coding
* My submission was the commit at 11AM, 50% done.
* The first part was straight forward (with AI)
* In the second part I was totally misled by the existing code. It was just __catastrophy__ to go into the direction of using SQL queries. Time was wasted and it did not work at all.
```python
return self.repository.session.execute(query, params).fetchall()
```

* The correct and elegant solution is to use Alchemy, see the last push.