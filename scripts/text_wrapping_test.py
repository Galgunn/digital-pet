import pygame, sys

pygame.init()

font = pygame.font.Font('freesansbold.ttf', 24)
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
messages = ['This is a message, no?', 
           'Another message is cool, no??',
           '^_^',
           'This is how a long message will be displayed here, IDK it might go on forever...']

""" This is the setup of the scrolling text"""
snip = font.render('', False, 'white') # Display the message, rn is empty
counter = 0
speed = 3
done = False
active_message = 0
message = messages[active_message]

running = True

while running:

    """Scrolling text continued"""
    if counter < speed * len(message):
        counter += 1
    elif counter >= speed * len(message):
        done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not done:
                counter = speed * len(message)
            elif event.key == pygame.K_SPACE and done and active_message < len(messages) - 1:
                active_message += 1
                done = False
                message = messages[active_message]
                counter = 0


    snip = font.render(message[0:counter//speed], True, 'white', None, 400)
    screen.blit(snip, (10, 310))

    # print(counter)

    print(counter//speed)

    print(font.size(message[0:counter//speed]))

    # if snip.get_width() > screen.get_width():
    #     screen.blit(snip, (10, 340))

    pygame.display.update()
    screen.fill('grey')
    pygame.draw.rect(screen, 'black', [0, 300, 400, 200])
    # pygame.draw.rect(screen, 'red', [0, 340, 400, 200])
    clock.tick(60)