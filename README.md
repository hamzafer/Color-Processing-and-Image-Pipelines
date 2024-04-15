**Day 1: Color Processing**

- CMOS
- Temporal Multiplexing
- Each camera has unique sensitivity graph/functions.
- Linear and Non-linear images
- Each manufacturer has their own RAW image storage.
- Adobe introduced a standard DNG.
- Linear images are not visually pleasant and aren't commonly used in photography.
- JPEG uses 8 bits.
- HEIC format, used by iPhone, allows for more bits.
- Non-linear images are aesthetically pleasing because our eyes perceive things non-linearly.

**Preprocessing:**

**Defective Pixel Correction:** Some sensors may fail, leading to interpolation. It's crucial to fix these at the beginning to prevent future issues.

**Co-linearization:** This is not always necessary, but occasionally you might need to apply a function to linearize the data.

**Dark Current Compensation:** Even when the lens is closed, some pixels may still produce data. To correct this, subtract the dark image. This procedure is generally performed using a common formula.

**Vignetting Correction:** Lower-quality lenses may cause the image to darken at the corners due to uneven illumination. To correct this, capture a white image and subtract it from the original in a similar manner as mentioned above. This can also be done using a specific formula.

**White Balancing:**

This process adjusts the colors to account for the color temperature of the light source, ensuring that white objects appear white in the final image.

Chromatic adaptation:

 is a fascinating aspect of visual perception. It refers to the human visual system's ability to adjust to changes in illumination in order to preserve the appearance of object colors. It plays a crucial role in how we perceive and interpret the world around us, allowing us to see consistent colors even under varying lighting conditions.

How its done in the cameras?

Cameras achieve chromatic adaptation through a process called color correction or color balance, which involves adjusting the intensities of colors (red, green, and blue primary colors). The goal is to render specific colors – particularly neutral colors – correctly; hence, the general method is sometimes called gray balance, neutral balance, or white balance.

Auto white balance.

Gray World Assumption:

The Gray World Assumption is an underlying principle in color constancy and digital photography. This assumption presumes that the average reflectance of objects in the world is approximately constant and hence, gray. It's a significant concept that plays a pivotal role in digital image processing where it aids in maintaining color consistency across different lighting conditions.

To maintain details, a **clamping** operation is needed to limit values within a range of 1. This ensures a balance between preserving detail and limiting value.

White Patch Algo

GIMP: When utilizing the Graphic Image Manipulation Program, also known as GIMP, for the purpose of white balancing, it's important to understand its functionalities. GIMP is an incredibly powerful tool that can significantly improve the quality of your images by adjusting the white balance. This process ensures that colors are rendered accurately in your images, which can be particularly useful when working with photographs taken under different lighting conditions.

**Deep learning algorithms** nowadays in auto white balancing.

Deep learning algorithms have greatly improved the accuracy and efficiency of auto white balancing. These algorithms use neural networks to analyze the color data in an image and adjust the white balance accordingly, producing images that are visually pleasing and accurately represent the scene.

Till here we are working with one channel image, but now moving onto the demosaicing.

**Demosaicing:**

You don’t get the demosaic image, camera outputs the RBG image.

**Interpolation:**

In the process of demosaicing, interpolation plays a crucial role. This process is used to estimate the missing colors in each pixel. Several methods exist for interpolation, each with their unique strengths and weaknesses.

Cameras have their own methods and they are not public - cuz its difficult

Same goes for DxO as well lol

`Deep learning methods - difficult DxO→ creating ground truth for supervised learning → Demosaic images, cuz we have images but not the output.`

Deep Prime - Super resolution and Demosaicing. → DxO products

Now we have the 3 channel image.

**Color Transform:**

Adobe color space?

In photolab we can use both color checkers

Custom made color patches for color calibration

You have to do it in a linear space

You want grey to have the same space?

**Least square solution**

Works 95% of the time

**Polynomial**

Start adding dependencies in the channel

Adding info that maybe useful

Overfitting

**Root Polynomial**

Not affected by exposure changes

Practice tomorrow!

There is no way to know until you try - you start with the linear one

Now we have the uniform color space, we can work in any software, adobe or colorlab

**From uniform to sRGB (lets assume) XYZ → RGB:**

sRGB is not good because we are going to lose a lot of colors

You will need to clamp - so thats why will lose details and info

Converting → Computing a matrix

**Post Processing:**

Tone curves: markets/people have their own preference

DxO try to calibrate on each manufacturer (tone curves)

Hard to find the scientific relationship btw tone curves, its just based on liking and preferences

Example Nikon and Canon would have different tone curves

When you apply tone curve - you are changing hues a bit (purple will become magenta lets say) → apply with hue preservation to preserve pixel hue → sometimes its not obvious → but matters in cases lets say a concert lights.

Now we have non linear image, and we can save the image as you want.

**Saving image (image pipeline ends).**

**Future Trends: (master thesis ideas)**

White balance → Mixed illumination (Deep learning struggles)

Denoising → Best solution deep learning → Creating dataset is still difficult → you have to create noise which is in the camera, only the gaussian noise won’t help. 

Demosaicing and Denoising are very close in the pipeline. Still not clear what you need to do first.

DeepPrime (DxO) does both at once - 2020 and onwards (but how?)

HDR → Deep learning - difficulty when object is moving - how to make a dataset was hard → how to get from a single image only (still challenging).

Multispectral Imaging → more complicated demosacing.

Hyperspectral Imaging → calibrating noise is complicated.

Spectra from RGB.

**Color science toolbox → Pycharm**
