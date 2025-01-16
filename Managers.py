class RosterManagement:
    cap = 18
    offseason = False

    def __init__(self):
        self.roster = {}
        self.roster_size = 0

    def add_player(self, position, player_name):
        self.roster[position] = player_name
        self.roster_size += 1

    def remove_player(self, position):
        if position in self.roster:
            del self.roster[position]
            self.roster_size -= 1

    def display_roster(self):
        for position, player in self.roster.items():
            print(f"{position}: {player}")

    @classmethod
    def update_cap(cls):
        if cls.offseason:
            cls.cap = 20

    def __len__(self):
        return self.roster_size

    


def main():
    roster = RosterManagement()
    roster2 = RosterManagement()
    roster.add_player("pg", "Steph Curry")
    roster.add_player("sf", "Lebron James")
    roster.display_roster()
    roster.remove_player("pg")
    print("\nAfter removal:")
    roster.display_roster()
    print(roster.cap)
    assert roster2.cap == 18
    RosterManagement.offseason = True
    RosterManagement.update_cap()
    print(RosterManagement.cap)
    print(len(roster))


if __name__ == "__main__":
    main()