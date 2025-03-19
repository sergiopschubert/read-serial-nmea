# Read NMEA Messages

Este script em Python é projetado para ler e interpretar mensagens NMEA do tipo `$GNGST` recebidas por uma porta serial, extraindo informações de precisão e calculando o erro padrão a partir dos valores obtidos.

## Funcionalidades

- **Leitura e interpretação de mensagens NMEA `$GNGST`** via porta serial.
- **Extração de desvios padrão** de latitude e longitude.
- **Cálculo do erro padrão** usando os desvios padrão obtidos.
- **Monitoramento contínuo** das mensagens recebidas com feedback imediato no console.

## Requisitos

- Python 3.x
- Biblioteca `pyserial`

## Instalação

```bash
pip install pyserial
```

## Configuração

Altere a variável `serial_port` no script para corresponder à sua configuração de hardware:

```python
serial_port = serial.Serial(port='COM7', baudrate=115200, timeout=2)
```

## Execução

Execute o script diretamente usando o comando:

```bash
python seu_script.py
```

Pressione `Ctrl+C` para interromper a execução do script.

## Saída

O script irá exibir continuamente no terminal:

```
Resultado do cálculo: [valor], lat_erro:[valor], lon_erro:[valor]
```

## Estrutura do Código

- `parse_gst_message(gst_message)`: Extrai os erros padrão de latitude e longitude.
- `calculate_error(lat_error, lon_error)`: Calcula o erro padrão combinado.
- `main()`: Executa a leitura contínua dos dados pela porta serial e exibe os resultados.

## Autor

Desenvolvido por Sérgio P. Schubert.

