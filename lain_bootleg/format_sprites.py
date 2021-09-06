import sys
import cv2
import os
import shutil

# wip, will expand the marks as more shit is needed

FORMAT = ".png"


class Sprite:
    def __init__(self, name, index):
        self.name = name + FORMAT
        self.index = index


class SpriteSheet:
    def __init__(self, name, start_index, end_index):
        self.name = name + FORMAT
        self.start_index = start_index
        self.end_index = end_index


marks = [
    Sprite("lain_room", 128),
    # DEFAULT OUTFIT
    Sprite("lain_default_standing", 129),
    SpriteSheet("lain_default_walk_right", 130, 140),
    SpriteSheet("lain_default_walk_left", 141, 148),
    # SCHOOL OUTFIT
    Sprite("school_outfit", 247),
    Sprite("lain_school_standing", 243),
    SpriteSheet("lain_school_walk_right", 149, 159),
    SpriteSheet("lain_school_walk_left", 160, 167),
    # HAT OUTFIT
    Sprite("hat_outfit", 248),
    Sprite("lain_hat_standing", 244),
    SpriteSheet("lain_hat_walk_right", 168, 178),
    SpriteSheet("lain_hat_walk_left", 179, 186),
    # BEAR OUTFIT
    Sprite("bear_outfit", 249),
    Sprite("lain_bear_standing", 245),
    SpriteSheet("lain_bear_walk_right", 187, 197),
    SpriteSheet("lain_bear_walk_left", 198, 205),
    # PAJAMA OUTFIT
    Sprite("pajama_outfit", 250),
    Sprite("lain_pajama_standing", 246),
    SpriteSheet("lain_pajama_walk_right", 206, 216),
    # ALIEN OUTFIT
    Sprite("lain_alien_standing", 225),
    SpriteSheet("lain_alien_walk_right", 226, 234),
    SpriteSheet("lain_alien_walk_left", 235, 242)
]


if __name__ == "__main__":
    src_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    if (not os.path.isdir(dest_dir)):
        os.mkdir(dest_dir)
    else:
        shutil.rmtree(dest_dir)
        os.mkdir(dest_dir)

    # copy to new directory with respective numbers as names
    for file_name in os.listdir(src_dir):
        new_name = file_name.split("_")[3]
        shutil.copyfile(src_dir + file_name, dest_dir + new_name)

    for mark in marks:
        if isinstance(mark, Sprite):
            src = os.path.join(dest_dir, str(mark.index))
            dest = os.path.join(dest_dir, mark.name)

            print("Renaming {} to {}...".format(src, dest))
            os.rename(os.path.abspath(src), os.path.abspath(dest))
        if isinstance(mark, SpriteSheet):
            spritesheet_length = mark.end_index - mark.start_index

            print("Making spritesheet {}...".format(mark.name))
            sprites = [cv2.imread(os.path.join(dest_dir, str(i)), cv2.IMREAD_UNCHANGED)
                       for i in range(mark.start_index, mark.end_index + 1)]

            im_tile = cv2.hconcat(sprites)
            cv2.imwrite(os.path.join(dest_dir + mark.name), im_tile)

            # remove frames since they're useless now
            for i in range(mark.start_index, mark.end_index + 1):
                os.remove(os.path.join(dest_dir + str(i)))