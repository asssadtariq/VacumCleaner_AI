import random

class Room:
    def __init__(self, n, s=False):
        self.name = n
        self.status = s

    def get_name(self):
        return self.name

    def get_status(self):
        return self.status

    def set_status(self, s):
        self.status = s

    def set_name(self, r):
        self.name = r

    def cleanRoom(self):
        cost = 1
        self.status = True
        return cost

    def display(self):
        print("Name : {} and Status = {}".format(self.name, self.status))

class VacumCleaner:
    def __init__(self, tc = 0):
        self.cost = 0
        self.total_cost = tc

    def clean_rooms(self, rooms, room_name=None):
        current_cost = 0
        room_index = -1

        # loop to get room index
        for index, value in enumerate(rooms):
            if value.name == room_name:
                room_index = index
                break

        for roomIndex in range(room_index, 0, -1):
            if not rooms[roomIndex].get_status():
                print("{} is dirty :) ".format(rooms[roomIndex].get_name()))
                print("cleaning!\n")
                self.cost += rooms[roomIndex].cleanRoom()

            else:
                print("{} is clean :) ".format(rooms[roomIndex].get_name()))

        for room in rooms:
            if not room.get_status():
                print("{} is dirty :) ".format(room.get_name()))
                print("cleaning!\n")
                self.cost += room.cleanRoom()

            else:
                print("{} is clean :) ".format(room.get_name()))

        t_cost = self.cost
        self.total_cost += self.cost
        self.cost = 0
        return t_cost


def main():
    total_rooms = []
    for i in range(0, 10):

        is_dirty = random.randint(0, 20)
        if is_dirty > 12:
           r = Room('room'+str(i))
        else:
            r = Room('room' + str(i), True)

        total_rooms.append(r)

    vc = VacumCleaner(0)
    cost = vc.clean_rooms(total_rooms, 'room'+str(random.randint(0,9)))
    print("Total Cost = {}".format(cost))

if __name__ == '__main__':
    main()
