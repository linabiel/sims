class House:
    def __init__(self, rooms, tenants, plot_size):
        self.rooms = rooms
        self.tenants = tenants
        self.plot_size = plot_size

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room):
        self.rooms.remove(room)

    def add_tenant(self, tenant):
        self.tenants.append(tenant)

    def remove_tenant(self, tenant):
        self.tenants.remove(tenant)

    def change_plot_size_size(self, width, length):
        self.plot_size = [width, length]


