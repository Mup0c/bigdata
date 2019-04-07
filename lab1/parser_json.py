from image_model import *
import re

BLOCK_SIZE = 4096


class Parser():
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.block = self.file.read(BLOCK_SIZE)
        splitted = self.block.split(",", maxsplit=3)
        self.height = int(re.findall(r'\b\d+\b', splitted[0])[0])
        self.width = int(re.findall(r'\b\d+\b', splitted[1])[0])
        self.frames_count = int(re.findall(r'\b\d+\b', splitted[2])[0])
        self.frame_number = 0
        self.frame = Frame(self.height, self.width, [])
        self.block = splitted[-1]


    def read_next_triplet(self):
        if len(self.block) < 100:
            self.block += self.file.read(BLOCK_SIZE)
        splitted = self.block.split(",", maxsplit=3);
        self.block = splitted[-1]
        return rgb(*[int(re.findall(r'\b\d+\b', splitted[i])[0]) for i in range(3)])

    def loop_file(self):
        self.file.seek(0)
        self.block = self.file.read(BLOCK_SIZE).split(",", maxsplit=3)[-1]
        self.frame_number = 0

    def parse(self):
        while len(self.frame.pixels) < self.width * self.height:
            self.frame.pixels.append(self.read_next_triplet())
        self.frame_number += 1
        if self.frame_number == self.frames_count:
            self.loop_file()
        frame = Frame(self.height, self.width, [])
        frame, self.frame = self.frame, frame
        return frame