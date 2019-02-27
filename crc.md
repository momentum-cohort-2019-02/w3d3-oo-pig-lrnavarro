
classes
    GAME
        needs or contains
            START GAME
            PLAYERS
            DETERMINE WINNER
            DETERMINE WHOSE TURN IT IS
            VIRTUAL DICE
            TOTAL SCORE
        interacts with
            PLAYER 1
            COMPUTER PLAYER

    PLAYER 1
        needs or contains
            PER PLAYER SCORE
            PER ROUND SCORE
            POSSIBLE POINTS
            TURN
            DICE ROLL
            CHOICE TO ROLL OR HOLD
        interacts with
            GAME
            COMPUTER PLAYER

    COMPUTER PLAYER
        needs or contains
            PER PLAYER SCORE
            PER ROUND SCORE
            POSSIBLE POINTS
            TURN
            DICE ROLL
            CHOICE TO ROLL OR HOLD (?WHILE PER ROUND SCORE <20 AND IF PER ROUND SCORE >=20?)

        

    

    