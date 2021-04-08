
class OrderTable:
    def __init__(self, order_id, order_no,name, p_method, g_total):
        self.order_id = order_id
        self.order_no = order_no
        self.name = name
        self.p_method = p_method
        self.g_total = g_total

    @property
    def data(self):
        if self.g_total:
            self.g_total = float(self.g_total)

        return {
            'order_id': self.order_id,
            'order_no': self.order_no,
            'name': self.name,
            'p_method': self.p_method,
            'g_total': self.g_total
        }
