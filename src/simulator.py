import pandas as pd

from src.amm import AutomatedMarketMaker


def simulate_scenarios(trades):
    """Simulate a sequence of trades on the given AMM.

    Args:
        trades: A list of dicts.

    Returns:
        A DataFrame with columns: name, amount_in, amount_out, effective_price, slippage
    """
    results = []
    for trade in trades:
        amm = AutomatedMarketMaker(
            reserve_a=trade['reserve_a'],
            reserve_b=trade['reserve_b'],
            fee=trade['fee']
        )
        amount_out, effective_price, slippage = amm.swap(trade['amount_in'], trade.get('from_a', True))
        results.append({
            'name': trade.get('name', ''),
            'amount_in': trade['amount_in'],
            'amount_out': amount_out,
            'effective_price': effective_price,
            'slippage %': slippage
        })
    return pd.DataFrame(results)
