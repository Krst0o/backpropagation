import numpy as np
from variables import *


def translate(center, angle):
    return Point(center.x + arm_length * np.sin(angle), center.y - arm_length * np.cos(angle))


def find_line_points(alpha, beta):
    draw_points = []
    alpha = np.pi - alpha * np.pi
    beta = beta * np.pi * (-1.0)
    elbow_point = translate(Point(img_width, img_height/2), alpha)
    forearm_point = translate(elbow_point, np.pi - beta + alpha)
    draw_points.append(elbow_point)
    draw_points.append(forearm_point)
    return draw_points


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Examples(object):
    def __init__(self):
        self.center = Point(img_width, img_height/2)
        self.input = []
        self.output = []

    def generate(self, number_of_examples):
        for i in range(number_of_examples):
            point = self.generate_point()
            self.input.append([point.x, point.y])
        return self.input, self.output

    def generate_point(self):
        alpha = np.random.random() * np.pi
        beta = np.random.random() * np.pi
        self.output.append([alpha, beta])
        temp_point = translate(self.center, alpha)
        final_point = translate(temp_point, np.pi - beta + alpha)
        return final_point
