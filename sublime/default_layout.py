import sublime
import sublime_plugin

class SetCustomLayoutCommand(sublime_plugin.WindowCommand):
    def run(self):
        layout = {
            "cols": [0.0, 0.75, 1.0],  # Define three columns
            "rows": [0.0, 0.33, 0.66, 1.0],  # Define four rows to create three equal-height sections
            "cells": [
                [0, 0, 1, 3],  # Group 1: covers 75% of width and entire height
                [1, 0, 2, 1],  # Group 2: covers 25% of width and top 33% height
                [1, 1, 2, 2],  # Group 2: covers 25% of width and middle 33% height
                [1, 2, 2, 3]   # Group 2: covers 25% of width and bottom 33% height
            ]
        }
        # Set the layout
        self.window.run_command("set_layout", layout)
