import time
import yfinance as yf

def get_petrobras_stock():
    ticker = "PETR4.SA"  # Código da Petrobrás na B3
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    if not data.empty:
        last_price = data["Close"].iloc[-1]  # Último preço de fechamento
        print(f"Último preço de fechamento da Petrobrás (PETR4): R$ {last_price:.2f}")
    else:
        print("Não foi possível obter os dados.")

if __name__ == "__main__":
    while True:
        get_petrobras_stock()
        time.sleep(3)
