import serial
import math
def parse_gst_message(gst_message):
    # Divida a mensagem NMEA em seus componentes
    fields = gst_message.split(',')
    
    # O campo 6 é Latitude Error Std Dev, e o campo 7 é Longitude Error Std Dev na mensagem GST
    try:
        latitude_error_std_dev = float(fields[6])
        longitude_error_std_dev = float(fields[7])
        return latitude_error_std_dev, longitude_error_std_dev
    except (IndexError, ValueError):
        print("Erro ao processar a mensagem GST.")
        return None, None

def calculate_error(lat_error, lon_error):
    std_error = math.sqrt(lat_error**2 + lon_error**2)
    return std_error

def main():
    # Configura a porta serial (substitua 'COMx' ou '/dev/ttyUSBx' conforme o sistema)
    serial_port = serial.Serial(port='COM7', baudrate=115200, timeout=2)

    try:
        while True:
            # Leia a linha da porta serial
            line = serial_port.readline().decode('ascii', errors='replace').strip()

            if line.startswith('$GNGST'):
                # Se for uma mensagem GST, parse e extraia os valores
                lat_error, lon_error = parse_gst_message(line)
                
                if lat_error is not None and lon_error is not None:
                    # Calcule algo com os valores e exiba o resultado

                    result = calculate_error(lat_error, lon_error)
                    # print(f"Lat_erro: }")
                    print(f"Resultado do cálculo: {result}, lat_erro:{lat_error}, lon_erro:{lon_error}")
    except KeyboardInterrupt:
        print("Finalizando script.")
    finally:
        # Feche a porta serial ao finalizar
        serial_port.close()

main()
# if __name__ == '__main__':
#     main()
