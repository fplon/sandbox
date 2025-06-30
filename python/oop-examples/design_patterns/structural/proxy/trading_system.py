from abc import ABC, abstractmethod


# Subject interface
class TradingSystem(ABC):
    @abstractmethod
    def execute_trade(self, symbol, quantity, action):
        pass


# RealTradingSystem class
class RealTradingSystem(TradingSystem):
    def execute_trade(self, symbol, quantity, action):
        print(f"Executing {action} trade for {quantity} shares of {symbol}")


# ProxyTradingSystem class
class ProxyTradingSystem(TradingSystem):
    def __init__(self, real_trading_system):
        self._real_trading_system = real_trading_system

    def execute_trade(self, symbol, quantity, action):
        if action.lower() == "buy":
            print("Proxy: Requesting buy trade approval")
            # Simulate approval logic (in real system, this could be more complex)
            approval_granted = True
            if approval_granted:
                self._real_trading_system.execute_trade(symbol, quantity, action)
            else:
                print("Proxy: Trade request denied")
        else:
            self._real_trading_system.execute_trade(symbol, quantity, action)


# Client code
if __name__ == "__main__":
    real_trading_system = RealTradingSystem()
    proxy = ProxyTradingSystem(real_trading_system)

    # Try executing different trades
    proxy.execute_trade("AAPL", 100, "buy")
    proxy.execute_trade("AAPL", 50, "sell")
