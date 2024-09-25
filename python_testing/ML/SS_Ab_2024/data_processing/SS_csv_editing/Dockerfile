# Usa una imagen base de Python con capacidades de construcción para compilar ciertas librerías
FROM python:3.8
WORKDIR /usr/src/app
COPY . .
RUN pip install pandas openpyxl
CMD ["python", "./visualize_numbers.py"]

