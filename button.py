from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math

# Fungsi yang dijalankan ketika tombol ditekan
def on_button_click():
    # Hapus UI utama dan mulai program 3D
    destroy(ui_elements)
    start_3d_program()

# Fungsi untuk memulai program 3D
def start_3d_program():
    class Labkom(Entity):
        def __init__(self, position=(0, 0, 0)):
            super().__init__()

            # Simpan posisi sebagai properti dari kelas
            self.position = position

            # Lantai
            self.floor = Entity(model='plane', scale=(50, 1, 50), texture='white_cube', texture_scale=(70, 70), color=color.light_gray, collider='box')

            # Dinding
            self.depan = Entity(model='cube', scale=(15, 5, 0.1), position=(0, 2.5, -12.5), texture="img/wall.png", collider='box')
            self.belakang = Entity(model='cube', scale=(15, 5, 0.1), position=(0, 2.5, 12.5), texture="img/wall.png", collider='box')
            self.kanan = Entity(model='cube', scale=(0.1, 5, 25), position=(-7.5, 2.5, 0), color=color.gray, collider='box')
            self.kiri = Entity(model='cube', scale=(0.1, 5, 25), position=(7.45, 2.5, 0), color=color.gray, collider='box')
            self.kanan_atas = Entity(model='cube', scale=(1, 1.9, 25), position=(-7.5, 4, 0), color=color.light_gray, collider='box')
            self.kanan_bawah1 = Entity(model='cube', scale=(1, 5.9, 1), position=(-7.5, 0.1, -5), color=color.light_gray, collider='box')
            self.kanan_bawah1 = Entity(model='cube', scale=(1, 5.9, 1), position=(-7.5, 0.1, 5), color=color.light_gray, collider='box')
            self.kanan_bawah2 = Entity(model='cube', scale=(1, 5.9, 0.5), position=(-7.5, 0.1, -12.3), color=color.light_gray, collider='box')
            self.kanan_bawah2 = Entity(model='cube', scale=(1, 5.9, 0.5), position=(-7.5, 0.1, 12.3), color=color.light_gray, collider='box')

            # Atap
            self.roof = Entity(model='cube', scale=(15, 0.1, 25), position=(0, 5, 0), texture="img/roof.png", collider='box')

            # Meja mahasiswa
            table_positions = [
                (-5.5, 0.1, -5), (-3.6, 0.1, -5), (-1.7, 0.1, -5), (0.2, 0.1, -5), (2.1, 0.1, -5), (4, 0.1, -5),
                (4, 0.1, -2), (2.1, 0.1, -2), (0.2, 0.1, -2), (-1.7, 0.1, -2), (-3.6, 0.1, -2), (-5.5, 0.1, -2),
                (-5.5, 0.1, 1), (4, 0.1, 1), (2.1, 0.1, 1), (0.2, 0.1, 1), (-1.7, 0.1, 1), (-3.6, 0.1, 1),
                (4, 0.1, 4), (2.1, 0.1, 4), (0.2, 0.1, 4), (-1.7, 0.1, 4), (-3.6, 0.1, 4), (-5.5, 0.1, 4)
            ]

            for pos in table_positions:
                table = Entity(model='img/Table.fbx', texture='img/table.jpg', scale=(0.25, 0.25, 0.25), position=pos, texture_scale=(1, 1), texture_offset=(0, 0))

            # Kursi mahasiswa
            chair_positions = [
                (-5.4, 0.1, -4), (-3.6, 0.1, -4), (-1.8, 0.1, -4), (0.1, 0.1, -4), (1.8, 0.1, -4), (3.6, 0.1, -4),
                (-5.4, 0.1, -1), (-3.6, 0.1, -1), (-1.8, 0.1, -1), (0.1, 0.1, -1), (1.8, 0.1, -1), (3.6, 0.1, -1),
                (-5.4, 0.1, 2), (-3.6, 0.1, 2), (-1.8, 0.1, 2), (0.1, 0.1, 2), (1.8, 0.1, 2), (3.6, 0.1, 2),
                (-5.4, 0.1, 5), (-3.6, 0.1, 5), (-1.8, 0.1, 5), (0.1, 0.1, 5), (1.8, 0.1, 5), (3.6, 0.1, 5)
            ]

            for pos in chair_positions:
                Entity(model='img/Office Chair.fbx', texture='img/green.png', scale=(0.005, 0.005, 0.005), position=pos, rotation=(0, 270, 0), texture_scale=(1, 1), texture_offset=(0, 0))

            # Computer
            computer_positions = [
                (-5.2, 1.73, -5.3), (-3.3, 1.73, -5.3), (-1.5, 1.73, -5.3), (0.5, 1.73, -5.3), (2.2, 1.73, -5.3), (3.8, 1.73, -5.3),
                (-5.2, 1.73, -2.3), (-3.3, 1.73, -2.3), (-1.5, 1.73, -2.3), (0.5, 1.73, -2.3), (2.5, 1.73, -2.3), (3.8, 1.73, -2.3),
                (-5.2, 1.73, 0.7), (-3.3, 1.73, 0.7), (-1.5, 1.73, 0.7), (0.5, 1.73, 0.7), (2.2, 1.73, 0.7), (3.8, 1.73, 0.7),
                (-5.2, 1.73, 3.7), (-3.3, 1.73, 3.7), (-1.5, 1.73, 3.7), (0.5, 1.73, 3.7), (2.2, 1.73, 3.7), (3.8, 1.73, 3.7),
            ]

            for pos in computer_positions:
                Entity(model='img/computer.fbx', color=color.black, scale=(0.003, 0.003, 0.003), position=pos, rotation=(0, 270, 0))

            # Screen
            screen_positions = [
                (-5.2, 1.73, -5.26), (-3.3, 1.73, -5.26), (-1.5, 1.73, -5.26), (0.5, 1.73, -5.26), (2.2, 1.73, -5.26), (3.8, 1.73, -5.26),
                (-5.2, 1.73, -2.26), (-3.3, 1.73, -2.26), (-1.5, 1.73, -2.26), (0.5, 1.73, -2.26), (2.5, 1.73, -2.26), (3.8, 1.73, -2.26),
                (-5.2, 1.73, 0.74), (-3.3, 1.73, 0.74), (-1.5, 1.73, 0.74), (0.5, 1.73, 0.74), (2.2, 1.73, 0.74), (3.8, 1.73, 0.74),
                (-5.2, 1.73, 3.74), (-3.3, 1.73, 3.74), (-1.5, 1.73, 3.74), (0.5, 1.73, 3.74), (2.2, 1.73, 3.74), (3.8, 1.73, 3.74),
            ]

            for pos in screen_positions:
                Entity(model='img/screen.fbx', color=color.rgba(100, 100, 100, 0.9), scale=(0.05, 0.05, 0.05), position=pos, rotation=(0, 270, 0))
            
            # mouse
            mouse = Entity(model='img/kursor.obj', texture='img/kursor.jpg', scale=0.02, position=(-2.1, 1.3, -1.8), rotation=(270, 0, 90), double_sided=True)

            # Keyboard
            keyboard_positions = [
                (-5.2, 1.3, -4.8),  (-3.3, 1.3, -4.8),  (-1.5, 1.3, -4.8),  (0.5, 1.3, -4.8),  (2.2, 1.3, -4.8),  (3.8, 1.3, -4.8),
                (-5.2, 1.3, -1.8),  (-3.3, 1.3, -1.8),  (-1.5, 1.3, -1.8),  (0.5, 1.3, -1.8),  (2.4, 1.3, -1.8),  (3.8, 1.3, -1.8),
                (-5.2, 1.3, 1.2),  (-3.3, 1.3, 1.2),  (-1.5, 1.3, 1.2),  (0.5, 1.3, 1.2),  (2.2, 1.3, 1.2),  (3.8, 1.3,  1.2),
                (-5.2, 1.3, 4.2),  (-3.3, 1.3, 4.2),  (-1.5, 1.3, 4.2),  (0.5, 1.3, 4.2),  (2.2, 1.3, 4.2),  (3.8, 1.3, 4.2),
            ]
        
            for pos in keyboard_positions:
                Entity(model='img/keyboard.obj', texture='img/keyboard.png', scale=0.002, position=pos, rotation=(10, 0, 0), double_sided=True)

            # meja asprak
            meja_asprak = Entity(model='img/Desk.fbx', texture='img/white.png', scale=(0.037, 0.037, 0.037), position=(-3, 0.1, -7.5), rotation=(0, 0, 0))

            # kursi asprak
            kursi_asprak = Entity(model='img/Office Chair.fbx', texture='img/green.png', scale=(0.005, 0.005, 0.005), position=(-4, 0.1, -8.4), rotation=(0, 90, 0))
            kursi_asprak = Entity(model='img/Office Chair.fbx', texture='img/green.png', scale=(0.005, 0.005, 0.005), position=(-2.5, 0.1, -8.4), rotation=(0, 90, 0))

            # computer asprak
            comp_asprak = Entity(model='img/computer.fbx', color=color.black, scale=(0.003, 0.003, 0.003), position=(-2.5, 1.76, -7.5), rotation=(0, 90, 0))

            # screen asprak
            screen_asprak=Entity(model='quad', texture='img/ss.png', scale=(1, 0.5),position=(-2.5, 1.76, -7.55), rotation=(0, 0, 0), collider='box')
        
            # keyboard asprak
            keyboad_asprak=Entity(model='img/keyboard.obj', texture='img/keyboard.png', scale=0.002, position=(-2.5, 1.39, -8.1), rotation=(0, 180, 0), double_sided=True)
 
            # Pintu lab
            self.door=Entity(model='quad', texture='img/door_wood.png', scale=(5, 5, 5), position=(7.3, 1.7, -10.7), rotation=(0, 90, 0), collider='box')

            # projector
            projector = Entity(model='img/projector.glb', texture='img/projector.jpeg', scale=(0.015, 0.015, 0.015), position=(1.5, 1.5, -2), rotation=(0, 0, 0))

            # Papan tulis
            whiteboard = Entity(model='img/papantulis.obj', texture='img/papantulis.png', scale=(5, 4, 2), position=(7.25, 2.4, 1), rotation=(0, 270, 0))

            # AC
            ac = Entity(model='img/ac.obj', texture='img/ac2.png', scale=(0.003, 0.003, 0.003), position=(-6.8, 4, 4), rotation=(0, 90, 0))
            ac = Entity(model='img/ac.obj', texture='img/ac2.png', scale=(0.003, 0.003, 0.003), position=(-6.8, 4, -3), rotation=(0, 90, 0))
        
            # jendela kanan
            jendela_positions = [
                (-7.4, 2.1, 0.7), (-7.4, 2.1, -1), (-7.4, 2.1, -9.7), (-7.4, 2.1, -8), (-7.4, 2.1, 9.7), (-7.4, 2.1, 8),
            ]
        
            for pos in jendela_positions:
                Entity(model='quad', texture='img/jendela.jpg', scale=(1.7, 1.7), position=pos, rotation=(0, 270, 0))

            # jendela kiri atas
            jendela_positions = [
                (7.3, 4.2, 0.7), (7.3, 4.2, 1.7), (7.3, 4.2, 2.7), (7.3, 4.2, 3.7), (7.3, 4.2, 4.7),
                (7.3, 4.2, 6.7), (7.3, 4.2, 7.7), (7.3, 4.2, 8.7), (7.3, 4.2, 9.7), (7.3, 4.2, 10.7), 
                (7.3, 4.2, -1.7), (7.3, 4.2, -2.7), (7.3, 4.2, -3.7), (7.3, 4.2, -4.7), (7.3, 4.2, -5.7), 
                (7.3, 4.2, -7.7), (7.3, 4.2, -8.7), (7.3, 4.2, -9.7), (7.3, 4.2, -10.7), 
            ]
        
            for pos in jendela_positions:
                Entity(model='quad', texture='img/jendela.jpg', scale=(1, 1), position=pos, rotation=(0, 90, 180))

            # Tiang utama
            self.tiang_utama = Entity(
                model='cube',
                scale=(0.06, 1, 0.09),  # Diameter (X, Z) dan Height (Y)
                position=(1.5, 1, -11.5),  # Di bawah layar proyektor
                color=color.black
            )

            # Kaki-kaki penyangga
            self.penyangga = Entity(
                model='cube',
                scale=(0.06, 0.9, 0.06),  # Diameter (X, Z) dan Height (Y)
                position=(1.5, 0.2, -11.8),
                rotation=(45, 0, 0),  # Di bawah layar proyektor
                color=color.black
            )
            self.penyangga = Entity(
                model='cube',
                scale=(0.06, 0.9, 0.06),  # Diameter (X, Z) dan Height (Y)
                position=(1.2, 0.2, -11.5),
                rotation=(0, 0, 45),  # Di bawah layar proyektor
                color=color.black
            )
            self.penyangga = Entity(
                model='cube',
                scale=(0.06, 0.9, 0.06),  # Diameter (X, Z) dan Height (Y)
                position=(1.8, 0.2, -11.5),
                rotation=(0, 180, 45),  # Di bawah layar proyektor
                color=color.black
            )

            # Layar proyektor
            self.layar = Entity(
                model='cube',
                scale=(4, 2, 0.02),  # Width (X), Height (Y), Depth (Z) for the screen
                position=(1.5, 2.5, -11.5),  # Position the screen above the base
                color=color.white
            )

            # Garis hitam atas layar
            self.garis_atas = Entity(
                model='cube',
                scale=(4, 0.1, 0.02),  # Slightly wider and thinner than the screen
                position=(1.5, 3.55, -11.5),  # Positioned at the top edge of the screen
                color=color.black
            )

            # Garis hitam bawah layar
            self.garis_bawah = Entity(
                model='cube',
                scale=(4, 0.1, 0.02),  # Slightly wider and thinner than the screen
                position=(1.5, 1.47, -11.5),  # Positioned at the bottom edge of the screen
                color=color.black
            )

            # screen projector
            self.screen_projector = Entity(model='cube', texture='img/materi.mp4', scale=(3.3, 1.7, 0.001), position=(1.5, 2.4, -11.4), rotation=(0, 180, 0), collider='box')

            # Membuat objek yang akan bergerak di sekitar lingkaran
            self.asprak1 = Entity(model='img/people6.fbx', texture='img/people6.jpg', position=(5, 0.1, -10), scale=(1.8, 1.8, 1.8), double_sided=True, rotation=(0, 240, 0))  # Mengurangi skala objek


            # mahasiswa1
            mhs1_positions = [
                (-1.8, 1.1, -4.6), (3.6, 1.1, -4.6),
                (-5.4, 1.1, -1.6), (3.6, 1.1, -1.6),
                (-1.8, 1.1, 1.4), (1.8, 1.1, 1.4),
                (0.1, 1.1, 4.4),
            ]

            for pos in mhs1_positions:
                Entity(model='img/people3.glb', texture='img/people3.jpg', scale=(0.8, 0.8, 0.8), position=pos, rotation=(0, 180, 0), double_sided=True)

            # asprak2 (objek garis bresenham)
            self.character = Entity(model='img/people5.fbx', texture='img/people5.jpeg', scale=(0.017, 0.017, 0.017), position=(5, 0.1, -10), double_sided=True)
        



    #lab_kom.move_mhs2()

    labkom = Labkom(position=(0, 0, 0))
    FirstPersonController()
    

app = Ursina()

# Buat UI utama
ui_elements = Entity()
message = Text(text='Click the button to start the 3D program', scale= (7, 7), position=(0, 0.8), origin=(0, 0), color=color.azure, parent=ui_elements)
button = Button(text='start', scale=(3, 1), position=(0, 0), color=color.blue, parent=ui_elements)

# Ketika tombol diklik, jalankan fungsi on_button_click
button.on_click = on_button_click

app.run()
