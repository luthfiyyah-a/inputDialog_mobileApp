import tensorflow as tf

model = tf.keras.models.load_model('Malicious_URL_Prediction.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("Malicioous_URL_Prediction.tflite", "wb").write(tflite_model)