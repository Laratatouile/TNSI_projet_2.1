import pyxel
import time
import math





##### _____ App _____ #####

class App:
    def __init__(self):
        # initialisation de pyxel
        pyxel.init(
                    256,
                    256,
                    title="L'attaque des bestioles",
                    fps=30,
                    quit_key=pyxel.KEY_ESCAPE,
                )
        pyxel.load("./3.pyxres")

        # initialisation des variables
        self.dict_objets_murs = {
            "objets" : {
                "sortie" : [(155, 395), (171, 411)]
            },
            "murs" : {
                # ceux du contour de la map
                "mur_ouest" : [(-5, -5), (0, 500)],
                "mur_nord" : [(-5, -5), (500, 0)],
                "mur_sud" : [(-5, 500), (505, 505)],
                "mur_est" : [(500, -5), (505, 505)],
                # les murs du labyrinthe
                "mur_0" : [(25, 25), (30, 65)],
                "mur_1" : [(30, 25), (150, 30)],
                "mur_2" : [(70, 0), (75, 25)],
                "mur_3" : [(55, 60), (120, 65)],
                "mur_4" : [(115, 65), (120, 95)],
                "mur_5" : [(25, 90), (90, 95)],
                "mur_6" : [(55, 60), (60, 90)],
                "mur_7" : [(85, 95), (90, 120)],
                "mur_8" : [(25, 95), (30, 160)],
                "mur_9" : [(0, 130), (25, 135)],
                "mur_10" : [(175, 25), (230, 30)],
                "mur_11" : [(175, 30), (180, 65)],
                "mur_12" : [(145, 60), (175, 65)],
                "mur_13" : [(145, 65), (150, 180)],
                "mur_14" : [(55, 120), (60, 185)],
                "mur_15" : [(115, 120), (120, 240)],
                "mur_16" : [(60, 145), (145, 150)],
                "mur_17" : [(85, 175), (115, 180)],
                "mur_18" : [(85, 180), (90, 210)],
                "mur_19" : [(120, 205), (145, 210)],
                "mur_20" : [(25, 185), (30, 240)],
                "mur_21" : [(30, 235), (175, 240)],
                "mur_22" : [(55, 210), (60, 235)],
                "mur_23" : [(150, 175), (270, 180)],
                "mur_24" : [(175, 90), (180, 150)],
                "mur_25" : [(180, 145), (240, 150)],
                "mur_26" : [(205, 60), (210, 120)],
                "mur_27" : [(210, 60), (260, 65)],
                "mur_28" : [(255, 0), (260, 60)],
                "mur_29" : [(235, 90), (240, 145)],
                "mur_30" : [(240, 90), (285, 95)],
                "mur_31" : [(285, 25), (290, 120)],
                "mur_32" : [(265, 120), (270, 150)],
                "mur_33" : [(270, 120), (350, 125)],
                "mur_34" : [(340, 0), (345, 30)],
                "mur_35" : [(315, 25), (340, 30)],
                "mur_36" : [(315, 30), (320, 95)],
                "mur_37" : [(320, 90), (350, 95)],
                "mur_38" : [(345, 55), (375, 60)],
                "mur_39" : [(375, 25), (410, 30)],
                "mur_40" : [(375, 30), (380, 155)],
                "mur_41" : [(405, 30), (410, 95)],
                "mur_42" : [(380, 120), (440, 125)],
                "mur_43" : [(435, 85), (440, 120)],
                "mur_44" : [(435, 0), (440, 60)],
                "mur_45" : [(440, 55), (465, 60)],
                "mur_46" : [(465, 25), (470, 125)],
                "mur_47" : [(470, 120), (475, 125)],
                "mur_48" : [(315, 125), (320, 155)],
                "mur_49" : [(295, 150), (315, 155)],
                "mur_50" : [(345, 150), (390, 155)],
                "mur_51" : [(295, 155), (300, 210)],
                "mur_52" : [(300, 180), (360, 185)],
                "mur_53" : [(170, 205), (175, 235)],
                "mur_54" : [(175, 205), (295, 210)],
                "mur_55" : [(325, 185), (330, 240)],
                "mur_56" : [(200, 235), (325, 240)],
                "mur_57" : [(200, 240), (205, 270)],
                "mur_58" : [(170, 265), (200, 270)],
                "mur_59" : [(230, 265), (330, 270)],
                "mur_60" : [(0, 265), (145, 270)],
                "mur_61" : [(25, 270), (30, 300)],
                "mur_62" : [(85, 295), (145, 300)],
                "mur_63" : [(140, 270), (145, 295)],
                "mur_64" : [(55, 295), (60, 325)],
                "mur_65" : [(0, 325), (90, 330)],
                "mur_66" : [(170, 270), (175, 330)],
                "mur_67" : [(115, 325), (170, 330)],
                "mur_68" : [(85, 330), (90, 420)],
                "mur_69" : [(115, 330), (120, 420)],
                "mur_70" : [(90, 415), (115, 420)],
                "mur_71" : [(25, 355), (60, 360)],
                "mur_72" : [(55, 355), (60, 390)],
                "mur_73" : [(25, 385), (55, 390)],
                "mur_74" : [(25, 390), (30, 420)],
                "mur_75" : [(30, 415), (60, 420)],
                "mur_76" : [(55, 420), (60, 450)],
                "mur_77" : [(25, 445), (55, 450)],
                "mur_78" : [(25, 450), (30, 480)],
                "mur_79" : [(30, 475), (140, 480)],
                "mur_80" : [(200, 295), (300, 300)],
                "mur_81" : [(200, 300), (205, 330)],
                "mur_82" : [(260, 300), (265, 325)],
                "mur_83" : [(230, 325), (330, 330)],
                "mur_84" : [(385, 155), (390, 210)],
                "mur_85" : [(390, 180), (420, 185)],
                "mur_86" : [(415, 150), (420, 180)],
                "mur_87" : [(420, 150), (450, 155)],
                "mur_88" : [(445, 150), (450, 215)],
                "mur_89" : [(475, 150), (500, 155)],
                "mur_90" : [(475, 155), (480, 245)],
                "mur_91" : [(445, 240), (475, 245)],
                "mur_92" : [(355, 210), (360, 270)],
                "mur_93" : [(355, 210), (420, 215)],
                "mur_94" : [(415, 215), (420, 245)],
                "mur_95" : [(385, 240), (415, 245)],
                "mur_96" : [(325, 270), (330, 300)],
                "mur_97" : [(385, 245), (390, 295)],
                "mur_98" : [(415, 270), (500, 275)],
                "mur_99" : [(330, 295), (420, 300)],
                "mur_100" : [(355, 300), (360, 330)],
                "mur_101" : [(325, 330), (330, 355)],
                "mur_102" : [(415, 300), (475, 305)],
                "mur_103" : [(415, 305), (420, 360)],
                "mur_104" : [(385, 325), (420, 330)],
                "mur_105" : [(385, 330), (390, 390)],
                "mur_106" : [(445, 330), (475, 335)],
                "mur_107" : [(470, 335), (475, 360)],
                "mur_108" : [(445, 335), (450, 385)],
                "mur_109" : [(145, 355), (385, 360)],
                "mur_110" : [(230, 355), (235, 390)],
                "mur_111" : [(235, 385), (290, 390)],
                "mur_112" : [(285, 390), (290, 420)],
                "mur_113" : [(320, 385), (365, 390)],
                "mur_114" : [(315, 360), (320, 450)],
                "mur_115" : [(390, 385), (500, 390)],
                "mur_116" : [(395, 390), (400, 425)],
                "mur_117" : [(345, 420), (395, 425)],
                "mur_118" : [(345, 425), (350, 475)],
                "mur_119" : [(315, 475), (380, 480)],
                "mur_120" : [(375, 450), (380, 475)],
                "mur_121" : [(425, 415), (430, 455)],
                "mur_122" : [(405, 450), (425, 455)],
                "mur_123" : [(405, 455), (410, 500)],
                "mur_124" : [(435, 475), (475, 480)],
                "mur_125" : [(455, 415), (460, 475)],
                "mur_126" : [(460, 415), (475, 420)],
                "mur_127" : [(460, 445), (500, 450)],
                "mur_128" : [(260, 445), (315, 450)],
                "mur_129" : [(255, 475), (290, 480)],
                "mur_130" : [(255, 415), (260, 480)],
                "mur_131" : [(200, 415), (255, 420)],
                "mur_132" : [(200, 385), (205, 415)],
                "mur_133" : [(145, 385), (200, 390)],
                "mur_134" : [(145, 390), (150, 445)],
                "mur_135" : [(150, 415), (175, 420)],
                "mur_136" : [(115, 445), (230, 450)],
                "mur_137" : [(135, 445), (140, 475)],
                "mur_138" : [(200, 450), (205, 475)],
                "mur_139" : [(165, 475), (230, 480)]
            },
            "entitees" : {
                "joueur" : [(35, 35), (51, 51)]
            }
        }
        self.endroit = "jeu"
        
        # initialisation des classes
        self.hitbox = Hitbox(self.dict_objets_murs)
        self.player = Player(self.hitbox, self.dict_objets_murs["entitees"]["joueur"][0])
        self.cam_decors = CamDecors()
        self.arme = Arme(self.hitbox)


        # lancement de pyxel
        pyxel.run(self.update, self.draw)




    def update(self):
        if self.endroit == "jeu":
            self.player.update()
            if self.player.arme_tir[0] == "explosion" and self.player.arme_tir[1] == True:
                self.arme.tir(self.player.x, self.player.y, self.player.direction, "explosion")
                self.player.arme_tir = "explosion", False
            elif self.player.arme_tir[0] == "balle" and self.player.arme_tir[1] == True:
                self.arme.tir(self.player.x, self.player.y, self.player.direction, "balle")
                self.player.arme_tir = "balle"
            self.arme.update(self.player.direction, [self.player.x, self.player.y])
        self.cam_decors.update(self.player.x, self.player.y, self.hitbox.dict_hit)





    def draw(self):
        if self.endroit == "jeu":
            self.cam_decors.draw()

            self.player.draw()
            self.arme.draw()













##### _____ Player _____ #####

class Player:
    def __init__(self, hitbox:object, position:list=[int, int]):
        # ses variables
        self.x, self.y = position
        # la classe qui gere les hitbox
        self.hitbox = hitbox
        self.arme_tir = "balle", False
        # direction 0 : droite, 1 : bas, 2 : gauche, 3 : haut
        self.direction = 0
        self.vitesse = 3
        # les positions pour que le perso bouge
        self.pos_perso = [[16, 24], [0, 8], [16, 8], [0, 24]]
        self.mega_player = False


    def update(self):
        # initialisations des variables au debut de chaque iteration
        self.bouge = False


        # mouvements du joueur
        # Haut
        if pyxel.btn(pyxel.KEY_Z):
            self.y -= self.vitesse
            if not self.deplacement_valide():
                self.y += self.vitesse
            self.direction = 3
            self.bouge = True
        # Bas
        if pyxel.btn(pyxel.KEY_S):
            self.y += self.vitesse
            if not self.deplacement_valide():
                self.y -= self.vitesse
            self.direction = 1
            self.bouge = True
        # Droite
        if pyxel.btn(pyxel.KEY_D):
            self.x += self.vitesse
            if not self.deplacement_valide():
                self.x -= self.vitesse
            self.direction = 0
            self.bouge = True
        # Gauche
        if pyxel.btn(pyxel.KEY_Q):
            self.x -= self.vitesse
            if not self.deplacement_valide():
                self.x += self.vitesse
            self.direction = 2
            self.bouge = True


        # les actions du joueur
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.mega_player == True:
                self.arme_tir = "explosion", True
            else:
                self.arme_tir = "balle", True
            


    def deplacement_valide(self):
        retour = self.hitbox.update("joueur", [self.x, self.y])
        # il peux avancer
        if retour[0] and retour[1] in ["rien", "entitee"]:
            return True
        if not retour[0]:
            return False
        # attention code a finir pour les objets
        if retour[0] and retour[1] == "objets":
            return True
        
        



    def draw(self):
        # le personnage
        if self.bouge:
            perso_nombre = self.calcul_nombre_temps(4, 2)
        else:
            perso_nombre = 3
        pyxel.blt(self.x,
            self.y,
            0,
            self.pos_perso[perso_nombre][0],
            self.pos_perso[perso_nombre][1],
            (-16 if self.direction == 2 else 16),
            16,
            5,
            rotate=((90 * self.direction) if (90 * self.direction) != 180 else 0)
        )


    def calcul_nombre_temps(self, nombre_max:int, vitesse:int=5) -> int:
        return pyxel.frame_count // vitesse % nombre_max














##### _____ Armes _____ #####

class Arme:
    def __init__(self, hitbox:object):
        self.hitbox = hitbox
        self.vitesse = 5
        self.infos_tir = [0, 1, "balle"]
        self.liste_balles = []
        self.liste_explosions = []
        self.liste_positions_feu = [56, 48, 40, 32]
        self.position_feu_y = -100
        self.position_feu_x = -100




    def update(self, direction:int, player_pos:list):
        # les variebles
        self.direction = direction
        player_x, player_y = player_pos


        if self.infos_tir == None:
            return
        
        if time.time() - self.infos_tir[0] >= 10:
            return


        # deplacer la balle si elle est encore présente ou la supprimer sinon
        for i in reversed(range(len(self.liste_balles))):
            balle = self.liste_balles[i]
            if balle[2] == 0:
                balle[0] += self.vitesse
                retour = self.hitbox.update("balle", [balle[0], balle[1]])
                if retour[0] == False or retour == [True, "entitee"] :
                    balle[0] -= self.vitesse
                    if balle[4] == "explosion":
                        self.explosion(balle[0], balle[1])
                    self.liste_balles.pop(i)
            elif balle[2] == 1:
                balle[1] += self.vitesse
                retour = self.hitbox.update("balle", [balle[0], balle[1]])
                if retour[0] == False or retour in [[True, "entitee"], [True, "mur"] ]:
                    balle[1] -= self.vitesse
                    if balle[4] == "explosion":
                        self.explosion(balle[0], balle[1])
                    self.liste_balles.pop(i)
            elif balle[2] == 2:
                balle[0] -= self.vitesse
                retour = self.hitbox.update("balle", [balle[0], balle[1]])
                if retour[0] == False or retour in [[True, "entitee"], [True, "mur"] ]:
                    balle[0] += self.vitesse
                    if balle[4] == "explosion":
                        self.explosion(balle[0], balle[1])
                    self.liste_balles.pop(i)
            else:
                balle[1] -= self.vitesse
                retour = self.hitbox.update("balle", [balle[0], balle[1]])
                if retour[0] == False or retour in [[True, "entitee"], [True, "mur"] ]:
                    balle[1] += self.vitesse
                    if balle[4] == "explosion":
                        self.explosion(balle[0], balle[1])
                    self.liste_balles.pop(i)




        # calculer la position du coup de feu du fusil si il a tire recement
        if self.infos_tir != None:
            # calcul des positions x et y du coup de feu
            if direction == 0:
                self.position_feu_x = player_x + 16
            elif direction == 1:
                self.position_feu_x = player_x + 5
            elif direction == 2:
                self.position_feu_x = player_x - 8
            else:
                self.position_feu_x = player_x + 3
            
            if direction in [0, 2]:
                self.position_feu_y = player_y + 3
            elif direction == 1:
                self.position_feu_y = player_y + 16
            else:
                self.position_feu_y = player_y - 8





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
                          (-8 if self.direction == 2 else 8),
                          8,
                          5,
                          rotate=((90 * self.direction) if (90 * self.direction) != 180 else 0))
        

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



    def tir(self, x:int, y:int, direction:int, type_tir:str):
        # enregistrer les informations concernant le tir effectue
        if time.time() - self.infos_tir[0] > 0.5:
            self.infos_tir = [time.time(), direction]
            if direction in [0, 2]:
                self.liste_balles.append([x, y-1, direction, time.time(), type_tir])
            elif direction == 1:
                self.liste_balles.append([x, y+8, direction, time.time(), type_tir])
            else :
                self.liste_balles.append([x, y-12, direction, time.time(), type_tir])













##### _____ CamDecors _____ #####

class CamDecors:
    def __init__(self):
        # plage_x, plage_y
        self.limites_monde = [[0, 500], [0, 500]]
        self.camera = [123, 123]
        self.liste_pos_sortie = [32, 48, 64, 48]


    def update(self, x_player:int, y_player:int, dict_objets:dict):
        self.dict_objets = dict_objets
        # calculer le deplcement possible
        if self.limites_monde[0][0]+123 <= x_player <= self.limites_monde[1][1]-123 and self.limites_monde[1][0]+123 <= y_player <= self.limites_monde[1][1]-123:
            self.camera = [x_player, y_player]
        elif self.limites_monde[0][0]+123 <= x_player <= self.limites_monde[1][1]-123:
            self.camera[0] = x_player
        elif self.limites_monde[1][0]+123 <= y_player <= self.limites_monde[1][1]-123:
            self.camera[1] = y_player




    def draw(self):
        # tout effacer
        pyxel.cls(5)


        # dessiner toutes les choses
        for truc, objet in self.dict_objets.items():
            if truc == "murs":
                for position in objet.values():
                    pyxel.rect(position[0][0], position[0][1], position[1][0]-position[0][0], position[1][1]-position[0][1], 0)
            if truc == "objets":
                for nom, position in objet.items():
                    if nom == "sortie":
                        pyxel.blt(
                            position[0][0],
                            position[0][1],
                            0,
                            self.liste_pos_sortie[self.calcul_nombre_temps(4, 7)],
                            32,
                            16,
                            16,
                            5
                        )



        pyxel.camera(self.camera[0]-128, self.camera[1]-128)


    
    def calcul_nombre_temps(self, nombre_max:int, vitesse:int=5) -> int:
        return pyxel.frame_count // vitesse % nombre_max













##### _____ Hitbox _____ #####

class Hitbox:
    def __init__(self, dictionnaire_objets:dict):
        self.dict_hit = dictionnaire_objets



    def update(self, entitee_nom:str, entitee_position:list[int, int]=[0, 0]) -> bool:
        """
            entitee_nom --> le nom de l'entitee
            entitee_position --> la position de l'entitee [x, y]
            lieu --> le nom du lieu ou l'entitee se trouve
            renvoie un tuple avec soit
            False si le mouvment n'est pas valide
            soit True + "rien" si le mouvement est valide
            soit True + "objet" + type_objet si on touche un objet
            soit True + "ennemi"
        """
        entitee_hitbox = [
            [entitee_position[0], entitee_position[1]],
            [entitee_position[0], entitee_position[1]+16],
            [entitee_position[0]+16, entitee_position[1]],
            [entitee_position[0]+16, entitee_position[1]+16]
        ]
        if entitee_nom != "balle":
            self.dict_hit["entitees"][entitee_nom] = entitee_hitbox


        # faire l'iteration pour les murs
        for nom, objets in self.dict_hit["murs"].items():
            # si un coin de l'entitee se trove dans l'objet
            for point_hitbox in entitee_hitbox:
                if objets[0][0] <= point_hitbox[0] <= objets[1][0] and objets[0][1] <= point_hitbox[1] <= objets[1][1]:
                    return False, "mur", nom
            
            # si un coin du mur se trouve dans l'entitee
            for point_obj in objets:
                if entitee_hitbox[0][0] <= point_obj[0] <= entitee_hitbox[1][0] and entitee_hitbox[0][1] <= point_obj[1] <= entitee_hitbox[1][1]:
                    return False, "mur", nom


            # si l'entite se trouve sur les 2 cote de la boite en x
            print((objets[0][1] <= entitee_hitbox[0][1] <= objets[1][1] or objets[0][1] <= entitee_hitbox[1][1] <= objets[1][1]))
            if objets[0][0] >= entitee_hitbox[0][0] and objets[1][0] <= entitee_hitbox[1][0]:# and (objets[0][1] <= entitee_hitbox[0][1] <= objets[1][1] or objets[0][1] <= entitee_hitbox[1][1] <= objets[1][1]):
                return False, "mur", nom
            # si l'entite se trouve sur les 2 cote de la boite en y
            # if objets[0][0] >= entitee_hitbox[0][1] and objets[1][1] <= entitee_hitbox[1][1] and (objets[0][0] >= entitee_hitbox[0][0] >= objets[1][0] or objets[0][0] <= entitee_hitbox[1][0] <= objets[1][0]):
            #     return False, "mur", nom


        # faire l'iteration pour les entities
        for cle, objets in self.dict_hit["entitees"].items():
            # si l'entite est nous meme
            if cle == entitee_nom:
                continue

            # si un coin de l'entitee se trove dans l'objet
            for point_hitbox in entitee_hitbox:
                if objets[0][0] < point_hitbox[0] < objets[1][0] and objets[0][1] < point_hitbox[1] < objets[1][1]:
                    return True, ("entitee" if cle != "joueur" else "joueur")
            
            # si un coin de l'objet se trouve dans l'entitee
            for point_obj in objets:
                if entitee_hitbox[0][0] < point_obj[0] < entitee_hitbox[1][0] and entitee_hitbox[0][1] < point_obj[1] < entitee_hitbox[1][1]:
                    return True, ("entitee" if cle != "joueur" else "joueur")


            # si l'entite se trouve sur les 2 cote de la boite en x
            if objets[0][0] > entitee_hitbox[0][0] and objets[1][0] < entitee_hitbox[1][0] and objets[0][1] < entitee_hitbox[0][1] and objets[1][1] > entitee_hitbox[1][1]:
                return True, ("entitee" if cle != "joueur" else "joueur")
            # si l'entite se trouve sur les 2 cote de la boite en y
            if objets[0][1] > entitee_hitbox[0][1] and objets[1][1] < entitee_hitbox[1][1] and objets[0][0] < entitee_hitbox[0][0] and objets[1][0] > entitee_hitbox[1][0]:
                return True, ("entitee" if cle != "joueur" else "joueur")


            
        # si l'entitee n'est pas le joueur alors elle n'a pas besoin des objets
        if entitee_nom != "joueur":
            return True, "rien"

        # les objets
        # faire l'iteration pour les entities
        for objets in self.dict_hit["objets"].values():
            # si un coin de l'entitee se trove dans l'objet
            for point_hitbox in entitee_hitbox:
                if objets[0][0] < point_hitbox[0] < objets[1][0] and objets[0][1] < point_hitbox[1] < objets[1][1]:
                    return True, "objets"
            
            # si un coin de l'objet se trouve dans l'entitee
            for point_obj in objets:
                if entitee_hitbox[0][0] < point_obj[0] < entitee_hitbox[1][0] and entitee_hitbox[0][1] < point_obj[1] < entitee_hitbox[1][1]:
                    return True, "objets"


            # si l'entite se trouve sur les 2 cote de la boite en x
            if objets[0][0] > entitee_hitbox[0][0] and objets[1][0] < entitee_hitbox[1][0] and objets[0][1] < entitee_hitbox[0][1] and objets[1][1] > entitee_hitbox[1][1]:
                return True, "objets"
            # si l'entite se trouve sur les 2 cote de la boite en y
            if objets[0][1] > entitee_hitbox[0][1] and objets[1][1] < entitee_hitbox[1][1] and objets[0][0] < entitee_hitbox[0][0] and objets[1][0] > entitee_hitbox[1][0]:
                return True, "objets"


        # si la position est correcte
        return True, "rien"













##### _____ Getion des monstres _____ #####

class GetionDesMonstres:
    def __init__(self):
        self.dictionnaire_monstres = {
            "monstre_1" : [10, 10]
        }
    

    def update(self):
        pass

    def draw(self):
        pass













##### _____ Monstres _____ #####

class Monstres:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass








# App
# Player
# arme
# CamDecor
# Hitbox
# GetionDesMontres
# Monstres



if __name__ == '__main__':
    App()