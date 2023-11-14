import numpy as np

part_a = None #TODO
# >>>>>>>>>>
part_a = np.eye(8)
# >>>>>>>>>>

part_b = None #TODO
# >>>>>>>>>>
part_b = 4 * np.eye(8)
# >>>>>>>>>>

part_c = None #TODO
# >>>>>>>>>>
part_c = np.eye(8, k=1)
# >>>>>>>>>>

part_d = None #TODO
# >>>>>>>>>>
part_d = np.diag(np.arange(1., 9))
# >>>>>>>>>>

part_e = None #TODO
# >>>>>>>>>>
part_e = 2 * np.diag(np.arange(1., 9)) + np.eye(8, k=1) + 3 * np.eye(8, k=-1)
# >>>>>>>>>>

part_f = None #TODO
# >>>>>>>>>>
part_f = np.diag(np.arange(8., 0, -1)) + np.diag(np.arange(1., 8), k=1)
# >>>>>>>>>>

part_g = None #TODO
# >>>>>>>>>>
part_g = np.zeros((8, 8))
# >>>>>>>>>>

part_h = None #TODO
# >>>>>>>>>>
part_h = 2 * np.ones((8, 8))
# >>>>>>>>>>

part_i = None #TODO
# >>>>>>>>>>
part_i = np.hstack((3 * np.ones((4, 4)), np.eye(4)))
# >>>>>>>>>>

part_j = None #TODO
# >>>>>>>>>>
part_j = np.vstack((np.hstack((np.ones((4, 5)), np.zeros((4, 3)))), np.hstack((np.eye(4), -2 * np.ones((4, 4))))))
# >>>>>>>>>>

part_k = None #TODO
# >>>>>>>>>>
part_k = np.eye(8)[:,[4, 1, 4, 6]]
# >>>>>>>>>>

part_l = None #TODO
# >>>>>>>>>>
part_l = np.eye(8)[range(7, -1, -1)]
# >>>>>>>>>>

part_m = None #TODO
# >>>>>>>>>>
part_m = np.tril(2 * np.ones((8, 8)))
# >>>>>>>>>>
