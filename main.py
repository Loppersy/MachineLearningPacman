import pygame
import os

from Pacman import Pacman
from Pellet import Pellet
from PowerPellet import PowerPellet
from Wall import Wall

WIDTH, HEIGHT = 1080, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")
BLACK = (0, 0, 0)

SCALE = 22
FPS = 60

INKY_SHEET_IMAGE = pygame.image.load(os.path.join("assets", "inky.png")).convert_alpha()
PINKY_SHEET_IMAGE = pygame.image.load(os.path.join("assets", "pinky.png")).convert_alpha()
BLINKY_SHEET_IMAGE = pygame.image.load(os.path.join("assets", "blinky.png")).convert_alpha()
CLYDE_SHEET_IMAGE = pygame.image.load(os.path.join("assets", "clyde.png")).convert_alpha()
PACMAN_SHEET_IMAGE = pygame.image.load(os.path.join("assets", "pacman.png")).convert_alpha()
EYES_SHEET_IMAGE = pygame.image.load(os.path.join("assets", "eyes.png")).convert_alpha()
PELLETS_SHEET_IMAGE = pygame.image.load(os.path.join("assets", "pallets.png")).convert_alpha()

MAZE1 = pygame.image.load(os.path.join("assets", "maze1.png")).convert_alpha()


def draw_window(sprite_list):
    screen.fill(BLACK)
    for sprite in sprite_list:
        sprite.draw(screen)

    pygame.display.update()


def register_keys(event):
    if event.key == pygame.K_LEFT:
        return "left"
    elif event.key == pygame.K_RIGHT:
        return "right"
    elif event.key == pygame.K_UP:
        return "up"
    elif event.key == pygame.K_DOWN:
        return "down"


# last_keys[0] is the current direction that all pacmans are moving and will continue to move in that direction unless
# there is a wall in the way or the user presses the opposite direction key.
# If there is a queued key that is 90 degrees from the current direction, then the current direction will be changed to
# the queued key once there is no wall in the way in the new direction.
def move_pacmans(last_keys, pacmans, maze_data):
    for pacman in pacmans:
        # print(pacman.can_change_direction(maze_data, "up", WIDTH, HEIGHT), " ",
        #        pacman.can_change_direction(maze_data, "down", WIDTH, HEIGHT), " ",
        #        pacman.can_change_direction(maze_data, "left", WIDTH, HEIGHT), " ",
        #        pacman.can_change_direction(maze_data, "right", WIDTH, HEIGHT))
        if last_keys[0] != "none" and pacman.direction == "stay":
            pacman.direction = last_keys[0]
        if last_keys[0] == "left":

            if pacman.direction == "left" and last_keys[1] == "up" and pacman.can_change_direction(maze_data, "up",
                                                                                                   WIDTH, HEIGHT):
                pacman.direction = "up"
                last_keys[0] = "up"
                last_keys[1] = last_keys[2]
                last_keys[2] = last_keys[3]
                last_keys[3] = "none"
                for i in range(1, len(last_keys)):
                    if last_keys[i] == "none":
                        last_keys[i] = "left"
                        break
            elif pacman.direction == "left" and last_keys[1] == "down" and pacman.can_change_direction(maze_data,
                                                                                                       "down",
                                                                                                       WIDTH, HEIGHT):
                pacman.direction = "down"
                last_keys[0] = "down"
                last_keys[1] = last_keys[2]
                last_keys[2] = last_keys[3]
                last_keys[3] = "none"
                for i in range(1, len(last_keys)):
                    if last_keys[i] == "none":
                        last_keys[i] = "left"
                        break
            elif pacman.direction == "left" and last_keys[1] == "right" and pacman.can_change_direction(maze_data,
                                                                                                        "right", WIDTH,
                                                                                                        HEIGHT):
                pacman.direction = "right"
                last_keys[0] = "right"
                last_keys[1] = last_keys[2]
                last_keys[2] = last_keys[3]
                last_keys[3] = "none"
                for i in range(1, len(last_keys)):
                    if last_keys[i] == "none":
                        last_keys[i] = "left"
                        break
            elif pacman.can_change_direction(maze_data, "left", WIDTH, HEIGHT):
                pacman.direction = "left"
        elif last_keys[0] == "right":
            if pacman.direction == "right" and last_keys[1] == "up" and pacman.can_change_direction(maze_data, "up",
                                                                                                    WIDTH, HEIGHT):
                pacman.direction = "up"
                last_keys[0] = "up"
                last_keys[1] = last_keys[2]
                last_keys[2] = last_keys[3]
                last_keys[3] = "none"
                for i in range(1, len(last_keys)):
                    if last_keys[i] == "none":
                        last_keys[i] = "right"
                        break
            elif pacman.direction == "right" and last_keys[1] == "down" and pacman.can_change_direction(maze_data,
                                                                                                        "down",
                                                                                                        WIDTH, HEIGHT):
                pacman.direction = "down"
                last_keys[0] = "down"
                last_keys[1] = last_keys[2]
                last_keys[2] = last_keys[3]
                last_keys[3] = "none"
                for i in range(1, len(last_keys)):
                    if last_keys[i] == "none":
                        last_keys[i] = "right"
                        break
            elif pacman.direction == "right" and last_keys[1] == "left" and pacman.can_change_direction(maze_data,
                                                                                                       "left", WIDTH,
                                                                                                       HEIGHT):
                pacman.direction = "left"
                last_keys[0] = "left"
                last_keys[1] = last_keys[2]
                last_keys[2] = last_keys[3]
                last_keys[3] = "none"
                for i in range(1, len(last_keys)):
                    if last_keys[i] == "none":
                        last_keys[i] = "right"
                        break
            elif pacman.can_change_direction(maze_data, "right", WIDTH, HEIGHT):
                pacman.direction = "right"
        elif last_keys[0] == "up":
            if pacman.direction == "up" and last_keys[1] == "right" and pacman.can_change_direction(maze_data, "right",
                                                                                                    WIDTH, HEIGHT):
                pacman.direction = "right"
                last_keys[0] = "right"
                last_keys[1] = last_keys[2]
                last_keys[2] = last_keys[3]
                last_keys[3] = "none"
                for i in range(1, len(last_keys)):
                    if last_keys[i] == "none":
                        last_keys[i] = "up"
                        break
            elif pacman.direction == "up" and last_keys[1] == "left" and pacman.can_change_direction(maze_data, "left",
                                                                                                    WIDTH, HEIGHT):
                pacman.direction = "left"
                last_keys[0] = "left"
                last_keys[1] = last_keys[2]
                last_keys[2] = last_keys[3]
                last_keys[3] = "none"
                for i in range(1, len(last_keys)):
                    if last_keys[i] == "none":
                        last_keys[i] = "up"
                        break
            elif pacman.direction == "up" and last_keys[1] == "down" and pacman.can_change_direction(maze_data, "down",
                                                                                                    WIDTH, HEIGHT):
                pacman.direction = "down"
                last_keys[0] = "down"
                last_keys[1] = last_keys[2]
                last_keys[2] = last_keys[3]
                last_keys[3] = "none"
                for i in range(1, len(last_keys)):
                    if last_keys[i] == "none":
                        last_keys[i] = "up"
                        break
            elif pacman.can_change_direction(maze_data, "up", WIDTH, HEIGHT):
                pacman.direction = "up"
        elif last_keys[0] == "down":
            if pacman.direction == "down" and last_keys[1] == "right" and pacman.can_change_direction(maze_data,
                                                                                                     "right", WIDTH,
                                                                                                     HEIGHT):
                pacman.direction = "right"
                last_keys[0] = "right"
                last_keys[1] = last_keys[2]
                last_keys[2] = last_keys[3]
                last_keys[3] = "none"
                for i in range(1, len(last_keys)):
                    if last_keys[i] == "none":
                        last_keys[i] = "down"
                        break
            elif pacman.direction == "down" and last_keys[1] == "left" and pacman.can_change_direction(maze_data, "left",
                                                                                                     WIDTH, HEIGHT):
                pacman.direction = "left"
                last_keys[0] = "left"
                last_keys[1] = last_keys[2]
                last_keys[2] = last_keys[3]
                last_keys[3] = "none"
                for i in range(1, len(last_keys)):
                    if last_keys[i] == "none":
                        last_keys[i] = "down"
                        break
            elif pacman.direction == "down" and last_keys[1] == "up" and pacman.can_change_direction(maze_data, "up",
                                                                                                    WIDTH, HEIGHT):
                pacman.direction = "up"
                last_keys[0] = "up"
                last_keys[1] = last_keys[2]
                last_keys[2] = last_keys[3]
                last_keys[3] = "none"
                for i in range(1, len(last_keys)):
                    if last_keys[i] == "none":
                        last_keys[i] = "down"
                        break
            elif pacman.can_change_direction(maze_data, "down", WIDTH, HEIGHT):
                pacman.direction = "down"

        if pacman.direction != "stay":
            if pacman.direction == "left" and pacman.check_open_path(maze_data, "left", WIDTH, HEIGHT):
                pacman.rect.x -= pacman.speed
            elif pacman.direction == "right" and pacman.check_open_path(maze_data, "right", WIDTH, HEIGHT):
                pacman.rect.x += pacman.speed
            elif pacman.direction == "up" and pacman.check_open_path(maze_data, "up", WIDTH, HEIGHT):
                pacman.rect.y -= pacman.speed
            elif pacman.direction == "down" and pacman.check_open_path(maze_data, "down", WIDTH, HEIGHT):
                pacman.rect.y += pacman.speed

    #print(last_keys)
    return last_keys


def update_sprites(maze_data, pacmans, ghosts, consumables):
    for pacman in pacmans:
        maze_data = pacman.update(maze_data, consumables, WIDTH, HEIGHT)

    for ghost in ghosts:
        ghost.update()

    return maze_data


class GhostHouse(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def main():
    clock = pygame.time.Clock()
    run = True

    maze_data = []
    for y in range(32):
        maze_data.append([])
        for x in range(32):
            # If the pixel is black, add a 0 to the maze_data list (representing empty space)
            if MAZE1.get_at((x, y)) == (0, 0, 0):
                maze_data[y].append(0)
            # If the pixel is yellow, add a 2 to the maze_data list (representing a pellet)
            elif MAZE1.get_at((x, y)) == (255, 255, 0):
                maze_data[y].append(2)
            # If the pixel is green, add a 3 to the maze_data list (representing a power pellet)
            elif MAZE1.get_at((x, y)) == (0, 255, 0):
                maze_data[y].append(3)
            # If the pixel is red, add a 4 to the maze_data list (representing a ghost house)
            elif MAZE1.get_at((x, y)) == (255, 0, 0):
                maze_data[y].append(4)
            # If the pixel is blue, add a 5 to the maze_data list (representing the player's starting position)
            elif MAZE1.get_at((x, y)) == (0, 0, 255):
                maze_data[y].append(5)
            # If the pixel is any other color, add a 1 to the maze_data list (representing a wall)
            else:
                maze_data[y].append(1)

    # Create a list for the sprites
    walls = pygame.sprite.Group()
    pellets = pygame.sprite.Group()
    power_pellets = pygame.sprite.Group()
    ghost_houses = pygame.sprite.Group()
    ghosts = pygame.sprite.Group()
    pacmans = pygame.sprite.Group()

    # populate maze with sprites based on maze_data. Maze centered and scaled to fit screen (using SCALE)
    for y in range(32):
        for x in range(32):
            if maze_data[y][x] == 1:
                walls.add(
                    Wall(x * SCALE + (WIDTH - 32 * SCALE) / 2, y * SCALE + (HEIGHT - 32 * SCALE) / 2, SCALE, SCALE))
            elif maze_data[y][x] == 2:
                pellets.add(
                    Pellet(x * SCALE + (WIDTH - 32 * SCALE) / 2, y * SCALE + (HEIGHT - 32 * SCALE) / 2, SCALE, SCALE,
                           PELLETS_SHEET_IMAGE))
            elif maze_data[y][x] == 3:
                power_pellets.add(
                    PowerPellet(x * SCALE + (WIDTH - 32 * SCALE) / 2, y * SCALE + (HEIGHT - 32 * SCALE) / 2, SCALE,
                                SCALE, PELLETS_SHEET_IMAGE))
            elif maze_data[y][x] == 4:
                ghost_houses.add(
                    GhostHouse(x * SCALE + (WIDTH - 32 * SCALE) / 2, y * SCALE + (HEIGHT - 32 * SCALE) / 2, SCALE,
                               SCALE))
            elif maze_data[y][x] == 5:
                # pacmans.add(
                #     Pacman(x * SCALE + (WIDTH - 31 * SCALE) / 2, y * SCALE + (HEIGHT - 32.4 * SCALE) / 2, SCALE, SCALE,
                #            2))
                pacmans.add(
                    Pacman(x * SCALE + (WIDTH - 32 * SCALE) / 2,
                           y * SCALE + (HEIGHT - 32 * SCALE) / 2,
                           SCALE, SCALE,
                           PACMAN_SHEET_IMAGE,
                           SCALE,
                           2))

    last_keys = ["none", "none", "none", "none"]
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Queue up the last 4 keys pressed, so that the player can easily change directions. Remove keys from the
            # queue if they are released and move the ones that are still pressed to the front of the queue.
            elif event.type == pygame.KEYDOWN:
                if last_keys[0] == "none" or last_keys[0] == register_keys(event):
                    last_keys[0] = register_keys(event)
                elif last_keys[1] == "none":
                    last_keys[1] = register_keys(event)
                elif last_keys[2] == "none":
                    last_keys[2] = register_keys(event)
                elif last_keys[3] == "none":
                    last_keys[3] = register_keys(event)

            elif event.type == pygame.KEYUP:
                if last_keys[0] == register_keys(event):
                    last_keys[0] = last_keys[1]
                    last_keys[1] = last_keys[2]
                    last_keys[2] = last_keys[3]
                    last_keys[3] = "none"
                elif last_keys[1] == register_keys(event):
                    last_keys[1] = last_keys[2]
                    last_keys[2] = last_keys[3]
                    last_keys[3] = "none"
                elif last_keys[2] == register_keys(event):
                    last_keys[2] = last_keys[3]
                    last_keys[3] = "none"
                elif last_keys[3] == register_keys(event):
                    last_keys[3] = "none"

        last_keys = move_pacmans(last_keys, pacmans, maze_data)

        maze_data = update_sprites(maze_data, pacmans, ghosts, [pellets, power_pellets])
        draw_window([pacmans, ghosts, walls, pellets, power_pellets, ghost_houses])

    pygame.quit()


if __name__ == "__main__":
    main()
