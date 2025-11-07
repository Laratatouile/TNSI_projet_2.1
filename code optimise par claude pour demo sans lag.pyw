import pyxel
import math
import random


class App:
    def __init__(self):
        pyxel.init(256, 256, title="L'attaque des bestioles", fps=30, quit_key=pyxel.KEY_ESCAPE)
        pyxel.load("./3.pyxres")
        
        self.state = "menu_debut"
        self.ray_tracing_enabled = False
        
        # Initialisation des systèmes
        self.world = World()
        self.hitbox = Hitbox(self.world)
        self.player = Player(self.hitbox, [35, 35])
        self.camera = Camera(self.world)
        self.weapon = Weapon(self.hitbox)
        self.monsters = MonsterManager(self.hitbox, self.world)
        self.ray_tracing = RayTracing(self.hitbox, precision=1, angle=60, ray_count=74)
        self.ui = UI(self.player, self.camera)
        self.menu_start = MenuStart(self)
        self.menu_end = MenuEnd()
        
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.state == "menu_debut":
            self.menu_start.update()
        elif self.state == "menu_fin":
            self.menu_end.update()
        elif self.state == "jeu":
            self._update_game()

    def _update_game(self):
        result = self.player.update()
        if result:
            self.state = "menu_fin"
            self.menu_end.fin(result == 1)
            return
        
        self.monsters.update()
        
        # Gestion des tirs
        if self.player.should_fire:
            weapon_type = "explosion" if self.player.weapon_type == "explosion" else "balle"
            self.weapon.fire(self.player.x, self.player.y, self.player.direction, weapon_type)
            self.player.should_fire = False
        
        self.weapon.update(self.player.direction, [self.player.x, self.player.y])
        self.camera.update(self.player.x, self.player.y, self.hitbox.entities, self.hitbox.objects)
        self.ui.update()

    def draw(self):
        if self.state == "jeu":
            self.camera.draw()
            self.monsters.draw()
            
            if self.ray_tracing_enabled:
                self.ray_tracing.update([self.player.x, self.player.y], self.player.direction, (self.camera.x, self.camera.y))
                self.ray_tracing.draw()
            
            self.player.draw()
            self.weapon.draw()
            self.ui.draw()
        elif self.state == "menu_debut":
            self.menu_start.draw()
        elif self.state == "menu_fin":
            self.menu_end.draw()


class World:
    """Contient toutes les données statiques du monde"""
    def __init__(self):
        self.objects = {
            "sortie": [(155, 395), (165, 405)],
            "vie_0": [(125, 155), (135, 165)],
            "vie_1": [(485, 160), (495, 170)],
            "vie_2": [(5, 275), (15, 285)],
            "balle_0": [(270, 100), (280, 110)],
            "balle_1": [(445, 30), (455, 40)],
            "balle_2": [(395, 310), (405, 320)],
            "balle_3": [(325, 365), (335, 375)],
            "masse_0": [(385, 305), (395, 315)],
            "masse_1": [(95, 185), (105, 195)],
            "masse_2": [(35, 395), (45, 405)],
            "baril_0": [(5, 50), (14, 60)],
            "baril_1": [(120, 275), (129, 285)],
            "baril_2": [(465, 455), (464, 465)]
        }
        
        self.walls = self._init_walls()
        self.monsters_start = self._init_monsters()
        
        # Map précalculée pour collisions rapides
        self.wall_map = self._create_wall_map()
    
    def _init_walls(self):
        """Initialise tous les murs - format original [(x1,y1), (x2,y2)]"""
        walls = {}
        
        # Contour
        walls["mur_ouest"] = [(-5, -5), (0, 500)]
        walls["mur_nord"] = [(-5, -5), (500, 0)]
        walls["mur_sud"] = [(-5, 500), (505, 505)]
        walls["mur_est"] = [(500, -5), (505, 505)]
        
        # Tous les murs du labyrinthe (données originales complètes)
        wall_list = [
            [(25, 25), (30, 65)], [(30, 25), (150, 30)], [(70, 0), (75, 25)], [(55, 60), (120, 65)],
            [(115, 65), (120, 95)], [(25, 90), (90, 95)], [(55, 60), (60, 90)], [(85, 95), (90, 120)],
            [(25, 95), (30, 160)], [(0, 130), (25, 135)], [(175, 25), (230, 30)], [(175, 30), (180, 65)],
            [(145, 60), (175, 65)], [(145, 65), (150, 180)], [(55, 120), (60, 185)], [(115, 120), (120, 240)],
            [(60, 145), (145, 150)], [(85, 175), (115, 180)], [(85, 180), (90, 210)], [(120, 205), (145, 210)],
            [(25, 185), (30, 240)], [(30, 235), (175, 240)], [(55, 210), (60, 235)], [(150, 175), (270, 180)],
            [(175, 90), (180, 150)], [(180, 145), (240, 150)], [(205, 60), (210, 120)], [(210, 60), (260, 65)],
            [(255, 0), (260, 60)], [(235, 90), (240, 145)], [(240, 90), (285, 95)], [(285, 25), (290, 120)],
            [(265, 120), (270, 150)], [(270, 120), (350, 125)], [(340, 0), (345, 30)], [(315, 25), (340, 30)],
            [(315, 30), (320, 95)], [(320, 90), (350, 95)], [(345, 55), (375, 60)], [(375, 25), (410, 30)],
            [(375, 30), (380, 155)], [(405, 30), (410, 95)], [(380, 120), (440, 125)], [(435, 85), (440, 120)],
            [(435, 0), (440, 60)], [(440, 55), (465, 60)], [(465, 25), (470, 125)], [(470, 120), (475, 125)],
            [(315, 125), (320, 155)], [(295, 150), (315, 155)], [(345, 150), (390, 155)], [(295, 155), (300, 210)],
            [(300, 180), (360, 185)], [(170, 205), (175, 235)], [(175, 205), (295, 210)], [(325, 185), (330, 240)],
            [(200, 235), (325, 240)], [(200, 240), (205, 270)], [(170, 265), (200, 270)], [(230, 265), (330, 270)],
            [(0, 265), (145, 270)], [(25, 270), (30, 300)], [(85, 295), (145, 300)], [(140, 270), (145, 295)],
            [(55, 295), (60, 325)], [(0, 325), (90, 330)], [(170, 270), (175, 330)], [(115, 325), (170, 330)],
            [(85, 330), (90, 420)], [(115, 330), (120, 420)], [(90, 415), (115, 420)], [(25, 355), (60, 360)],
            [(55, 355), (60, 390)], [(25, 385), (55, 390)], [(25, 390), (30, 420)], [(30, 415), (60, 420)],
            [(55, 420), (60, 450)], [(25, 445), (55, 450)], [(25, 450), (30, 480)], [(30, 475), (140, 480)],
            [(200, 295), (300, 300)], [(200, 300), (205, 330)], [(260, 300), (265, 325)], [(230, 325), (330, 330)],
            [(385, 155), (390, 210)], [(390, 180), (420, 185)], [(415, 150), (420, 180)], [(420, 150), (450, 155)],
            [(445, 150), (450, 215)], [(475, 150), (500, 155)], [(475, 155), (480, 245)], [(445, 240), (475, 245)],
            [(355, 210), (360, 270)], [(355, 210), (420, 215)], [(415, 215), (420, 245)], [(385, 240), (415, 245)],
            [(325, 270), (330, 300)], [(385, 245), (390, 295)], [(415, 270), (500, 275)], [(330, 295), (420, 300)],
            [(355, 300), (360, 330)], [(325, 330), (330, 355)], [(415, 300), (475, 305)], [(415, 305), (420, 360)],
            [(385, 325), (420, 330)], [(385, 330), (390, 390)], [(445, 330), (475, 335)], [(470, 335), (475, 360)],
            [(445, 335), (450, 385)], [(145, 355), (385, 360)], [(230, 355), (235, 390)], [(235, 385), (290, 390)],
            [(285, 390), (290, 420)], [(320, 385), (365, 390)], [(315, 360), (320, 450)], [(390, 385), (500, 390)],
            [(395, 390), (400, 425)], [(345, 420), (395, 425)], [(345, 425), (350, 475)], [(315, 475), (380, 480)],
            [(375, 450), (380, 475)], [(425, 415), (430, 455)], [(405, 450), (425, 455)], [(405, 455), (410, 500)],
            [(435, 475), (475, 480)], [(455, 415), (460, 475)], [(460, 415), (475, 420)], [(460, 445), (500, 450)],
            [(260, 445), (315, 450)], [(255, 475), (290, 480)], [(255, 415), (260, 480)], [(200, 415), (255, 420)],
            [(200, 385), (205, 415)], [(145, 385), (200, 390)], [(145, 390), (150, 445)], [(150, 415), (175, 420)],
            [(115, 445), (230, 450)], [(135, 445), (140, 475)], [(200, 450), (205, 475)], [(165, 475), (230, 480)]
        ]
        
        for i, wall_coords in enumerate(wall_list):
            walls[f"mur_{i}"] = wall_coords
        
        return walls
    
    def _init_monsters(self):
        """Positions de départ des monstres"""
        return {
            "monstre_1": (5, 5),
            "monstre_2": (235, 35),
            "monstre_3": (5, 235),
            "monstre_4": (295, 95),
            "monstre_5": (480, 130),
            "monstre_6": (475, 395),
            "monstre_7": (475, 280),
            "monstre_8": (305, 300),
            "monstre_9": (35, 455),
            "monstre_10": (225, 424),
            "monstre_11": (265, 450)
        }
    
    def _create_wall_map(self):
        """Crée une grille booléenne pour détection rapide des murs"""
        grid = [[False] * 505 for _ in range(505)]
        for (x1, y1), (x2, y2) in self.walls.values():
            for y in range(max(0, y1), min(505, y2)):
                for x in range(max(0, x1), min(505, x2)):
                    grid[y][x] = True
        return grid


class Hitbox:
    """Gestion optimisée des collisions"""
    RULES = {
        "joueur": ([1], [3, 4, 5, 8, 9]),
        "monstre": ([1], []),
        "lumiere": ([1], []),
        "balle": ([1, 3, 5, 8, 9], [])
    }
    
    def __init__(self, world):
        self.world = world
        self.entities = {}
        self.objects = {}
        self.player_pos = [35, 35]
        
        # Initialisation des entités
        for name, (x, y) in world.monsters_start.items():
            self.entities[name] = [x, y, 16, 16]
        
        for name, ((x1, y1), (x2, y2)) in world.objects.items():
            self.objects[name] = [x1, y1, 10, 10]
    
    def check_collision(self, entity_type, pos, size=(16, 16)):
        """Vérifie les collisions pour une entité"""
        x, y = pos
        w, h = size
        
        # Vérification des limites
        if x < 0 or y < 0 or x + w > 505 or y + h > 505:
            return False, "mur", None
        
        # Vérification rapide avec la wall_map
        wall_map = self.world.wall_map
        
        # Vérifier les bords de la hitbox
        for check_y in [y, min(y + h, 504)]:
            for check_x in range(x, min(x + w + 1, 505)):
                if wall_map[check_y][check_x]:
                    return False, "mur", None
        
        for check_x in [x, min(x + w, 504)]:
            for check_y in range(y, min(y + h + 1, 505)):
                if wall_map[check_y][check_x]:
                    return False, "mur", None
        
        # Pour le joueur : vérifier collision avec entités (prendre des dégâts)
        if entity_type == "joueur":
            for name, (ex, ey, ew, eh) in self.entities.items():
                if self._boxes_overlap((x, y, w, h), (ex, ey, ew, eh)):
                    return False, "entitee", name
        
        # Pour les monstres et balles : ne PAS bloquer sur d'autres monstres
        if entity_type in ["monstre", "balle"]:
            # Les balles peuvent toucher les monstres
            if entity_type == "balle":
                for name, (ex, ey, ew, eh) in self.entities.items():
                    if self._boxes_overlap((x, y, w, h), (ex, ey, ew, eh)):
                        return False, "entitee", name
        
        # Vérification des objets (seulement pour le joueur)
        if entity_type == "joueur":
            for name, (ox, oy, ow, oh) in self.objects.items():
                if self._boxes_overlap((x, y, w, h), (ox, oy, ow, oh)):
                    return True, "objet", name
        
        return True, "rien", None
    
    def _boxes_overlap(self, box1, box2):
        """Vérifie si deux boîtes se chevauchent"""
        x1, y1, w1, h1 = box1
        x2, y2, w2, h2 = box2
        return not (x1 + w1 < x2 or x2 + w2 < x1 or y1 + h1 < y2 or y2 + h2 < y1)
    
    def move_entity(self, name, x, y):
        """Déplace une entité"""
        if name in self.entities:
            self.entities[name][:2] = [x, y]
    
    def remove_entity(self, name):
        """Supprime une entité"""
        if name in self.entities:
            del self.entities[name]
    
    def remove_object(self, name):
        """Supprime un objet"""
        if name in self.objects:
            del self.objects[name]


class Player:
    WEAPONS = ["masse", "fusil"]
    
    def __init__(self, hitbox, pos):
        self.hitbox = hitbox
        self.x, self.y = pos
        self.direction = 0
        self.speed = 2
        
        self.hp = 3
        self.bullets = 3
        self.hammers = 3
        self.current_weapon = 0
        
        self.should_fire = False
        self.weapon_type = "balle"
        self.invulnerable_time = 0
        self.hammer_cooldown = 0
        self.moving = False
        self.exit_status = 0
        
    def update(self):
        self.moving = False
        if self.invulnerable_time > 0:
            self.invulnerable_time -= 1
        if self.hammer_cooldown > 0:
            self.hammer_cooldown -= 1
        
        # Changement d'arme
        if pyxel.btnp(pyxel.KEY_E):
            self.current_weapon = (self.current_weapon + 1) % len(self.WEAPONS)
        
        # Déplacement
        if self.hammer_cooldown == 0:
            dx, dy = 0, 0
            new_dir = self.direction
            
            if pyxel.btn(pyxel.KEY_Z):
                dy = -self.speed
                new_dir = 3
            elif pyxel.btn(pyxel.KEY_S):
                dy = self.speed
                new_dir = 1
            
            if pyxel.btn(pyxel.KEY_D):
                dx = self.speed
                new_dir = 0
            elif pyxel.btn(pyxel.KEY_Q):
                dx = -self.speed
                new_dir = 2
            
            self.direction = new_dir
            
            if dx or dy:
                self._try_move(dx, dy)
            else:
                # Vérifier quand même les collisions avec monstres
                _, collision_type, _ = self.hitbox.check_collision("joueur", (self.x, self.y), (15, 14))
                if collision_type == "entitee" and self.invulnerable_time == 0:
                    self.hp -= 1
                    self.invulnerable_time = 30
                    if self.hp <= 0:
                        self.exit_status = -1
        
        # Tir/Attaque
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.WEAPONS[self.current_weapon] == "masse" and self.hammers > 0:
                self.hammers -= 1
                self.hammer_cooldown = 7
                self._hammer_attack()
            elif self.WEAPONS[self.current_weapon] == "fusil" and self.bullets > 0:
                self.bullets -= 1
                self.weapon_type = "balle"
                self.should_fire = True
        
        return self.exit_status
    
    def _try_move(self, dx, dy):
        """Tente de déplacer le joueur pixel par pixel"""
        for _ in range(abs(dx)):
            step = 1 if dx > 0 else -1
            new_x = self.x + step
            valid, collision_type, obj_id = self.hitbox.check_collision("joueur", (new_x, self.y), (15, 14))
            
            if valid:
                self.x = new_x
                self.moving = True
                if collision_type == "objet":
                    self._collect_object(obj_id)
            elif collision_type == "entitee" and self.invulnerable_time == 0:
                self.hp -= 1
                self.invulnerable_time = 30
                if self.hp <= 0:
                    self.exit_status = -1
                break
            else:
                break
        
        for _ in range(abs(dy)):
            step = 1 if dy > 0 else -1
            new_y = self.y + step
            valid, collision_type, obj_id = self.hitbox.check_collision("joueur", (self.x, new_y), (15, 14))
            
            if valid:
                self.y = new_y
                self.moving = True
                if collision_type == "objet":
                    self._collect_object(obj_id)
            elif collision_type == "entitee" and self.invulnerable_time == 0:
                self.hp -= 1
                self.invulnerable_time = 30
                if self.hp <= 0:
                    self.exit_status = -1
                break
            else:
                break
    
    def _collect_object(self, name):
        """Ramasse un objet"""
        if name.startswith("balle"):
            self.bullets += 1
        elif name.startswith("vie"):
            self.hp += 1
        elif name.startswith("masse"):
            self.hammers += 1
        elif name.startswith("sortie"):
            self.exit_status = 1
        self.hitbox.remove_object(name)
    
    def _hammer_attack(self):
        """Attaque au marteau"""
        offsets = [(16, 0), (0, 16), (-16, 0), (0, -16)]
        dx, dy = offsets[self.direction]
        target = (self.x + dx, self.y + dy)
        
        for name, (ex, ey, _, _) in list(self.hitbox.entities.items()):
            if abs(ex - target[0]) < 16 and abs(ey - target[1]) < 16:
                self.hitbox.remove_entity(name)
                break
    
    def draw(self):
        weapon_idx = self.current_weapon
        u, v = 0, 72
        
        if weapon_idx == 0:  # Masse
            if self.hammer_cooldown > 0:
                u, v = 16, 88
            elif self.moving:
                frames = [(0, 88), (16, 88), (0, 104), (16, 104)]
                u, v = frames[(pyxel.frame_count // 7) % 4]
        else:  # Fusil
            if self.moving:
                frames = [(16, 24), (0, 8), (16, 8), (0, 24)]
                u, v = frames[(pyxel.frame_count // 2) % 4]
            else:
                u, v = 0, 8
        
        w = -16 if self.direction == 2 else 16
        rot = (90 * self.direction) if self.direction != 2 else 0
        pyxel.blt(self.x, self.y, 0, u, v, w, 16, 5, rotate=rot)


class Monster:
    def __init__(self, x, y, hitbox, name):
        self.x, self.y = x, y
        self.hitbox = hitbox
        self.name = name
        self.direction = random.randint(0, 3)
        self.speed = 2
    
    def update(self):
        if self.name not in self.hitbox.entities:
            return
            
        self.x, self.y = self.hitbox.entities[self.name][:2]
        
        # Déplacement
        if self.direction == 0:
            new_x, new_y = self.x + self.speed, self.y
        elif self.direction == 1:
            new_x, new_y = self.x, self.y + self.speed
        elif self.direction == 2:
            new_x, new_y = self.x - self.speed, self.y
        else:
            new_x, new_y = self.x, self.y - self.speed
        
        valid, _, _ = self.hitbox.check_collision("monstre", (new_x, new_y))
        
        if valid:
            self.x, self.y = new_x, new_y
            self.hitbox.move_entity(self.name, self.x, self.y)
        else:
            # Changer de direction quand on touche un mur
            if random.randint(0, 1) == 1:
                self.direction = (self.direction + 1) % 4
            else:
                self.direction = (self.direction + 3) % 4
        
        # Changement aléatoire de direction
        if random.randint(0, 50) == 0:
            self.direction = random.randint(0, 3)
    
    def draw(self):
        frame = (pyxel.frame_count // 5) % 4
        w = -16 if self.direction == 2 else 16
        rot = (90 * self.direction) if self.direction != 2 else 0
        pyxel.blt(self.x, self.y, 0, 16 * frame, 136, w, 16, 5, rotate=rot)


class MonsterManager:
    def __init__(self, hitbox, world):
        self.hitbox = hitbox
        self.monsters = {}
        for name in world.monsters_start:
            x, y = hitbox.entities[name][:2]
            self.monsters[name] = Monster(x, y, hitbox, name)
    
    def update(self):
        for name in list(self.monsters.keys()):
            if name not in self.hitbox.entities:
                del self.monsters[name]
            else:
                self.monsters[name].update()
    
    def draw(self):
        for monster in self.monsters.values():
            monster.draw()


class Weapon:
    def __init__(self, hitbox):
        self.hitbox = hitbox
        self.bullets = []
        self.explosions = []
        self.fire_frame = 0
        self.fire_pos = (-100, -100)
        self.fire_dir = 0
    
    def fire(self, x, y, direction, weapon_type):
        self.fire_frame = pyxel.frame_count
        self.fire_dir = direction
        
        # Ajuster position de départ selon direction
        if direction in [0, 2]:
            self.bullets.append([x, y - 1, direction, pyxel.frame_count, weapon_type])
        elif direction == 1:
            self.bullets.append([x, y + 8, direction, pyxel.frame_count, weapon_type])
        else:
            self.bullets.append([x, y - 12, direction, pyxel.frame_count, weapon_type])
    
    def update(self, direction, player_pos):
        x, y = player_pos
        
        # Position du flash de tir
        if direction == 0:
            self.fire_pos = (x + 16, y + 3)
        elif direction == 1:
            self.fire_pos = (x + 5, y + 16)
        elif direction == 2:
            self.fire_pos = (x - 8, y + 3)
        else:
            self.fire_pos = (x + 3, y - 8)
        
        self.fire_dir = direction
        
        # Mise à jour des projectiles
        for i in reversed(range(len(self.bullets))):
            bullet = self.bullets[i]
            moves = [(5, 0), (0, 5), (-5, 0), (0, -5)]
            dx, dy = moves[bullet[2]]
            bullet[0] += dx
            bullet[1] += dy
            
            valid, collision, target = self.hitbox.check_collision("balle", (bullet[0], bullet[1]), (8, 5))
            
            if not valid or collision in ["entitee", "mur"]:
                if bullet[4] == "explosion":
                    self.explosions.append([bullet[0], bullet[1], pyxel.frame_count])
                if collision == "entitee" and target:
                    self.hitbox.remove_entity(target)
                self.bullets.pop(i)
        
        # Nettoyage des explosions
        self.explosions = [e for e in self.explosions if pyxel.frame_count - e[2] < 8]
    
    def draw(self):
        # Flash de tir
        if pyxel.frame_count - self.fire_frame <= 15:
            elapsed = pyxel.frame_count - self.fire_frame
            frame = 0 if elapsed <= 3 else (1 if elapsed <= 6 else (2 if elapsed <= 9 else 3))
            u = [56, 48, 40, 32][frame]
            w = -8 if self.fire_dir == 2 else 8
            rot = (90 * self.fire_dir) if self.fire_dir != 2 else 0
            pyxel.blt(self.fire_pos[0], self.fire_pos[1], 0, u, 16, w, 8, 5, rotate=rot)
        
        # Projectiles
        for bullet in self.bullets:
            frame = 0 if pyxel.frame_count - bullet[3] < 3 else (1 if pyxel.frame_count - bullet[3] < 9 else 2)
            u = [32, 48, 64][frame]
            w = -16 if bullet[2] == 2 else 16
            rot = (90 * bullet[2]) if bullet[2] != 2 else 0
            pyxel.blt(bullet[0], bullet[1], 0, u, 56, w, 16, 5, rotate=rot)
        
        # Explosions
        for exp in self.explosions:
            frame = min(7, (pyxel.frame_count - exp[2]) * 10)
            pyxel.blt(exp[0], exp[1], 0, 128 + frame * 16, 32, 16, 16, 5)


class Camera:
    def __init__(self, world):
        self.world = world
        self.x, self.y = -5, -5
        self.entities = {}
        self.objects = {}
    
    def update(self, player_x, player_y, entities, objects):
        self.entities = entities
        self.objects = objects
        
        # Calcul de la position de la caméra
        if player_x <= 100:
            self.x = -5
        elif player_x >= 397:
            self.x = 294
        else:
            self.x = player_x - 103
        
        if player_y <= 128:
            self.y = -5
        elif player_y >= 372:
            self.y = 244
        else:
            self.y = player_y - 128
    
    def draw(self):
        pyxel.cls(5)
        
        # Objets
        for name, (x, y, _, _) in self.objects.items():
            if name == "sortie":
                frame = (pyxel.frame_count // 7) % 4
                u = [32, 48, 64, 48][frame]  # Animation : 32 -> 48 -> 64 -> 48
                pyxel.blt(x, y, 0, u, 32, 16, 16, 5)
            elif name.startswith("vie"):
                pyxel.blt(x, y, 0, 51, 203, 10, 10, 5)
            elif name.startswith("balle"):
                pyxel.blt(x, y, 0, 3, 203, 10, 10, 5)
            elif name.startswith("masse"):
                pyxel.blt(x, y, 0, 19, 203, 10, 10, 5)
        
        # Murs optimisés
        wall_map = self.world.wall_map
        for y in range(max(0, self.y), min(self.y + 256, 505)):
            for x in range(max(0, self.x), min(self.x + 256, 505)):
                if wall_map[y][x]:
                    pyxel.pset(x, y, 0)
        
        # Bordures
        pyxel.rect(-5, -5, 505, 5, 0)
        pyxel.rect(-5, -5, 5, 505, 0)
        
        pyxel.camera(self.x, self.y)


class RayTracing:
    def __init__(self, hitbox, precision, angle, ray_count):
        self.hitbox = hitbox
        step = angle / ray_count
        self.angles = [-(angle/2) + i * step for i in range(ray_count)]
        self.light_grid = [[False] * 505 for _ in range(505)]
        
        # Précalcul des directions AVEC rotation pré-calculée pour les 4 directions
        self.ray_dirs_cache = [[], [], [], []]  # [direction][rayon_idx] = (dx, dy)
        for player_dir in range(4):
            for a in self.angles:
                rad = math.radians(a)
                cos_val = math.cos(rad)
                sin_val = math.sin(rad)
                
                # Pré-calculer la rotation pour chaque direction
                if player_dir == 0:
                    dx, dy = int(cos_val * 1000), int(sin_val * 1000)
                elif player_dir == 1:
                    dx, dy = int(-sin_val * 1000), int(cos_val * 1000)
                elif player_dir == 2:
                    dx, dy = int(-cos_val * 1000), int(sin_val * 1000)
                else:
                    dx, dy = int(sin_val * 1000), int(-cos_val * 1000)
                
                self.ray_dirs_cache[player_dir].append((dx, dy))
        
        self.cam_x = 0
        self.cam_y = 0
        self.max_distance = 200
        self.endpoints = []  # Réutiliser le même array
    
    def update(self, pos, direction, camera_pos):
        x, y = pos
        offsets = [(15, 7), (8, 15), (0, 7), (7, 0)]
        dx, dy = offsets[direction]
        x, y = x + dx, y + dy
        
        self.cam_x, self.cam_y = camera_pos
        
        # Reset optimisé - SEULEMENT la zone visible
        min_y = max(0, camera_pos[1])
        max_y = min(505, camera_pos[1] + 256)
        min_x = max(0, camera_pos[0])
        max_x = min(505, camera_pos[0] + 256)
        
        # Reset ultra-rapide avec slicing
        for i in range(min_y, max_y):
            row = self.light_grid[i]
            for j in range(min_x, max_x):
                row[j] = False
        
        # Récupérer les directions pré-calculées
        ray_dirs = self.ray_dirs_cache[direction]
        wall_map = self.hitbox.world.wall_map
        
        # Réutiliser la liste au lieu d'en créer une nouvelle
        self.endpoints.clear()
        
        # Tracer tous les rayons (optimisé inline)
        num_rays = len(ray_dirs)
        for i in range(num_rays):
            dx, dy = ray_dirs[i]
            px, py = x * 1000, y * 1000
            
            # Boucle de tracé ultra-optimisée
            for _ in range(self.max_distance):
                curr_x, curr_y = px // 1000, py // 1000
                if not (0 <= curr_x < 505 and 0 <= curr_y < 505) or wall_map[curr_y][curr_x]:
                    self.endpoints.append((curr_x, curr_y))
                    break
                px += dx
                py += dy
            else:
                self.endpoints.append((px // 1000, py // 1000))
        
        # Remplir les triangles (optimisé)
        for i in range(num_rays - 1):
            x1, y1 = self.endpoints[i]
            x2, y2 = self.endpoints[i + 1]
            self._fill_triangle_optimized(x, y, x1, y1, x2, y2, wall_map)
    
    def _fill_triangle_optimized(self, x0, y0, x1, y1, x2, y2, wall_map):
        """Remplissage de triangle ULTRA OPTIMISÉ"""
        # Trier par Y (bubble sort pour 3 éléments = plus rapide)
        if y0 > y1:
            x0, y0, x1, y1 = x1, y1, x0, y0
        if y1 > y2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        if y0 > y1:
            x0, y0, x1, y1 = x1, y1, x0, y0
        
        # Éviter division par zéro
        if y2 == y0:
            return
        
        # Précalculer les pentes (éviter divisions répétées)
        inv_total_height = 1.0 / (y2 - y0)
        
        # Scanline simplifié
        light_grid = self.light_grid
        
        for y in range(max(0, y0), min(505, y2 + 1)):
            # Calcul des intersections X optimisé
            t = (y - y0) * inv_total_height
            x_left = int(x0 + t * (x2 - x0))
            
            # Déterminer x_right selon le segment
            if y < y1:
                if y1 != y0:
                    t2 = (y - y0) / (y1 - y0)
                    x_right = int(x0 + t2 * (x1 - x0))
                else:
                    x_right = x_left
            else:
                if y2 != y1:
                    t2 = (y - y1) / (y2 - y1)
                    x_right = int(x1 + t2 * (x2 - x1))
                else:
                    x_right = x_left
            
            # Assurer que x_left < x_right
            if x_left > x_right:
                x_left, x_right = x_right, x_left
            
            # Remplir la ligne (accès direct optimisé)
            x_start = max(0, x_left)
            x_end = min(504, x_right)
            row_wall = wall_map[y]
            row_light = light_grid[y]
            
            for x in range(x_start, x_end + 1):
                if not row_wall[x]:
                    row_light[x] = True
    
    def draw(self):
        """Affichage ultra-optimisé avec accès mémoire continu"""
        start_y = max(0, self.cam_y)
        end_y = min(505, self.cam_y + 256)
        start_x = max(0, self.cam_x)
        end_x = min(505, self.cam_x + 256)
        
        # Accès optimisé : par ligne pour localité cache
        light_grid = self.light_grid
        for y in range(start_y, end_y):
            row = light_grid[y]
            for x in range(start_x, end_x):
                if not row[x]:
                    pyxel.pset(x, y, 0)


class UI:
    def __init__(self, player, camera):
        self.player = player
        self.camera = camera
    
    def update(self):
        pass
    
    def draw(self):
        x = self.camera.x + 206
        y = self.camera.y
        
        pyxel.rect(x, y, 50, 256, 0)
        
        pyxel.text(x + 5, y + 10, "balles:", 13)
        pyxel.blt(x + 5, y + 20, 0, 0 if self.player.bullets > 0 else 112, 216, 16, 16, 5)
        if self.player.bullets > 0:
            pyxel.text(x + 25, y + 25, f"X {self.player.bullets}", 13)
        
        pyxel.text(x + 5, y + 40, "vie:", 13)
        pyxel.blt(x + 5, y + 50, 0, 48, 216, 15, 15, 5)
        pyxel.text(x + 25, y + 55, f"X {self.player.hp}", 13)
        
        pyxel.text(x + 5, y + 70, "masses:", 13)
        pyxel.blt(x + 5, y + 80, 0, 16, 216, 15, 15, 5)
        pyxel.text(x + 25, y + 85, f"X {self.player.hammers}", 13)


class MenuStart:
    def __init__(self, app):
        self.app = app
        self.ray_tracing = False
        pyxel.mouse(True)
    
    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx, my = pyxel.mouse_x, pyxel.mouse_y
            
            if 88 <= mx <= 168 and 20 <= my <= 36:
                self.ray_tracing = not self.ray_tracing
            elif 88 <= mx <= 168 and 50 <= my <= 66:
                pyxel.mouse(False)
                self.app.ray_tracing_enabled = self.ray_tracing
                self.app.state = "jeu"
    
    def draw(self):
        pyxel.cls(0)
        self._draw_button(88, 20, 80, 16, "ray tracing", self.ray_tracing)
        self._draw_button(88, 50, 80, 16, "jouer", None)
    
    def _draw_button(self, x, y, w, h, text, state):
        if state is None:  # Bouton action
            bg, border = 15, 14
        elif state:  # Actif
            bg, border = 11, 3
        else:  # Inactif
            bg, border = 8, 4
        
        pyxel.rect(x, y, w, h, border)
        pyxel.rect(x + 2, y + 2, w - 4, h - 4, bg)
        pyxel.text(x + w // 2 - len(text) * 2, y + 5, text, 0)


class MenuEnd:
    def __init__(self):
        self.victory = False
    
    def fin(self, victory):
        self.victory = victory
        pyxel.mouse(True)
        pyxel.camera(0, 0)
    
    def update(self):
        pass
    
    def draw(self):
        pyxel.cls(0)
        result = "gagne" if self.victory else "perdu"
        pyxel.text(88, 20, f"Vous avez {result}", 11)
        pyxel.text(60, 40, "en tout cas merci d'avoir joue", 6)
        pyxel.text(60, 50, "et d'avoir passe un bon moment", 6)
        pyxel.text(88, 70, "Appuyez sur echap", 14)


if __name__ == '__main__':
    App()