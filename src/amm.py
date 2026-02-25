class AutomatedMarketMaker:
    def __init__(self, reserve_a: float, reserve_b: float, fee: float):
        self.reserve_a = reserve_a
        self.reserve_b = reserve_b
        self.fee = fee

    def swap(self, amount_in, from_a: bool = True):
        """Swap amount_in from A (if from_a=True) or from B.

        Returns a tuple (amount_out, effective_price, slippage) where:
        - `effective_price` is output per input (B per A when swapping A->B, A per B when B->A)
        - `slippage` is the relative difference between spot price and effective price, expressed in percent
        """
        if amount_in <= 0:
            raise ValueError("Amount must be positive")

        x, y = (self.reserve_a, self.reserve_b) if from_a else (self.reserve_b, self.reserve_a)

        # Apply fee and calculate output amount
        amount_in_with_fee = amount_in * (1 - self.fee)
        amount_out = (y * amount_in_with_fee) / (x + amount_in_with_fee)
        effective_price = amount_out / amount_in
        spot_price = y / x
        slippage = (spot_price - effective_price) / spot_price * 100.0

        # Update reserves
        if from_a:
            self.reserve_a += amount_in
            self.reserve_b -= amount_out
        else:
            self.reserve_b += amount_in
            self.reserve_a -= amount_out

        return amount_out, effective_price, slippage
