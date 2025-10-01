import pyxel
import time
import math





##### _____ App _____ #####

class App:
    def __init__(self):
        # initialisation de pyxel
        pyxel.init(256,
                   256,
                   title="L'attaque des bestioles",
                   fps=30,
                   quit_key=pyxel.KEY_ESCAPE)
        pyxel.load("./3.pyxres")
        
        # initialisation des classes
        self.player = Player()
        self.cam_decors = CamDecors()


        # lancement de pyxel
        pyxel.run(self.update, self.draw)




    def update(self):
        self.player.update()
        self.cam_decors.update(self.player.x, self.player.y)
        


    def draw(self):
        self.cam_decors.draw()

        self.player.draw()













##### _____ Player _____ #####

class Player:
    def __init__(self):
        # ses variables
        self.x = 50
        self.y = 50
        # direction 0 : droite, 1 : bas, 2 : gauche, 3 : haut
        self.direction = 0
        self.vitesse = 3
        self.pos_perso = [[16, 24], [0, 8], [16, 8], [0, 24]]

        # ses classes
        self.arme = Arme(self)


    def update(self):
        # initialisations des variables au debut de chaque iteration
        self.bouge = False


        # mouvements du joueur
        if pyxel.btn(pyxel.KEY_Z):
            self.y -= self.vitesse
            if not self.deplacement_valide():
                self.y += self.vitesse
            self.direction = 3
            self.bouge = True
        if pyxel.btn(pyxel.KEY_S):
            self.y += self.vitesse
            if not self.deplacement_valide():
                self.y -= self.vitesse
            self.direction = 1
            self.bouge = True
        if pyxel.btn(pyxel.KEY_D):
            self.x += self.vitesse
            if not self.deplacement_valide():
                self.x -= self.vitesse
            self.direction = 0
            self.bouge = True
        if pyxel.btn(pyxel.KEY_Q):
            self.x -= self.vitesse
            if not self.deplacement_valide():
                self.x += self.vitesse
            self.direction = 2
            self.bouge = True


        # les actions du joueur
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.arme.tir(self.x+16, self.y+3)


        self.arme.update()


    def deplacement_valide(self):
        # si le joueur sort de la map
        if not 0 <= self.x <= 484:
            return False
        elif not 0 <= self.y <= 484:
            return False
        # si le joueur franchis un mur
        # bah nan c pas fait ya pas de murs
        return True




    def draw(self):
        # le personnage
        pyxel.blt(self.x,
                    self.y,
                    0,
                    self.pos_perso[(pyxel.frame_count%4 if self.bouge else 0)][0],
                    self.pos_perso[(pyxel.frame_count%4 if self.bouge else 0)][1],
                    (-16 if self.direction == 2 else 16),
                    16,
                    5,
                    rotate=((90 * self.direction) if (90 * self.direction) != 180 else 0))

        # l'arme
        self.arme.draw()













##### _____ Armes _____ #####

class Arme:
    def __init__(self, parent:object):
        self.parent = parent
        self.vitesse = 5
        self.infos_tir = [0, 1]
        self.liste_balles = []
        self.liste_explosions = []
        self.liste_positions_feu = [56, 48, 40, 32]




    def update(self):
        if self.infos_tir == None:
            return
        
        if time.time() - self.infos_tir[0] >= 10:
            return


        # deplacer la balle si elle est encore présente ou la supprimer sinon
        for i in reversed(range(len(self.liste_balles))):
            balle = self.liste_balles[i]
            if 16 < balle[0] < 484 and 16 < balle[1] < 484:
                if balle[2] == 0:
                    balle[0] += self.vitesse
                elif balle[2] == 1:
                    balle[1] += self.vitesse
                elif balle[2] == 2:
                    balle[0] -= self.vitesse
                else:
                    balle[1] -= self.vitesse
            else:
                # supprimer les balles et ajouter des explosions
                self.explosion(balle[0], balle[1])
                self.liste_balles.pop(i)

        # calculer la position du coup de feu du fusil si il a tire recement
        if self.infos_tir != None:
            # calcul des positions x et y du coup de feu
            if self.parent.direction == 0:
                self.position_feu_x = self.parent.x + 16
            elif self.parent.direction == 1:
                self.position_feu_x = self.parent.x + 5
            elif self.parent.direction == 2:
                self.position_feu_x = self.parent.x - 8
            else:
                self.position_feu_x = self.parent.x + 3
            
            if self.parent.direction in [0, 2]:
                self.position_feu_y = self.parent.y + 3
            elif self.parent.direction == 1:
                self.position_feu_y = self.parent.y + 16
            else:
                self.position_feu_y = self.parent.y - 8




    def draw(self):
        # si on tire en ce moment on affiche le feu du fusil
        if self.infos_tir != None:
            # affichage du feu
            if time.time() - self.infos_tir[0] <= 0.5:
                pyxel.blt(self.position_feu_x,
                          self.position_feu_y,
                          0,
                          (self.liste_positions_feu[0] if time.time() - self.infos_tir[0] <= 0.1 else (self.liste_positions_feu[1] if time.time() - self.infos_tir[0] <= 0.2 else (self.liste_positions_feu[2] if time.time() - self.infos_tir[0] <= 0.3 else self.liste_positions_feu[3]))),
                          16,
                          (-8 if self.parent.direction == 2 else 8),
                          8,
                          5,
                          rotate=((90 * self.parent.direction) if (90 * self.parent.direction) != 180 else 0))
        

        # on affiche toutes les balles
        for balle in self.liste_balles:
            pyxel.blt(balle[0],
                        balle[1],
                        0,
                        (32 if time.time() - balle[3] < 0.1 else (48 if time.time() - balle[3] < 0.3 else 64)),
                        56,
                        (-16 if balle[2] == 2 else 16),
                        16,
                        5,
                        rotate=((90 * balle[2]) if (90 * balle[2]) != 180 else 0))
            
        # on affiche toutes les explosions
        temps = time.time()
        for boom in self.liste_explosions:
            pyxel.blt(
                boom[0],
                boom[1],
                0,
                128 + math.floor((temps - boom[2])*10)*16,
                32,
                16,
                16,
                5
            )




    def explosion(self, x:int, y:int):
        self.liste_explosions.append([x, y, time.time()])



    def tir(self, x:int, y:int):
        # enregistrer les informations concernant le tir effectue
        if time.time() - self.infos_tir[0] > 0.5:
            self.infos_tir = [time.time(), self.parent.direction]
            if self.parent.direction in [0, 2]:
                self.liste_balles.append([(x-25 if self.parent.direction == 2 else x-10), y-3, self.parent.direction, time.time()])
            elif self.parent.direction == 1:
                self.liste_balles.append([x-15, y+8, self.parent.direction, time.time()])
            else :
                self.liste_balles.append([x-15, y-12, self.parent.direction, time.time()])













##### _____ CamDecors _____ #####

class CamDecors:
    def __init__(self):
        # plage_x, plage_y
        self.limites_monde = [[0, 500], [0, 500]]
        self.camera = [128, 128]

    def update(self, x_player:int, y_player:int):
        # calculer le deplcement possible
        if self.limites_monde[0][0]+128 <= x_player <= self.limites_monde[1][1]-123 and self.limites_monde[1][0]+128 <= y_player <= self.limites_monde[1][1]-123:
            self.camera = [x_player, y_player]
        elif self.limites_monde[0][0]+128 <= x_player <= self.limites_monde[1][1]-123:
            self.camera[0] = x_player
        elif self.limites_monde[1][0]+128 <= y_player <= self.limites_monde[1][1]-123:
            self.camera[1] = y_player

    
    def draw(self):
        # tout effacer
        pyxel.cls(5)

        # les murs de la carte
        pyxel.rect(self.limites_monde[0][0], self.limites_monde[1][0], 5, self.limites_monde[0][1], 0) ## mur Ouest
        pyxel.rect(self.limites_monde[0][0], self.limites_monde[1][0], self.limites_monde[1][1], 5, 0) ## mur Nord
        pyxel.rect(self.limites_monde[0][1], self.limites_monde[1][0], 5, self.limites_monde[1][1], 0) ## mur Est
        pyxel.rect(self.limites_monde[1][0], self.limites_monde[0][1], self.limites_monde[0][1]+5, 5, 0) ## mur Sud



        pyxel.camera(self.camera[0]-128, self.camera[1]-128)













if __name__ == '__main__':
    App()