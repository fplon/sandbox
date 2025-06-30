from typing import List, Tuple


class Asset:
    def __init__(self, name: str, returns: List[float]) -> None:
        self.name = name
        self.returns = returns


class PortfolioIterator:
    def __init__(self, assets: List[Asset]) -> None:
        self.assets = assets
        self.index = 0

    def __iter__(self) -> "PortfolioIterator":
        return self

    def __next__(self) -> Asset:
        if self.index < len(self.assets):
            asset = self.assets[self.index]
            self.index += 1
            return asset
        else:
            raise StopIteration


class Portfolio:
    def __init__(self, assets: List[Asset]) -> None:
        self.assets = assets

    def optimize(self) -> Tuple[float, List[float]]:
        total_returns = [0.0] * len(self.assets[0].returns)
        for asset in self:
            for i, ret in enumerate(asset.returns):
                total_returns[i] += ret

        avg_returns = [ret / len(self.assets) for ret in total_returns]
        return sum(avg_returns), avg_returns

    def __iter__(self) -> PortfolioIterator:
        return PortfolioIterator(self.assets)


# Example usage
if __name__ == "__main__":
    asset1 = Asset("Stock A", [0.05, 0.03, 0.06, 0.02, 0.04])
    asset2 = Asset("Stock B", [0.03, 0.04, 0.02, 0.05, 0.06])
    asset3 = Asset("Stock C", [0.06, 0.07, 0.05, 0.08, 0.04])

    portfolio = Portfolio([asset1, asset2, asset3])

    expected_return, avg_returns = portfolio.optimize()
    print("Expected Portfolio Return:", expected_return)
    print("Average Returns of Each Asset:", avg_returns)
