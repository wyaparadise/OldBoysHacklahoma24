#Event 1

t0 = (" WELCOME TO VEGA")

t1 = ("USER> COMPUTER, WHAT SHOULD WE DO?",
    "- - - - - - - - - - - - - - - - - - - - - -",
    "1. Go to the Dark Nebula.",
    "2. Sell the food stores.",
    "3. Plot a course to the Andromeda System.",
    "4. Upgrade the hull."
)

#A tree

t1a = (
    "USER> THE DARK NEBULA? WHAT'S THERE FOR US?",
    "- - - - - - - - - - - - - - - - - - - - - -",
    "1. Ancient alien ruins.",
    "2. Fuel sources",
)
t1aa = (
    "USER> I don't think thats wise,",
    "I'll consult the other crew.",
    "- - - - - - - - - - - - - - - - - - - - - -",
)
t1ab = (
    "USER> We'll begin mining immediately,",
    "Though we'll need food for the journey ",
    "- - - - - - - - - - - - - - - - - - - - - -",
    "",
    "    -* FOOD STORES DEPLETED 10kg *-",
    "    -* FUEL TANK FILLED 30L *-"

)

#B tree  

t1b = (
    "USER> How much do you suggest we sell?",
    "we are low enough as it is.",
    "- - - - - - - - - - - - - - - - - - - - - -",
    "1. 10kg",
    "2. 25kg",
    "3. All of the food stores."
)
t1ba = (
    "USER> It has been done.",
    "I hope you are as intelligent as you seem.",
    "- - - - - - - - - - - - - - - - - - - - - -",
    "",
    "    -* SOLD 10kg FOOD STORES *-"

    ##MINUS 10 FOOD
)
t1bb = (
    "USER> It has been done.",
    "I hope you are as intelligent as you seem.",
    "- - - - - - - - - - - - - - - - - - - - - -",
    "",
    "    -* SOLD 25kg FOOD STORES *-"

    ##MINUS 25 FOOD
)
t1bc = (
    "USER> Are you crazy?? We'll surely die!!",
    "- - - - - - - - - - - - - - - - - - - - - -",
    "",
    "    -* SOLD ALL FOOD STORES *-"

    ##MINUS ALL FOOD
)




textDict = {
    "0"   : t0, #TITLE SCREEN
    "1"   : t1,  

    "1a"   : t1a,
    "1aa"  : t1aa,
    "1ab"  : t1ab,

    "1b" : t1b,
    "1ba" : t1ba,
    "1bb" : t1bb,
    "1bc" : t1bc
} 

