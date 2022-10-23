# Budget App Challenge for freeCodeCamp Course
# "Scientific Computing with Python"
# Author: Blake McManaway
# GitHub: McManaway
#
# Notable specifications:
# When transferring money between categories, if the amount being
# withdrawn is greater than the current balance of the category,
# the transaction is ignored: nothing is logged, no errors are thrown.
# Tests were performed externally
# ------------------------------------------------------------------- #


class Category:
    """A class representing a category of budget. The class has a
    ledger which keeps track of all transactions against it."""

    def __init__(self, name: str):
        self.name = name
        self.ledger = []

    def deposit(self, amount: float, description="") -> None:
        self.ledger.append({"amount": amount,
                            "description": description})

    def withdraw(self, amount: float, description="") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -1*amount,
                                "description": description})
            return True
        return False

    def get_balance(self) -> float:
        running_total = 0
        for entry in self.ledger:
            running_total += entry["amount"]
        return running_total

    def transfer(self, amount: float, other) -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -1*amount, "description":
                                f"Transfer to {other.name}"})
            other.ledger.append({"amount": amount, "description":
                                f"Transfer from {self.name}"})
            return True
        return False

    def check_funds(self, amount: float) -> bool:
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        # When printing a category, it should print what looks like a
        # receipt, showing every transaction
        statement = "{:*^30}".format(self.name)
        statement += "\n"
        for entry in self.ledger:
            statement += "{:<23}".format(entry["description"][:23])
            statement += "{:>7.2f}".format(entry["amount"])
            statement += "\n"
        statement += "Total: {}".format(self.get_balance())
        return statement


def create_spend_chart(categories: list) -> str:
    total_spent = 0
    statement = ""
    statement += "Percentage spent by category\n"

    # Looping through negative transactions in all categories
    # Because total_spent has to be calculated after all
    # categories have been looped through, added the instance
    # variables <spent> and <percent_spent> so the data persists after
    # the loop
    for cat in categories:
        cat.spent = 0
        for entry in cat.ledger:
            if entry["amount"] < 0:
                cat.spent += entry["amount"]
        total_spent += cat.spent
    for cat in categories:
        cat.percent_spent = (cat.spent / total_spent * 100)
        cat.percent_spent -= cat.percent_spent % 10

    for i in range(100, -1, -10):
        count_list = []
        for j in range(len(categories)):
            if categories[j].percent_spent >= i:
                count_list.append("o")
            else:
                count_list.append(" ")
        statement += "{:>3}".format(i) + "| "
        for count in count_list:
            statement += "{}  ".format(count)
        statement += "\n"
    statement += "    "
    for i in range(3*len(categories)+1):
        statement += "-"
    statement += "\n"

    # The column labels are written vertically, so have to loop
    # through names and store them in chunks based on index. First
    # loop is to find the longest name, so the second loop can add
    # each letter to a list of lists, substituting " " if it's beyond
    # the length of a given name.
    longest_name = 0
    for cat in categories:
        if len(cat.name) > longest_name:
            longest_name = len(cat.name)

    letter_list = []
    for i in range(longest_name):
        row_letters = []
        for cat in categories:
            if i >= len(cat.name):
                row_letters.append(" ")
            else:
                row_letters.append(cat.name[i])
        letter_list.append(row_letters)

    for i in range(len(letter_list)):
        statement += "     "
        for j in letter_list[i]:
            statement += "{}  ".format(j)
        if i == len(letter_list) - 1:
            continue
        else:
            statement += "\n"
    return statement

