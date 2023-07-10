class lo:
    """
    A simple class to keep track of the important parts of an ebay listing
    """
    def __init__(self, name, price, link, image, trigger):
        self._name = name
        self._price = price
        self._link = link
        self._image = image
        self._trigger = list(trigger)

    #brief summary for notification
    def summary(self):
        trigger = self._trigger[0] if len(self._trigger) == 1 else self._trigger
        word = "Triggers" if len(self._trigger) > 1 else "Trigger"
        return f"{word} '{trigger}' activated for {self._price}"

    #print all members for terminal tests
    def show(self):
        print(f"name: {self._name}")
        print(f"price: {self._price}")
        print(f"trigger(s): {self._trigger}")
        print(f"listing: {self._link}")
        print("\n")
