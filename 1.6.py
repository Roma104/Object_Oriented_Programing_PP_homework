class Smartphone:
    def __init__(self, model=None, battery_level=100):
        self.model = model
        self.is_turned_on = False
        self.battery_level = battery_level
        self.current_app = None

    def __str__(self):
        return (f"Phone: {self.model}\n"
                "-----------------\n"
                f"State:\t{'turned on' if self.is_turned_on else 'turned off'}\n"
                f"Battery:\t{self.battery_level}%\n"
                f"Current app:\t{self.current_app}"
                )

    def power_on(self):
        if self.battery_level > 10:
            self.is_turned_on = True
            print(f"{self.model} is now turned on!")
        else:
            print("Battery level too low")

    def power_off(self):
        self.is_turned_on = False
        self.current_app = None
        print(f"{self.model} is now turned off.")

    def launch_app(self, app_name):
        if self.is_turned_on:
            self.current_app = app_name
            print(f"Launched {app_name}")
        else:
            print("Phone is turned off. Cannot launch app.")

    def charge_battery(self, charge_amount=10):
        self.is_charging = True
        self.battery_level = min(100, self.battery_level + charge_amount)
        print(f"Charging... Current battery level: {self.battery_level}%")
        self.is_charging = False


def main():
    my_phone = Smartphone("Samsung", battery_level=70)
    print(my_phone)
    print()

    print("Turning it on...")
    my_phone.power_on()
    print(my_phone)
    print()

    my_phone.launch_app("TikTok")
    print(my_phone)
    print()

    my_phone.charge_battery()
    print(my_phone)
    print()

    my_phone.power_off()
    print(my_phone)
    print()


if __name__ == "__main__":
    main()