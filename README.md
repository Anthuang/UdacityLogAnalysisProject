# Instructions
1. Simply run in the command line:
```
python logger.py
```

# Design
## Question 1
Here I join the tables log and articles on the slug versions of the articles' name. Since paths are stored in log, I first parse out the last part of the path which is the slug. I also ignore all paths that are the root which means the user isn't reading any articles.

## Question 2
This is similar to before, except I also joined with the authors table so I can count by author instead of by article.

## Question 3
This is more complicated. I am running a subquery that returns a table grouped by date and includes the number of each status code, which is done by doing a sum on a case statement. The outer query calculates the percentage error and only returns rows that include days where those percentages are greater than 1%, and also the percentages itself.
