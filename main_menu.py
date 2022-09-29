from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import recpl_2S_modes, recpl_4S_modes, recpl_2S_2C_modes, beam_1F_1C_modes, beam_2S_modes, cirpl_1C_modes
import set_freq_matrix, generate_txt_file
import recpl_4S_plot, recpl_2S_2C_plot, beam_1F_1C_plot, beam_2S_plot, cirpl_1C_plot
import reccav_modes, cylcav_modes

class main_GUI(ttk.Frame):

    def __init__(self, root):
        self.root = root

        ########First level: structures or shells

        #First level menu frame
        self.main_menu_frame = ttk.LabelFrame(self.root, text = 'Calculating the natural frequencies of structures and shells')

        #First level menu buttons
        self.structures_button = ttk.Button(self.main_menu_frame, text = "Structures", command = self.show_structures, width = 16, style = "Accent.TButton")
        self.shells_button = ttk.Button(self.main_menu_frame, text = "Shells", command = self.show_shells, width = 16, style = "Accent.TButton")


        ########Second level: which type of structures or shells

        #Second level menu frames
        self.structures_menu_frame = ttk.LabelFrame(self.root, text = 'Click on a structure to show its boundary conditions')
        self.shells_menu_frame = ttk.LabelFrame(self.root, text = 'Click on a shell to calculate its resonance frequencies')

        #Second level structures menu buttons
        self.rectangular_plate_button = ttk.Button(self.structures_menu_frame, text = "Rectangular Plate", command = self.show_rectangular_plate_boundaries_conditions, width = 16, style = "Accent.TButton")
        self.beam_button = ttk.Button(self.structures_menu_frame, text = "Beam", command = self.show_beam_boundaries_conditions, width = 16, style = "Accent.TButton")
        self.circular_plate_button = ttk.Button(self.structures_menu_frame, text = "Circular Plate", command = self.show_circular_plate_boundaries_conditions,  width = 16, style = "Accent.TButton")

        #Second level shells menu buttons
        self.rectangular_cavity_button = ttk.Button(self.shells_menu_frame, text = "Rectangular cavity", command = self.data_rectangular_cavity, width = 18, style = "Accent.TButton")
        self.cylindrical_cavity_button = ttk.Button(self.shells_menu_frame, text = "Cylindrical cavity", command = self.data_cylindrical_cavity, width = 18, style = "Accent.TButton")
        
        #Second level return buttons
        self.return_to_main_button_0 = ttk.Button(self.structures_menu_frame, text = "Return to main menu", command = self.main_menu, width = 18, style = "Accent.TButton")
        self.return_to_main_button_1 = ttk.Button(self.shells_menu_frame, text = "Return to main menu", command = self.main_menu, width = 18, style = "Accent.TButton")


        ########Third level: boundaries conditions

        #Third level menu frame for structures
        self.rectangular_plate_menu_frame = ttk.LabelFrame(self.root, text = 'Click on a rectangular plate boundary condition')
        self.beam_menu_frame = ttk.LabelFrame(self.root, text = 'Click on a beam boundary condition')
        self.circular_plate_menu_frame = ttk.LabelFrame(self.root, text = 'Click on a circular plate boundary condition')

        #Third level rectangular plate boundaries conditions buttons
        self.iso_rectangular_plate_2S = ttk.Button(self.rectangular_plate_menu_frame, text = "Isotropic SS", command = self.data_iso_rectangular_plate_2S, width = 20, style = "Accent.TButton")
        self.iso_rectangular_plate_4S = ttk.Button(self.rectangular_plate_menu_frame, text = "Isotropic SSSS", command = self.data_iso_rectangular_plate_4S, width = 20, style = "Accent.TButton")
        self.iso_rectangular_plate_2S_2C = ttk.Button(self.rectangular_plate_menu_frame, text = "Isotropic SCSC", command = self.data_iso_rectangular_plate_2S_2C, width = 20, style = "Accent.TButton")

        self.ortho_rectangular_plate_2S = ttk.Button(self.rectangular_plate_menu_frame, text = "Orthotropic SS", command = self.data_iso_rectangular_plate_2S, width = 20, style = "Accent.TButton")
        self.ortho_rectangular_plate_4S = ttk.Button(self.rectangular_plate_menu_frame, text = "Orthotropic SSSS", command = self.data_iso_rectangular_plate_4S, width = 20, style = "Accent.TButton")
        self.ortho_rectangular_plate_2S_2C = ttk.Button(self.rectangular_plate_menu_frame, text = "Orthotropic SCSC", command = self.data_iso_rectangular_plate_2S_2C, width = 20, style = "Accent.TButton")

        #Third level beam boundaries conditions buttons
        self.beam_1F_1C = ttk.Button(self.beam_menu_frame, text = "Beam FC", command = self.data_beam_1F_1C, width = 33, style = "Accent.TButton")
        self.beam_2S = ttk.Button(self.beam_menu_frame, text = "Beam SS", command = self.data_beam_2S, width = 33, style = "Accent.TButton")

        #Third level circular plate boundaries conditions buttons
        self.circular_plate_C = ttk.Button(self.circular_plate_menu_frame, text = "Circular plate C", command = self.data_circular_plate_C, width = 22, style = "Accent.TButton")

        #Third level return buttons    
        self.return_to_structures_from_rectangular_plate = ttk.Button(self.rectangular_plate_menu_frame, text = "Return to structures menu", command = self.show_structures, width = 22, style = "Accent.TButton")
        self.return_to_structures_from_beam = ttk.Button(self.beam_menu_frame, text = "Return to structures menu", command = self.show_structures, width = 22, style = "Accent.TButton")
        self.return_to_structures_from_circular_plate = ttk.Button(self.circular_plate_menu_frame, text = "Return to structures menu", command = self.show_structures, width = 22, style = "Accent.TButton")


        #######Fourth level: data acquisition 

        #Fourth level menu frames
        self.rectangular_plate_2S_data_frame = ttk.LabelFrame(self.root, text = 'Enter data to calculate the natural frequencies')
        self.rectangular_plate_4S_data_frame = ttk.LabelFrame(self.root, text = 'Enter data to calculate the natural frequencies')
        self.rectangular_plate_2S_2C_data_frame = ttk.LabelFrame(self.root, text = 'Enter data to calculate the natural frequencies')
        self.beam_1F_1C_data_frame = ttk.LabelFrame(self.root, text = 'Enter data to calculate the natural frequencies')
        self.beam_2S_data_frame = ttk.LabelFrame(self.root, text = 'Enter data to calculate the natural frequencies')
        self.circular_plate_1C_data_frame = ttk.LabelFrame(self.root, text = 'Enter data to calculate the natural frequencies')

        #Fourth level menu frame for data acquisition
        self.rectangular_cavity_data_frame = ttk.LabelFrame(self.root, text = 'Enter data to calculate the natural frequencies')
        self.cylindrical_cavity_data_frame = ttk.LabelFrame(self.root, text = 'Enter data to calculate the natural frequencies')

        #Setting up all the return buttons
        self.return_to_iso_recpl_bconditions_from_2S = ttk.Button(self.root, text = 'Return to boundary conditions', command = self.show_rectangular_plate_boundaries_conditions, style = "Accent.TButton")
        self.return_to_iso_recpl_bconditions_from_4S = ttk.Button(self.root, text = 'Return to boundary conditions', command = self.show_rectangular_plate_boundaries_conditions, style = "Accent.TButton")
        self.return_to_iso_recpl_bconditions_from_2S_2C = ttk.Button(self.root, text = 'Return to boundary conditions', command = self.show_rectangular_plate_boundaries_conditions, style = "Accent.TButton")

        self.return_to_ortho_recpl_bconditions_from_2S = ttk.Button(self.root, text = 'Return to boundary conditions', command = self.show_rectangular_plate_boundaries_conditions, style = "Accent.TButton")
        self.return_to_ortho_recpl_bconditions_from_4S = ttk.Button(self.root, text = 'Return to boundary conditions', command = self.show_rectangular_plate_boundaries_conditions, style = "Accent.TButton")
        self.return_to_ortho_recpl_bconditions_from_2S_2C = ttk.Button(self.root, text = 'Return to boundary conditions', command = self.show_rectangular_plate_boundaries_conditions, style = "Accent.TButton")

        self.return_to_beam_bconditions_from_1F_1C = ttk.Button(self.root, text = 'Return to boundary conditions', command = self.show_beam_boundaries_conditions, style = "Accent.TButton")
        self.return_to_beam_bconditions_from_2S = ttk.Button(self.root, text = 'Return to boundary conditions', command = self.show_beam_boundaries_conditions, style = "Accent.TButton")
        self.return_to_circpl_bconditions_from_1C = ttk.Button(self.root, text = 'Return to boundary conditions', command = self.show_circular_plate_boundaries_conditions, style = "Accent.TButton")

        self.return_to_shells_from_rectangular_cavity = ttk.Button(self.root, text="Return to rectangular cavity menu", command = self.show_shells, style = "Accent.TButton")
        self.return_to_shells_from_cylindrical_cavity = ttk.Button(self.root, text="Return to cylindrical cavity menu", command = self.show_shells, style = "Accent.TButton")

        
        #Setting up all the widgets to calculate the natural frequencies
        self.modes_settings_frame = ttk.LabelFrame(self.root, text = 'Settings', width = 400)

        self.freq_var_settings = IntVar()
        self.radio_freq_0 = ttk.Radiobutton(self.modes_settings_frame, text = 'Set how many modes to display                                                ', variable = self.freq_var_settings, value = 0, command = lambda:self.show_freq_0())
        self.radio_freq_1 = ttk.Radiobutton(self.modes_settings_frame, text = 'Set the max frequency to display', variable = self.freq_var_settings, value = 1, command = lambda:self.show_freq_1())
        self.freq_0_entry = ttk.Entry(self.modes_settings_frame, width = 5)
        self.freq_1_entry = ttk.Entry(self.modes_settings_frame, width = 5)
        self.freq_0_label = ttk.Label(self.modes_settings_frame, text = 'modes ')
        self.freq_1_label = ttk.Label(self.modes_settings_frame, text = 'hz')

        self.text_file_var = IntVar()
        self.modes_plot_var = IntVar()
        self.text_file_switch = ttk.Checkbutton(self.modes_settings_frame, text = 'Generate a text file', style='Switch.TCheckbutton', var = self.text_file_var)
        self.modes_plot_switch = ttk.Checkbutton(self.modes_settings_frame, text = 'Display modes', style='Switch.TCheckbutton', var = self.modes_plot_var)

        self.L4_entrybox = ttk.Entry(self.beam_1F_1C_data_frame)
        self.L5_entrybox = ttk.Entry(self.beam_2S_data_frame)
        self.m4_entrybox = ttk.Entry(self.beam_1F_1C_data_frame)
        self.m5_entrybox = ttk.Entry(self.beam_2S_data_frame)
        self.E1_entrybox = ttk.Entry(self.rectangular_plate_2S_data_frame)
        self.E2_entrybox = ttk.Entry(self.rectangular_plate_4S_data_frame)
        self.E3_entrybox = ttk.Entry(self.rectangular_plate_2S_2C_data_frame)
        self.E4_entrybox = ttk.Entry(self.beam_1F_1C_data_frame)
        self.E5_entrybox = ttk.Entry(self.beam_2S_data_frame)
        self.E6_entrybox = ttk.Entry(self.circular_plate_1C_data_frame)
        self.I4_entrybox = ttk.Entry(self.beam_1F_1C_data_frame)
        self.I5_entrybox = ttk.Entry(self.beam_2S_data_frame)
        self.v1_entrybox = ttk.Entry(self.rectangular_plate_2S_data_frame)
        self.v2_entrybox = ttk.Entry(self.rectangular_plate_4S_data_frame)
        self.v3_entrybox = ttk.Entry(self.rectangular_plate_2S_2C_data_frame)
        self.v6_entrybox = ttk.Entry(self.circular_plate_1C_data_frame)
        self.rho1_entrybox = ttk.Entry(self.rectangular_plate_2S_data_frame)
        self.rho2_entrybox = ttk.Entry(self.rectangular_plate_4S_data_frame)
        self.rho3_entrybox = ttk.Entry(self.rectangular_plate_2S_2C_data_frame)
        self.rho6_entrybox = ttk.Entry(self.circular_plate_1C_data_frame)
        self.h1_entrybox = ttk.Entry(self.rectangular_plate_2S_data_frame)
        self.h2_entrybox = ttk.Entry(self.rectangular_plate_4S_data_frame)
        self.h3_entrybox = ttk.Entry(self.rectangular_plate_2S_2C_data_frame)
        self.h6_entrybox = ttk.Entry(self.circular_plate_1C_data_frame)
        self.a1_entrybox = ttk.Entry(self.rectangular_plate_2S_data_frame)
        self.a2_entrybox = ttk.Entry(self.rectangular_plate_4S_data_frame)
        self.a3_entrybox = ttk.Entry(self.rectangular_plate_2S_2C_data_frame)
        self.b2_entrybox = ttk.Entry(self.rectangular_plate_4S_data_frame)
        self.b3_entrybox = ttk.Entry(self.rectangular_plate_2S_2C_data_frame)
        self.r6_entrybox = ttk.Entry(self.circular_plate_1C_data_frame)
        self.K7_entrybox = ttk.Entry(self.rectangular_cavity_data_frame)
        self.K8_entrybox = ttk.Entry(self.cylindrical_cavity_data_frame)
        self.rho_fluid7_entrybox = ttk.Entry(self.rectangular_cavity_data_frame)
        self.rho_fluid8_entrybox = ttk.Entry(self.cylindrical_cavity_data_frame)
        self.R8_entrybox = ttk.Entry(self.cylindrical_cavity_data_frame)
        self.D8_entrybox = ttk.Entry(self.cylindrical_cavity_data_frame)
        self.Lx7_entrybox = ttk.Entry(self.rectangular_cavity_data_frame)
        self.Ly7_entrybox = ttk.Entry(self.rectangular_cavity_data_frame)
        self.Lz7_entrybox = ttk.Entry(self.rectangular_cavity_data_frame)
        self.ac7_entrybox = ttk.Entry(self.rectangular_cavity_data_frame)
        self.ac8_entrybox = ttk.Entry(self.cylindrical_cavity_data_frame)

        self.L4_label = ttk.Label(self.beam_1F_1C_data_frame, text = 'Beam lenght                              ')
        self.L5_label = ttk.Label(self.beam_2S_data_frame, text = 'Beam lenght                              ')
        self.m4_label = ttk.Label(self.beam_1F_1C_data_frame, text = 'Beam mass')
        self.m5_label = ttk.Label(self.beam_2S_data_frame, text = 'Beam mass')
        self.E1_label = ttk.Label(self.rectangular_plate_2S_data_frame, text = "Young's modulus")
        self.E2_label = ttk.Label(self.rectangular_plate_4S_data_frame, text = "Young's modulus")
        self.E3_label = ttk.Label(self.rectangular_plate_2S_2C_data_frame, text = "Young's modulus")
        self.E4_label = ttk.Label(self.beam_1F_1C_data_frame, text = "Young's modulus")
        self.E5_label = ttk.Label(self.beam_2S_data_frame, text = "Young's modulus")
        self.E6_label = ttk.Label(self.circular_plate_1C_data_frame, text = "Young's modulus                       ")
        self.I4_label = ttk.Label(self.beam_1F_1C_data_frame, text = 'Area moment of inertia')
        self.I5_label = ttk.Label(self.beam_2S_data_frame, text = 'Area moment of inertia')
        self.v1_label = ttk.Label(self.rectangular_plate_2S_data_frame, text = "Poisson's modulus")
        self.v2_label = ttk.Label(self.rectangular_plate_4S_data_frame, text = "Poisson's modulus")
        self.v3_label = ttk.Label(self.rectangular_plate_2S_2C_data_frame, text = "Poisson's modulus")
        self.v6_label = ttk.Label(self.circular_plate_1C_data_frame, text = "Poisson's modulus")
        self.rho1_label = ttk.Label(self.rectangular_plate_2S_data_frame, text = 'Plate density')
        self.rho2_label = ttk.Label(self.rectangular_plate_4S_data_frame, text = 'Plate density')
        self.rho3_label = ttk.Label(self.rectangular_plate_2S_2C_data_frame, text = 'Plate density')
        self.rho6_label = ttk.Label(self.circular_plate_1C_data_frame, text = 'Plate density')
        self.h1_label = ttk.Label(self.rectangular_plate_2S_data_frame, text = 'Plate thickness')
        self.h2_label = ttk.Label(self.rectangular_plate_4S_data_frame, text = 'Plate thickness')
        self.h3_label = ttk.Label(self.rectangular_plate_2S_2C_data_frame, text = 'Plate thickness')
        self.h6_label = ttk.Label(self.circular_plate_1C_data_frame, text = 'Plate thickness')
        self.a1_label = ttk.Label(self.rectangular_plate_2S_data_frame, text = 'Plate width                                ')
        self.a2_label = ttk.Label(self.rectangular_plate_4S_data_frame, text = 'Plate width                                ')
        self.a3_label = ttk.Label(self.rectangular_plate_2S_2C_data_frame, text = 'Plate width                             ')
        self.b2_label = ttk.Label(self.rectangular_plate_4S_data_frame, text = 'Plate length')
        self.b3_label = ttk.Label(self.rectangular_plate_2S_2C_data_frame, text = 'Plate length')
        self.r6_label = ttk.Label(self.circular_plate_1C_data_frame, text = 'Plate radius')
        self.K7_label = ttk.Label(self.rectangular_cavity_data_frame, text = "Cavity bulk modulus                   ")
        self.K8_label = ttk.Label(self.cylindrical_cavity_data_frame, text = "Cavity bulk modulus                   ")
        self.rho_fluid7_label = ttk.Label(self.rectangular_cavity_data_frame, text = 'Density of the fluid')
        self.rho_fluid8_label = ttk.Label(self.cylindrical_cavity_data_frame, text = 'Density of the fluid')
        self.R8_label = ttk.Label(self.cylindrical_cavity_data_frame, text = 'Cavity radius')
        self.D8_label = ttk.Label(self.cylindrical_cavity_data_frame, text = 'Cavity depth')
        self.Lx7_label = ttk.Label(self.rectangular_cavity_data_frame, text = 'Cavity lenght')
        self.Ly7_label = ttk.Label(self.rectangular_cavity_data_frame, text = 'Cavity width')
        self.Lz7_label = ttk.Label(self.rectangular_cavity_data_frame, text = 'Cavity depth')
        self.ac7_label = ttk.Label(self.rectangular_cavity_data_frame, text = 'Speed of sound')
        self.ac8_label = ttk.Label(self.cylindrical_cavity_data_frame, text = 'Speed of sound')

        self.get_values_iso_recpl_2S = ttk.Button(self.root, text = 'Calculate modes', command = lambda:self.generate_list_modes_iso_recpl_2S(), style = "Accent.TButton")
        self.get_values_iso_recpl_4S = ttk.Button(self.root, text = 'Calculate modes', command = lambda:self.generate_list_modes_iso_recpl_4S(), style = "Accent.TButton")
        self.get_values_iso_recpl_2S_2C = ttk.Button(self.root, text = 'Calculate modes', command = lambda:self.generate_list_modes_iso_recpl_2S_2C(), style = "Accent.TButton")

        self.get_values_ortho_recpl_2S = ttk.Button(self.root, text = 'Calculate modes', command = lambda:self.generate_list_modes_iso_recpl_2S(), style = "Accent.TButton")
        self.get_values_ortho_recpl_4S = ttk.Button(self.root, text = 'Calculate modes', command = lambda:self.generate_list_modes_iso_recpl_4S(), style = "Accent.TButton")
        self.get_values_ortho_recpl_2S_2C = ttk.Button(self.root, text = 'Calculate modes', command = lambda:self.generate_list_modes_iso_recpl_2S_2C(), style = "Accent.TButton")

        self.get_values_beam_1F_1C = ttk.Button(self.root, text = 'Calculate modes', command = lambda:self.generate_list_modes_beam_1F_1C(), style = "Accent.TButton")
        self.get_values_beam_2S = ttk.Button(self.root, text = 'Calculate modes', command = lambda:self.generate_list_modes_beam_2S(), style = "Accent.TButton")
        self.get_values_cirpl_1C = ttk.Button(self.root, text = 'Calculate modes', command = lambda:self.generate_list_modes_cirpl_1C(), style = "Accent.TButton")
        self.get_values_rec_cav = ttk.Button(self.root, text = 'Calculate modes', command = lambda:self.generate_list_modes_reccav(), style = "Accent.TButton")
        self.get_values_cyl_cav = ttk.Button(self.root, text = 'Calculate modes', command = lambda:self.generate_list_modes_cylcav(), style = "Accent.TButton")
        

        self.modes_values_list = list()
        self.m_values_list = list()
        self.n_values_list = list()

        self.main_menu()




    def main_menu(self):
        self.remove_all_1()
        self.remove_all_2()
        self.root.geometry('465x300')
        self.main_menu_frame.grid(row = 0, column  =0, padx = (20, 10), pady = (20, 10), sticky = 'nw')
        self.structures_button.grid(row = 0, column = 0, padx = 40, pady = 10)
        self.shells_button.grid(row = 0, column = 1, padx = 40, pady = 10)

    def show_structures(self):
        self.remove_all_1()
        self.remove_all_2()
        self.root.geometry('440x300')
        self.structures_menu_frame.grid(row=  0, column=  0, padx = (20, 10), pady = (20, 10), sticky = 'nw')
        self.rectangular_plate_button.grid(row = 0, column = 0, padx = 20, pady = 10)
        self.beam_button.grid(row = 1, column = 0, padx = 20, pady = 10)
        self.circular_plate_button.grid(row = 2, column = 0, padx = 20, pady = 10)
        self.return_to_main_button_0.grid(row = 2, column = 2, padx = 40, pady = 10)

    def show_shells(self):
        self.remove_all_1()
        self.remove_all_2()
        self.root.geometry('415x300')
        self.shells_menu_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky = 'nw')
        self.rectangular_cavity_button.grid(row = 0, column = 0, padx = 20, pady = 10)
        self.cylindrical_cavity_button.grid(row = 1, column = 0, padx = 20, pady = 10)
        self.return_to_main_button_1.grid(row = 1, column = 2, padx = 20, pady = 10)

    def show_rectangular_plate_matherial_type(self):
        self.remove_all_1()
        self.remove_all_2()
        self.root.geometry('560x300')
        self.ortho_rectangular_plate_menu_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky = 'nw')



    def show_rectangular_plate_boundaries_conditions(self):
        self.remove_all_1()
        self.remove_all_2()
        self.root.geometry('560x300')
        self.rectangular_plate_menu_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky = 'nw')
        self.iso_rectangular_plate_2S.grid(row = 0, column = 0, padx = 20, pady = 10)
        self.iso_rectangular_plate_4S.grid(row = 1, column = 0, padx = 20, pady = 10)
        self.iso_rectangular_plate_2S_2C.grid(row = 2, column = 0, padx = 20, pady = 10)
        self.ortho_rectangular_plate_2S.grid(row = 0, column = 1, padx = 20, pady = 10)
        self.ortho_rectangular_plate_4S.grid(row = 1, column = 1, padx = 20, pady = 10)
        self.ortho_rectangular_plate_2S_2C.grid(row = 2, column = 1, padx = 20, pady = 10)
        self.return_to_structures_from_rectangular_plate.grid(row = 2, column = 3, padx = 20, pady = 10)

    def show_beam_boundaries_conditions(self):
        self.remove_all_1()
        self.remove_all_2()
        self.root.geometry('545x300')
        self.beam_menu_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky = 'nw')
        self.beam_1F_1C.grid(row = 0, column = 0, padx = 20, pady = 10)
        self.beam_2S.grid(row = 1, column = 0, padx = 20, pady = 10)
        self.return_to_structures_from_beam.grid(row = 1, column = 1, padx = 20, pady = 10)

    def show_circular_plate_boundaries_conditions(self):
        self.remove_all_1()
        self.remove_all_2()
        self.root.geometry('470x300')
        self.circular_plate_menu_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky = 'nw')
        self.circular_plate_C.grid(row = 0, column = 0, padx = 20, pady = 10)
        self.return_to_structures_from_circular_plate.grid(row = 0, column = 1, padx = 20, pady = 10)

    


    def data_iso_rectangular_plate_2S(self):
        self.remove_all_1()
        self.remove_all_2()
        self.rectangular_plate_2S_data_frame.grid(row = 0, column = 0, columnspan = 2, padx = (20, 10), pady = (20, 10), sticky = 'nw')
        self.a1_label.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.a1_entrybox.grid(row = 0, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.h1_label.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.h1_entrybox.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.rho1_label.grid(row = 2, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.rho1_entrybox.grid(row = 2, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.E1_label.grid(row = 3, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.E1_entrybox.grid(row = 3, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.v1_label.grid(row = 4, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.v1_entrybox.grid(row = 4, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.root.geometry('480x650')
        self.show_radio_and_switch()
        self.show_freq_0()
        self.return_to_iso_recpl_bconditions_from_2S.grid(row = 2, column = 1, padx = 20, pady = 10)
        self.get_values_iso_recpl_2S.grid(row = 2, column = 0, padx = 20, pady = 10)
        self.modes_plot_switch.configure(state = DISABLED)

    def generate_list_modes_iso_recpl_2S(self):
        try: 
            self.a = float(self.a1_entrybox.get())
            self.h = float(self.h1_entrybox.get())
            self.rho = float(self.rho1_entrybox.get())
            self.E = float(self.E1_entrybox.get())
            self.v = float(self.v1_entrybox.get())
        except:
            messagebox.showwarning('Warning', 'Enter correct values')

        if self.a < 0 or self.h < 0 or self.rho < 0 or self.E < 0 or not 0 < self.v < 1:
            messagebox.showwarning('Warning', 'Some of the geometry values are inconsistent')
        else: 
            self.get_settings()
    
            if self.freq_var_settings.get() == 0:
                self.modes_values_list, self.m_values_list, self.n_values_list = recpl_2S_modes.calculate_modes(self.a, self.h, self.rho, self.E, self.v, 0, self.freq_var_value)
            elif self.freq_var_settings.get() == 1:
                self.modes_values_list, self.m_values_list, self.n_values_list = recpl_2S_modes.calculate_modes(self.a, self.h, self.rho, self.E, self.v, 1, self.freq_var_value)
            self.root.geometry('950x630')
            self.treeview_grid()

            if self.text_file_var.get() == 1:
                generate_txt_file.txt_file(self.modes_values_list, self.m_values_list, self.n_values_list)





    def data_iso_rectangular_plate_4S(self):
        self.remove_all_1()
        self.remove_all_2()
        self.rectangular_plate_4S_data_frame.grid(row = 0, column = 0, columnspan = 2, padx = (20, 10), pady = (20, 10), sticky = 'nw')
        self.a2_label.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.a2_entrybox.grid(row = 0, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.b2_label.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.b2_entrybox.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.h2_label.grid(row = 2, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.h2_entrybox.grid(row = 2, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.rho2_label.grid(row = 3, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.rho2_entrybox.grid(row = 3, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.E2_label.grid(row = 4, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.E2_entrybox.grid(row = 4, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.v2_label.grid(row = 5, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.v2_entrybox.grid(row = 5, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.root.geometry('480x700')
        self.show_radio_and_switch()
        self.show_freq_0()
        self.return_to_iso_recpl_bconditions_from_4S.grid(row = 2, column = 1, padx = 20, pady = 10)
        self.get_values_iso_recpl_4S.grid(row = 2, column = 0, padx = 20, pady = 10)
        self.modes_plot_switch.configure(state = NORMAL)


    def generate_list_modes_iso_recpl_4S(self):
        try: 
            self.a = float(self.a2_entrybox.get())
            self.b = float(self.b2_entrybox.get())
            self.h = float(self.h2_entrybox.get())
            self.rho = float(self.rho2_entrybox.get())
            self.E = float(self.E2_entrybox.get())
            self.v = float(self.v2_entrybox.get())
        except:
            messagebox.showwarning('Warning', 'Some of the geometry values are not a numbers')

        if self.a < 0 or self.b < 0 or self.h < 0 or self.rho < 0 or self.E < 0 or not 0 < self.v < 1:
            messagebox.showwarning('Warning', 'Some of the geometry values are inconsistent')
        else: 
            self.get_settings()
    
            if self.freq_var_settings.get() == 0:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = recpl_4S_modes.calculate_modes(self.a, self.b, self.h, self.rho, self.E, self.v, 0, self.freq_var_value)
            elif self.freq_var_settings.get() == 1:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = recpl_4S_modes.calculate_modes(self.a, self.b, self.h, self.rho, self.E, self.v, 1, self.freq_var_value)
            self.root.geometry('950x660')
            self.treeview_grid()

            if self.text_file_var.get() == 1:
                generate_txt_file.txt_file(self.modes_values_list, self.m_values_list, self.n_values_list)
            if self.modes_plot_var.get() == 1:
                self.freq_matrix = set_freq_matrix.set_freq_matrix(self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list)
                recpl_4S_plot.recpl_4s_plot(self.a, self.b, self.freq_matrix)

        
    def data_iso_rectangular_plate_2S_2C(self):
        self.remove_all_1()
        self.remove_all_2()
        self.rectangular_plate_2S_2C_data_frame.grid(row = 0, column = 0, columnspan = 2, padx = (20, 10), pady = (20, 10), sticky = 'nw')
        self.a3_label.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.a3_entrybox.grid(row = 0, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.b3_label.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.b3_entrybox.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.h3_label.grid(row = 2, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.h3_entrybox.grid(row = 2, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.rho3_label.grid(row = 3, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.rho3_entrybox.grid(row = 3, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.E3_label.grid(row = 4, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.E3_entrybox.grid(row = 4, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.v3_label.grid(row = 5, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.v3_entrybox.grid(row = 5, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.root.geometry('480x700')
        self.show_radio_and_switch()
        self.show_freq_0()
        self.return_to_iso_recpl_bconditions_from_2S_2C.grid(row = 2, column = 1, padx = 20, pady = 10)
        self.get_values_iso_recpl_2S_2C.grid(row = 2, column = 0, padx = 20, pady = 10)
        self.modes_plot_switch.configure(state = NORMAL)

    def generate_list_modes_iso_recpl_2S_2C(self):
        try: 
            self.a = float(self.a3_entrybox.get())
            self.b = float(self.b3_entrybox.get())
            self.h = float(self.h3_entrybox.get())
            self.rho = float(self.rho3_entrybox.get())
            self.E = float(self.E3_entrybox.get())
            self.v = float(self.v3_entrybox.get())
        except:
            messagebox.showwarning('Warning', 'Some of the geometry values are not a numbers')

        if self.a < 0 or self.b < 0 or self.h < 0 or self.rho < 0 or self.E < 0 or not 0 < self.v < 1:
            messagebox.showwarning('Warning', 'Some of the geometry values are inconsistent')
        else: 
            self.get_settings()
    
            if self.freq_var_settings.get() == 0:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = recpl_2S_2C_modes.calculate_modes(self.a, self.b, self.h, self.rho, self.E, self.v, 0, self.freq_var_value)
            elif self.freq_var_settings.get() == 1:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = recpl_2S_2C_modes.calculate_modes(self.a, self.b, self.h, self.rho, self.E, self.v, 1, self.freq_var_value)
            self.root.geometry('950x630')
            self.treeview_grid()

            if self.text_file_var.get() == 1:
                generate_txt_file.txt_file(self.modes_values_list, self.m_values_list, self.n_values_list)
            if self.modes_plot_var.get() == 1:
                self.freq_matrix = set_freq_matrix.set_freq_matrix(self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list)
                recpl_2S_2C_plot.recpl_2S_2C_plot(self.a, self.b, self.freq_matrix)
        
    def data_beam_1F_1C(self):
        self.remove_all_1()
        self.remove_all_2()
        self.beam_1F_1C_data_frame.grid(row = 0, column = 0, columnspan = 2, padx = (20, 10), pady = (20, 10), sticky = 'nw')
        self.L4_label.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.L4_entrybox.grid(row = 0, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.m4_label.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.m4_entrybox.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.I4_label.grid(row = 2, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.I4_entrybox.grid(row = 2, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.E4_label.grid(row = 3, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.E4_entrybox.grid(row = 3, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.root.geometry('480x600')
        self.show_radio_and_switch()
        self.show_freq_0()
        self.return_to_beam_bconditions_from_1F_1C.grid(row = 2, column = 1, padx = 20, pady = 10)
        self.get_values_beam_1F_1C.grid(row = 2, column = 0, padx = 20, pady = 10)
        self.modes_plot_switch.configure(state = NORMAL)

    def generate_list_modes_beam_1F_1C(self):
        try: 
            self.L = float(self.L4_entrybox.get())
            self.m = float(self.m4_entrybox.get())
            self.I = float(self.I4_entrybox.get())
            self.E = float(self.E4_entrybox.get())
        except:
            messagebox.showwarning('Warning', 'Some of the geometry values are not a numbers')

        if self.L < 0 or self.m < 0 or self.I < 0 or self.E < 0:
            messagebox.showwarning('Warning', 'Some of the geometry values are inconsistent')
        else: 
            self.get_settings()
    
            if self.freq_var_settings.get() == 0:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = beam_1F_1C_modes.calculate_modes(self.L, self.m, self.I, self.E, 0, self.freq_var_value)
            elif self.freq_var_settings.get() == 1:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = beam_1F_1C_modes.calculate_modes(self.L, self.m, self.I, self.E, 1, self.freq_var_value)
            self.root.geometry('950x630')
            self.treeview_grid()

            if self.text_file_var.get() == 1:
                generate_txt_file.txt_file(self.modes_values_list, self.m_values_list, self.n_values_list)
            if self.modes_plot_var.get() == 1:
                self.freq_matrix = set_freq_matrix.set_freq_matrix(self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list)
                beam_1F_1C_plot.beam_1F_1C_plot(self.L, self.freq_matrix)
        
    def data_beam_2S(self):
        self.remove_all_1()
        self.remove_all_2()
        self.beam_2S_data_frame.grid(row = 0, column = 0, columnspan = 2, padx = (20, 10), pady = (20, 10), sticky = 'nw')
        self.L5_label.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.L5_entrybox.grid(row = 0, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.m5_label.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.m5_entrybox.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.I5_label.grid(row = 2, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.I5_entrybox.grid(row = 2, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.E5_label.grid(row = 3, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.E5_entrybox.grid(row = 3, column = 1, padx = 20, pady = 10, sticky = 'e')#
        self.root.geometry('480x600')
        self.show_radio_and_switch()
        self.show_freq_0()
        self.return_to_beam_bconditions_from_2S.grid(row = 2, column = 1, padx = 20, pady = 10)
        self.get_values_beam_2S.grid(row = 2, column = 0, padx = 20, pady = 10)
        self.modes_plot_switch.configure(state = NORMAL)
    
    def generate_list_modes_beam_2S(self):
        try: 
            self.L = float(self.L5_entrybox.get())
            self.m = float(self.m5_entrybox.get())
            self.I = float(self.I5_entrybox.get())
            self.E = float(self.E5_entrybox.get())
        except:
            messagebox.showwarning('Warning', 'Some of the geometry values are not a numbers')

        if self.L < 0 or self.m < 0 or self.I < 0 or self.E < 0:
            messagebox.showwarning('Warning', 'Some of the geometry values are inconsistent')
        else: 
            self.get_settings()
    
            if self.freq_var_settings.get() == 0:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = beam_2S_modes.calculate_modes(self.L, self.m, self.I, self.E, 0, self.freq_var_value)
            elif self.freq_var_settings.get() == 1:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = beam_2S_modes.calculate_modes(self.L, self.m, self.I, self.E, 1, self.freq_var_value)
            self.root.geometry('950x630')
            self.treeview_grid()

            if self.text_file_var.get() == 1:
                generate_txt_file.txt_file(self.modes_values_list, self.m_values_list, self.n_values_list)
            if self.modes_plot_var.get() == 1:
                self.freq_matrix = set_freq_matrix.set_freq_matrix(self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list)
                beam_2S_plot.beam_2S_plot(self.L, self.freq_matrix)

    def data_circular_plate_C(self):
        self.remove_all_1()
        self.remove_all_2()
        self.circular_plate_1C_data_frame.grid(row = 0, column = 0, columnspan = 2, padx = (20, 10), pady = (20, 10), sticky = 'nw')
        self.r6_label.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.r6_entrybox.grid(row = 0, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.h6_label.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.h6_entrybox.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.rho6_label.grid(row = 2, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.rho6_entrybox.grid(row = 2, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.E6_label.grid(row = 3, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.E6_entrybox.grid(row = 3, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.v6_label.grid(row = 4, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.v6_entrybox.grid(row = 4, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.root.geometry('480x630')
        self.show_radio_and_switch()
        self.show_freq_0()
        self.return_to_circpl_bconditions_from_1C.grid(row = 2, column = 1, padx = 20, pady = 10)
        self.get_values_cirpl_1C.grid(row = 2, column = 0, padx = 20, pady = 10)
        self.modes_plot_switch.configure(state = NORMAL)
    
    def generate_list_modes_cirpl_1C(self):
        try: 
            self.r = float(self.r6_entrybox.get())
            self.h = float(self.h6_entrybox.get())
            self.rho = float(self.rho6_entrybox.get())
            self.E = float(self.E6_entrybox.get())
            self.v = float(self.v6_entrybox.get())
        except:
            messagebox.showwarning('Warning', 'Some of the geometry values are not a numbers')

        if self.r < 0 or self.h < 0 or self.rho < 0 or self.E < 0 or not 0 < self.v < 1:
            messagebox.showwarning('Warning', 'Some of the geometry values are inconsistent')
        else: 
            self.get_settings()
    
            if self.freq_var_settings.get() == 0:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = cirpl_1C_modes.calculate_modes(self.r, self.h, self.rho, self.E, self.v, 0, self.freq_var_value)
            elif self.freq_var_settings.get() == 1:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = cirpl_1C_modes.calculate_modes(self.r, self.h, self.rho, self.E, self.v, 1, self.freq_var_value)
            self.root.geometry('950x630')
            self.treeview_grid()


            if self.text_file_var.get() == 1:
                generate_txt_file.txt_file(self.modes_values_list, self.m_values_list, self.n_values_list)
            if self.modes_plot_var.get() == 1:
                self.freq_matrix = set_freq_matrix.set_freq_matrix(self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list)
                cirpl_1C_plot.cirpl_1C_plot(self.r, self.freq_matrix)
        

    def data_rectangular_cavity(self):
        self.remove_all_1()
        self.remove_all_2()
        self.rectangular_cavity_data_frame.grid(row = 0, column = 0, columnspan = 2, padx = (20, 10), pady = (20, 10), sticky = 'nw')
        self.Lx7_label.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.Lx7_entrybox.grid(row = 0, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.Ly7_label.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.Ly7_entrybox.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.Lz7_label.grid(row = 2, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.Lz7_entrybox.grid(row = 2, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.ac7_label.grid(row = 5, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.ac7_entrybox.grid(row = 5, column = 1, padx = 20, pady = 10, sticky = 'w')
        self.root.geometry('480x680')
        self.show_radio_and_switch()
        self.show_freq_0()
        self.return_to_shells_from_rectangular_cavity.grid(row = 2, column = 1, padx = 20, pady = 10)
        self.get_values_rec_cav.grid(row = 2, column = 0, padx = 20, pady = 10)
        self.modes_plot_switch.configure(state = DISABLED)
    
    def generate_list_modes_reccav(self):
        try: 
            self.Lx = float(self.Lx7_entrybox.get())
            self.Ly = float(self.Ly7_entrybox.get())
            self.Lz = float(self.Lz7_entrybox.get())
            self.ac = float(self.ac7_entrybox.get())
        except:
            messagebox.showwarning('Warning', 'Some of the geometry values are not a numbers')

        if self.Lx < 0 or self.Ly < 0 or self.Lz < 0 or self.ac < 0:
            messagebox.showwarning('Warning', 'Some of the geometry values are inconsistent')
        else: 
            self.get_settings()
    
            if self.freq_var_settings.get() == 0:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = reccav_modes.calculate_modes(self.Lx, self.Ly, self.Lz, self.ac, 0, self.freq_var_value)
            elif self.freq_var_settings.get() == 1:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = reccav_modes.calculate_modes(self.Lx, self.Ly, self.Lz, self.ac, 1, self.freq_var_value)
            self.root.geometry('1050x680')
            self.treeview_grid_cavities()

            if self.text_file_var.get() == 1:
                generate_txt_file.txt_file(self.modes_values_list, self.m_values_list, self.n_values_list)

    def data_cylindrical_cavity(self):
        self.remove_all_1()
        self.remove_all_2()
        self.cylindrical_cavity_data_frame.grid(row = 0, column = 0, columnspan = 2, padx = (20, 10), pady = (20, 10), sticky = 'nw')
        self.R8_label.grid(row = 0, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.R8_entrybox.grid(row = 0, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.D8_label.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.D8_entrybox.grid(row = 1, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.ac8_label.grid(row = 2, column = 0, padx = 20, pady = 10, sticky = 'w')
        self.ac8_entrybox.grid(row = 2, column = 1, padx = 20, pady = 10, sticky = 'e')
        self.root.geometry('480x630')
        self.show_radio_and_switch()
        self.show_freq_0()
        self.return_to_shells_from_cylindrical_cavity.grid(row = 2, column = 1, padx = 20, pady = 10)
        self.get_values_cyl_cav.grid(row = 2, column = 0, padx = 20, pady = 10)
        self.modes_plot_switch.configure(state = DISABLED)

    def generate_list_modes_cylcav(self):
        try: 
            self.R = float(self.R8_entrybox.get())
            self.D = float(self.D8_entrybox.get())
            self.ac = float(self.ac8_entrybox.get())
        except:
            messagebox.showwarning('Warning', 'Some of the geometry values are not a numbers')

        if self.R < 0 or self.D < 0 or self.ac < 0:
            messagebox.showwarning('Warning', 'Some of the geometry values are inconsistent')
        else: 
            self.get_settings()
    
            if self.freq_var_settings.get() == 0:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = cylcav_modes.calculate_modes(self.R, self.D, self.ac, 0, self.freq_var_value)
            elif self.freq_var_settings.get() == 1:
                self.modes_values_list, self.Kn_values_list, self.m_values_list, self.n_values_list = cylcav_modes.calculate_modes(self.R, self.D, self.ac, 1, self.freq_var_value)
            self.root.geometry('1050x680')
            self.treeview_grid_cavities()

            if self.text_file_var.get() == 1:
                generate_txt_file.txt_file(self.modes_values_list, self.m_values_list, self.n_values_list)    



    def treeview_grid(self):
        self.treeview_columns = ('Mode_number', 'Frequency', 'M_value', 'N_value')
        self.modes_treeview = ttk.Treeview(self.root, columns = self.treeview_columns, show = 'headings')
        self.modes_treeview.column('Mode_number', width = 100, anchor = CENTER)
        self.modes_treeview.column('Frequency', width = 100, anchor = CENTER)
        self.modes_treeview.column('M_value', width = 100, anchor = CENTER)
        self.modes_treeview.column('N_value', width = 100, anchor = CENTER)
        self.modes_treeview.heading('Mode_number', text = 'Mode Number')
        self.modes_treeview.heading('Frequency', text = 'Frequency')
        self.modes_treeview.heading('M_value', text = 'M value')
        self.modes_treeview.heading('N_value', text = 'N value')
        for i in range(len(self.modes_values_list)):
            self.modes_treeview.insert(parent = '', index = i, iid = i, values = (i + 1, self.modes_values_list[i], self.m_values_list[i], self.n_values_list[i]))
        self.modes_treeview.grid(row = 0, column = 3, sticky = 'nw', pady = 29)

    def treeview_grid_cavities(self):
        self.treeview_columns = ('Mode_number', 'Frequency', 'L_value', 'M_value', 'N_value')
        self.modes_treeview = ttk.Treeview(self.root, columns = self.treeview_columns, show = 'headings')
        self.modes_treeview.column('Mode_number', width = 100, anchor = CENTER)
        self.modes_treeview.column('Frequency', width = 100, anchor = CENTER)
        self.modes_treeview.column('L_value', width = 100, anchor = CENTER)
        self.modes_treeview.column('M_value', width = 100, anchor = CENTER)
        self.modes_treeview.column('N_value', width = 100, anchor = CENTER)
        self.modes_treeview.heading('Mode_number', text = 'Mode Number')
        self.modes_treeview.heading('Frequency', text = 'Frequency')
        self.modes_treeview.heading('L_value', text = 'L value')
        self.modes_treeview.heading('M_value', text = 'M value')
        self.modes_treeview.heading('N_value', text = 'N value')
        for i in range(len(self.modes_values_list)):
            self.modes_treeview.insert(parent = '', index = i, iid = i, values = (i + 1, self.modes_values_list[i], self.Kn_values_list[i], self.m_values_list[i], self.n_values_list[i]))
        self.modes_treeview.grid(row = 0, column = 3, sticky = 'nw', pady = 29, rowspan = 2)
        

    def get_settings(self):
        if self.freq_var_settings.get() == 0 and int(self.freq_0_entry.get()) > 0 :
            self.freq_var_value = int(self.freq_0_entry.get())
        elif self.freq_var_settings.get() == 1 and int(self.freq_1_entry.get()) > 0:
            self.freq_var_value = int(self.freq_1_entry.get())
        else: messagebox.showwarning('Warning', 'Some of the settings values are inconsistent')

    def show_radio_and_switch(self):
        self.modes_settings_frame.grid(row = 1, column = 0, columnspan = 2, padx = (20, 10), pady = (20, 10), sticky = 'nw')
        self.radio_freq_0.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'nsew')
        self.radio_freq_1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = 'nsew')
        self.text_file_switch.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = 'w')
        self.modes_plot_switch.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = 'w')
  
    def show_freq_0(self):
        self.freq_1_entry.delete(0, 'end')
        self.freq_1_entry.place_forget()
        self.freq_1_label.place_forget()
        self.freq_0_entry.place(x = 317, y = 5)
        self.freq_0_label.place(x = 372, y = 12)
    
    def show_freq_1(self):
        self.freq_0_entry.delete(0, 'end')
        self.freq_0_entry.place_forget()
        self.freq_0_label.place_forget()
        self.freq_1_entry.place(x = 317, y = 52)
        self.freq_1_label.place(x = 372, y = 59)


    def remove_all_1(self):
        #First level
        self.main_menu_frame.grid_forget()
        self.structures_button.grid_forget()
        self.shells_button.grid_forget()

        #Second level
        self.structures_menu_frame.grid_forget()
        self.shells_menu_frame.grid_forget()
        self.rectangular_plate_button.grid_forget()
        self.beam_button.grid_forget()
        self.circular_plate_button.grid_forget()
        self.rectangular_cavity_button.grid_forget()
        self.cylindrical_cavity_button.grid_forget()
        self.return_to_main_button_0.grid_forget()
        self.return_to_main_button_1.grid_forget()

        #Third level
        self.rectangular_plate_menu_frame.grid_forget()
        self.beam_menu_frame.grid_forget()
        self.circular_plate_menu_frame.grid_forget()
        self.iso_rectangular_plate_2S.grid_forget()
        self.iso_rectangular_plate_4S.grid_forget()
        self.iso_rectangular_plate_2S_2C.grid_forget()
        self.ortho_rectangular_plate_2S.grid_forget()
        self.ortho_rectangular_plate_4S.grid_forget()
        self.ortho_rectangular_plate_2S_2C.grid_forget()
        self.beam_1F_1C.grid_forget()
        self.beam_2S.grid_forget()
        self.circular_plate_C.grid_forget()
        self.return_to_structures_from_rectangular_plate.grid_forget()
        self.return_to_structures_from_beam.grid_forget()
        self.return_to_structures_from_circular_plate.grid_forget()

        #Fourth level
        self.rectangular_plate_2S_data_frame.grid_forget()
        self.rectangular_plate_4S_data_frame.grid_forget()
        self.rectangular_plate_2S_2C_data_frame.grid_forget()
        self.beam_1F_1C_data_frame.grid_forget()
        self.beam_2S_data_frame.grid_forget()
        self.circular_plate_1C_data_frame.grid_forget()
        self.rectangular_cavity_data_frame.grid_forget()
        self.cylindrical_cavity_data_frame.grid_forget()
        self.return_to_iso_recpl_bconditions_from_2S.grid_forget()
        self.return_to_iso_recpl_bconditions_from_2S_2C.grid_forget()
        self.return_to_iso_recpl_bconditions_from_4S.grid_forget()
        self.return_to_ortho_recpl_bconditions_from_2S.grid_forget()
        self.return_to_ortho_recpl_bconditions_from_2S_2C.grid_forget()
        self.return_to_ortho_recpl_bconditions_from_4S.grid_forget()
        self.return_to_beam_bconditions_from_1F_1C.grid_forget()
        self.return_to_beam_bconditions_from_2S.grid_forget()
        self.return_to_circpl_bconditions_from_1C.grid_forget()
        self.return_to_shells_from_rectangular_cavity.grid_forget()
        self.return_to_shells_from_cylindrical_cavity.grid_forget()
        self.modes_settings_frame.grid_forget()

        self.get_values_iso_recpl_2S.grid_forget()
        self.get_values_iso_recpl_2S_2C.grid_forget()
        self.get_values_iso_recpl_4S.grid_forget()
        self.get_values_ortho_recpl_2S.grid_forget()
        self.get_values_ortho_recpl_2S_2C.grid_forget()
        self.get_values_ortho_recpl_4S.grid_forget()
        self.get_values_beam_1F_1C.grid_forget()
        self.get_values_beam_2S.grid_forget()
        self.get_values_cirpl_1C.grid_forget()
        self.get_values_rec_cav.grid_forget()
        self.get_values_cyl_cav.grid_forget()

    def remove_all_2(self):
        self.radio_freq_0.grid_forget()
        self.radio_freq_1.grid_forget()
        self.freq_0_entry.place_forget()
        self.freq_1_entry.place_forget()
        self.freq_0_label.place_forget()
        self.freq_1_label.place_forget()
        self.L4_entrybox.grid_forget()
        self.L5_entrybox.grid_forget()
        self.m4_entrybox.grid_forget()
        self.m5_entrybox.grid_forget()
        self.E1_entrybox.grid_forget()
        self.E2_entrybox.grid_forget()
        self.E3_entrybox.grid_forget()
        self.E4_entrybox.grid_forget()
        self.E5_entrybox.grid_forget()
        self.E6_entrybox.grid_forget()
        self.I4_entrybox.grid_forget()
        self.I5_entrybox.grid_forget()
        self.v1_entrybox.grid_forget()
        self.v2_entrybox.grid_forget()
        self.v3_entrybox.grid_forget()
        self.v6_entrybox.grid_forget()
        self.rho1_entrybox.grid_forget()
        self.rho2_entrybox.grid_forget()
        self.rho3_entrybox.grid_forget()
        self.rho6_entrybox.grid_forget()
        self.h1_entrybox.grid_forget()
        self.h2_entrybox.grid_forget()
        self.h3_entrybox.grid_forget()
        self.h6_entrybox.grid_forget()
        self.a1_entrybox.grid_forget()
        self.a2_entrybox.grid_forget()
        self.a3_entrybox.grid_forget()
        self.b2_entrybox.grid_forget()
        self.b3_entrybox.grid_forget()
        self.r6_entrybox.grid_forget()
        self.K7_entrybox.grid_forget()
        self.K8_entrybox.grid_forget()
        self.rho_fluid7_entrybox.grid_forget()
        self.rho_fluid8_entrybox.grid_forget()
        self.R8_entrybox.grid_forget()
        self.D8_entrybox.grid_forget()
        self.Lx7_entrybox.grid_forget()
        self.Ly7_entrybox.grid_forget()
        self.Lz7_entrybox.grid_forget()
        self.ac7_entrybox.grid_forget()
        self.ac8_entrybox.grid_forget()
        self.L4_label.grid_forget()
        self.L5_label.grid_forget()
        self.m4_label.grid_forget()
        self.m5_label.grid_forget()
        self.E1_label.grid_forget()
        self.E2_label.grid_forget()
        self.E3_label.grid_forget()
        self.E4_label.grid_forget()
        self.E5_label.grid_forget()
        self.E6_label.grid_forget()
        self.I4_label.grid_forget()
        self.I5_label.grid_forget()
        self.v1_label.grid_forget()
        self.v2_label.grid_forget()
        self.v3_label.grid_forget()
        self.v6_label.grid_forget()
        self.rho1_label.grid_forget()
        self.rho2_label.grid_forget()
        self.rho3_label.grid_forget()
        self.rho6_label.grid_forget()
        self.h1_label.grid_forget()
        self.h2_label.grid_forget()
        self.h3_label.grid_forget()
        self.h6_label.grid_forget()
        self.a1_label.grid_forget()
        self.a2_label.grid_forget()
        self.a3_label.grid_forget()
        self.b2_label.grid_forget()
        self.b3_label.grid_forget()
        self.r6_label.grid_forget()
        self.K7_label.grid_forget()
        self.K8_label.grid_forget()
        self.rho_fluid7_label.grid_forget()
        self.rho_fluid8_label.grid_forget()
        self.R8_label.grid_forget()
        self.D8_label.grid_forget()
        self.Lx7_label.grid_forget()
        self.Ly7_label.grid_forget()
        self.Lz7_label.grid_forget()
        self.ac7_label.grid_forget()
        self.ac8_entrybox.grid_forget()


if __name__ == '__main__':

    root = Tk()

    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
    root.title('Natural Frequencies')
    GameGUI = main_GUI(root)
    root.mainloop()