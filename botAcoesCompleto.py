import time
import yfinance as yf
import os

def get_petrobras_stock():
    ticker = "PETR4.SA"  # Código da Petrobrás na B3
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    info = stock.info
    
    if not data.empty:
        last_price = data["Close"].iloc[-1]  # Último preço de fechamento
        open_price = data["Open"].iloc[-1]   # Preço de abertura
        high_price = data["High"].iloc[-1]   # Máxima do dia
        low_price = data["Low"].iloc[-1]     # Mínima do dia
        volume = data["Volume"].iloc[-1]     # Volume negociado

        os.system('cls')
        print("=== Informações da Ação ===")
        print(f"Codigo: {ticker}")
        print(f"Último preço de fechamento: R$ {last_price:.2f}")
        #print(f"Preço de abertura: R$ {open_price:.2f}")
        print(f"Máxima do dia: R$ {high_price:.2f}")
        print(f"Mínima do dia: R$ {low_price:.2f}")
        #print(f"Volume negociado: {volume}")        
        #print(f"Capitalização de Mercado: {info.get('marketCap', 'N/A')}")
        print(f"Beta: {info.get('beta', 'N/A')}")
        print(f"Setor: {info.get('sector', 'N/A')}")
        print(f"PE Ratio Retorno %: {info.get('trailingPE', 'N/A')}")
        print("===============================\n")
    else:
        print("Não foi possível obter os dados.")

def get_weg_stock():
    ticker = "WEGE3.SA"  # Código da Petrobrás na B3
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    info = stock.info
    
    if not data.empty:
        last_price = data["Close"].iloc[-1]  # Último preço de fechamento
        open_price = data["Open"].iloc[-1]   # Preço de abertura
        high_price = data["High"].iloc[-1]   # Máxima do dia
        low_price = data["Low"].iloc[-1]     # Mínima do dia
        volume = data["Volume"].iloc[-1]     # Volume negociado
        
        print("=== Informações da Ação ===")
        print(f"Codigo: {ticker}")
        print(f"Último preço de fechamento: R$ {last_price:.2f}")
        #print(f"Preço de abertura: R$ {open_price:.2f}")
        print(f"Máxima do dia: R$ {high_price:.2f}")
        print(f"Mínima do dia: R$ {low_price:.2f}")
        #print(f"Volume negociado: {volume}")        
        #print(f"Capitalização de Mercado: {info.get('marketCap', 'N/A')}")
        print(f"Beta: {info.get('beta', 'N/A')}")
        print(f"Setor: {info.get('sector', 'N/A')}")
        print(f"PE Ratio Retorno %: {info.get('trailingPE', 'N/A')}")
        print("===============================\n")
    else:
        print("Não foi possível obter os dados.")

    

if __name__ == "__main__":
    while True:
        get_petrobras_stock()
        get_weg_stock()
        time.sleep(3)



#O Beta mede a volatilidade de uma ação em relação ao mercado como um todo.

#Um Beta de 1 indica que a ação tende a se mover com o mercado.

#Um Beta maior que 1 significa que a ação é mais volátil que o mercado (ou seja, mais arriscada).

#Um Beta menor que 1 indica que a ação é menos volátil que o mercado, ou seja, apresenta menor risco em comparação.


#PE RATIO

#Indústria	        Alta relação P/L	Baixa relação preço/lucro
#Tecnologia	            >50	                    10>
#Finança	            >20	                     5>
#Assistência médica	    >30	                    10>
#Energia	            >20	                     5>


#O Price-to-Earnings Ratio (P/E Ratio) é a relação entre o preço de mercado de uma ação e o lucro por ação (EPS).

#Ele é calculado dividindo o preço atual da ação pelo lucro por ação.

#Um P/E Ratio de 10.59 significa que você está pagando 10.59 vezes os lucros da empresa por cada ação que possui.

#P/E Ratio alto pode sugerir que a ação está supervalorizada, enquanto um P/E Ratio baixo pode indicar que a ação está subvalorizada.