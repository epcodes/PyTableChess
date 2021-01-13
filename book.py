import challenger
book = ["rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2", "rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2",
"r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3", "rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2",
"r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3", "rnbqkbnr/pp1ppppp/8/2p5/4P3/2N5/PPPP1PPP/R1BQKBNR b KQkq - 1 2",
"rnbqkbnr/ppp1pppp/8/3p4/4P3/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 2", "rnbqkb1r/ppp1pppp/3p1n2/8/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 1 3",
"rnbqkbnr/pp1ppppp/8/2p5/4P3/2P5/PP1P1PPP/RNBQKBNR b KQkq - 0 2", "rnbqkb1r/pppppppp/5n2/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 1 2",
"rnbqkbnr/pppp1ppp/8/4p3/4PP2/8/PPPP2PP/RNBQKBNR b KQkq f3 0 2", "r1bqkbnr/pppp1ppp/2n5/4p3/3PP3/5N2/PPP2PPP/RNBQKB1R b KQkq d3 0 3",
"rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR b KQkq c3 0 2", "rnbqkbnr/pp2pppp/2p5/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3",
"rnbqkb1r/pppppp1p/5np1/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3", "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/2N5/PP2PPPP/R1BQKBNR w KQkq - 2 4",
"rnbqkb1r/p1pp1ppp/1p2pn2/8/2PP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 0 4", "rnbqk2r/pppp1ppp/4pn2/8/1bPP4/5N2/PP2PPPP/RNBQKB1R w KQkq - 2 4",
"rnbqkb1r/ppp1pp1p/5np1/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq d6 0 4", "rnbqkbnr/ppppp1pp/8/5p2/3P4/8/PPP1PPPP/RNBQKBNR w KQkq f6 0 2",
"rnbqkb1r/pppppppp/5n2/6B1/3P4/8/PPP1PPPP/RN1QKBNR b KQkq - 2 2", "rnbqkb1r/p2ppppp/5n2/1ppP4/2P5/8/PP2PPPP/RNBQKBNR w KQkq b6 0 4",
"rnbqkb1r/ppp1pppp/5n2/3p4/3P1B2/5N2/PPP1PPPP/RN1QKB1R b KQkq - 3 3", "rnbqkb1r/pp3ppp/3p1n2/2pP4/8/2N5/PP2PPPP/R1BQKBNR w KQkq - 0 6",
"rnbqkb1r/pppp1ppp/4pn2/8/2PP4/6P1/PP2PP1P/RNBQKBNR b KQkq - 0 3", "rnbqkbnr/pppppppp/8/8/8/5N2/PPPPPPPP/RNBQKB1R b KQkq - 1 1",
"rnbqkbnr/pppppppp/8/8/2P5/8/PP1PPPPP/RNBQKBNR b KQkq c3 0 1", "rnbqkbnr/pppppppp/8/8/5P2/8/PPPPP1PP/RNBQKBNR b KQkq f3 0 1",
"rnbqkbnr/ppp1pppp/8/3p4/8/5NP1/PPPPPP1P/RNBQKB1R b KQkq - 0 2", "rnbqkbnr/pppppppp/8/8/8/6P1/PPPPPP1P/RNBQKBNR b KQkq - 0 1",
"rnbqkbnr/pppppppp/8/8/8/1P6/P1PPPPPP/RNBQKBNR b KQkq - 0 1", "rnbqkbnr/pppppppp/8/8/1P6/8/P1PPPPPP/RNBQKBNR b KQkq b3 0 1",
"rnbqkbnr/pppppppp/8/8/6P1/8/PPPPPP1P/RNBQKBNR b KQkq g3 0 1" 
]

def get_opening():
    fen = input("Input FEN from chess.com")
    if fen == book[0]:
        print("Sicilian Defense")
    elif fen == book[1]:
        print("French Defense")    
    elif fen == book[2]:
        print("Ruy López Opening")   
    elif fen == book[3]:
        print("Caro-Kann Defense")   
    elif fen == book[4]:
        print("Italian Game")   
    elif fen == book[5]:
        print("Sicilian Defense: Closed")   
    elif fen == book[6]:
        print("Scandinavian Defense")   
    elif fen == book[7]:
        print("Pirc Defense: 2.d4 Nf6")   
    elif fen == book[8]:
        print("Sicilian Defense: Alapin Variation")   
    elif fen == book[9]:
        print("Alekhine's Defense")                                   
    elif fen == book[10]:
        print("King's Gambit")   
    elif fen == book[11]:
        print("Scotch Game")   
    elif fen == book[12]:
        print("Queen's Gambit")   
    elif fen == book[13]:
        print("Slav Defense")   
    elif fen == book[14]:
        print("King's Indian Defense")   
    elif fen == book[15]:
        print("Nimzo-Indian Defense")   
    elif fen == book[16]:
        print("Queen's Indian Defense")   
    elif fen == book[17]:
        print("Bogo-Indian Defense") 
    elif fen == book[18]:
        print("Grünfeld Defense")   
    elif fen == book[19]:
        print("Dutch Defense")   
    elif fen == book[20]:
        print("Trompowsky Attack")   
    elif fen == book[21]:
        print("Benko Gambit")   
    elif fen == book[22]:
        print("London System")                                   
    elif fen == book[23]:
        print("Benoni Defense: Modern Variation, 4.Nc3 exd5 5.cxd5 d6")   
    elif fen == book[24]:
        print("Catalan Opening")   
    elif fen == book[25]:
        print("Réti Opening")   
    elif fen == book[26]:
        print("English Opening")   
    elif fen == book[27]:
        print("Bird's Opening")   
    elif fen == book[28]:
        print("King's Indian Attack")   
    elif fen == book[29]:
        print("King's Fianchetto Opening")   
    elif fen == book[30]:
        print("Nimzowitsch-Larsen Attack")    
    elif fen == book[31]:
        print("Polish Opening") 
    elif fen == book[32]:
        print("Grob Opening")
    else:
        print("Opening not found in book")
                                   

        

#get_opening()        
#print(book)

