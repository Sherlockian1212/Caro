import pygame
from random import randint

pygame.init()

pygame.display.update

#tạo cửa sổ chương trình
screen = pygame.display.set_mode((500,500))

#đặt tiêu đề
pygame.display.set_caption('Caro Ver-1.0')

#gán giá trị màu
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = '#FF0000'

#load hình quân cờ X O
img_O = pygame.image.load('O.png')
img_X = pygame.image.load('X.png')
 
#đặt biến quản lí cửa sổ
in_main = True
in_play_with_robot = False
in_play_two_people = False

map = [[0,0,0],[0,0,0],[0,0,0]] #khởi tạo map
turn = 1 #lượt chơi đầu tiên

running = True #biến running cho toàn bộ chương trình

#hàm viết chữ
def drawText(text, size, color, x, y):
    font = pygame.font.SysFont('comicsansms',size)
    draw_text = font.render(text, True, color) 
    screen.blit(draw_text, (x,y)) 

#hàm tạo hiệu ứng rê chuột lên bàn cờ
def animation(mouse_x, mouse_y):
    if turn == 1:
        img = img_X
    else:
        img = img_O
    if (100 < mouse_x and mouse_x < 200):
        if (150 < mouse_y and mouse_y < 250) and map[0][0] == 0:
            screen.blit(img, (105,160))
            #print ('0:0')
        if (250 < mouse_y and mouse_y < 350) and map[1][0] == 0:
            screen.blit(img, (105,255))
            #print ('1:0')
        if (350 < mouse_y and mouse_y < 450) and map[2][0] == 0:
            screen.blit(img, (105,350))
            #print ('2:0')
    if (200 < mouse_x and mouse_x < 300):
        if (150 < mouse_y and mouse_y < 250) and map[0][1] == 0:
            screen.blit(img, (205,160))
            #print ('0:1')
        if (250 < mouse_y and mouse_y < 350) and map[1][1] == 0:
            screen.blit(img, (205,255))
            #print ('1:1')
        if (350 < mouse_y and mouse_y < 450) and map[2][1] == 0:
            screen.blit(img, (205,350))
            #print ('2:1')
    if (300 < mouse_x and mouse_x < 400):
        if (150 < mouse_y and mouse_y < 250) and map[0][2] == 0:
            screen.blit(img, (300,160))
            #print ('0:2')
        if (250 < mouse_y and mouse_y < 350) and map[1][2] == 0:
            screen.blit(img, (300,255))
            #print ('1:2')
        if (350 < mouse_y and mouse_y < 450) and map[2][2] == 0:
            screen.blit(img, (300,350))
            #print ('2:2') 

#hàm tạo hiệu ứng khi đến lượt người chơi đi
def animationTurn():
    if turn == 1:
        pygame.draw.rect(screen, RED, (100, 50, 125, 70),5, 10 ) #khung player 1
        drawText('Player 1', 30, RED, 108,55)
    elif turn == 2:
        pygame.draw.rect(screen, RED, (275, 50, 125, 70),5, 10 ) #khung player 2
        drawText('Player 2', 30, RED, 283, 55) 

#hàm vẽ cảnh chính    
def main():
    pygame.draw.rect(screen, BLACK, (100, 100, 300, 100),5, 10) #chơi 2 người
    pygame.draw.rect(screen, BLACK, (100, 300, 300, 100),5, 10) #chơi với máy

    drawText('2 players', 40, BLACK, 170, 120)
    drawText('Play with robot', 40, BLACK, 110, 320)

#hàm vẽ cảnh chơi với máy
def playWithRobot():
    pygame.draw.rect(screen, BLACK, (5,5,70,50), 5, 10) #back
    pygame.draw.rect(screen, BLACK, (5,60,70,50), 5, 10) #reset
    pygame.draw.rect(screen, BLACK, (100, 150, 300, 300),5, 10) #viền ngoài
    pygame.draw.rect(screen, BLACK, (100, 50, 125, 70),5, 10 ) #khung player
    pygame.draw.rect(screen, BLACK, (275, 50, 125, 70),5, 10 ) #khung robot
    pygame.draw.line(screen, BLACK, (120, 250), (380, 250), 3) #thanh ngang 1
    pygame.draw.line(screen, BLACK, (120, 350), (380, 350), 3) #thanh ngang 2
    pygame.draw.line(screen, BLACK, (200, 170), (200, 430), 3) #thanh dứng 1
    pygame.draw.line(screen, BLACK, (300, 170), (300, 430), 3) #thanh đứng 2

    drawText('Player 1', 30, BLACK, 108,55)
    drawText('Robot', 30, BLACK, 300, 55)
    drawText('Back',20, BLACK, 15, 10)
    drawText('Reset',20, BLACK,12,70)

#hàm vẽ cảnh chơi 2 người
def playTwoPeople():
    pygame.draw.rect(screen, BLACK, (5,5,70,50), 5, 10) #back
    pygame.draw.rect(screen, BLACK, (5,60,70,50), 5, 10) #reset
    pygame.draw.rect(screen, BLACK, (100, 150, 300, 300),5, 10) #viền ngoài
    pygame.draw.rect(screen, BLACK, (100, 50, 125, 70),5, 10 ) #khung player 1
    pygame.draw.rect(screen, BLACK, (275, 50, 125, 70),5, 10 ) #khung player 2
    pygame.draw.line(screen, BLACK, (120, 250), (380, 250), 3) #thanh ngang 1
    pygame.draw.line(screen, BLACK, (120, 350), (380, 350), 3) #thanh ngang 2
    pygame.draw.line(screen, BLACK, (200, 170), (200, 430), 3) #thanh dứng 1
    pygame.draw.line(screen, BLACK, (300, 170), (300, 430), 3) #thanh đứng 2

    drawText('Player 1', 30, BLACK, 108,55)
    drawText('Player 2', 30, BLACK, 283, 55)
    drawText('Back',20, BLACK, 15, 10)
    drawText('Reset',20, BLACK,12,70)

#hàm vẽ lên màn hình từ vị trí của map
def drawChessboard():
    i = 0
    j = 0
    for i in range (3):
        for j in range (3):
            if map[i][j] == 1:
                screen.blit(img_X , (posChange(j,'y'),posChange(i,'x')))
            elif map[i][j] == 2:
                screen.blit(img_O , (posChange(j,'y'),posChange(i,'x')))    

#hàm chuyển vị trí trong map ra màn hình, phục vụ việc vẽ lên màn hình từ vị trí của map
def posChange(number, type):
    if type == 'y':
        if number == 0:
            return 105
        if number == 1:
            return 205
        if number == 2:
            return 300   
    elif type == 'x':
        if number == 0:
            return 160
        if number == 1:
            return 255
        if number == 2:
            return 350  

#hàm ghi nhận vị trí từ chuột ánh xạ lên map
def addPoint(x, y, player_number):
    if map[x][y] == 0:
        map[x][y] = player_number
        return True
    return False    

#hàm kiểm tra trận hòa
def checkDraw():
    i = 0
    j = 0
    count = 0
    for i in range(3):
        for j in range(3):
            if map[i][j] != 0:
                count = count + 1
    if count == 9:            
        return True
    else:
        return False    

#hàm kiểm tra người chơi thắng chưa
def checkWin(player_number):
    i = 0
    j = 0
    for i in range(3):
        if map[i][0] == map[i][1] and map[i][0] == map[i][2] and map[i][0] == player_number:
            return True
    for j in range(3):
        if map[0][j] == map[1][j] and map[0][j] == map[2][j] and map[0][j] == player_number:
            return True 
    if map[0][0] == map[1][1] and map[0][0] == map[2][2] and map[0][0] == player_number:
        return True
    if map[0][2] == map[1][1] and map[0][2] == map[2][0] and map[0][2] == player_number:
        return True 
    return False

#hàm sinh ra nước đi của máy
def robot():
    endturn = False
    if not endturn:
        x = 0
        y = 0
        i = 0
        j = 0
        count = 0  
        #xác định máy đã đi 2 ô hàng ngang và đánh vào ô còn lại đề thắng nếu ô đó trống                             
        for i in range(3):
            for j in range(3):
                if map[i][j] == 2:
                    count = count + 1    
            if count == 2:
                for j in range(3):
                    if map[i][j] == 0: 
                        y = j 
                        x = i
                        map[x][y] = 2
                        endturn = True
                        return endturn
            count = 0
        i = 0
        j = 0
        #xác định máy đã đi 2 ô hàng dọc và đánh vào ô còn lại để thắng nếu ô đó trống
        for j in range(3):
            for i in range(3):
                if map[i][j] == 2:
                    count = count + 1    
            if count == 2:
                for i in range(3):
                    if map[i][j] == 0: 
                        x = i
                        y = j   
                        map[x][y] = 2
                        endturn = True 
                        return endturn
            count = 0
        i = 0
        #xác định máy đã đi 2 ô đường chéo dấu huyền và đánh vào ô còn lại nếu ô đó trống
        for i in range (3):
            if map[i][i] == 2:
                count = count + 1
        if count == 2:
            for i in range(3):
                if map[i][i] == 0: 
                    x = i
                    y = i   
                    map[x][y] = 2
                    endturn = True 
                    return endturn
        count = 0    
        i = 0
        #xác định máy đã đi 2 ô đường chéo dấu sắc và đánh vào ô còn lại nếu ô đó trống
        for i in range (3):
            if map[i][2-i] == 2:
                count = count + 1
        if count == 2:
            for i in range(3):
                if map[i][2-i] == 0: 
                    x = i
                    y = 2-i  
                    map[x][y] = 2
                    endturn = True 
                    return endturn
        count = 0        
        i = 0
        j = 0
        #xác định người chơi đã đi 2 ô hàng ngang và đánh vào ô còn lại đề thắng nếu ô đó trống
        for i in range(3):
            for j in range(3):
                if map[i][j] == 1:
                    count = count + 1    
            if count == 2:
                for j in range(3):
                    if map[i][j] == 0: 
                        y = j 
                        x = i
                        map[x][y] = 2
                        endturn = True
                        return endturn
            count = 0
        i = 0
        j = 0    
        #xác định người chơi đã đi 2 ô hàng dọc và đánh vào ô còn lại đề thắng nếu ô đó trống
        for j in range(3):
            for i in range(3):
                if map[i][j] == 1:
                    count = count + 1    
            if count == 2:
                for i in range(3):
                    if map[i][j] == 0: 
                        x = i
                        y = j   
                        map[x][y] = 2
                        endturn = True 
                        return endturn
            count = 0
        i = 0
        #xác định người chơi đã đi 2 ô đường chéo dấu huyền và đánh vào ô còn lại nếu ô đó trống
        for i in range (3):
            if map[i][i] == 1:
                count = count + 1
        if count == 2:
            for i in range(3):
                if map[i][i] == 0: 
                    x = i
                    y = i   
                    map[x][y] = 2
                    endturn = True 
                    return endturn
        count = 0
        i = 0
        #xác định người chơi đã đi 2 ô đường chéo dấu sắc và đánh vào ô còn lại nếu ô đó trống
        for i in range (3):
            if map[i][2-i] == 1:
                count = count + 1
        if count == 2:
            for i in range(3):
                if map[i][2-i] == 0: 
                    x = i
                    y = 2-i   
                    map[x][y] = 2
                    endturn = True 
                    return endturn
        count = 0    
    #sinh ngẫu nhiên vị trí tiếp theo   
    while not endturn:
        x = randint(0,2)
        y = randint(0,2)
        if map[x][y] == 0: 
            #print(x,y)  
            map[x][y] = 2
            endturn = True
            return endturn
    return endturn
   
while running:

    screen.fill(WHITE)

    #nhận vị trí chuột
    mouse_x, mouse_y = pygame.mouse.get_pos()
   
    if in_play_with_robot:
        playWithRobot()
        drawChessboard()
        if checkWin (1):
            #print('player 1 win')
            finish = True
            drawText('Player 1 win', 30, RED, 100, 5)
        elif checkWin (2):
            #print('player 2 win')
            finish = True
            drawText('Player 2 win', 30, RED, 100, 5)
        elif checkDraw():
            #print('draw')
            finish = True
            drawText('Draw', 30, RED, 100, 5)
        else:    
            if turn == 1:   
                animation(mouse_x, mouse_y)
            animationTurn()
        if turn == 2 and not finish:
            if robot():
                turn = 1   
            else:
                print('error')    
                turn = 1

    if in_play_two_people:
        playTwoPeople()
        drawChessboard()
        if checkWin (1):
            #print('player 1 win')
            finish = True
            drawText('Player 1 win', 30, RED, 100, 5)
        elif checkWin (2):
            #print('player 2 win')
            finish = True
            drawText('Player 2 win', 30, RED, 100, 5)
        elif checkDraw():
            #print('draw')
            finish = True
            drawText('Draw', 30, RED, 100, 5)
        else:       
            animation(mouse_x, mouse_y)
            animationTurn()
    
    if in_main:
        main()
        map = [[0,0,0],[0,0,0],[0,0,0]]
        turn = 1
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #nếu click chuột trái
                if in_main:
                    if (100 <= mouse_x and mouse_x <=400 and 100 <= mouse_y and mouse_y <= 200 ):
                        in_main = False
                        in_play_with_robot = False
                        in_play_two_people = True
                        finish = False
                    if (100 <= mouse_x and mouse_x <=400 and 300 <= mouse_y and mouse_y <= 400 ):
                        in_main = False
                        in_play_with_robot = True   
                        in_play_two_people = False  
                        finish = False  
                elif (5 <= mouse_x and mouse_x <=75 and 5 <= mouse_y and mouse_y <= 55 ): #click vào nút back
                    in_main = True
                    in_play_with_robot = False  
                    in_play_two_people = False
                elif (5 <= mouse_x and mouse_x <=75 and 60 <= mouse_y and mouse_y <= 110): #click vào nút reset
                    map = [[0,0,0],[0,0,0],[0,0,0]]
                    turn = 1
                    finish = False
                elif in_play_two_people and not finish:
                    if (100 < mouse_x and mouse_x < 200):
                        if (150 < mouse_y and mouse_y < 250):
                            if  addPoint(0,0,turn):
                                if turn == 1:
                                    turn = 2
                                else:
                                    turn = 1    
                        if (250 < mouse_y and mouse_y < 350):
                            if  addPoint(1,0,turn):
                                if turn == 1:
                                    turn = 2
                                else:
                                    turn = 1
                        if (350 < mouse_y and mouse_y < 450):
                            if  addPoint(2,0,turn):
                                if turn == 1:
                                    turn = 2
                                else:
                                    turn = 1
                    if (200 < mouse_x and mouse_x < 300):
                        if (150 < mouse_y and mouse_y < 250):
                            if  addPoint(0,1,turn):
                                if turn == 1:
                                    turn = 2
                                else:
                                    turn = 1
                        if (250 < mouse_y and mouse_y < 350):
                            if  addPoint(1,1,turn):
                                if turn == 1:
                                    turn = 2
                                else:
                                    turn = 1
                        if (350 < mouse_y and mouse_y < 450):
                            if  addPoint(2,1,turn):
                                if turn == 1:
                                    turn = 2
                                else:
                                    turn = 1
                    if (300 < mouse_x and mouse_x < 400):
                        if (150 < mouse_y and mouse_y < 250):
                            if  addPoint(0,2,turn):
                                if turn == 1:
                                    turn = 2
                                else:
                                    turn = 1
                        if (250 < mouse_y and mouse_y < 350):
                            if  addPoint(1,2,turn):
                                if turn == 1:
                                    turn = 2
                                else:
                                    turn = 1
                        if (350 < mouse_y and mouse_y < 450):
                            if  addPoint(2,2,turn):
                                if turn == 1:
                                    turn = 2
                                else:
                                    turn = 1
                elif in_play_with_robot and not finish:
                    if turn == 1:
                        if (100 < mouse_x and mouse_x < 200):
                            if (150 < mouse_y and mouse_y < 250):
                                if  addPoint(0,0,turn):
                                    turn = 2
                            if (250 < mouse_y and mouse_y < 350):
                                if  addPoint(1,0,turn):
                                   turn = 2
                            if (350 < mouse_y and mouse_y < 450):
                                if  addPoint(2,0,turn):
                                    turn = 2
                        if (200 < mouse_x and mouse_x < 300):
                            if (150 < mouse_y and mouse_y < 250):
                                if  addPoint(0,1,turn):
                                    turn = 2
                            if (250 < mouse_y and mouse_y < 350):
                                if  addPoint(1,1,turn):
                                    turn = 2
                            if (350 < mouse_y and mouse_y < 450):
                                if  addPoint(2,1,turn):
                                    turn = 2
                        if (300 < mouse_x and mouse_x < 400):
                            if (150 < mouse_y and mouse_y < 250):
                                if  addPoint(0,2,turn):
                                    turn = 2
                            if (250 < mouse_y and mouse_y < 350):
                                if  addPoint(1,2,turn):
                                    turn = 2
                            if (350 < mouse_y and mouse_y < 450):
                                if  addPoint(2,2,turn):
                                    turn = 2 
                    
    pygame.display.flip()

pygame.quit()            