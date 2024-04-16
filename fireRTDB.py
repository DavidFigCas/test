import firebase_admin
from firebase_admin import credentials, db

# Path al archivo de configuración de Firebase
cred = credentials.Certificate('/home/pi/FTP/sensors/google-services.json')

# Inicializa la aplicación con Firebase
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-industry-panels-default-rtdb.firebaseio.com/'
})


# Suponiendo que tienes una función que lee datos del sensor
sensor_data = 12

# Referencia a tu base de datos
ref = db.reference('path/data')

# Envía los datos al RTDB
ref.set(sensor_data)

