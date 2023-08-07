class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount%10==5:return 100-purchaseAmount-5
        return 100-(round(purchaseAmount/10)*10)