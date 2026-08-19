# Unoptimized Legacy Monolithic Order Processing Engine
class LegacyOrderProcessor:
    def __init__(self):
        self.orders = []

    def process_bulk_orders(self, raw_orders):
        # BUG/INEFFICIENCY: O(N^2) linear search for duplicates and unindexed filtering
        processed = []
        for order in raw_orders:
            is_duplicate = False
            for existing in self.orders:
                if existing['id'] == order['id']:
                    is_duplicate = True
                    break
            if not is_duplicate:
                self.orders.append(order)
                processed.append(order)
        return processed
