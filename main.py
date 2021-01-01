import matplotlib.pyplot as plt
from Examples import *
from variables import *
pygame.init()

button_text = pygame.font.SysFont('Comic Sans MS', 20)


ex = Examples()
e = ex.generate(4000)
x_min = np.min(e[0])
x_max = np.max(e[0])
x_train = (np.array(e[0]) - x_min) / (x_max - x_min) * 0.8 + 0.1
y_train = np.array(e[1]) / np.pi * 0.8 + 0.1
NN = Neural_Network()
screen.fill(WHITE)
pygame.display.flip()

while running:
    screen.blit(robot_img, (0, 0))
    learn_text = button_text.render(learn_button_text, False, (0, 0, 0))
    learn_button = pygame.draw.rect(screen, (200, 200, 200), (screen.get_width()/2-32, 360, 64, 32))
    screen.blit(learn_text, learn_button)

    pygame.draw.line(screen, BLACK, (0, 351), (450, 351), width=1)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 0 <= pygame.mouse.get_pos()[1] <= 350:
                screen.fill(WHITE)
                pygame.draw.circle(screen, (255, 0, 0), (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]), 4)
                clicked_x = pygame.mouse.get_pos()[0] - img_width
                clicked_y = pygame.mouse.get_pos()[1] - img_height / 2
                clicked_y *= -1.0
                clicked_x = (clicked_x + arm_length * 2) / (arm_length * 4)
                clicked_x *= 0.8 + 0.1
                clicked_y = (clicked_y + arm_length * 2) / (arm_length * 4)
                clicked_y *= 0.8 + 0.1

                predicted_angles = NN.forward((clicked_x, clicked_y))

                arm_pts = find_line_points(predicted_angles[0], predicted_angles[1])
                pygame.draw.line(screen, BLACK, (img_width, img_height / 2), (arm_pts[0].x, arm_pts[0].y), width=3)
                pygame.draw.line(screen, BLACK, (arm_pts[0].x, arm_pts[0].y), (arm_pts[1].x, arm_pts[1].y), width=3)
            if 360 <= pygame.mouse.get_pos()[1] <= 392 and (screen.get_width()/2-32) <= pygame.mouse.get_pos()[0] <= (screen.get_width()/2+32):
                for i in range(20000):
                    NN.train(x_train, y_train)
                err = NN.errors
                plt.plot(range(len(err)), err)
                plt.savefig('errors.png')

                fig, ax = plt.subplots()
                ax.axis('equal')
                for (x, y) in e[0]:
                    plt.scatter(x, y, marker='o')
                plt.savefig('e_0.png')

                fig, ax = plt.subplots()
                ax.axis('equal')
                for (x, y) in e[1]:
                    plt.scatter(x, y, marker='o')
                plt.savefig('e_1.png')
                learn_button_text = "LEARNED!"
