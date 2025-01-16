import random


class Thermometer:
    def __init__(self):
        self.is_on = False
        self.current_temperature = None

    def turn_on(self):
        self.is_on = True
        print("Thermometer is turned on.")

    def turn_off(self):
        self.is_on = False
        self.current_temperature = None
        print("Thermometer is turned off.")

    def measure_temperature(self):
        if not self.is_on:
            print("Thermometer is off. Cannot measure temperature.")
            return None

        self.current_temperature = round(random.uniform(34.0, 42.0), 1)
        return self.current_temperature

    def display_temperature(self):
        if not self.is_on:
            print("Thermometer is off. No temperature to display.")
            return

        if self.current_temperature is None:
            print("No temperature measurement yet.")
            return

        output = f"Temperature: {self.current_temperature}°C"

        if self.current_temperature >= 37.0:
            output += " (fever)"

        if self.current_temperature >= 41.0:
            output += " CRITICAL TEMPERATURE!!"

        print(output)