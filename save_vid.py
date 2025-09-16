# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 13:48:05 2025

@author: WilliamNguyen
"""

import os
import glob
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as mpimg

def make_animation_from_pngs(image_dir=r"C:\Users\WilliamNguyen\Downloads\neutral",
                             pattern="iter*.png",
                             output="single_beam.mp4",
                             fps=30):
    files = sorted(glob.glob(os.path.join(image_dir, pattern)),
                   key=lambda f: int(''.join(filter(str.isdigit, os.path.basename(f)))))
    if not files:
        raise FileNotFoundError(f"No files found in {image_dir}\\{pattern}")

    # Read first image to get size
    img0 = mpimg.imread(files[0])
    height, width = img0.shape[:2]

    # Figure size in inches = pixels / dpi
    dpi = 300  # control here, but final video uses pixel size anyway
    fig = plt.figure(figsize=(width/dpi, height/dpi), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])  # fill entire figure, no borders
    ax.axis("off")

    im = ax.imshow(img0)

    def update(i):
        frame = mpimg.imread(files[i])
        im.set_array(frame)
        return [im]

    ani = animation.FuncAnimation(fig, update, frames=len(files),
                                  interval=1000/fps, blit=True)

    out_path = os.path.join(image_dir, output)
    ani.save(out_path, fps=fps, dpi=dpi)  # fps set here
    plt.close(fig)
    print(f"Saved animation to {out_path}")

make_animation_from_pngs(fps=4)
