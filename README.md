## Project structure

```
constant_product_explorer/
├─ README.md
├─ src/
│  ├─ amm.py             # AutomatedMarketMaker implementation
│  └─ simulator.py       # Logic for simulation scenarios
└─ notebooks/
   └─ analysis.ipynb
```

## How to setup

1. Ensure that you have **Python 3.11.13**
2. Create and activate Python virtual environment
    - `python -m venv venv`
    - `source venv/bin/activate` on **macOS/Linux** 
    - `venv\Scripts\activate` on **Windows**
3. Install **Pandas**
    - `pip install pandas`
4. To see results use **Jupyter Notebook**. It is the most convinient way for analysis. You can find it in `notebooks/analysis.ipynb`

## Formula explanation (`amountOut`)

Constant-product formula

$$xy = k$$

To swap $x$ with $y$ 

$$ (x + dx)(y - dy) =k=xy$$

Let's find $dy$

$$ y - dy = \dfrac{xy}{x+dx} 
\implies dy = y - \dfrac{xy}{x+dx} = \dfrac{xy + ydx - xy}{x+dx} = \dfrac{ydx}{x+dx} $$

But, we also have fee, let's consider $dx_{net} = dx \cdot (1 - fee)$

$$ dy = \dfrac{ydx_{net}}{x+dx_{net}} $$


## Results for different scenarios
| Name | Amount In | Amount Out | Effective Price | Slippage % |
|------|-----------|------------|-----------------|-----------|
| Swap (1%) | 10.0 | 4.935790 | 0.493579 | 1.284197 |
| Swap (10%) | 100.0 | 45.330545 | 0.453305 | 9.338911 |
| Swap (40%) | 400.0 | 142.550758 | 0.356377 | 28.724621 |
| Swap (50%) | 500.0 | 166.333000 | 0.332666 | 33.466800 |
| Swap (90%) | 900.0 | 236.467612 | 0.262742 | 47.451642 |
| Swap (100%) | 1000.0 | 249.624437 | 0.249624 | 50.075113 |

## How slippage behaves

- As swap size increases, slippage grows exponentially.
- The formula ensures the pool never runs out of tokens. It's mathematically impossible to drain the reserves to zero.
- Larger $k$ or deeper liquidity pool results in lower slippage.
