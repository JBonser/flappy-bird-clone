from unittest import TestCase
from main import (
    collision_point_to_box,
    collision_box_to_box
)


class TestCollisions(TestCase):

    def test_collision_point_to_box(self):
        # Check just inside bounds
        self.assertTrue(collision_point_to_box(0.01, 0.01, 0, 0, 5, 5))
        self.assertTrue(collision_point_to_box(4.99, 4.99, 0, 0, 5, 5))

        # Check just outside bounds
        self.assertFalse(collision_point_to_box(-0.01, -0.01, 0, 0, 5, 5))
        self.assertFalse(collision_point_to_box(5.01, 5.01, 0, 0, 5, 5))

        # Check on the bounds
        self.assertTrue(collision_point_to_box(0, 0, 0, 0, 5, 5))
        self.assertTrue(collision_point_to_box(5, 5, 0, 0, 5, 5))

    def test_collision_box_to_box(self):
        # Check top right box 1 touches bottom left box 2
        self.assertTrue(collision_box_to_box(0, 5, 5, 5, 5, 0, 5, 5))

        # Check top right box 2 touches bottom left box 1
        self.assertTrue(collision_box_to_box(5, 0, 5, 5, 0, 5, 5, 5))

        # Check top left box 1 touches bottom right box 2
        self.assertTrue(collision_box_to_box(5, 5, 5, 5, 0, 0, 5, 5))

        # Check top left box 2 touches bottom right box 1
        self.assertTrue(collision_box_to_box(0, 0, 5, 5, 5, 5, 5, 5))

        # Check no collision
        self.assertFalse(collision_box_to_box(0, 0, 5, 5, 6, 6, 5, 5))
