# Refactored Modern Order Processor (O(N) Hash Set Lookup)
from typing import List, Dict, Any, Set

class ModernOrderProcessor:
    def __init__(self) -> None:
        self.orders: List[Dict[str, Any]] = []
        self._seen_ids: Set[str] = set()

    def process_bulk_orders(self, raw_orders: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Processes incoming orders in O(N) time complexity using set lookups.
        """
        processed: List[Dict[str, Any]] = []
        for order in raw_orders:
            order_id = order["id"]
            if order_id not in self._seen_ids:
                self._seen_ids.add(order_id)
                self.orders.append(order)
                processed.append(order)
        return processed
