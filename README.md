# House Hunting

## Description

After graduating from Momentum, you start a new job with a good salary and now you want to save up to buy a house. You're going to need a down payment, though. In this lab, you are going to write a program to help you determine how long it will take to save enough money to make the down payment.

## Objectives

After completing this assignment, you should understand:

- How variables work
- How `while` works
- How `if` works
- How to get and transform user input

After completing this assignment, you should be able to:

- Write a Python script
- Ask for input
- Print output

## Details

1. Call the cost of your dream home `total_cost​`.
2. Call the portion of the cost needed for a down payment `portion_down_payment​`. For simplicity, assume that `portion_down_payment` = 0.25 (25%).
3. Call the amount that you have saved thus far `current_savings​`. You start with a current savings of $0.
4. Assume that you invest your current savings wisely, with an annual return of `r` ​(in other words, at the end of each month, you receive an additional `current_savings*r/12`​ funds to put into your savings – the 12 is because `r`​ is an annual rate). Assume that your investments earn a return of `r` = 0.04 (4%).
5. Call your annual salary `annual_salary​`.
6. Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. `Call that portion_saved`​. This variable should be in decimal form (i.e. 0.1 for 10%).
7. At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your monthly salary ​(annual salary / 12).

Write a program to calculate how many months it will take you to save up enough money for a down payment.

Your program should ask the user to enter the following variables:

1. The starting annual salary (`annual_salary`)
2. The portion of salary to be saved (`portion_saved`)
3. The cost of your dream home (`total_cost`)

Please make your program print results in the format shown in the test cases below.

### Test Case 1

```
Enter your annual salary: 120000
Enter the percent of your salary to save, as a decimal: .10
Enter the cost of your dream home: 1000000
Number of months: 183
```

### Test Case 2

```
Enter your annual salary: 80000
Enter the percent of your salary to save, as a decimal: .15
Enter the cost of your dream home: 500000
Number of months: 105
```

### Hints

To help you get started, here is a rough outline of the stages you should probably follow in writing your code:

- Retrieve user input. Look at `input()` if you need help with getting user input. For this problem set, you can assume that users will enter valid input (e.g. they won’t enter a string when you expect a number.)
- Initialize some state variables. You should decide what information you need. Be careful about values that represent annual amounts and those that represent monthly amounts.
- Try different inputs and see how long it takes to save for a down payment.

### Hard Mode

Add the ability to set the percentage of the total cost you need for a down payment and the rate of expected return on investment. For each of these, allow the user to enter the value. If they choose not to enter a value, then use the default, like in the following case:

```
Enter your annual salary: 80000
Enter the percent of your salary to save, as a decimal: .15
Enter the expected annual rate of return [0.04]:
Enter the cost of your dream home: 500000
Enter the percent of your home's cost to save as a down payment [0.25]: 0.2
Number of months: ???
```

## Credit

This assignment is adapted from the [MIT Introduction to Computer Science](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/) course.
