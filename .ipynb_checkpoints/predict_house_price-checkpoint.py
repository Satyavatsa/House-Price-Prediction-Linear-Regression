import pickle
import pandas as pd

# Load the saved model
with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

print("California House Price Predictor")
print("-" * 35)

MedInc = float(input("Median Income: "))
HouseAge = float(input("House Age: "))
AveRooms = float(input("Average Rooms: "))
AveBedrms = float(input("Average Bedrooms: "))
Population = float(input("Population: "))
AveOccup = float(input("Average Occupancy: "))
Latitude = float(input("Latitude: "))
Longitude = float(input("Longitude: "))

new_data = pd.DataFrame({
    "MedInc": [MedInc],
    "HouseAge": [HouseAge],
    "AveRooms": [AveRooms],
    "AveBedrms": [AveBedrms],
    "Population": [Population],
    "AveOccup": [AveOccup],
    "Latitude": [Latitude],
    "Longitude": [Longitude]
})

prediction = model.predict(new_data)

print("\nPredicted House Price:", prediction[0])