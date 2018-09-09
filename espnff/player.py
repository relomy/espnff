class Player(object):
    def __init__(self, data):
        self.is_on_bench = data['slotCategoryId'] == 20
        self.first_name = data['player']['firstName']
        self.last_name = data['player']['lastName']
        self.current_slot = data['slotCategoryId']
        self.trade_locked = data['isTradeLocked']
        self.health_status = data['player']['healthStatus']
        self.draft_rank = data['player']['draftRank']
        self.is_active = data['player']['isActive']
        self.droppable = data['player']['droppable']
        self.lock_status = data['lockStatus']
        self.eligible_slots = data['player']['eligibleSlotCategoryIds']
        self.percent_change = data['player']['percentChange']
        self.percent_owned = data['player']['percentOwned']
        self.percent_started = data['player']['percentStarted']
        self.player_id = data['player']['playerId']
        self.pro_team_id = data['player']['proTeamId']

    def __repr__(self):
        return 'Player(%s)' % (self.first_name + " " + self.last_name + " " + str(self.player_id),)

    def attr_list(self, should_print=False):
        items = self.__dict__.items()
        if should_print:
            [print(f"attribute: {k:20s} : {v}") for k, v in items]
        return items
