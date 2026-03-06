#Author: Jacob Matlock

from flask import Flask, jsonify
import random, math

app = Flask(__name__)

#==================================================
# CLASS DEFINITION
#==================================================

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.secrets = {}
        self.monsters = []
        self.visited = False

#==================================================
# ROOM CREATION
#==================================================

sleeping_quarters = Room("Sleeping Quarters", "This room has with ten beds lining both the left and "
                                              "right sides of the room, with a chest at the foot of each.")
sleeping_quarters.secrets = {0: "You search through each chest and find nothing remarkable, save for some ink in one "
                                "near the rear of the room."}
sleeping_quarters.items = ["ink"]

large_room = Room("Large Room", "You are in a large, empty room with beautiful paintings lining each "
                                "of the four walls.")

sword_room = Room("Sword Room", "You are in a small room with dim lighting. In the center of the room "
                                "is a pedestal with a shiny, glinting sword placed in it. Engraved on the hilt of the "
                                "sword is a gryphon with a snake in its talons.")
sword_room.secrets = {0: "There some text in an unfamiliar script on the pedestal in front of the blade of the sword."}
sword_room.items = ["sword"]
sword_room.alt_description = ("You are a small room with dim lighting. In the center of the room is the pedestal from "
                              "which you took your sword in exchange for your ring.")


statue_room = Room("Statue Room", "You are in a medium sized room with several rows of monster statues "
                         "of all different kinds. While counting, you see a cyclops, man-bat, pigman, goblin, ogre, "
                         "mimic, and minotaur to name a few. Your final count makes 25 total statues in the room.")

empty_room = Room("Empty Room", "You are in a small room with torches lining the walls but is otherwise"
                                " empty.")

wand_room = Room("Wand Room", "You are in a small room with a pedestal in the center. Carved on the "
                              "pedestal are strange, curving runes. Placed on top of the pedestal is a thin wooden rod "
                              "with similar runes engraved in it. Upon further inspection, you see a small diamond "
                              "embedded in the tip of the wand.")
wand_room.items = ["wand"]
wand_room.alt_description = ("You are in the small room from which you took your wand. You look at the familiar runes "
                             "on the pedestal and ponder their meaning.")

minotaur_room = Room("Minotaur Room", "Upon entering this room, you are blasted with a wall of stench."
                                " It is so overpowering that you almost leave the room but you notice a menacing "
                                "Minotaur with matted, midnight black fur across the room. It glares at you, snorting "
                                "and stamping its feet, seemingly preparing to charge.")
minotaur_room.items = ["minotaur horn"]
minotaur_room.monsters = ["Minotaur"]
minotaur_room.alt_description = ("You are in the room where you fought and slayed the Minotaur. Its body remains where "
                                 "you left it, missing a horn.")

strange_room = Room("Strange Room", "You are in a cluttered room with lots of strange, unfamiliar "
                                "objects. Among them, a crystal orb, preserved monster parts, piles of bones and other "
                                "curiosities. There are a few old cabinets dotting the walls.")
strange_room.items = ["potion"]
strange_room.secrets = {0:"You search through the cabinets in the room and find a small glass bottle with a blue, "
                          "shimmering liquid in it. The bottle is labeled 'magic in a bottle' with poor handwriting."}

pit_room = Room("Pit Room", "You barely stop walking into this room in time to not fall into the gaping"
                            " pit that spans the majority of where the floor should be. There is a narrow ledge running"
                            " along the south and east walls, allowing passage between the two doors there.")
pit_room.exits = {"north": None, "east": Room, "south": Room, "west": None}

art_room = Room("Art Room", "You are in awe of the beauty in this room. Scattered throughout the dimly "
                            "lit space are partially finished works of art. There is a painting of a beautiful sunset, "
                            "left without its landscape, a statue of a man fighting an invisible enemy, with his legs "
                            "forever entombed in stone, and many other pieces, abandoned by their creator.")

gk_room = Room("Golden Key Room", "Suspended by a rope in the middle of this room is a golden key with "
                                  "wings on its bow.")
gk_room.items = ["Golden Key"]
gk_room.alt_description = ("You are in the room where you retrieved the golden key. The rope still dangles from the "
                           "ceiling in the center of the room.")

torture_chamber = Room("Torture Chamber", "This room is full of medieval torture devices. Looking at "
                                          "them sends shivers down your spine.")

manbat_room = Room("Man-Bat Room", "At first glance, this room seemed empty, but as you look around, "
                                   "you hear a slight squeaking coming from above you. You look up and see a man-bat "
                                   "hybrid hanging from the ceiling. It appears to be smelling the air between you.")
manbat_room.items = ["man-bat wing"]
manbat_room.monsters = ["Man-Bat"]
manbat_room.alt_description = ("Now that this room is safe from any monsters, you notice the thin layer of guano lining"
                               " the floor and scratches all over the walls and ceiling.")

workshop = Room("Workshop", "This room is filled with machines belonging to masters of many different "
                            "trades. There is a smithy, a tanning rack, carpenters tools, and plenty more. There is no "
                            "work in progress at any of the workstations so it appears to serve more as a storage room "
                            "right now.")

dining_room = Room("Dining Room", "You are in a long dining room with a table spanning almost the "
                                  "length of the whole room. There are chairs at each head and at even intervals down "
                                  "each side. While the places at the table are set, ready for a meal, there is no food"
                                  " in the room, save for some fresh fruit in bowls lining the center of the table. "
                                  "There is a single door in the west wall.")
dining_room.items = ["fruit"]
dining_room.secrets = {0: "You run your fingers along the trim that lines the walls and you feel something catch. When "
                          "you go back to see what it was, you find that there is a small button embedded in the wood "
                          "of the trim."}
dining_room.alt_description = ("You are in a long dining room with a table spanning almost the length"
                                  " of the whole room. There are chairs at each head and at even intervals down each "
                                  "side. While the places at the table are set, ready for a meal, there is no food in "
                                  "the room, save for some fresh fruit in bowls lining the center of the table. There "
                                  "is a single door in the west wall and a secret passageway that you found.")

garden = Room("Garden", "Light streams into this room from skylights in the ceiling. The sunlight bathe"
                        "s and feeds rows upon rows of plants. You see fruits and vegetables of all kinds, ripe for the"
                        " picking. There are doors in the east and west walls.")
garden.items = ["fruit", "vegetables"]

ogre_room = Room("Ogre Room", "You step into this room and are greeted by a thunderous roar. Across the"
                              " room you see a massive ogre heft a giant club onto his shoulder. Drool drips onto the "
                              "floor from his under-bitten jaw as he takes a step towards you, menacingly.")
ogre_room.items = ["ogre tooth", "ogre club"]
ogre_room.monsters = ["Ogre"]

ogre_room.alt_description = ("The floor and walls in this room are littered with craters from where the ogre tried "
                             "smashing you with its club. There is at least a clear path between the doors on the east "
                             "and west walls.")

lava_room = Room("Lava Room", "You step into this room and wilt under the oppressive heat. You see a "
                              "two foot wide bridge spanning a lava pool twenty feet below you. The bridge connects the"
                              " east and west walls, where this room’s doors are located.")

library = Room("Library", "You are in the biggest library you have ever seen. There are rows upon rows "
                          "of bookshelves, packed to the brim that run from the floor to the ceiling. In the center of "
                          "the room are some desks for studying. There are doors in the north, south, and west walls.")
library.items = ["potion"]
library.secrets = {0: "You search through the desks and find a small, glass bottle with a blue, shimmering liquid in it"
                      ". The bottle is labeled “magic in a bottle” with poor handwriting."}

scroll_room = Room("Scroll Room", "You are in a dusty room with scroll cubbies lining the east and west"
                                  " walls. In the center of the room, there is a lectern with a scroll unrolled, and "
                                  "held open with paperweights. There are doors on the north and south walls.")
scroll_room.items = ["scroll of blasting"]
scroll_room.alt_description = ("You are in a dusty room with scroll cubbies lining the east and west walls. In the "
                            "center of the room, there is the lectern from which you tool the scroll. There are doors"
                            " on the north and south walls.")

mimic_room = Room("Mimic Room", "You are in a simple, plain room with no ornamentation and no furniture"
                                " other than a singular table, chair, and chest. There are doors on the east and south "
                                "walls.")
mimic_room.items = ["mimic tongue"]
mimic_room.secrets = {0: "As you approach the chest, you notice that something about it looks…wrong. You reach out your"
                         " hand only to jerk it back as the chest lunges forward, almost biting your hand off. It "
                         "appears that the chest was really a mimic. The mimic seems to be squatting, as if to prepare "
                         "for its next strike."}
mimic_room.monsters = ["Mimic"]
mimic_room.alt_description = ("You are in the room in which you fought the mimic. Its orange blood runs along the floor"
                              "from where you removed its tongue.")

key_exit = Room("Key Exit", "In this room, on the east wall, you see a grand, golden door. There is a "
                            "keyhole in the center of the door with radiant golden wings extending out from both sides."
                            " The only other door is on the west wall.")

cyclops_room = Room("Cyclops Room", "You can see the wavering light of torches on the wall across the "
                                    "room but you can't seem to see them. Before too long, you realize that is because "
                                    "you are in the shadow of a huge cyclops. You have to tilt your head back in order "
                                    "to see its singular eye staring right at you with malice.")
cyclops_room.items = ["cyclops eye"]
cyclops_room.monsters = ["Cyclops"]
cyclops_room.alt_description = ("The cyclops's corpse covers almost the entire floor in this room and you have to climb"
                                " over it to navigate between the doors on the north and south walls.")

collapsed_room = Room("Collapsed Room", "The roof in the center of this room has seemingly collapsed. "
                                        "You can see a door on the north, east, and west walls, but those are the only "
                                        "other things of note in this room.")

kitchen = Room("Kitchen", "You find yourself in a clean, bright kitchen that looks like it is ready for"
                          " use by a master chef. You see doors in the south and west walls.")
kitchen.items = ["knife", "food"]
kitchen.secrets = {0: "You search through each cabinet in the entire kitchen, and in one of the final drawers you "
                      "search, you find a small button hidden underneath the counter."}
kitchen.alt_description = ("You find yourself in a clean, bright kitchen that looks like it is ready for use by a "
                           "master chef. You see doors in the south and west walls, as well as the secret passage you "
                           "opened in one of the cabinets.")

dark_room = Room("Dark Room", "You can see nothing in this room, save for some light leaking through "
                              "from underneath the door on the east wall.")

pigman_room = Room("Pigman Room", "You smell a sweet scent upon entering this room and you notice a "
                    "person sitting at a hearth on the northern wall. You begin to walk towards them but they let out "
                    "an inhuman shrieking sound before you can get too close. It whips around and you find yourself "
                    "facing a pigman, a monster you've only heard stories of.")
pigman_room.items = ["pigman snout"]
pigman_room.monsters = ["Pigman"]
pigman_room.alt_description = ("You shudder as you re-enter this room, remembering the traumatic fight you had with the"
                               " terrifying pigman. You make yourself leave though one of the doors on the north or "
                               "south walls as fast as you can.")

broom_closet = Room("Broom Closet", "You are in a dusty broom closet with miscellaneous cleaning and"
                                    "maintenance supplies. There is a door on the west wall.")
broom_closet.exits = {"north": None, "east": Room, "south": None, "west": Room}
broom_closet.secrets = {0: "You start rummaging through the supplies and you hear a clunk and the sound of stone "
                          "grinding on stone. You look up to see a secret passage on the east wall."}
broom_closet.alt_description = ["You are in a dusty broom closet with miscellaneous cleaning and maintenance supplies. "
                                "There is a door on the west wall and the secret passage you opened on the east wall."]

lavatory = Room("Lavatory", "You are in a small stone room with a foul stench. In one corner is a "
                            "pitiful toilet with flies buzzing around it. You see one exit on the west wall")

music_room = Room("Music Room", "You are in a round room with stairs leading down to a center stage. "
                                "Sitting on the stage, bathed in a mysterious light are many instruments, including a"
                                "piano, flute, trumpet, cello, and more. You can see an exit on the eastern side of "
                                "the room")

dusty_room = Room("Dusty Room", "You are in a room that hasn't been disturbed in so long, the coat of "
                                "dust on the floor is visible to the naked eye. Dust particles dance in the air and"
                                "cobwebs and dust-bunnies hang off of wall sconces, empty shelves, and anything else"
                                "remaining in this room.")
dusty_room.alt_description = ("You are in a room that hasn't been disturbed in so long, the coat of dust on the floor "
                              "is visible to the naked eye. Dust particles dance in the air and cobwebs and "
                              "dust-bunnies hang off of wall sconces, empty shelves, and anything else remaining in "
                              "this room. There is a trail of footprints from the last time you were in this room")

training_room = Room("Training Room", "In the center of this room there is a circular mat with years of"
                                      "sweat stains marking it. Lining the walls are racks of wooden practice weapons "
                                      "and padded leather armor for training.")

elegant_bedroom = Room("Elegant Bedroom", "You are in the most elegant and lavish bedroom you have ever"
                                          "seen. The bedposts are carved from a delicate wood and trimmed with gold, as"
                                          "with everything else in this room. You also see garish jewels embedded in "
                                          "various pieces of furniture around the room. On one of the tables is a plate"
                                          " of steaming food of all varieties.")
elegant_bedroom.items = ["golden goblet", "food"]

supply_room = Room("Supply Room", "In this room, you see everything that someone could possibly need to"
                                  "supply a group of people the size of an army for a year. You see fabrics to make "
                                  "clothes, wood for fires, tools for repair work and many more things.")
supply_room.items = ["wood", "wood", "wood", "wood"]

locked_room = Room("Locked Room", "This is the first locked door that you have come across since "
                                  "leaving the cell hall")
locked_room.items = ["Amulet of Time", "blueprints", "teleportation book", "stealth book", "bodybuilding "
                        "book", "secrets book"]
locked_room.secrets = {0: "You inspect the circular table and find that it is lined with drawers that are "
                          "barely visible.", 1: "Among the papers on the desk, you find the blueprints for the dungeon "
                          "you are in. You can see four exits on the blueprint with a symbol by each. There is a rope, "
                          "a key, a puzzle piece, and a cauldron representing each exit.", 2: "On the bookshelf, you "
                          "see many books but the titles to four stand out to you: 'The Guide to Teleportation',"
                          " 'Harvey's Instructions for Ultimate Stealth', 'Bodybuilding for the Common Guard', and "
                          "'Secrets of the Nohman Mountains'."}
locked_room.alt_description = ("You unlock the door with the rusty key you found and it swings open with a squeal. At "
                               "first glance, you can't see any reason why this room would be locked. All you see "
                               "immediately is a desk to your left with papers strewn about, a bookshelf to your right,"
                               " and a circular table in the center.")

destroyed_room = Room("Destroyed Room", "The only things remaining in this room have been reduced to "
                                "splinters and ash desks and bookshelves have been crushed and burned, and glass "
                                "cabinets have been shattered.")

cold_room = Room("Cold Room", "This room is somehow significantly colder than the one you just left. It"
                            " feels as though you are in the middle of a raging winter storm. You see icicles hanging "
                              "from the ceiling and scattered pieces of frosty furniture.")

muggy_room = Room("Muggy Room", "The air in this room is thick and it feels as though you might choke "
                                "on it. You see moss growing on the stone walls and floor. In one corner you see a "
                                "small swamp-like formation. There is a small variety of plants and you here a few"
                                "distinctive animal calls as well.")

rain_room = Room("Rain Room", "Rain pours down on you from above as you enter this room. You look up to"
                              "see the source but all you can make out is a seemingly endless blackness that "
                              "occasionally hosts a flash of lightning and clap of thunder.")

windy_room = Room("Windy Room", "You almost fall over as you are blasted with a powerful gust of wind."
                                "You regain your balance and look for the source but can find none. The wind continues "
                                "and you struggle to maintain your feet.")

animal_room = Room("Animal Room", "This room is filled with the sounds and scents of countless animals."
                                  "There are rows upon rows of pens, enclosures, and cages housing all kinds of animals"
                                  "from chickens to horses to panthers. As you catalog the animals in your mind you "
                                  "even hear the rattle of a rattlesnake and other sounds that make your skin crawl.")

armory = Room("Armory","You see before you several racks of shining swords and armor, polished so that"
                       " you can see your reflection. You cringe at your ragged appearance.")
armory.items = ["armor", "sword"]

carpet_room = Room("Carpet Room", "You find your self in a brightly colored room that has a wonderfully"
                                  "soft carpet lining the floor, walls, and ceiling.")

stairwell = Room("Stairwell", "You are in a long hallway that contains only stairs, and a burning "
                              "sconce every 10 feet.")

balcony = Room("Balcony", "You open this door into warm rays of golden sunlight. At first you think you"
                          "are free but then you notice the 1000-foot drop and realize you are just on a balcony, over-"
                          "looking the city you grew up in.")

chapel = Room("Chapel", "You find yourself in some sort of chapel or temple to an unknown god. You do "
                        "not recognize any holy symbols or idols.")

pool = Room("Pool", "In the center of this room is an enormous pool fit for training professional "
                    "athletes.")

fire_room = Room("Fire Room", "This room is overwhelmingly hot due to the fires that blaze in braziers"
                              "that take up every free space in this room except the paths between the doors. Braziers"
                              " on the floor, on shelves, on tabletops, hanging from the ceiling. The orange fire licks"
                              "threateningly at the air.")

future_room = Room("Future Room", "This room has a lot of unfamiliar machines. Bright white lights hang"
                                  "from the ceiling by chains. Boxes emitting light with moving pictures on them sit on"
                                  "tabletops.")
future_room.items = ["laser gun"]
future_room.secrets = {0: "On one of the desks, next to one of the unfamiliar machines, you see a strange looking "
                    "newspaper. At the top of one of the pages, you see a date that is almost 300 years in the future!"}

game_room = Room("Game Room", "This room looks ready for a night of fun with a billiards table, dart"
                              " board, ring toss, and many other simple games for whiling away the time.")
game_room.items = ["darts"]

werewolf_room = Room("Werewolf Room", "You enter this room to a devilish snarling emanating from an "
                                    "angry werewolf across the room from you. You cannot recall when the last full moon"
                                    " was, but that matters not as you see the monster start to dash towards you.")
werewolf_room.items = ["werewolf pelt"]
werewolf_room.monsters = ["Werewolf"]
werewolf_room.alt_description = ("Upon returning to the room where you slayed the werewolf, instead of finding a "
                                 "skinned werewolf, you find a skinned human. Fighting the urge to vomit, you avert "
                                 "your eyes and move on.")

fountain_room = Room("Fountain Room", "This room contains only a simple fountain in the center of the "
                                      "room. The fountain has some embellishments and adornments but is not something"
                                      " one would find in a palace garden.")
fountain_room.secrets = {0:"You find a small plaque on the base of the fountain that reads: 'Find the two goblets "
                           "placed in this dungeon. Bring them here and choose one with which to drink the water from "
                           "this fountain. Choose wisely."}

rope_room = Room("Rope Room", "This room seems to house nothing but huge coils of rope. They are "
                              "stacked atop one another as if a giant was stacking his spools of thread here.")
rope_room.items = ["rope"]

spikes_room = Room("Spikes Room", "Your cautiousness pays off as you barely stop yourself from sliding"
                                  " off the ledge of the doorway into this room and falling into a pit of sharp spikes."
                                  "There are bridges crossing the room in several places but are cleverly not placed "
                                  "directly in front of the doors.")

observatory = Room("Observatory", "You step into this room and see a lonely telescope sitting in the "
                                  "center of the room. The observatory window is already open. You look through the "
                                  "viewport and although it is daytime, the telescope is so powerful, you can still see"
                                  "into space.")

goblin_room = Room("Goblin Room", "A sickening laughter echoes through this room as you enter. You see"
                                  "an ugly little goblin bouncing around on the opposite side of the room from you. "
                                  "When you make eye contact, his eyes narrow and his grin widens. He brandishes a long"
                                  " dagger and runs towards you.")
goblin_room.items = ["goblin ear", "dagger"]
goblin_room.monsters = ["Goblin"]

monster_exit = Room("Monster Exit", "You step into this room and you are greeted by an elderly wizard,"
                                    " sitting on a stool in front of a bubbling cauldron. 'Hello, young one,' he says"
                                    " with a smile. 'I've been trapped here for so long without a friendly face, I had"
                                    " almost given up hope. I am far too weak at this old age but if you can slay all"
                                    " 6 monsters in this dungeon and bring me a part from each, I can cast a spell to"
                                    " get us out of this horrid place!")

puzzle_exit = Room("Puzzle Exit", "You step into this room and find yourself in a shadow. You look up "
                                  "to a grinning face. A chimera looms over you and begins to laugh wickedly. 'Welcome"
                                  " to my lair. If you pass my puzzles, you can pass me and leave this place. If you "
                                  "fail my test I will eat you. Or you can refuse and go on your way.'")



eligible_rooms= [sleeping_quarters, large_room, sword_room, statue_room, empty_room, wand_room, strange_room, pit_room,
                 art_room, gk_room, torture_chamber, workshop, dining_room, garden, lava_room, library, scroll_room,
                 collapsed_room, kitchen, dark_room, broom_closet, lavatory, music_room, dusty_room, training_room,
                 elegant_bedroom, supply_room, locked_room, destroyed_room, cold_room, muggy_room, rain_room,
                 windy_room, animal_room, armory, carpet_room, stairwell, balcony, chapel, pool, fire_room, future_room,
                 game_room, fountain_room, rope_room, spikes_room, observatory]

#The rooms in the following two lists are included in the room pool but are not included in the above list.

monster_rooms = [minotaur_room, manbat_room, ogre_room, mimic_room, cyclops_room, pigman_room, werewolf_room,
                 goblin_room]
exit_rooms = [key_exit, monster_exit, puzzle_exit]

floating_items = ["rusty key", "lewd drawing", "guard clothes", "rusty fork", "broken manacles", "tankard",
                  "sealed letter", "moldy bread"]

#==================================================
#==================================================

def choose_rooms(num_rooms: int, eligible_rooms: list) -> dict:
    """

    Parameters:
        num_rooms - int
        eligible_rooms - list of room objects

    Returns:
        room_coordinates - dictionary
    """
    rooms_remaining = eligible_rooms.copy()
    rooms_list = []

    for item in exit_rooms:
        rooms_list.append(item)

    monster_rooms_used = random.sample(monster_rooms, 6) #if you change this number, change the appropriate number in
                                                         #monster_exit and in your client file
    for item in monster_rooms_used:
        rooms_list.append(item)

    num_rooms = num_rooms - len(rooms_list)

    # ==================================================
    # Here I will be defining the rules and conditions
    # for which rooms need to be included
    # ==================================================

    required_items = ["sword", "food"]

    for item in required_items:
        items_rooms = [room for room in rooms_remaining if item in room.items]

        if not items_rooms:
            raise ValueError(f"No rooms available with the required item: {item}.")

        room_chosen = random.choice(items_rooms)
        rooms_list.append(room_chosen)
        rooms_remaining.remove(room_chosen)

    num_rooms = num_rooms - len(required_items)

    #choose the remaining rooms at random
    while num_rooms > 0:
        room = random.choice(rooms_remaining)
        rooms_list.append(room)
        rooms_remaining.remove(room)
        num_rooms -= 1

    room_coordinates = place_rooms(rooms_list)
    return room_coordinates

def place_rooms(rooms_list: list) -> dict:
    """
    This function takes the list of rooms being used in the game and assigns a coordinate to each. Then, the exits of
    each room are defined.

    Parameters:
        rooms_list - list of room objects

    Returns:
        room_coordinates - dictionary
    """

    edge_rooms = exit_rooms.copy()

    if balcony in rooms_list:
        edge_rooms.append(balcony)

    dimension = int(len(rooms_list) ** 0.5)
    room_coordinates = {(x,y): None for x in range(dimension) for y in range(dimension)}

    left_edge = [(0,y) for y in range(dimension)]
    right_edge = [(dimension,y) for y in range(dimension)]
    top_edge = [(x,dimension) for x in range(dimension)]
    bottom_edge = [(x,0) for x in range(dimension)]
    edge_list = list(set(left_edge + right_edge + top_edge + bottom_edge))

    # ensure that exits and some other rooms spawn on the edge of the map
    while len(edge_rooms) > 0:
        coordinate_choice = random.choice(edge_list)
        edge_list.remove(coordinate_choice)

        room_choice = random.choice(edge_rooms)
        edge_rooms.remove(room_choice)
        rooms_list.remove(room_choice)

        room_coordinates[coordinate_choice] = room_choice

    remaining_rooms = [key for key, value in room_coordinates.items() if value is None]
    weapon_placed = False
    locked_room_placed = False

    while len(remaining_rooms) > 0:
        room_choice = random.choice(rooms_list)
        rooms_list.remove(room_choice)

        if ("sword" in room_choice.items or "wand" in room_choice.items) and not weapon_placed: #ensures the player can
            first_row_empty = [key for key in remaining_rooms if key[0] == 0] #get a weapon before seeing a monster
            coordinate_choice = random.choice(first_row_empty)
            room_coordinates[coordinate_choice] = room_choice

            remaining_rooms.remove(coordinate_choice)
            weapon_placed = True #allows other rooms with weapons to be placed normally

        elif room_choice == locked_room:
            coordinate_choice = random.choice(remaining_rooms)
            room_coordinates[coordinate_choice] = room_choice
            locked_room_placed = True

        else:
            coordinate_choice = random.choice(remaining_rooms)
            room_coordinates[coordinate_choice] = room_choice

        filled_rooms = [key for key, value in room_coordinates.items() if value is not None]
        if locked_room_placed and len(filled_rooms) > 1: #if len(filled_rooms) == 1 then the key would be placed in
            filled_rooms.remove(locked_room)             #locked_room
            key_room = random.choice(filled_rooms)
            key_room.items.append("rusty key")

        # ==================================================
        # DEFINE ROOM EXITS
        # ==================================================

        # ==================================================
        # START WITH CORNERS
        # ==================================================
        if coordinate_choice == (0,0): #room is bottom left corner
            room_choice.exits["west"] = None
            room_choice.exits["south"] = None

            north_room = room_coordinates[(0,1)]
            east_room = room_coordinates[(1,0)]

            if north_room is not None:
                room_choice.exits["north"] = north_room
                north_room.exits["south"] = room_choice
            if east_room is not None:
                room_choice.exits["east"] = east_room
                east_room.exits["west"] = room_choice

        elif coordinate_choice == (0,dimension): #room is top left corner
            room_choice.exits["west"] = None
            room_choice.exits["north"] = None

            south_room = room_coordinates[(0,dimension-1)]
            east_room = room_coordinates[(1,dimension)]

            if south_room is not None:
                room_choice.exits["south"] = south_room
                south_room.exits["north"] = room_choice
            if east_room is not None:
                room_choice.exits["east"] = east_room
                east_room.exits["west"] = room_choice

        elif coordinate_choice == (dimension,0): #room is bottom right corner
            room_choice.exits["east"] = None
            room_choice.exits["south"] = None

            north_room = room_coordinates[(dimension,1)]
            west_room = room_coordinates[(dimension-1,0)]

            if north_room is not None:
                room_choice.exits["north"] = north_room
                north_room.exits["south"] = room_choice
            if west_room is not None:
                room_choice.exits["west"] = west_room
                west_room.exits["east"] = room_choice

        elif coordinate_choice == (dimension,dimension): #room is top right corner
            room_choice.exits["east"] = None
            room_choice.exits["north"] = None

            south_room = room_coordinates[(dimension, dimension-1)]
            west_room = room_coordinates[(dimension-1, dimension)]

            if south_room is not None:
                room_choice.exits["south"] = south_room
                south_room.exits["north"] = room_choice
            if west_room is not None:
                room_choice.exits["west"] = west_room
                west_room.exits["east"] = room_choice

        # ==================================================
        # NEXT, EDGES
        # ==================================================
        elif coordinate_choice[0] == 0: #room is on left edge and not the corner
            room_choice.exits["west"] = None

            north_room = room_coordinates[(0, coordinate_choice[1]+1)]
            south_room = room_coordinates[(0, coordinate_choice[1]-1)]
            east_room = room_coordinates[(1, coordinate_choice[1])]

            if north_room is not None:
                room_choice.exits["north"] = north_room
                north_room.exits["south"] = room_choice
            if south_room is not None:
                room_choice.exits["south"] = south_room
                south_room.exits["north"] = room_choice
            if east_room is not None:
                room_choice.exits["east"] = east_room
                east_room.exits["west"] = room_choice

        elif coordinate_choice[0] == dimension: #room is on right edge and not the corner
            room_choice.exits["east"] = None

            north_room = room_coordinates[(dimension, coordinate_choice[1]+1)]
            south_room = room_coordinates[(dimension, coordinate_choice[1]-1)]
            west_room = room_coordinates[(dimension-1, coordinate_choice[1])]

            if north_room is not None:
                room_choice.exits["north"] = north_room
                north_room.exits["south"] = room_choice
            if south_room is not None:
                room_choice.exits["south"] = south_room
                south_room.exits["north"] = room_choice
            if west_room is not None:
                room_choice.exits["west"] = west_room
                west_room.exits["east"] = room_choice

        elif coordinate_choice[1] == 0: #room is on bottom edge and not the corner
            room_choice.exits["south"] = None

            north_room = room_coordinates[(coordinate_choice[0], 1)]
            east_room = room_coordinates[(coordinate_choice[0]+1, 0)]
            west_room = room_coordinates[(coordinate_choice[0]-1,0)]

            if north_room is not None:
                room_choice.exits["north"] = north_room
                north_room.exits["south"] = room_choice
            if west_room is not None:
                room_choice.exits["west"] = west_room
                west_room.exits["east"] = room_choice
            if east_room is not None:
                room_choice.exits["east"] = east_room
                east_room.exits["west"] = room_choice


        elif coordinate_choice[1] == dimension: #room is on top edge and not the corner
            room_choice.exits["north"] = None

            south_room = room_coordinates[(coordinate_choice[0], dimension-1)]
            east_room = room_coordinates[(coordinate_choice[0]+1, dimension)]
            west_room = room_coordinates[(coordinate_choice[0]-1, dimension)]

            if south_room is not None:
                room_choice.exits["south"] = south_room
                south_room.exits["north"] = room_choice
            if west_room is not None:
                room_choice.exits["west"] = west_room
                west_room.exits["east"] = room_choice
            if east_room is not None:
                room_choice.exits["east"] = east_room
                east_room.exits["west"] = room_choice

        # ==================================================
        # FINALLY, CENTER ROOMS
        # ==================================================
        else:
            north_room = room_coordinates[(coordinate_choice[0], coordinate_choice[1]+1)]
            south_room = room_coordinates[(coordinate_choice[0], coordinate_choice[1]-1)]
            east_room = room_coordinates[(coordinate_choice[0]+1, coordinate_choice[1])]
            west_room = room_coordinates[(coordinate_choice[0]-1, coordinate_choice[1])]

            if north_room is not None:
                room_choice.exits["north"] = north_room
                north_room.exits["south"] = room_choice
            if south_room is not None:
                room_choice.exits["south"] = south_room
                south_room.exits["north"] = room_choice
            if west_room is not None:
                room_choice.exits["west"] = west_room
                west_room.exits["east"] = room_choice
            if east_room is not None:
                room_choice.exits["east"] = east_room
                east_room.exits["west"] = room_choice

    return room_coordinates
# ==================================================
# DEFINE ENDPOINTS
# ==================================================
@app.get('/room-layout/<int:num_rooms>')
def room_layout(num_rooms):
    if num_rooms <= 0 or not isinstance(num_rooms, int) or not math.isqrt(num_rooms):
        return jsonify({"error": "Number of rooms must be a positive, square integer"}), 400

    if num_rooms > len(rooms_list):
        return jsonify({"error", "Rooms requested greater than rooms available"}), 400

    rooms_used = choose_rooms(num_rooms, eligible_rooms)
    return jsonify(rooms_used), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1400, debug=True)