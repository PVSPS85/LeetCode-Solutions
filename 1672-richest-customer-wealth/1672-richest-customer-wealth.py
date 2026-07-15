class Solution:
    def maximumWealth(self, accounts):
        maximum = 0

        for customer in accounts:
            wealth = sum(customer)

            if wealth > maximum:
                maximum = wealth

        return maximum