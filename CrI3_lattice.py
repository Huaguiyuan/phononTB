import os.path
import time
from math import *
from math import sqrt
from numpy.linalg import *
import numpy as np
import matplotlib.pyplot as plt
import cmath
from matplotlib.collections import LineCollection
import matplotlib.cm as cm
from draw_phononTB_HAN import *
#from numeric import *




lat = [[1.0,  -np.sqrt(3),0.0], [1.0,  np.sqrt(3),0.0],[0.0, 0.0, 20.0]]
orb =  [[0.33333300000000 ,  0.66666700000000 ,  0.33333269177304],  [0.00000000000000 ,  0.00000000000000 ,  0.33333330822695],   [0.02668627626651 ,  0.33333267140451 ,  0.25162013616076],    [0.66666732859549 ,  0.69335260486200 ,  0.25162013616076],  [0.30664739513801 ,  0.97331372373349 ,  0.25162013616076],  [0.66666667140451 ,  0.97331339513800 ,  0.41504686383924],  [0.02668660486200 ,  0.69335227626650 ,  0.41504686383924], [0.30664772373350 ,  0.33333332859549 ,  0.41504686383924]]
mass = np.array([51.9961, 51.9961, 126.90, 126.90, 126.90, 126.90, 126.90, 126.90])/51.9961
fc_nn  =  [[-1.0,0.0],[0.0,-1.0]]
fc_nn1 = [[-22.19684176,   -7.699687431],[-7.699687431,   -13.306]]
fc_nn2 = [[-22.19684176 ,    7.699687431],[ 7.699687431,   -13.306]]
fc_nn3 = [[-8.860588573805234,    -0.000000000000000],[-0.000000000000000 ,  -26.642257254446765]]
fc_nnn = [[0.1,0.0],[0.0,0.3]]
V_info = [-2.6, -0.5]
V_info2 = [-0.5, -0.1]
###############################################################################
FC = ForceConstant(3, 8)

FC.set_geometry(lat, orb, mass)
FC.set_hopping(0,2,[0.0,0.0,0.0],V_info)
FC.set_hopping(0,3,[0.0,0.0,0.0],V_info)
FC.set_hopping(0,4,[0.0,0.0,0.0],V_info)
FC.set_hopping(0,5,[0.0,0.0,0.0],V_info)
FC.set_hopping(0,6,[0.0,0.0,0.0],V_info)
FC.set_hopping(0,7,[0.0,0.0,0.0],V_info)

FC.set_hopping(1,2,[0.0,0.0,0.0],V_info)
FC.set_hopping(1,3,[-1.0,-1.0,0.0],V_info)
FC.set_hopping(1,4,[0.0,-1.0,0.0],V_info)
FC.set_hopping(1,5,[-1.0,-1.0,0.0],V_info)
FC.set_hopping(1,6,[0.0,-1.0,0.0],V_info)
FC.set_hopping(1,7,[0.0,0.0,0.0],V_info)

FC.set_hopping(0,1,[0.0,0.0,0.0],V_info2)
FC.set_hopping(0,1,[0.0,1.0,0.0],V_info2)
FC.set_hopping(0,1,[1.0,1.0,0.0],V_info2)

#FC_dice.set_hopping(0,0,[0.0,0.0],V_info_hex2)
#FC_dice.set_hopping(1,1,[0.0,0.0],V_info_hex2)

#FC_dice.set_hopping(1,1,[-1.0,-1.0],V_info2_hex)
#FC_dice.set_hopping(1,1,[0.0,1.0],V_info2_hex)
#FC_dice.set_hopping(1,1,[1.0,0.0],V_info2_hex)
#FC_dice.set_hopping(0,0,[-1.0,0.0],V_info2_           hex)
#FC_dice.set_hopping(0,0,[1.0,1.0],V_info2_hex)
#FC_dice.set_hopping(0,0,[0.0,-1.0],V_info2_hex)

FC.set_acoustic_sum_rule()
#FC_dice.set_acoustic_sum_rule()

FC.print_info()


###############################################################################
alpha0 = [[0.0,0.0,0.0]]
alpha3 = [[0.0,0.0,0.005],[0.0,0.0,0.0],[0.0,0.0,0.0]]
q_path = [[0, 0, 0.0], [0.5, 0.0, 0.0], [1.0/3, 1.0/3, 0.0], [0.0, 0, 0.0]]

q_spacing = 100


q_grid = ['slice',[31, 31, 1], 0.0]  #### [q_slice mode, [nx, ny, nz], fixed_qpoints]
q_path_K = [[1.0/3+0.01,1.0/3-0.01],[1.0/3+0.01,1.0/3+0.01],[1.0/3-0.01,1.0/3+0.01],[1.0/3-0.01,1.0/3-0.01],[1.0/3+0.01,1.0/3-0.01]]
q_path_Kp = [[2.0/3+0.01,-1.0/3-0.01],[2.0/3+0.01,-1.0/3+0.01],[2.0/3-0.01,-1.0/3+0.01],[2.0/3-0.01,-1.0/3-0.01],[2.0/3+0.01,-1.0/3-0.01]]
q_path_X = [[1.0/2+0.0001,0.0/2-0.0001],[1.0/2+0.0001,0.0/2+0.0001],[1.0/2-0.0001,0.0/2+0.0001],[1.0/2-0.0001,0.0/2-0.0001],[1.0/2+0.0001,0.0/2-0.0001]]
q_grid_berry_K = ['berryphase', q_path_K, 50]
q_grid_berry_X = ['berryphase', q_path_X, 50]

###############################################################################
DM = DynamicalMatrix('CrI3_test', FC ,alpha0)


DM.get_phonon_band(q_path,q_spacing)
DM.draw_phonon_band()
#DM.make_phband_PROCAR_format(q_grid)

###############################################################################
##CTI_dice = ComputeTopologicalInvariants('dice_test',band_range, q_grid)
#CTI_dice.get_Willsons_loop()
#CTI_hex.calculate_Berry_phase()

