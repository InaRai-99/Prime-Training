from abc import ABC, abstractmethod

# Observer Interface
class OrderPlacedObserver(ABC):
    @abstractmethod
    def update(self, order):
        pass


# Concrete Observers
class EmailNotifier(OrderPlacedObserver):
    def update(self, order):
        print(f"Email sent for order {order}")


class InventoryManager(OrderPlacedObserver):
    def update(self, order):
        print(f"Inventory updated for order {order}")


class ShippingNotifier(OrderPlacedObserver):
    def update(self, order):
        print(f"Shipping notified for order {order}")


class LoyaltyPointManager(OrderPlacedObserver):
    def update(self, order):
        print(f"Loyalty points updated for order {order}")


# Subject
class OrderService:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer: OrderPlacedObserver):
        self.observers.append(observer)

    def notify_observers(self, order):
        for observer in self.observers:
            observer.update(order)

    def place_order(self, order):
        print(f"Order placed: {order}")
        self.notify_observers(order)


# Client Code
order_service = OrderService()
order_service.register_observer(EmailNotifier())
order_service.register_observer(InventoryManager())
order_service.register_observer(ShippingNotifier())
order_service.register_observer(LoyaltyPointManager())

order_service.place_order("ORDER123")
