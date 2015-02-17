'''
Created on Feb 14, 2015

(Create an investment-value calculator) Write a program that calculates the
future value of an investment at a given interest rate for a specified number
of years. The formula for the calculation is as follows:

futureValue = investmentAmount * (1 + monthlyInterestRate) ** (years * 12)

Use text fields for users to enter the investment amount, years, and interest
rate. Display the future amount in a text field when the user clicks the
Calculate button

@author: M
'''
import tkinter as tk

class InvestmentCalculator:
    def __init__(self):
        self.__window = tk.Tk()
        self.__window.title("Investment Calculator")
        tk.Label(self.__window, text="Investment Amount").grid(row=1,
                                                        column=1, sticky=tk.W)
        self.__amount = tk.DoubleVar()
        tk.Entry(self.__window, textvariable=self.__amount,
              justify = tk.RIGHT).grid(row=1, column=2)
        tk.Label(self.__window, text="Years").grid(row=2, column=1, sticky=tk.W)
        self.__years = tk.DoubleVar()
        tk.Entry(self.__window, textvariable = self.__years,
              justify = tk.RIGHT).grid(row=2, column=2)
        tk.Label(self.__window, text="Annual Interest Rate"\
                 ).grid(row=3, column=1, sticky=tk.W)
        self.__interest_rate = tk.DoubleVar()
        tk.Entry(self.__window, textvariable = self.__interest_rate,
              justify = tk.RIGHT).grid(row=3, column=2)
        tk.Label(self.__window, text="Future Value").grid(row=4,
                                                          column=1, sticky=tk.W)
        tk.Button(self.__window, text="Calculate",
                  command=self.compute_future_value)\
                  .grid(row=5, column=2, sticky=tk.E)
        self.__window.mainloop()

    def compute_future_value(self):
        """
        Computes the future value of an investment at a given interest rate
        for a specified number of years.
        """
        future_value = self.__amount.get() * \
            (1 + self.__interest_rate.get() / 1200) ** \
            (self.__years.get() * 12)
        future_value = format(future_value, ".2f")
        tk.Label(self.__window,
                 text = future_value).grid(row=4, column=2, sticky=tk.E)

InvestmentCalculator()