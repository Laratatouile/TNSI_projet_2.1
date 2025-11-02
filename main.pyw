import pyxel
import time
import math
import random





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
                "sortie" : [(155, 395), (171, 411)],
                "vie_0" : [(125, 155), (141, 161)],
                "vie_1" : [(485, 160), (501, 176)],
                "vie_2" : [(5, 275), (21, 291)],
                "balle_0" : [(270, 100), (286, 116)],
                "balle_1" : [(445, 30), (461, 46)],
                "balle_2" : [(395, 310), (411, 326)],
                "balle_3" : [(325, 365), (341, 381)],
                "masse_0" : [(385, 305), (401, 321)],
                "masse_1" : [(95, 185), (111, 201)],
                "masse_2" : [(35, 395), (51, 411)]
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
            "joueur" : {
                "joueur" : [(35, 35), (51, 51)]
            },
            "entitees" : {
                "monstre_1" : [(5, 5), (21, 21)],
                "monstre_2" : [(235, 35), (241, 41)],
                "monstre_3" : [(5, 235), (21, 241)],
                "monstre_4" : [(295, 95), (311, 111)],
                "monstre_5" : [(480, 130), (496, 146)],
                "monstre_6" : [(475, 395), (491, 411)],
                "monstre_7" : [(475, 280), (491, 296)],
                "monstre_8" : [(305, 300), (321, 316)],
                "monstre_9" : [(35, 455), (51, 471)],
                "monstre_10" : [(225, 424), (241, 441)],
                "monstre_11" : [(265, 450), (281, 466)]
            }
        }
        self.endroit = "jeu"


        

        ###  /!\ parametres du ray tracing  ###

        self.dict_ray_tracing = {
            "on" : False,
            "precision" : 1,
            "angle" : 60,
            "nombre_rayons" : 100
        }
        plein_ecran = False



        
        # initialisation des classes
        self.hitbox = Hitbox(self.dict_objets_murs)
        self.player = Player(self.hitbox, [self.dict_objets_murs["joueur"]["joueur"][0][0], self.dict_objets_murs["joueur"]["joueur"][0][1]])
        self.cam_decors = CamDecors(self.dict_objets_murs)
        self.arme = Arme(self.hitbox)
        self.getion_monstres = GetionDesMonstres(self.hitbox)
        if self.dict_ray_tracing["on"]:
            self.ray_tracing = RayTracing(self.hitbox, self.dict_ray_tracing["precision"], self.dict_ray_tracing["angle"], self.dict_ray_tracing["nombre_rayons"])
        self.ui = UI(self.player, self.cam_decors)


        # lancement de pyxel
        pyxel.fullscreen(plein_ecran)
        pyxel.run(self.update, self.draw)




    def update(self):
        # si on joue
        if self.endroit == "jeu":
            if self.player.update() in [-1, 1]:
                self.endroit = "sortie"
            self.getion_monstres.update()
            if self.player.arme_tir[0] == "explosion" and self.player.arme_tir[1] == True:
                self.arme.tir(self.player.x, self.player.y, self.player.direction, "explosion")
                self.player.arme_tir = "explosion", False
            elif self.player.arme_tir[0] == "balle" and self.player.arme_tir[1] == True:
                self.arme.tir(self.player.x, self.player.y, self.player.direction, "balle")
                self.player.arme_tir = "balle"
            self.arme.update(self.player.direction, [self.player.x, self.player.y])
            self.cam_decors.update(self.player.x, self.player.y, self.hitbox.dict_pos_entitee, self.hitbox.dict_pos_objets)
            self.ui.update()

            if pyxel.btnp(pyxel.KEY_K):
                with open("file.txt", "w") as fichier:
                    for layer in self.hitbox.map:
                        ligne = ""
                        for case in layer:
                            ligne += str(case)[0]
                        fichier.write(ligne)    

        # si on est sorti du labyrinthe
        elif self.endroit == "sortie":
            pyxel.quit()





    def draw(self):
        if self.endroit == "jeu":
            self.cam_decors.draw()
            self.getion_monstres.draw()
            # le ray tracing n'est en fait qu'un affichage c'est pourquoi on realise les calculs dans le draw
            if self.dict_ray_tracing["on"]:
                self.ray_tracing.update([self.player.x, self.player.y], self.player.direction)
                self.ray_tracing.draw()

            self.player.draw()
            self.arme.draw()
            self.ui.draw()












##### _____ CamDecors _____ #####

class CamDecors:
    def __init__(self, dictionnaire_hitbox:dict):
        # plage_x, plage_y
        self.camera = [-5, -5]
        self.liste_pos_sortie = [32, 48, 64, 48]
        self.couleur_mur = 0

        # on cree une map qui contient les pixels avec les murs pour ne pas surcharger les calculs a chaque fois
        self.map = [[False]*505 for _ in range(505)]
        for (x1, y1), (x2, y2) in dictionnaire_hitbox["murs"].values():
            for y in range(y1, y2):
                for x in range(x1, x2):
                    self.map[y][x] = True




    def update(self, x_player:int, y_player:int, dict_pos_entitee:dict, dict_pos_objets:dict) -> None:
        self.dict_pos_entitee = dict_pos_entitee
        self.dict_pos_objets = dict_pos_objets

        
        # reajuster la camera en x
        if -5 <= x_player <= 100:
            self.camera[0] = -5
        elif 397 <= x_player <= 500:
            self.camera[0] = 294
        else:
            self.camera[0] = x_player - 103
        # et en y
        if -5 <= y_player <= 128:
            self.camera[1] = -5
        elif 372 <= y_player <= 500:
            self.camera[1] = 244
        else:
            self.camera[1] = y_player - 128
        



    def draw(self):
        # tout effacer
        pyxel.cls(5)


        # dessiner toutes les choses
        for nom, (x, y, l, h) in self.dict_pos_objets.items():
            if nom == "sortie":
                pyxel.blt(
                    x,
                    y,
                    0,
                    self.liste_pos_sortie[self.calcul_nombre_temps(4, 7)],
                    32,
                    16,
                    16,
                    5
                )
            elif nom.startswith("vie"):
                pyxel.blt(
                    x,
                    y,
                    0,
                    51, 203,
                    10, 10,
                    5
                )
            elif nom.startswith("balle"):
                pyxel.blt(
                    x,
                    y,
                    0,
                    3, 203,
                    10, 10,
                    5
                )
            elif nom.startswith("masse"):
                pyxel.blt(
                    x,
                    y,
                    0,
                    19, 203,
                    10, 10,
                    5
                )
        for y, ligne in enumerate(self.map):
            for x, case in enumerate(ligne):
                if case == 1:
                    pyxel.rect(
                        x, y,
                        1, 1,
                        self.couleur_mur
                    )
        # il manque les murs nords et ouest du a leur position donc on les rajoutes
        pyxel.rect(
            -5, -5,
            505, 5,
            self.couleur_mur
        )
        pyxel.rect(
            -5, -5,
            5, 505,
            self.couleur_mur
        )
                    


        pyxel.camera(self.camera[0], self.camera[1])


    
    def calcul_nombre_temps(self, nombre_max:int, vitesse:int=5) -> int:
        return pyxel.frame_count // vitesse % nombre_max
    

    def recup_camera(self):
        return self.camera





##### _____ Hitbox _____ #####

class Hitbox:
    def __init__(self, dictionnaire_objets:dict) -> None:
        """
            initialise la class des hitbox
        """

        # regles de passage
        self.regles_passages = {
            "joueur" : ([1], [3, 4, 5, 8, 9]),
            "monstre" : ([1], []),
            "lumiere" : ([1], []),
            "balle" : ([1, 3, 5, 8, 9], [])
        }


        # on cree la map en virtuel avec des murs pour calculer les hitbox comme un pro ;)
        # les variables
        self.dict_pos_entitee = {}
        self.dict_pos_objets = {}
        # cree la map vide
        self.map = [[0]*506 for _ in range(506)]
        # ajoute les objets
        # rien = 0, mur = 1, joueur = 2, monstre = 3, objet = 4, joueur+monstre = 5, monstre+monstre = 6
        for chose, dico in dictionnaire_objets.items():
            for nom, ((x1, y1), (x2, y2)) in dico.items():
                for y in range(y1, y2+1):
                    for x in range(x1, x2+1):
                        if chose == "murs":
                            self.map[y][x] = 1
                        elif chose == "joueur":
                            self.map[y][x] = 2
                        elif chose == "monstre":
                            self.map[y][x] = 30
                        elif chose == "objets":
                            self.map[y][x] = 4
                # ajouter les positions dans les dictionnaires pour permettre le deplacement
                if chose == "entitees":
                    self.dict_pos_entitee[nom] = [
                        x1, y1,
                        16, 16
                    ]
                elif chose == "objets":
                    self.dict_pos_objets[nom] = [
                        x1, y1,
                        10, 10
                    ]
                elif chose == "joueur":
                    self.player_x, self.player_y = x1, y1
        
        # dictionnaire qui permet de transformer le chiffre de la map en truc utilisable en privilegiant le plus important
        self.transformation = {
            0 : "rien",
            1 : "mur",
            2 : "joueur",
            3 : "entitee",
            4 : "objet",
            5 : "entitee",
            6 : "balle",
            7 : "balle",
            8 : "balle",
            9 : "entitee"
        }

        return None



    def update(self, entitee_nom:str, entitee_position:list) -> bool:
        """
            entitee_nom : le nom de l'entitee

            entitee_position : la position de l'entitee [x, y]

            renvoie un tuple qui contient :
            - si le mouvement est valide
            - la chose qui fait que ce mouvement est valide ou non
            - si on touche quelque chose l'identifiant (id) de ce qu'on touche
        """

        # calculer les choses necessaires aux hitbox
        if entitee_nom == "lumiere":
            largeur = hauteur = 1
        elif entitee_nom == "monstre":
            largeur = hauteur = 16
            entitee_hitbox = [
                [entitee_position[0], entitee_position[1]],
                [entitee_position[0]+largeur, entitee_position[1]+hauteur]
            ]
        elif entitee_nom == "joueur":
            decalage_y = 1
            largeur = 15
            hauteur = 14
            entitee_hitbox = [
                [entitee_position[0], entitee_position[1]+decalage_y],
                [entitee_position[0]+largeur, entitee_position[1]+hauteur+decalage_y]
            ]
        elif entitee_nom == "balle":
            decalage_x = 8
            decalage_y = 5
            largeur = 8
            hauteur = 5
            entitee_hitbox = [
                [entitee_position[0]+decalage_x, entitee_position[1]+decalage_y],
                [entitee_position[0]+decalage_x+largeur, entitee_position[1]+decalage_y+hauteur]
            ]
        else:
            largeur = hauteur = 16
            entitee_hitbox = [
                [entitee_position[0], entitee_position[1]],
                [entitee_position[0]+largeur, entitee_position[1]+hauteur]
            ]


        # calcul des hitbox

        # si la chose mesure un pixel de cote
        if largeur == hauteur == 1:
            retour = self.hitbox_petite(entitee_position, entitee_nom)
            if retour != None:
                return retour

        # si elle en mesure plus
        else:
            retour = self.hitbox_grande(entitee_hitbox, entitee_nom)
            if retour[1] != "rien":
                return retour



        # la position est correcte
        return True, "rien"



    def hitbox_grande(self, entitee_hitbox:list, entitee_nom:str) -> tuple:
        """
            calcule si un mur se trouve dans un objet completement
        """
        def fct(entitee_hitbox:list) -> bool:
            """
                renvoie si l'entitee a le droit de passer ou pas
            """
            # faire une liste avec tous les cas ou l'entitee n'a pas le droit de passer ou a des conditions
            passage = self.regles_passages[entitee_nom][0] + self.regles_passages[entitee_nom][1]
            trouve = None

            # pour les cotes haut et bas
            (x1, y1), (x2, y2) = entitee_hitbox
            for x in range(x1, x2+1):
                case = int(str(self.map[y1][x])[0])
                if case in passage:
                    trouve = case
                    if case in self.regles_passages[entitee_nom][0]:
                        return False, case
                case = int(str(self.map[y2][x])[0])
                if case in passage:
                    trouve = case
                    if case in self.regles_passages[entitee_nom][0]:
                        return False, case

            # les cotes de droite et de gauche
            for y in range(y1, y2+1):
                case = int(str(self.map[y][x1])[0])
                if case in passage:
                    trouve = case
                    if case in self.regles_passages[entitee_nom][0]:
                        return False, case
                case = int(str(self.map[y][x2])[0])
                if case in passage:
                    trouve = case
                    if case in self.regles_passages[entitee_nom][0]:
                        return False, case

            # les cases de l'entitee ne sont pas sur des cases qui contiennent des actions
            if trouve == None:
                return True, 0
            return False, trouve

        
        # detection d'un mur dans l'entitee
        # on imbrique une fonction pour centraliser les retours
        (x1, y1), (x2, y2) = entitee_hitbox
        if 0 <= x1 and x2 <= 505 and 0 <= y1 and y2 <= 505:
            retour = fct(entitee_hitbox)
            deplacement = retour[1] in self.regles_passages[entitee_nom][1]
            if not retour[0] and entitee_nom == "joueur":
                # calculer si le deplacement est possible
                if retour[1] in [4, 9]:
                    id_obj = self.recup_id(entitee_hitbox[0], "objet")
                    return deplacement, "objet", id_obj
                return deplacement, self.transformation[retour[1]]
            elif not retour[0]:
                return deplacement, self.transformation[retour[1]]

        # hors de la map
        else:
            return False, "mur"

        # si il n'y a rien
        return True, "rien"



    def hitbox_petite(self, entitee_position:list, entitee_nom:str) -> tuple:
        """
            realise un calcul simple pour savoir si un objet est dans un mur ou non
            fonction utilie pour le calcul des lumieres qui peuvent provoquer des lags extremes
        """
        x, y = entitee_position
        if 0 < x < 500 and 0 < y < 500:
            case = self.map[y][x]
            if case == 1:
                return False, "mur"
        else:
            # hors de la map
            return False, "mur"
        return None



    def recup_id(self, position:list, truc:str, dist_xy:list[int, int]=[16, 16]) -> str:
        """
            recupere l'identifient de l'objet ou du monstre a partir d'une position et le supprimer
        """
        if truc == "objet":
            for nom, (x, y, l, h) in self.dict_pos_objets.items():
                if x-dist_xy[0] <= position[0] <= x+dist_xy[0] and y-dist_xy[1] <= position[1] <= y+dist_xy[1]:
                    self.retire(nom, truc)
                    return nom
        elif truc == "monstre":
            for nom, (x, y, l, h) in self.dict_pos_entitee.items():
                if x-dist_xy[0] <= position[0] <= x+dist_xy[0] and y-dist_xy[1] <= position[1] <= y+dist_xy[1]:
                    self.retire(nom, truc)
                    return nom
        return "rien" # attention ca marche pas hein



    def deplace_monstre(self, nom:str, pos_x:int, pos_y:int) -> None:
        """
            deplace la position d'une entitee vers pos_x, pos_y
        """
        # recuperer les informations de l'entitee
        x, y, l, h  = self.dict_pos_entitee[nom]
        # retirer les cases de la grille virtuelle
        self.retire(nom, "monstre")
        # remettre les cases de la nouvelle position sur la nouvelle grille et dans le infos des entititeed
        self.ajoute_monstre(nom, [pos_x, pos_y, l, h])



    def deplace_joueur(self, pos_x:int, pos_y:int) -> None:
        """
            deplace le joueur vers la pos_x, pos_y
        """
        self.retire("", "joueur")
        self.player_x = pos_x
        self.player_y = pos_y
        self.ajoute_joueur(pos_x, pos_y)    



    def retire(self, nom:str, truc:str) -> None:
        """
            retire le truc de la map
            (soit un "objet" soit une "entitee")
        """
        if truc == "monstre":
            x, y, l, h  = self.dict_pos_entitee[nom]
            for yi in range(y, y+h+1):
                for xi in range(x, x+l+1):
                    case = int(str(self.map[yi][xi])[0])
                    if case in [3, 5, 8, 9]:
                        nombre = int(str(self.map[yi][xi])[1:])-1
                        if nombre == 0:
                            if case == 3:
                                case = 0
                            elif case == 5:
                                case = 2
                            elif case == 8:
                                case = 6
                            elif case == 9:
                                case = 4
                        else:
                            case = int(f"{case}{nombre}")
                    self.map[yi][xi] = case
            del self.dict_pos_entitee[nom]

        elif truc == "objet":
            x, y, l, h  = self.dict_pos_objets[nom]
            for y in range(y, y+h+1):
                for x in range(x, x+l+1):
                    case = int(str(self.map[y][x])[0])
                    if case == 4:
                        case = 0
                    elif case == 9:
                        nombre = int(str(self.map[y][x])[1:])
                        case = int(f"3{nombre}")
                    self.map[y][x] = case
            del self.dict_pos_objets[nom]

        elif truc == "joueur":
            for y in range(self.player_y, self.player_y+17):
                for x in range(self.player_x, self.player_x+17):
                    case = int(str(self.map[y][x])[0])
                    if case == 2:
                        case = 0
                    elif case == 5:
                        nombre = int(str(self.map[y][x])[1:])
                        case = int(f"3{nombre}")
                    elif case == 7:
                        case == 6
                    self.map[y][x] = case

    

    def ajoute_monstre(self, nom:str, infos:list) -> None:
        """
            ajoute une entitee sur la map ;
            infos : [x, y, l, h]
        """
        self.dict_pos_entitee[nom] = infos.copy()
        x, y, l, h  = infos
        for yi in range(y, y+h+1):
            for xi in range(x, x+l+1):
                case = int(str(self.map[yi][xi])[0])
                if case in [0, 2, 3, 4, 5, 6, 8, 9]:
                    if case in [3, 5, 8, 9]:
                        nombre = int(str(self.map[yi][xi])[1:])+1
                        case = int(f"{case}{nombre}")
                    else:
                        if case == 0:
                            case = 31
                        elif case == 2:
                            case = 51
                        elif case == 4:
                            case = 91
                        elif case == 6:
                            case = 81
                    self.map[yi][xi] = case



    def ajoute_joueur(self, pos_x:int, pos_y:int) -> None:
        """
            met le joueur sur la carte a la position definie
        """
        for y in range(pos_y, pos_y+17):
            for x in range(pos_x, pos_x+17):
                case = int(str(self.map[y][x])[0])
                if case == 0:
                    case = 2
                if case in [3, 5]:
                    nombre = int(str(self.map[y][x])[1:])
                    case = int(f"5{nombre}")
                elif case == 6:
                    case = 7
                self.map[y][x] = case


    
    def recup_pos_monstre(self, nom:str) -> list:
        """ renvoie la position du monstre """
        return self.dict_pos_entitee[nom][0:2]





##### _____ Armes _____ #####

class Arme:
    def __init__(self, hitbox:Hitbox):
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

            # si elle va vers la droite
            if balle[2] == 0:
                balle[0] += self.vitesse
                retour = self.hitbox.update("balle", [balle[0], balle[1]])
                if retour[1] == "mur" :
                    balle[0] -= self.vitesse
                    if balle[4] == "explosion":
                        self.explosion(balle[0], balle[1])
                    self.liste_balles.pop(i)
            
            # si elle va vers le bas
            elif balle[2] == 1:
                balle[1] += self.vitesse
                retour = self.hitbox.update("balle", [balle[0], balle[1]])
                if retour[1] == "mur":
                    balle[1] -= self.vitesse
                    if balle[4] == "explosion":
                        self.explosion(balle[0], balle[1])
                    self.liste_balles.pop(i)
            
            # si elle va vers la gauche
            elif balle[2] == 2:
                balle[0] -= self.vitesse
                retour = self.hitbox.update("balle", [balle[0], balle[1]])
                if retour[1] == "mur":
                    balle[0] += self.vitesse
                    if balle[4] == "explosion":
                        self.explosion(balle[0], balle[1])
                    self.liste_balles.pop(i)

            
            # si elle va vers le bas
            else:
                balle[1] -= self.vitesse
                retour = self.hitbox.update("balle", [balle[0], balle[1]])
                # si on touche un truc
                if retour[1] == "mur":
                    balle[1] += self.vitesse
                    if balle[4] == "explosion":
                        self.explosion(balle[0], balle[1])
                    self.liste_balles.pop(i)

            
            # si on touche un monstre
            if retour[1] == "entitee":
                if balle[4] == "explosion":
                    self.explosion(balle[0], balle[1])
                    self.hitbox.recup_id([balle[0], balle[1]], "monstre")
                else:
                    self.hitbox.recup_id([balle[0], balle[1]], "monstre", [8, 8])
                self.liste_balles.pop(i)

                    





        # calculer la position du coup de feu du fusil si il a tire
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





##### _____ Player _____ #####

class Player:
    def __init__(self, hitbox:Hitbox, position:list):
        # ses variables
        self.x, self.y = position
        self.balles = 3
        self.vie = 3
        self.sortie = 0
        self.vie_temps = 0
        self.masse = 3
        self.arme_selec = "masse"
        self.arme_liste = [0, ["masse", "fusil"]]
        # la classe qui gere les hitbox
        self.hitbox = hitbox
        self.arme_tir = "balle", False
        # direction 0 : droite, 1 : bas, 2 : gauche, 3 : haut
        self.direction = 0
        self.vitesse = 2
        self.mega_player = False
        self.frappe = 0


    def update(self):
        # initialisations des variables au debut de chaque iteration
        self.bouge = False
        if self.vie_temps > 0:
            self.vie_temps -= 1
        if self.frappe > 0:
            self.frappe -= 1

        

        # changement d'arme
        if pyxel.btnp(pyxel.KEY_E):
            self.arme_liste[0] += 1
            if self.arme_liste[0] == len(self.arme_liste[1]):
                self.arme_liste[0] = 0
            self.arme_selec = self.arme_liste[1][self.arme_liste[0]]




        # mouvements du joueur
        # Haut
        if self.frappe == 0:
            if pyxel.btn(pyxel.KEY_Z):
                for _ in range(self.vitesse):
                    self.y -= 1
                    if not self.deplacement_valide():
                        self.y += 1
                    else:
                        self.bouge = True
                self.direction = 3
            # Bas
            if pyxel.btn(pyxel.KEY_S):
                for _ in range(self.vitesse):
                    self.y += 1
                    if not self.deplacement_valide():
                        self.y -= 1
                    else:
                        self.bouge = True
                self.direction = 1
            # Droite
            if pyxel.btn(pyxel.KEY_D):
                for _ in range(self.vitesse):
                    self.x += 1
                    if not self.deplacement_valide():
                        self.x -= 1
                    else:
                        self.bouge = True
                self.direction = 0
            # Gauche
            if pyxel.btn(pyxel.KEY_Q):
                for _ in range(self.vitesse):
                    self.x -= 1
                    if not self.deplacement_valide():
                        self.x += 1
                    else:
                        self.bouge = True
                self.direction = 2

        # si le joueur ne se deplace pas on doit quand meme verifier si un monstre ne touche pas le joueur
        if not self.bouge:
            self.deplacement_valide()
        


        # les actions du joueur
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.arme_selec == "masse":
                if self.masse != 0:
                    self.frappe = 7
                    self.frappe_unite()
            elif self.arme_selec == "fusil":
                if self.balles != 0:
                    self.balles -= 1
                    if self.mega_player == True:
                        self.arme_tir = "explosion", True
                    else:
                        self.arme_tir = "balle", True

        return self.sortie
            


    def deplacement_valide(self):
        """ renvoie si le deplacement est valide ou non """
        # calculer si le deplacement est valide
        retour = self.hitbox.update("joueur", [self.x, self.y])
        
        # si il ya a des actions a faire on les faits
        if retour[1] == "objet":
            self.objet(retour[2])
        elif retour[1] == "entitee":
            if self.vie_temps == 0:
                self.vie -= 1
                self.vie_temps = 30
                if not self.vie > 0:
                    self.sortie = -1
        
        if retour[0]:
            self.hitbox.deplace_joueur(self.x, self.y)
        return retour[0]
        
        



    def draw(self) -> None:
        """ affiche le personnage """
        # le personnage
        # si il a la masse
        if self.arme_liste[0] == 0:
            # calculer la position de l'image du personnage a afficher
            if self.frappe > 0:
                pos_perso = [16, 88]
            else:
                if not self.bouge:
                    pos_perso = [0, 72]
                else:
                    pos_perso = [[0, 88], [16, 88], [0, 104], [16, 104]][self.calcul_nombre_temps(4, 7)]
            # afficher le personnage
            pyxel.blt(
                self.x,
                self.y,
                0,
                pos_perso[0],
                pos_perso[1],
                (-16 if self.direction == 2 else 16),
                16,
                5,
                rotate=((90 * self.direction) if (90 * self.direction) != 180 else 0)
            )

        # si il a le fusil
        elif self.arme_liste[0] == 1:
            if self.bouge:
                pos_perso = [[16, 24], [0, 8], [16, 8], [0, 24]][self.calcul_nombre_temps(4, 2)]
            else:
                pos_perso = [0, 8]
            pyxel.blt(
                self.x,
                self.y,
                0,
                pos_perso[0],
                pos_perso[1],
                (-16 if self.direction == 2 else 16),
                16,
                5,
                rotate=((90 * self.direction) if (90 * self.direction) != 180 else 0)
            )







    def calcul_nombre_temps(self, nombre_max:int, vitesse:int=5) -> int:
        """ calcul qui permet de faire l'annimation du personnage """
        return pyxel.frame_count // vitesse % nombre_max
    

    def recup_ui(self) -> tuple:
        """ renvoie les informations utiles pour afficher l'UI """
        return self.balles, self.vie, self.masse
    

    def objet(self, nom:str) -> None:
        """ realise les actions necessaires si le joueur touche un objet """
        # appliquer les reactions sur le joueur
        if nom.startswith("balle"):
            self.balles += 1
        elif nom.startswith("vie"):
            self.vie += 1
        elif nom.startswith("sortie"):
            self.sortie = 1
        elif nom.startswith("masse"):
            self.masse += 1


    def frappe_unite(self) -> None:
        """ frappe une unite et la tue """
        x, y = self.x, self.y
        if self.direction == 0:
            x += 16
        elif self.direction == 1:
            y += 16
        elif self.direction == 2:
            x -= 16
        else:
            y -= 16
        
        self.hitbox.recup_id([x, y], "monstre")





##### _____ Getion des monstres _____ #####

class GetionDesMonstres:
    def __init__(self, hitbox:Hitbox) -> None:
        """ construit sa liste de monstres avec ceux presents de base dans la liste hitbox """
        self.hitbox = hitbox
        self.dict_monstres = {}
        for nom, monstre in self.hitbox.dict_pos_entitee.items():
            self.dict_monstres[nom] = Monstre(monstre[0], monstre[1], random.randint(0, 3), self.hitbox, nom)
    

    def update(self) -> None:
        """ met a jour chaqun des monstres """
        liste_supp = []
        for nom in self.dict_monstres.keys():
            if not nom in self.hitbox.dict_pos_entitee.keys():
                liste_supp.append(nom)

        for nom in liste_supp:
            del self.dict_monstres[nom]

            
        for monstre in self.dict_monstres.values():
            monstre.update()

    def draw(self) -> None:
        """ affiche les monstres un par un avec une boucle for """
        for monstre in self.dict_monstres.values():
            monstre.draw()





##### _____ Monstre _____ #####

class Monstre:
    def __init__(self, pos_x:int, pos_y:int, direction:int, hitbox:Hitbox, nom:str):
        self.x = pos_x
        self.y = pos_y
        self.direction = direction
        self.hitbox = hitbox
        self.nom = nom
        self.VITESSE = 2
        # probabilite de tourner
        self.tourner = 50



    def update(self):
        """ le monstre doit se deplacer le plus vers le joueur possible si il rencontre un mur il va chercher un autre passage et avancer jusqu'a un autre mur """
        # recuperer notre position au pres de hitbox
        self.x, self.y = self.hitbox.recup_pos_monstre(self.nom)
        if self.direction == 0:
            self.x += self.VITESSE
            if not self.deplacement_valide():
                self.x -= self.VITESSE
                if random.randint(0, 1) == 1:
                    self.direction = 3
                else:
                    self.direction = 1
        if self.direction == 1:
            self.y += self.VITESSE
            if not self.deplacement_valide():
                self.y -= self.VITESSE
                if random.randint(0, 1) == 1:
                    self.direction = 0
                else:
                    self.direction = 2
        if self.direction == 2:
            self.x -= self.VITESSE
            if not self.deplacement_valide():
                self.x += self.VITESSE
                if random.randint(0, 1) == 1:
                    self.direction = 1
                else:
                    self.direction = 3
        if self.direction == 3:
            self.y -= self.VITESSE
            if not self.deplacement_valide():
                self.y += self.VITESSE
                if random.randint(0, 1) == 1:
                    self.direction = 2
                else:
                    self.direction = 0



        # tourner aleatoirement pour plus de suspense
        if random.randint(0, self.tourner) == 0:
            self.direction = random.randint(0, 3)

        # deplacer l'entitee dans la base des hitbox
        
        self.hitbox.deplace_monstre(self.nom, self.x, self.y)
        


    
    def deplacement_valide(self):
        retour = self.hitbox.update("monstre", [self.x, self.y])
        return retour[0]
    


    def draw(self):
        pyxel.blt(
            self.x, self.y,
            0,
            16*self.calcul_nombre_temps(4, 5),
            136,
            (-16 if self.direction == 2 else 16), 16,
            colkey=5,
            rotate=((90 * self.direction) if (90 * self.direction) != 180 else 0)
        )

    
    def calcul_nombre_temps(self, nombre_max:int, vitesse:int=5) -> int:
        return pyxel.frame_count // vitesse % nombre_max











##### _____ ray tracing _____ #####
# Pour le raytracing j'ai choisi un rayon qui part du personnage et qui va tout droit selon un angle
# On pourra modifier l'angle de vision de la camera et on pourra aussi modifier le nombre de rayons calcules pour eviter de faire trop ralentir le jeu.
# Pour calculer les cases eclairees on creera un rayon qu'on agrandira de 1 pixel a chaque iteration jusqu'a tomber sur une case de mur.

class RayTracing:
    def __init__(self, hitbox:Hitbox, precision:int, angle:int, nombre_rayons:int):
        self.hitbox = hitbox
        self.precision = precision

        # creer une liste avec tous les rayons a tester
        decalage_angle = angle / nombre_rayons
        self.liste_angles = [-(angle/2) + i*decalage_angle for i in range(nombre_rayons)]

        # la grille qui contiendra les pixels qui pourront etre affiches car sous la lumiere
        self.g_lumiere = [[False]*505 for _ in range(505)]
    

    def update(self, pos_perso:list, direction:int):
        # calculer la position de depart de la lumiere
        if direction == 0:
            pos_perso[0] += 15
            pos_perso[1] += 7
        elif direction == 1:
            pos_perso[0] += 8
            pos_perso[1] += 15
        elif direction == 2:
            pos_perso[1] += 7
        else:
            pos_perso[0] += 7


        self.g_lumiere = [[False]*505 for _ in range(505)]
        x, y = pos_perso
        # pour chaque rayon
        for angle in self.liste_angles:
            self.calcul_rayon(x, y, angle, direction)

        
    def calcul_rayon(self, pos_x:int, pos_y:int, angle:float, direction:int):
        """
            calcule le rayon jusqu'a tomber sur la couleur 11
        """
        longueur = 0
        position_x, position_y = pos_x, pos_y
        while self.hitbox.update("lumiere", [position_x, position_y])[0]:
            for _ in range(self.precision):
                longueur += 1
                self.g_lumiere[position_y][position_x] = True
                position_x, position_y = self.calculer_pos_pixel(pos_x, pos_y, angle, longueur, direction)


    def calculer_pos_pixel(self, pos_x:int, pos_y:int, angle:float, longueur:float, direction:int) -> tuple:
        """
            calcule la position d'un pixel avec les informations donnees
        """
        position = []
        # calculer x et y pour une orientation de 0 mais on changera dans l'ajout
        decalage_x = round(longueur*math.cos(math.radians(angle)))
        decalage_y = round(longueur*math.sin(math.radians(angle)))
        # les ajouter
        # direction de base
        if direction == 0:
            position = [pos_x + decalage_x, pos_y + decalage_y]
        elif direction == 1:
            position = [pos_x - decalage_y, pos_y + decalage_x]
        elif direction == 2:
            position = [pos_x - decalage_x, pos_y + decalage_y]
        else:
            position = [pos_x + decalage_y, pos_y - decalage_x]
        
        return position




    def draw(self):
        for y, ligne in enumerate(self.g_lumiere):
            for x, case in enumerate(ligne):
                if not case:
                    pyxel.pset(x, y, 0)







##### _____ UI _____ #####

class UI:
    def __init__(self, personnage:Player, cam_decors:CamDecors):
        self.personnage = personnage
        self.cam_decors = cam_decors


    def update(self):
        self.camera = self.cam_decors.recup_camera()
        self.balles, self.vie, self.masse = self.personnage.recup_ui()


    def draw(self):
        # calcul des variables
        x, y = self.camera[0] + 206, self.camera[1]

        ### affichage de l'ui
        # le fond noir
        pyxel.rect(
            x,
            y,
            50,
            256,
            0
        )

        # les balles
        pyxel.text(x+5, y+10, "balles :", 13)
        pyxel.blt(
            x+5,
            y+20,
            0,
            (0 if self.balles > 0 else 112),
            216,
            16, 16,
            5
        )
        if self.balles > 0:
            pyxel.text(x+25, y+25, f"X {self.balles}", 13)

        # la vie
        pyxel.text(x+5, y+40, "vie :", 13)
        pyxel.blt(
            x+5,
            y+50,
            0,
            48, 216,
            15, 15,
            5
        )
        pyxel.text(x+25, y+55, f"X {self.vie}", 13)

        # les masses
        pyxel.text(x+5, y+70, "masses :", 13)
        pyxel.blt(
            x+5,
            y+80,
            0,
            16, 216,
            15, 15,
            5
        )
        pyxel.text(x+25, y+85, f"X {self.masse}", 13)







# App
# CamDecor
# Hitbox
# arme
# Player
# GetionDesMontres
# Monstres
# ray tracing
# UI



if __name__ == '__main__':
    App()