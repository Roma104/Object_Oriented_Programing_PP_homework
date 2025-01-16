class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def show_status(self):
        if self.is_on:
            if 1 <= self.channel_no <= len(self.channels):
                print(
                    f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no - 1]}), volume {self.volume}")
            else:
                print(f"TV is on, channel {self.channel_no}, volume {self.volume}")
        else:
            print("TV is off")

    def set_channels(self, channels_list):
        self.channels = channels_list

    def show_channels(self):
        print("Channel list:")
        for i, channel in enumerate(self.channels, 1):
            print(f"{i}. {channel}")

    def volume_up(self):
        if self.is_on and self.volume < 10:
            self.volume += 1

    def volume_down(self):
        if self.is_on and self.volume > 0:
            self.volume -= 1