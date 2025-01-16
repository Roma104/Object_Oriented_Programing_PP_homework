from thermometer import Thermometer


def main():
    medical_thermometer = Thermometer()

    medical_thermometer.turn_on()

    medical_thermometer.measure_temperature()

    medical_thermometer.display_temperature()

    medical_thermometer.turn_off()


if __name__ == "__main__":
    main()