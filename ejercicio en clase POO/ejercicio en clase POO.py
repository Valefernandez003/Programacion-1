from moto import Motorbike
moto1= Motorbike("blanco","AB123CD",10,2,"Harley Davidson","Grand American Touring","2023",220,400)
moto2= Motorbike("amarillo","AF256GH",10,2,"Kawasaki","Ninja","2022",190,372)
print("Prueba: Arrancar motor")
moto1.start_engine() #arranca el motor
moto1.start_engine() #tiene que avisar que el motor ya está encendido
print("Prueba: Detener motor")
moto1.stop_engine() #apaga el motor
moto1.stop_engine() #debe avisar que el motor ya está detenido

moto1.price=1500000 #precio de la moto 1
print(f"el precio de la moto {moto1.brand} {moto1.model} es de: {moto1.price}")
