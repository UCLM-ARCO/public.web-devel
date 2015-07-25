#!/usr/bin/env python
# -*- coding: utf-8; mode: python; -*-

import os
from argparse import ArgumentParser
from PIL import Image, ImageDraw


class TileMaker(object):
    def __init__(self, args):
        self.source = Image.open(args.image)
        self.output_dir = args.output

        self.prepare_source()
        for i in range(args.zoom):
            self.make_tile_for_zoom(i)

    def prepare_source(self):
        w, h = self.source.size
        size = max(w, h)
        background = Image.new("RGB", (size, size))
        background.paste(self.source, ((size - w) / 2, (size - h) / 2))
        self.source = background

    def make_output_dir(self, name):
        path = os.path.join(self.output_dir, name)
        if os.path.exists(path):
            return path

        os.makedirs(path)
        return path

    def make_tile_for_zoom(self, zoom):
        img = self.resize_image(self.source, zoom)
        self.crop_tiles(img, zoom)

    def resize_image(self, img, zoom):
        w, h = img.size

        new_h = 256 * 2 ** zoom
        ratio = float(new_h) / h
        new_w = int(w * ratio)

        return img.resize((new_w, new_h))

    def crop_tiles(self, src, zoom):
        w, h = src.size
        for x in range(w / 256):
            for y in range(h / 256):
                self.save_tile(src, x, y, zoom)

    def save_tile(self, src, x, y, z):
        left = 256 * x
        upper = 256 * y
        right = left + 256
        lower = upper + 256

        dir_path = "{}/{}".format(z, x)
        dir_path = self.make_output_dir(dir_path)

        img_path = "{}/{}.jpg".format(dir_path, y)
        print "tiling image '{}'...".format(img_path)
        tile = src.crop((left, upper, right, lower))

        draw = ImageDraw.Draw(tile)
        draw.text((0, 0), "{}/{}/{}".format(z, x, y))

        tile.save(img_path)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("image", help="Source Image")
    parser.add_argument("-o", "--output", default="output", help="Output directory")
    parser.add_argument("-z", "--zoom", default=5, type=int, help="Zoom level")

    args = parser.parse_args()
    TileMaker(args)
