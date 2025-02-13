# ➕ Aproximação de Funções com Séries de Fourier

Olá! Neste repositório você encontrará um script em Python para aproximar funções utilizando séries de Fourier. O objetivo é visualizar de gráfica como a aproximação é realizada conforme o número de termos da soma aumenta.

## 🔹 Requisitos
- Python 3.x.
-  Dependências listadas no arquivo `requirements.txt`.

## 🔹 Instalação
1. Clone este repositório.
    ```
    git clone https://github.com/marcosnevary/fourier-series.git
    cd fourier-series
    ```
2. Instale as dependências necessárias.
    ```
    pip install -r requirements.txt
    ```
## 🔹 Funcionamento
1. Altere a variável `f` para a função que será aproximada.
   - Caso a função seja continua, defina diretamente.
     - Exemplo:
       ```
       f = x ** 2
       ```
   - Caso a função seja definida por partes, utilize a seguinte estrutura:
     ```
     f = sp.Piecewise((<função>, <intervalo>), (<função>, <intervalo>))
     ```
     - Exemplo:
       ```
       f = sp.Piecewise((-1, (x > -sp.pi) & (x < 0)), (1, (x > 0) & (x < sp.pi)))
       ```
3. Altere a variável `n` para o número de termos que a soma terá.
4. Execute o script.
   ```
   python fourier_series.py
   ```

