import unittest
import numpy as np
from gradescope_utils.autograder_utils.decorators import weight, number, visibility
from hw07progsol import perspective, hom_rotate_x, hom_rotate_y, hom_rotate_z, translate, full_transform_matrix, matrix_to_projection, global_params, shape_matrices

def perspective_sol(d):
    return np.array(
        [[1., 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 0],
         [0, 0, -1./d, 1]])

def hom_rotate_x_sol(theta):
    return np.array(
        [[1, 0, 0, 0],
         [0, np.cos(theta), -np.sin(theta), 0],
         [0, np.sin(theta), np.cos(theta), 0],
         [0, 0, 0, 1]])

def hom_rotate_y_sol(theta):
    return np.array(
        [[np.cos(theta), 0, np.sin(theta), 0],
         [0, 1, 0, 0],
         [-np.sin(theta), 0, np.cos(theta), 0],
         [0, 0, 0, 1]])


def hom_rotate_z_sol(theta):
    return np.array(
        [[np.cos(theta), -np.sin(theta), 0, 0],
         [np.sin(theta), np.cos(theta), 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]])

def translate_sol(x, y, z):
    return np.array(
        [[1.0, 0, 0, x],
         [0, 1, 0, y],
         [0, 0, 1, z],
         [0, 0, 0, 1]])

def full_transform_matrix_sol(p):
    return np.linalg.multi_dot(
        [perspective(p['d']),
         translate(p['tx'], p['ty'], p['tz']),
         hom_rotate_z(p['rz']),
         hom_rotate_y(p['ry']),
         hom_rotate_x(p['rx'])])

def matrix_to_projection_sol(m):
    two_d_m = np.apply_along_axis(lambda p: p[:-2] / p[-1], 0, m)
    points = list(two_d_m.T)
    return list(zip(points[0::2], points[1::2]))

class TestSubmission(unittest.TestCase):

    @weight(5)
    def test_shape(self):
        self.assertEqual(perspective(10.0).shape, (4, 4))
        self.assertEqual(hom_rotate_x(10.0).shape, (4, 4))
        self.assertEqual(hom_rotate_y(10.0).shape, (4, 4))
        self.assertEqual(hom_rotate_z(10.0).shape, (4, 4))
        self.assertEqual(translate(10.0, 10.0, 10.0).shape, (4, 4))

    @weight(5)
    def test_perspective(self):
        for _ in range(5):
            x = np.random.rand()
            self.assertTrue(np.allclose(perspective(x), perspective_sol(x)))

    @weight(5)
    def test_rx(self):
        for _ in range(5):
            t = np.random.rand()
            self.assertTrue(np.allclose(hom_rotate_x(t), hom_rotate_x_sol(t)))

    @weight(5)
    @visibility("after_due_date")
    def test_ry(self):
        for _ in range(5):
            t = np.random.rand()
            self.assertTrue(np.allclose(hom_rotate_y(t), hom_rotate_y_sol(t)))

    @weight(5)
    @visibility("after_due_date")
    def test_rz(self):
        for _ in range(5):
            t = np.random.rand()
            self.assertTrue(np.allclose(hom_rotate_z(t), hom_rotate_z_sol(t)))

    @weight(5)
    @visibility("after_due_date")
    def test_translate(self):
        for _ in range(5):
            t = np.random.rand(3)
            self.assertTrue(np.allclose(translate(t[0], t[1], t[2]), translate_sol(t[0], t[1], t[2])))

    @weight(2)
    def test_full_shape(self):
        self.assertEqual(full_transform_matrix().shape, (4, 4))

    @weight(2)
    def test_full_p(self):
        global_params['d'] = 10.0
        global_params['tx'] = 0.0
        global_params['ty'] = 0.0
        global_params['tz'] = 0.0
        global_params['rx'] = 0.0
        global_params['ry'] = 0.0
        global_params['rz'] = 0.0
        for _ in range(5):
            self.assertTrue(np.allclose(full_transform_matrix(), perspective_sol(10.0)))

    @weight(3)
    @visibility("after_due_date")
    def test_full_r(self):
        for _ in range(5):
            global_params['d'] = 10.0
            global_params['tx'] = 0.0
            global_params['ty'] = 0.0
            global_params['tz'] = 0.0
            rx, ry, rz = np.random.rand(3)
            global_params['rx'] = rx
            global_params['ry'] = ry
            global_params['rz'] = rz
            self.assertTrue(np.allclose(full_transform_matrix(), perspective_sol(10.0) @ hom_rotate_z_sol(rz) @ hom_rotate_y_sol(ry) @ hom_rotate_x_sol(rx)))

    @weight(3)
    @visibility("after_due_date")
    def test_full_t(self):
        for _ in range(5):
            tx, ty, tz = np.random.rand(3)
            global_params['d'] = 10.0
            global_params['tx'] = tx
            global_params['ty'] = ty
            global_params['tz'] = tz
            global_params['rx'] = 0.0
            global_params['ry'] = 0.0
            global_params['rz'] = 0.0
            self.assertTrue(np.allclose(full_transform_matrix(), perspective_sol(10.0) @ translate_sol(tx, ty, tz)))

    @weight(5)
    @visibility("after_due_date")
    def test_full(self):
        for _ in range(5):
            global_params['d'] = 10.0 + np.random.rand()
            global_params['tx'] = np.random.rand()
            global_params['ty'] = np.random.rand()
            global_params['tz'] = np.random.rand()
            global_params['rx'] = np.random.rand()
            global_params['ry'] = np.random.rand()
            global_params['rz'] = np.random.rand()
            self.assertTrue(np.allclose(full_transform_matrix(), full_transform_matrix_sol(global_params)))

    @weight(2)
    def test_m_to_p_length(self):
        self.assertTrue(len(matrix_to_projection(perspective_sol(10.0) @ shape_matrices['cube'])) == 15)

    @weight(2)
    @visibility("after_due_date")
    def test_m_to_p_length_2(self):
        self.assertTrue(len(matrix_to_projection(perspective_sol(10.0) @ shape_matrices['pyramid'])) == 11)

    @weight(2)
    @visibility("after_due_date")
    def test_m_to_p_points(self):
        points = matrix_to_projection(perspective_sol(10.0) @ shape_matrices['pyramid'])
        for i in range(len(points)):
            assert(len(points[i]) == 2)

    @weight(3)
    def test_m_to_p_basic_1(self):
        example = np.array(
            [[1.0, 1, 1, 1],
             [1, 1, 1, 1],
             [0, 0, 0, 0],
             [1, 2, 3, 4]])
        output = [(np.array([1., 1.]), np.array([0.5, 0.5])),
                  (np.array([0.33333333, 0.33333333]), np.array([0.25, 0.25]))]
        test = matrix_to_projection(example)
        for i in range(2):
            x, y = test[i]
            self.assertTrue(np.allclose(x, output[i][0]))
            self.assertTrue(np.allclose(y, output[i][1]))

    @weight(4)
    def test_m_to_p_basic_2(self):
        points = matrix_to_projection(perspective_sol(10.0) @ shape_matrices['pyramid'])
        sol = matrix_to_projection_sol(perspective_sol(10.0)@ shape_matrices['pyramid'])
        for i in range(len(sol)):
            x, y = points[i]
            xs, ys = sol[i]
            self.assertTrue(np.allclose(x, xs))
            self.assertTrue(np.allclose(y, ys))

    @weight(7)
    @visibility("after_due_date")
    def test_m_to_p_full(self):
        a = np.random.rand(3, 100)
        a = np.vstack((a, np.array([np.zeros(100)])))
        sub = matrix_to_projection(perspective_sol(10.0) @ a)
        sol = matrix_to_projection_sol(perspective_sol(10.0) @ a)
        for i in range(len(sol)):
            x, y = sub[i]
            xs, ys = sol[i]
            self.assertTrue(np.allclose(x, xs))
            self.assertTrue(np.allclose(y, ys))
