import time
import json

from Classes.ByteStreamHelper import ByteStreamHelper
from Classes.Packets.PiranhaMessage import PiranhaMessage


class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        ownedBrawlersCount = len(player.OwnedBrawlers)
        ownedPinsCount = len(player.OwnedPins)
        ownedThumbnailCount = len(player.OwnedThumbnails)
        ownedSkins = []

        for brawlerInfo in player.OwnedBrawlers.values():
            try:
                ownedSkins.extend(brawlerInfo["Skins"])
            except KeyError:
                continue

        self.writeVInt(int(time.time()))
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(player.Trophies) # Trophies
        self.writeVInt(player.HighestTrophies) # Highest Trophies
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(player.TrophyRoadTier)
        self.writeVInt(player.Experience) # Experience
        self.writeDataReference(28, player.Thumbnail) # Thumbnail
        self.writeDataReference(43, player.Namecolor) # Namecolor

        self.writeVInt(0)

        self.writeVInt(0) # Selected Skins

        self.writeVInt(0) # Randomizer Skin Selected

        self.writeVInt(0) # Current Random Skin

        self.writeVInt(len(ownedSkins))

        for skinID in ownedSkins:
            self.writeDataReference(29, skinID)

        self.writeVInt(0) # Unlocked Skin Purchase Option

        self.writeVInt(0) # New Item State

        self.writeVInt(0)
        self.writeVInt(player.HighestTrophies)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeBoolean(True)
        self.writeVInt(player.TokensDoubler)
        self.writeVInt(999999) # Trophy Road Timer
        self.writeVInt(999999) # Power Play Timer(Don't Work)
        self.writeVInt(999999)# BrawlPass Timer

        self.writeVInt(141)
        self.writeVInt(135)

        self.writeVInt(5)

        self.writeVInt(93)
        self.writeVInt(206)
        self.writeVInt(456)
        self.writeVInt(792)
        self.writeVInt(729)

        self.writeBoolean(False) # Offer 1
        self.writeBoolean(False) # Offer 2
        self.writeBoolean(True) # Token Doubler Enabled
        self.writeVInt(2)  # Token Doubler New Tag State
        self.writeVInt(2)  # Event Tickets New Tag State
        self.writeVInt(2)  # Coin Packs New Tag State
        self.writeVInt(0)  # Change Name Cost
        self.writeVInt(0)  # Timer For the Next Name Change

        shop = json.loads(open("shop.json", 'r').read()) # import json
        
        self.writeVInt(len(shop) + 3) # Offers count

        self.writeVInt(1)  # RewardCount
        for i in range(1):
            self.writeVInt(6)  # ItemType
            self.writeVInt(0) # Amount
            self.writeDataReference(0)  # CsvID
            self.writeVInt(0) # SkinID

        self.writeVInt(0) # Currency(0-Gems,1-Gold,3-StarpoInts)
        self.writeVInt(666) #Cost
        self.writeVInt(172800) #Time
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeBoolean(False) #Claim
        self.writeVInt(3917)
        self.writeVInt(0)
        self.writeBoolean(False) #Daily Offer
        self.writeVInt(1) # Old price
        self.writeInt(0)
        self.writeString("Unlock all skins") # Text
        self.writeBoolean(False)
        self.writeString("offer_mrbeast") # Background
        self.writeVInt(-1)
        self.writeBoolean(False) # This purchase is already being processed
        self.writeVInt(1) # Type Benefit
        self.writeVInt(100) # Benefit
        self.writeString()
        self.writeBoolean(False) # One time offer
        self.writeBoolean(False) # Claimed
        
        self.writeVInt(2)  # RewardCount
        for i in range(1):
            self.writeVInt(1)  # ItemType
            self.writeVInt(1000) # Amount
            self.writeDataReference(0)  # CsvID
            self.writeVInt(0) # SkinID
        for i in range(1):
            self.writeVInt(16)  # ItemType
            self.writeVInt(250) # Amount
            self.writeDataReference(0)  # CsvID
            self.writeVInt(0) # SkinID

        self.writeVInt(0) # Currency(0-Gems,1-Gold,3-StarpoInts)
        self.writeVInt(0) #Cost
        self.writeVInt(172800) #Time
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeBoolean(False) #Claim
        self.writeVInt(3917)
        self.writeVInt(0)
        self.writeBoolean(False) #Daily Offer
        self.writeVInt(549) # Old price
        self.writeInt(0)
        self.writeString("Gift🤑") # Text
        self.writeBoolean(False)
        self.writeString("offer_special") # Background
        self.writeVInt(-1)
        self.writeBoolean(False) # This purchase is already being processed
        self.writeVInt(2) # Type Benefit
        self.writeVInt(300) # Benefit
        self.writeString()
        self.writeBoolean(False) # One time offer
        self.writeBoolean(False) # Claimed
        
        self.writeVInt(3)  # RewardCount
        
        for i in range(1):
            self.writeVInt(19)  # ItemType
            self.writeVInt(250) # Amount
            self.writeDataReference(52, 47)  # CsvID
            self.writeVInt(47) # SkinID
        for i in range(1):
            self.writeVInt(4)  # ItemType
            self.writeVInt(0) # Amount
            self.writeDataReference(29, 375)  # CsvID
            self.writeVInt(375) # SkinID
        for i in range(1):
            self.writeVInt(9)  # ItemType
            self.writeVInt(1000) # Amount
            self.writeDataReference(0)  # CsvID
            self.writeVInt(1000) # SkinID

        self.writeVInt(0) # Currency(0-Gems,1-Gold,3-StarpoInts)
        self.writeVInt(109) #Cost
        self.writeVInt(172800) #Time
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeBoolean(False) #Claim
        self.writeVInt(3917)
        self.writeVInt(0)
        self.writeBoolean(False) #Daily Offer
        self.writeVInt(159) # Old price
        self.writeInt(0)
        self.writeString("Special Offer") # Text
        self.writeBoolean(False)
        self.writeString("offer_wf") # Background
        self.writeVInt(-1)
        self.writeBoolean(False) # This purchase is already being processed
        self.writeVInt(1) # Type Benefit
        self.writeVInt(2) # Benefit
        self.writeString()
        self.writeBoolean(False) # One time offer
        self.writeBoolean(False) # Claimed
        
        for shop in shop:
            self.writeVInt(1)  # RewardCount
            self.writeVInt(shop['ItemType'])  # ItemType
            self.writeVInt(shop['Amount']) # Amount
            self.writeDataReference(shop['CsvID1'], shop['CsvID2'])  # CsvID
            self.writeVInt(shop['SkinID']) # SkinID
            self.writeVInt(shop['Currency']) # Currency(0-Gems, 1-Gold, 3-StarpoInts)
            self.writeVInt(shop['Cost']) #Cost
            self.writeVInt(shop['Time']) #Time
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(shop['Claim'])
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(shop['DailyOffer']) # Daily Offer
            self.writeVInt(shop['OldPrice']) # Old price
            self.writeInt(0)
            self.writeString(shop['Text']) # Text
            self.writeBoolean(False)
            self.writeString(shop['Background']) # Background
            self.writeVInt(0)
            self.writeBoolean(shop['Processed']) # This purchase is already being processed
            self.writeVInt(shop['TypeBenefit']) # Type Benefit
            self.writeVInt(shop['Benefit']) # Benefit
            self.writeString()
            self.writeBoolean(shop['OneTimeOffer']) # One time offer
            self.writeBoolean(shop['Claimed']) # Claimed
        

        self.writeVInt(player.Tokens)
        self.writeVInt(-1)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(len(player.SelectedBrawlers))
        for i in player.SelectedBrawlers:
            self.writeDataReference(16, i)

        self.writeString(player.Region)
        self.writeString(player.ContentCreator)

        self.writeVInt(19)
        self.writeLong(2, 1)  # Unknown
        self.writeLong(3, 0)  # TokensGained
        self.writeLong(4, 0)  # TrophiesGained
        self.writeLong(6, 0)  # DemoAccount
        self.writeLong(7, 0)  # InvitesBlocked
        self.writeLong(8, 0)  # StarPointsGained
        if player.StarPoints == 0:
        	self.writeLong(9, 0)  # HideStarPoInts
        else:
        	self.writeLong(9, 1)  # ShowStarPoInts
        self.writeLong(10, 0)  # PowerPlayTrophiesGained
        self.writeLong(12, 1)  # Unknown
        self.writeLong(14, 0)  # CoinsGained
        self.writeLong(15, 0)  # AgeScreen | 3 = underage (disable social media) | 1 = age popup
        self.writeLong(16, 1)
        self.writeLong(17, 0)  # TeamChatMuted
        self.writeLong(18, 1)  # EsportButton
        self.writeLong(19, 0)  # ChampionShipLivesBuyPopup
        self.writeLong(20, 0)  # GemsGained
        self.writeLong(21, 0)  # LookingForTeamState
        self.writeLong(22, 1)
        self.writeLong(24, 1)  # Have already watched club league stupid animation

        self.writeVInt(0)

        self.writeVInt(2)  # Brawlpass
        for i in range(9, 11):
            self.writeVInt(i) # Season
            self.writeVInt(34500) # Pass Tikens
            self.writeBoolean(False)
            self.writeVInt(0) # Pass Progress

            self.writeByte(2)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)

            self.writeByte(1)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)

        self.writeVInt(0)

        quests = json.loads(open("quests.json", 'r').read()) # import json
        self.writeBoolean(True) # LogicQuests
        self.writeVInt(len(quests)) # Quests Count
        for x in range(1):
        		for quests in quests:
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(quests['MissionType'])     # Mission Type
        			self.writeVInt(quests['AchievedGoal'])     # Achieved Goal
        			self.writeVInt(quests['QuestGoal'])     # Quest Goal
        			self.writeVInt(quests['TokensReward'])    # Tokens Reward
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(quests['CurrentLevel'])     # Current level
        			self.writeVInt(quests['MaxLevel'])     # Max level
        			self.writeVInt(quests['Timer'])     # Timer
        			self.writeInt8(quests['QuestState'])    # Quest State
        			self.writeDataReference(16, quests['BrawlerID']) # Brawler(16, <BrawlerID>)
        			self.writeVInt(quests['GameMode'])     # GameMode
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(2)     # Unknown
        			self.writeVInt(2)     # Unknown

        self.writeBoolean(True)
        self.writeVInt(ownedPinsCount + ownedThumbnailCount)  # Vanity Count
        for i in player.OwnedPins:
            self.writeDataReference(52, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        for i in player.OwnedThumbnails:
            self.writeDataReference(28, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        self.writeBoolean(False)

        self.writeInt(0)

        self.writeVInt(0)

        self.writeVInt(25) # Count

        # Event Slots IDs Array Start #
        self.writeVInt(1) # Gem Grab
        self.writeVInt(2) # Showdown
        self.writeVInt(3) # Daily Events
        self.writeVInt(4) # Team Events
        self.writeVInt(5) # Duo Showndown
        self.writeVInt(6) # Team Events 2
        self.writeVInt(7) # Special Events(Big Game and other…)
        self.writeVInt(8) # Solo Events (As well as Seasonal Events)
        self.writeVInt(9) # Power Play (Not working)
        self.writeVInt(10) # Seasonal Events
        self.writeVInt(11) # Seasonal Events 2
        self.writeVInt(12) # Candidates of The Day
        self.writeVInt(13) # Winner of The Day
        self.writeVInt(14) # Solo Mode Power League
        self.writeVInt(15) # Team Mode Power League
        self.writeVInt(16) # Club League(Default Map)
        self.writeVInt(17) # Club League(Power Match)
        self.writeVInt(20) # Championship Challenge (Stage 1)
        self.writeVInt(21) # Championship Challenge (Stage 2)
        self.writeVInt(22) # Championship Challenge (Stage 3)
        self.writeVInt(23) # Championship Challenge (Stage 4)
        self.writeVInt(24) # Championship Challenge (Stage 5)
        self.writeVInt(30) # Team Events 3?
        self.writeVInt(31) # Team Events 4?
        self.writeVInt(32) # Team Events 5?
        # Event Slots IDs Array End #

        events = json.loads(open("events.json", 'r').read()) # import json
        
        self.writeVInt(len(events) + 7) # Events Count(7 it a ChampionShip(3 Stages) and ClubLeague(PowerMatch and Default Game Mode)) and PowerLeague(Solo and Team Mode)
        for event in events:
              # Default Slots Start Array #
              self.writeVInt(0)
              self.writeVInt(events.index(event) + 1)  # EventType
              self.writeVInt(event['CountdownTimer'])  # EventsBeginCountdown
              self.writeVInt(event['Timer'])  # Timer
              self.writeVInt(event['TokensReward'])  # tokens reward for new event
              self.writeDataReference(15, event['ID'])  # MapID
              self.writeVInt(-64)  # GameModeVariation
              self.writeVInt(event['Status'])  # Status
              self.writeString()
              self.writeVInt(0)
              self.writeVInt(0)
              self.writeVInt(0)
              if event['Modifier'] > 0:
                 self.writeBoolean(True) #Modifier Data Array
                 self.writeVInt(event['Modifier']) #Modifer ID
              else:
                 self.writeBoolean(False) # Modifier Data Array
              self.writeVInt(0)
              self.writeVInt(0)
              self.writeBoolean(False)  # Map Maker Map Structure Array
              self.writeVInt(0)
              self.writeBoolean(False)  # Power League Data Array
              self.writeVInt(0)
              self.writeVInt(0)
              self.writeBoolean(False)  # ChronosTextEntry
              self.writeBoolean(False)
              self.writeBoolean(False)
              self.writeVInt(-1)
              self.writeBoolean(False)
              self.writeBoolean(False)
              # Default Slots End Array #

        # Championship Challenge Slot Start Array #
        # Championship Challenge Stage 1 #
        self.writeVInt(0)
        self.writeVInt(20)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 10)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() #?
        self.writeVInt(0) #?
        self.writeVInt(0) #Defeates?
        self.writeVInt(3) #Wins In Event Choose
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0) #Wins
        self.writeVInt(0) #Modifier Data Array
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) #Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(9) #Total Wins
        self.writeVInt(3) #?
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)# ???
        self.writeBoolean(False) #???
        self.writeVInt(-1)
        self.writeBoolean(False) #???
        self.writeBoolean(False) #???
        
        # Championship Challenge Stage 2 #   
        self.writeVInt(0)
        self.writeVInt(21)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 53)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() #?
        self.writeVInt(0) #?
        self.writeVInt(0) #Defeates?
        self.writeVInt(3) #Wins In Event Choose
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0) #Wins
        self.writeVInt(0) #Modifier Data Array
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) #Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(9) #Total Wins
        self.writeVInt(3) #?
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False) #???
        self.writeBoolean(False) #???
        self.writeVInt(-1)
        self.writeBoolean(False) #???
        self.writeBoolean(False) #???
        
        # Championship Challenge Stage 3 #   
        self.writeVInt(0)
        self.writeVInt(22)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 293)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString() #?
        self.writeVInt(0) #?
        self.writeVInt(0) #Defeates?
        self.writeVInt(3) #Wins In Event Choose
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0) #Wins
        self.writeVInt(0) #Modifier Data Array
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0) #Defeates
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(9) #Total Wins
        self.writeVInt(3) #?
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False) #???
        self.writeBoolean(False) #???
        self.writeVInt(-1)
        self.writeBoolean(False) #???
        self.writeBoolean(False) #???
        # Championship Slots End Array #
        
        # Club League Slots Start Array #
        # Club League Default Map Array #
        self.writeVInt(0)
        self.writeVInt(16)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 7)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(2)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        # Club League Power Match Array #
        self.writeVInt(0)
        self.writeVInt(17)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(51208)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 25)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(2)  # State
        self.writeString() 
        self.writeVInt(0) 
        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(False)  # Power League Data Array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        # Club League Slots End Array #
        
        # Power League Solo Mode #
        self.writeVInt(0)
        self.writeVInt(14)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(99999)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 4)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(True)  # Power League Data Array
        # Power League Data Array Start #
        self.writeVInt(7) # Season
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        # Power League Data Array End #
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        
        # Power League Team Mode #
        self.writeVInt(0)
        self.writeVInt(15)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(99999)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 4)  # MapID
        self.writeVInt(-64)  # GameModeVariation
        self.writeVInt(0)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(3)
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        self.writeVInt(0)
        self.writeBoolean(True)  # Power League Data Array
        # Power League Data Array Start #
        self.writeVInt(7) # Season
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        # Power League Data Array End #
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeBoolean(False)
        

        self.writeVInt(0) # Comming Events

        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800]) # Brawler Upgrade Cost
        ByteStreamHelper.encodeIntList(self, [20, 50, 140, 280]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [150, 400, 1200, 2600]) # Shop Coins Amount

        self.writeBoolean(True)  # Show Offers Packs

        self.writeVInt(0) # ReleaseEntry

        self.writeVInt(23)  # IntValueEntry

        self.writeLong(10008, 501)
        self.writeLong(65, 2)
        self.writeLong(1, 41000039)  # ThemeID
        self.writeLong(60, 36270)
        self.writeLong(66, 0) # Graveyard Shift
        self.writeLong(61, 36270)  # SupportDisabled State | if 36218 < state its true
        self.writeLong(48, 36217)
        self.writeLong(29, 14)  # Skin Group Active For Campaign
        self.writeLong(48, 41381)
        self.writeLong(50, 1)  # Coming up quests placeholder
        self.writeLong(1100, 500)
        self.writeLong(1101, 500)
        self.writeLong(1003, 1)
        self.writeLong(36, 0)
        self.writeLong(14, 0)  # Double Token Event
        self.writeLong(31, 0)  # Gold rush event
        self.writeLong(79, 149999)
        self.writeLong(80, 160000)
        self.writeLong(28, 4)
        self.writeLong(74, 1)
        self.writeLong(78, 1)
        self.writeLong(17, 4)
        self.writeLong(10046, 1)

        self.writeVInt(0) # Timed Int Value Entry

        self.writeVInt(0)  # Custom Event

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeLong(player.ID[0], player.ID[1])  # PlayerID

        self.writeVInt(0) # NotificationFactory

        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(False)

        self.writeVLong(player.ID[0], player.ID[1])
        self.writeVLong(0, 0)
        self.writeVLong(0, 0)

        self.writeString(player.Name)
        self.writeBoolean(player.Registered)

        self.writeInt(0)

        self.writeVInt(16)

        self.writeVInt(3 + ownedBrawlersCount)

        for brawlerInfo in player.OwnedBrawlers.values():
            self.writeDataReference(23, brawlerInfo["CardID"])
            self.writeVInt(-1)
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(-1)
        self.writeVInt(player.Coins)

        self.writeDataReference(5, 10)
        self.writeVInt(-1)
        self.writeVInt(player.StarPoints)

        self.writeDataReference(5, 13)
        self.writeVInt(-1)
        self.writeVInt(99999) # Club coins

        self.writeVInt(ownedBrawlersCount)

        for brawlerID,brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["Trophies"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["HighestTrophies"])

        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["PowerPoints"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["PowerLevel"] - 1)

        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["State"])

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(0)

        self.writeVInt(player.Gems)  # Diamonds
        self.writeVInt(player.Gems)  # Free Diamonds
        self.writeVInt(player.Level)  # Player Level
        self.writeVInt(100)
        self.writeVInt(0)  # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(0)  # Battle Count
        self.writeVInt(0)  # WinCount
        self.writeVInt(0)  # LoseCount
        self.writeVInt(0)  # WinLooseStreak
        self.writeVInt(0)  # NpcWinCount
        self.writeVInt(0)  # NpcLoseCount
        self.writeVInt(2)  # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(0)

    def decode(self):
        fields = {}
        # fields["AccountID"] = self.readLong()
        # fields["HomeID"] = self.readLong()
        # fields["PassToken"] = self.readString()
        # fields["FacebookID"] = self.readString()
        # fields["GamecenterID"] = self.readString()
        # fields["ServerMajorVersion"] = self.readInt()
        # fields["ContentVersion"] = self.readInt()
        # fields["ServerBuild"] = self.readInt()
        # fields["ServerEnvironment"] = self.readString()
        # fields["SessionCount"] = self.readInt()
        # fields["PlayTimeSeconds"] = self.readInt()
        # fields["DaysSinceStartedPlaying"] = self.readInt()
        # fields["FacebookAppID"] = self.readString()
        # fields["ServerTime"] = self.readString()
        # fields["AccountCreatedDate"] = self.readString()
        # fields["StartupCooldownSeconds"] = self.readInt()
        # fields["GoogleServiceID"] = self.readString()
        # fields["LoginCountry"] = self.readString()
        # fields["KunlunID"] = self.readString()
        # fields["Tier"] = self.readInt()
        # fields["TencentID"] = self.readString()
        #
        # ContentUrlCount = self.readInt()
        # fields["GameAssetsUrls"] = []
        # for i in range(ContentUrlCount):
        #     fields["GameAssetsUrls"].append(self.readString())
        #
        # EventUrlCount = self.readInt()
        # fields["EventAssetsUrls"] = []
        # for i in range(EventUrlCount):
        #     fields["EventAssetsUrls"].append(self.readString())
        #
        # fields["SecondsUntilAccountDeletion"] = self.readVInt()
        # fields["SupercellIDToken"] = self.readCompressedString()
        # fields["IsSupercellIDLogoutAllDevicesAllowed"] = self.readBoolean()
        # fields["isSupercellIDEligible"] = self.readBoolean()
        # fields["LineID"] = self.readString()
        # fields["SessionID"] = self.readString()
        # fields["KakaoID"] = self.readString()
        # fields["UpdateURL"] = self.readString()
        # fields["YoozooPayNotifyUrl"] = self.readString()
        # fields["UnbotifyEnabled"] = self.readBoolean()
        # super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion