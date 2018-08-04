import pygame_setup as pg
import pygame, os, time

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BOARDBROWN = (117,57,4)
BOARDWHITE = (255,228,196)

current_directory = os.getcwd()
    
class BoardCell():
    def __init__(self):
        self.Color = None
        self.ContainedPiece = None
        self.X = 0
        self.Y = 0
        self.Width = 50
        self.Height = 50

    def SetX(self,x):
        self.X = x
    def SetY(self,y):
        self.Y = y
    def GetWidth(self):
        return self.Width
    def GetHeight(self):
        return self.Height
    def GetX(self):
        return self.X
    def GetY(self):
        return self.Y
        
    def SetColor(self,color):
        self.Color = color
    def ShowCell(self):
        return pygame.draw.rect(app.getScreen(),self.Color,(self.X,self.Y,self.Width,self.Height),0)

    def SetContainedPiece(self,ChessPiece):
        self.ContainedPiece = ChessPiece

    def GetContainedPiece(self):
        return self.ContainedPiece
        
    def ShowContainedPiece(self):
        if self.ContainedPiece != None:
            self.ContainedPiece.ShowPiece(self.X,self.Y)

class Piece():
    def __init__(self,color):
        self.Color = color
        self.PieceImage = pygame.image.load("{}//Images//{}.png".format(current_directory,self.Name+self.Color))
        self.PieceImage = pygame.transform.scale(self.PieceImage,(45,45))

    def ShowPiece(self,x,y):
        app.getScreen().blit(self.PieceImage,(x,y))
    def GetName(self):
        return self.Name
    def GetColor(self):
        return self.Color
        
class Pawn(Piece):
    def __init__(self,color):
        self.Name = "Pawn"
        self.HasBeenMoved = False
        Piece.__init__(self,color)

    def SetHasBeenMoved(self):
        self.HasBeenMoved = True
    
    def GetDestinations(self,PlayerTurn,CurrentCell):
        x,y = GetIndexFromCell(CurrentCell)
        ValidMoves = []
        #Moves - [YOffset,XOffset]
        BlackClearMoves = [[-1,0]]
        WhiteClearMoves = [[1,0]]
        if self.HasBeenMoved == False:
            BlackClearMoves.append([-2,0])
            WhiteClearMoves.append([2,0])
        if PlayerTurn == "Black":
            for PotentialMove in BlackClearMoves:
                try:
                    if Board[x+PotentialMove[0]][y+PotentialMove[1]].GetContainedPiece() == None:
                        ValidMoves.append(Board[x+PotentialMove[0]][y+PotentialMove[1]])
                except:
                    pass
        elif PlayerTurn == "White":
            for PotentialMove in WhiteClearMoves:
                try:
                    if Board[x+PotentialMove[0]][y+PotentialMove[1]].GetContainedPiece() == None:
                        ValidMoves.append(Board[x+PotentialMove[0]][y+PotentialMove[1]])
                except:
                    pass

        BlackTakeMoves = [[-1,-1],[-1,1]]
        WhiteTakeMoves = [[1,-1],[1,1]]
        if PlayerTurn == "Black":
            for PotentialMove in BlackTakeMoves:
                try:
                    if Board[x+PotentialMove[0]][y+PotentialMove[1]].GetContainedPiece() != None:
                        if Board[x+PotentialMove[0]][y+PotentialMove[1]].GetContainedPiece().GetColor() != PlayerTurn:
                            ValidMoves.append(Board[x+PotentialMove[0]][y+PotentialMove[1]])
                except:
                    pass
        elif PlayerTurn == "White":
            for PotentialMove in WhiteTakeMoves:
                try:
                    if Board[x+PotentialMove[0]][y+PotentialMove[1]].GetContainedPiece() != None:
                        if Board[x+PotentialMove[0]][y+PotentialMove[1]].GetContainedPiece().GetColor() != PlayerTurn:
                            ValidMoves.append(Board[x+PotentialMove[0]][y+PotentialMove[1]])
                except:
                    pass
            
        return ValidMoves

class Rook(Piece):
    def __init__(self,color):
        self.Name = "Rook"
        Piece.__init__(self,color)

    def GetDestinations(self,PlayerTurn,CurrentCell):
        ValidMoves = []
        Staggers = [[0,1],[1,0],[0,-1],[-1,0]]
        for Stagger in Staggers:
            NextSquare = True
            TempCurrentCell = CurrentCell
            while NextSquare == True:
                x,y = GetIndexFromCell(TempCurrentCell)
                if x+Stagger[0] >=0 and y+Stagger[1] >=0:
                    try:
                        if Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece() == None:
                            ValidMoves.append(Board[x+Stagger[0]][y+Stagger[1]])
                            TempCurrentCell = Board[x+Stagger[0]][y+Stagger[1]]
                        elif Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece() != None:
                            if Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece().GetColor() != PlayerTurn:
                                ValidMoves.append(Board[x+Stagger[0]][y+Stagger[1]])
                                NextSquare = False
                            elif Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece().GetColor() == PlayerTurn:
                                NextSquare = False
                    except:
                        NextSquare = False
                else:
                    NextSquare = False
        return ValidMoves
        

class Knight(Piece):
    def __init__(self,color):
        self.Name = "Knight"
        Piece.__init__(self,color)

    def GetDestinations(self,PlayerTurn,CurrentCell):
        ValidMoves = []
        Staggers = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
        x,y = GetIndexFromCell(CurrentCell)
        for Stagger in Staggers:
            if x+Stagger[0] >=0 and y+Stagger[1] >=0:
                try:
                    if Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece() == None:
                        ValidMoves.append(Board[x+Stagger[0]][y+Stagger[1]])
                    elif Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece() != None:
                        if Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece().GetColor() != PlayerTurn:
                            ValidMoves.append(Board[x+Stagger[0]][y+Stagger[1]])
                        elif Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece().GetColor() == PlayerTurn:
                            pass
                except:
                    pass
            else:
                pass
        return ValidMoves

class Bishop(Piece):
    def __init__(self,color):
        self.Name = "Bishop"
        Piece.__init__(self,color)

    def GetDestinations(self,PlayerTurn,CurrentCell):
        ValidMoves = []
        Staggers = [[1,1],[1,-1],[-1,-1],[-1,1]]
        for Stagger in Staggers:
            NextSquare = True
            TempCurrentCell = CurrentCell
            while NextSquare == True:
                x,y = GetIndexFromCell(TempCurrentCell)
                if x+Stagger[0] >=0 and y+Stagger[1] >=0:
                    try:
                        if Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece() == None:
                            ValidMoves.append(Board[x+Stagger[0]][y+Stagger[1]])
                            TempCurrentCell = Board[x+Stagger[0]][y+Stagger[1]]
                        elif Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece() != None:
                            if Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece().GetColor() != PlayerTurn:
                                ValidMoves.append(Board[x+Stagger[0]][y+Stagger[1]])
                                NextSquare = False
                            elif Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece().GetColor() == PlayerTurn:
                                NextSquare = False
                    except:
                        NextSquare = False
                else:
                    NextSquare = False
        return ValidMoves

class King(Piece):
    def __init__(self,color):
        self.Name = "King"
        self.HasBeenMoved = False
        Piece.__init__(self,color)

    def SetHasBeenMoved(self):
        self.HasBeenMoved = True

    def GetDestinations(self,PlayerTurn,CurrentCell):
        ValidMoves = []
        Staggers = [[1,1],[1,-1],[-1,-1],[-1,1],[0,1],[1,0],[0,-1],[-1,0]]
        x,y = GetIndexFromCell(CurrentCell)
        for Stagger in Staggers:
            if x+Stagger[0] >=0 and y+Stagger[1] >=0:
                try:
                    if Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece() == None:
                        ValidMoves.append(Board[x+Stagger[0]][y+Stagger[1]])
                    elif Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece() != None:
                        if Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece().GetColor() != PlayerTurn:
                            ValidMoves.append(Board[x+Stagger[0]][y+Stagger[1]])
                        elif Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece().GetColor() == PlayerTurn:
                            pass
                except:
                    pass
            else:
                pass
        y,x = GetIndexFromCell(CurrentCell)
        if self.HasBeenMoved == False:
            if Board[y][0].GetContainedPiece() != None:
                if Board[y][0].GetContainedPiece().GetName() == "Rook":
                    ClearLeft = True
                    for i in range(1,x):
                        if Board[y][i].GetContainedPiece() != None:
                            ClearLeft = False
                            break
                    if ClearLeft == True:
                        ValidMoves.append(Board[y][x-2])
            if Board[y][7].GetContainedPiece() != None:
                if Board[y][7].GetContainedPiece().GetName() == "Rook":
                    ClearRight = True
                    for i in range(x+1,7):
                        if Board[y][i].GetContainedPiece() != None:
                            ClearRight = False
                            break
                    if ClearRight == True:
                        ValidMoves.append(Board[y][x+2])
        return ValidMoves

class Queen(Piece):
    def __init__(self,color):
        self.Name = "Queen"
        Piece.__init__(self,color)

    def GetDestinations(self,PlayerTurn,CurrentCell):
        ValidMoves = []
        Staggers = [[1,1],[1,-1],[-1,-1],[-1,1],[0,1],[1,0],[0,-1],[-1,0]]
        for Stagger in Staggers:
            NextSquare = True
            TempCurrentCell = CurrentCell
            while NextSquare == True:
                x,y = GetIndexFromCell(TempCurrentCell)
                if x+Stagger[0] >=0 and y+Stagger[1] >=0:
                    try:
                        if Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece() == None:
                            ValidMoves.append(Board[x+Stagger[0]][y+Stagger[1]])
                            TempCurrentCell = Board[x+Stagger[0]][y+Stagger[1]]
                        elif Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece() != None:
                            if Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece().GetColor() != PlayerTurn:
                                ValidMoves.append(Board[x+Stagger[0]][y+Stagger[1]])
                                NextSquare = False
                            elif Board[x+Stagger[0]][y+Stagger[1]].GetContainedPiece().GetColor() == PlayerTurn:
                                NextSquare = False
                    except:
                        NextSquare = False
                else:
                    NextSquare = False
        return ValidMoves


class PlayerClass():
    def __init__(self,PlayerColor):
        self.PlayerColor = PlayerColor
        self.TimePlayed = 0
        self.InCheck = False

    def GetPlayerColor(self):
        return self.PlayerColor
    def SetInCheck(self,NewStatus):
        self.InCheck = NewStatus
    def GetInCheck(self):
        return self.InCheck
    def IsInCheck(self):
        if self.PlayerColor == "Black":
            OtherPlayerColor = "White"
        else:
            OtherPlayerColor = "Black"
        for i in range(8):
            for j in range(8):
                Piece = Board[i][j].GetContainedPiece()
                if Piece != None:
                    if Piece.GetColor() != self.PlayerColor and Piece.GetName() != "King":
                        Destinations = Piece.GetDestinations(OtherPlayerColor,Board[i][j])
                        for Dest in Destinations:
                            if Dest.GetContainedPiece() != None:
                                if Dest.GetContainedPiece().GetName() == "King":
                                    if Dest.GetContainedPiece().GetColor() == self.PlayerColor:
                                        return True
        return False

class GameClass():
    def __init__(self):
        self.Turn = "White"
    def SwitchTurn(self):
        if self.Turn == "White":
            self.Turn = "Black"
        else:
            self.Turn = "White"
    def GetTurn(self):
        return self.Turn

#__________________________________#
def SetBoard():
    Count = 0
    for i in range(8):
        for j in range(8):
            if Count%2 == 0:
                if i%2==0:
                    Board[i][j].SetColor(BOARDWHITE)
                else:
                    Board[i][j].SetColor(BOARDBROWN)
            else:
                if i%2 == 0:
                    Board[i][j].SetColor(BOARDBROWN)
                else:
                    Board[i][j].SetColor(BOARDWHITE)
            Board[i][j].SetX(Count*Board[i][j].GetWidth())
            Board[i][j].SetY(i*Board[i][j].GetHeight())
            Count = (Count + 1) % 8
            
def SetPieces(filename):
    LoadBoard = []
    file = open(filename,'r')
    for row in file.readlines():
        LoadBoard.append(row.strip().split(','))
    for i in range(8):
        for k in range(8):
            if LoadBoard[i][k] != 'XX':
                Piece = LoadBoard[i][k]
                Color = GetColor(Piece[1])
                if Piece[0] == "P":
                    Board[i][k].SetContainedPiece(Pawn(Color))
                elif Piece[0] == "R":
                    Board[i][k].SetContainedPiece(Rook(Color))
                elif Piece[0] == "N":
                    Board[i][k].SetContainedPiece(Knight(Color))
                elif Piece[0] == "B":
                    Board[i][k].SetContainedPiece(Bishop(Color))
                elif Piece[0] == "K":
                    Board[i][k].SetContainedPiece(King(Color))
                elif Piece[0] == "Q":
                    Board[i][k].SetContainedPiece(Queen(Color))

def GetColor(Color):
    if Color == "W":
        return "White"
    else:
        return "Black"

def ShowBoard():
    for i in range(8):
        for j in range(8):
            Board[i][j].ShowCell()
def ShowPieces():
    for i in range(8):
        for j in range(8):
            if Board[i][j].GetContainedPiece() != None:
                Board[i][j].ShowContainedPiece()
def GetIndexFromCell(Cell):
    for i in range(8):
        for j in range(8):
            if Board[i][j] == Cell:
                return i,j
#__________________________________#
def Turn(Player):
    CanMove = GetCanMove(Player.GetPlayerColor())
    if not CanMove:
        return
    if Player.IsInCheck() == True:
        CheckMate = InCheckMate(Player,Player.GetPlayerColor())
        if CheckMate:
            print("Check mate")
            return "Game Over"
        else:
            Render(Check=True)
            print("Check")

    ValidPiece = False
    while not ValidPiece:
        PieceCell = SelectPiece()
        Piece = PieceCell.GetContainedPiece()
        if Piece.GetColor() == Player.GetPlayerColor():
            ValidPiece = True
    ValidMoves = Piece.GetDestinations(Player.GetPlayerColor(),PieceCell)
    ValidMoves = FilterUnCheckMoves(PieceCell,ValidMoves,Player)
    if Player.IsInCheck() == True:
        ValidMoves = FilterUnCheckMoves(PieceCell,ValidMoves,Player)
    if len(ValidMoves) == 0:
        print("No valid moves for that piece")
        return Turn(Player)
    else:
        Render(True,ValidMoves,Check=Player.IsInCheck())
        ValidDest = False
        DestCell = SelectDest()
        if DestCell not in ValidMoves:
            Render(Check=Player.IsInCheck())
            return Turn(Player)
        else:
            if Piece.GetName() == "Pawn" or Piece.GetName() == "King":
                Piece.SetHasBeenMoved()
            if Piece.GetName() == "King":
                SY, SX = GetIndexFromCell(PieceCell)
                DY, DX = GetIndexFromCell(DestCell)
                if abs(SX-DX) != 1:
                    CastleSwap(PieceCell,DestCell)
                else:
                    Move(PieceCell,DestCell)
            else:
                Move(PieceCell,DestCell)
    
def SelectPiece():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app.exit()
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i in range(8):
                    for j in range(8):
                        Cell = Board[i][j]
                        if Cell.ShowCell().collidepoint(mx,my):
                            if Cell.GetContainedPiece() != None:
                                print(Cell.GetContainedPiece().GetName())
                                return Cell
def SelectDest():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app.exit()
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i in range(8):
                    for j in range(8):
                        Cell = Board[i][j]
                        if Cell.ShowCell().collidepoint(mx,my):
                            return Cell

def Move(Source,Dest):
    Dest.SetContainedPiece(Source.GetContainedPiece())
    Source.SetContainedPiece(None)

def CastleSwap(SourceKing,Dest):
    DY, DX = GetIndexFromCell(Dest)
    KY, KX = GetIndexFromCell(SourceKing)
    if DX < KX:
        SourceCastle = Board[KY][0]
    else:
        SourceCastle = Board[KY][7]
    CY, CX = GetIndexFromCell(SourceCastle)
    if abs(KX-CX) == 4:
        Board[KY][KX+2].SetContainedPiece(SourceKing.GetContainedPiece())
        Board[CY][CX-3].SetContainedPiece(SourceCastle.GetContainedPiece())
    else:
        Board[KY][KX-2].SetContainedPiece(SourceKing.GetContainedPiece())
        Board[CY][CX+2].SetContainedPiece(SourceCastle.GetContainedPiece())
        print(Board[KY][KX-2].GetContainedPiece().GetName())
    SourceKing.SetContainedPiece(None)
    SourceCastle.SetContainedPiece(None)

def GetCanMove(PlayerTurn):
    for i in range(8):
        for j in range(8):
            Piece = Board[i][j].GetContainedPiece()
            if Piece != None:
                if Piece.GetColor() == PlayerTurn:
                    ValidMoves = Piece.GetDestinations(PlayerTurn,Board[i][j])
                    if len(ValidMoves) > 0:
                        return True
    return False

def InCheckMate(Player,PlayerTurn):
    for i in range(8):
        for j in range(8):
            Piece = Board[i][j].GetContainedPiece()
            if Piece != None:
                #if Piece.GetName() == "King":
                if Piece.GetColor() == PlayerTurn:
                    ValidMoves = Piece.GetDestinations(PlayerTurn,Board[i][j])
                    ValidMoves = FilterUnCheckMoves(Board[i][j],ValidMoves,Player)
                    if len(ValidMoves) != 0:
                        return False
    return True

def FilterUnCheckMoves(Source,ValidMoves,Player):
    NewValidMoves = []
    for Dest in ValidMoves:
        TempTaken = None
        if Dest.GetContainedPiece() != None:
            TempTaken = Dest.GetContainedPiece()
        Move(Source,Dest)
        if Player.IsInCheck() == False:
            NewValidMoves.append(Dest)
        Move(Dest,Source)
        if TempTaken != None:
            Dest.SetContainedPiece(TempTaken)
    return NewValidMoves    
#__________________________________#
def Render(ShowValidDests=False,ValidDests=[],Check=False,Checkmate=False):
    app.getScreen().fill(WHITE)
    ShowBoard()
    ShowPieces()
    if ShowValidDests == True:
        for Cell in ValidDests:
            pygame.draw.circle(app.getScreen(),GREEN,(Cell.GetX()+(Cell.GetWidth()//2),Cell.GetY()+(Cell.GetHeight()//2)),5)
    if Game.GetTurn() == "White":
        PlayerOneColor = GREEN
        PlayerTwoColor = BLACK
    elif Game.GetTurn() == "Black":
        PlayerOneColor = BLACK
        PlayerTwoColor = GREEN
    pg.renderText("White",20,PlayerOneColor,25,app.getHeight()-35,app.getScreen())
    pg.renderText("Black",20,PlayerTwoColor,app.getWidth()-75,app.getHeight()-35,app.getScreen())
    if Check == True and Checkmate == False:
        pg.renderText("Check",20,RED,(app.getWidth()//2)-50,app.getHeight()-35,app.getScreen())
    elif Checkmate == True:
        pg.renderText("Checkmate",20,RED,(app.getWidth()//2)-75,app.getHeight()-35,app.getScreen())
    pygame.display.update()
    app.Tick()

def Events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app.exit()

def Main():
    GameOver = False
    app.begin()
    SetBoard()
    SetPieces('default.txt')
    while not GameOver:
        Render()
        if Game.GetTurn() == "White":
            Status = Turn(PlayerOne)
        else:
            Status = Turn(PlayerTwo)
        if Status == "Game Over":
            GameOver = True
        Game.SwitchTurn()
    while True:
        Render(Check=True,Checkmate=True)
        Events()
    
if __name__ == "__main__":
    app = pg.App(400,450,16,"Chess")
    Board = [[BoardCell() for i in range(8)] for dimensions in range(8)]
    Game = GameClass()
    PlayerOne = PlayerClass("White")
    PlayerTwo = PlayerClass("Black")
    Main()
