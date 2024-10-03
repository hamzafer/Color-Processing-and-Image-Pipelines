# Color Processing and Image Pipelines

## Overview
This repository contains detailed analyses and R&D work on color processing and image pipelines, with a focus on CMOS sensors, demosaicing, white balancing, and advanced deep learning techniques in the field of photography and image processing. The project covers everything from early-stage color correction (preprocessing) to final image output, focusing on how modern cameras and software systems process raw images.

## Key Topics Covered
1. **Color Processing Fundamentals:**
   - **CMOS Sensors & Temporal Multiplexing:** Analysis of sensor-specific color sensitivity functions.
   - **Linear vs. Non-linear Images:** Differences in representation and usage across formats (e.g., RAW, JPEG, HEIC).
   - **Defective Pixel Correction, Vignetting Correction, and Dark Current Compensation:** Essential preprocessing tasks to enhance image quality.
   - **White Balancing:** From basic methods like Gray World Assumption to advanced deep learning algorithms for auto white balancing.

2. **Chromatic Adaptation & Color Transformation:**
   - **Chromatic Adaptation in Cameras:** Techniques like auto white balancing and color correction to adjust image colors according to lighting conditions.
   - **Color Transformations:** From Adobe color space calibration to converting color spaces (e.g., XYZ to sRGB) while managing color loss and clamping.

3. **Demosaicing and Interpolation:**
   - **Demosaicing Process:** Techniques to reconstruct a full RGB image from camera sensor data using interpolation.
   - **Deep Learning in Demosaicing:** How neural networks improve interpolation, ground truth creation for supervised learning, and the challenges faced (e.g., DxO’s DeepPrime solution).

4. **Post-processing Techniques:**
   - **Tone Curves:** Applying and calibrating tone curves with hue preservation, and how preferences vary between manufacturers like Nikon and Canon.
   - **Non-linear Image Finalization:** Methods to create aesthetically pleasing images based on user or market preferences.

## Future Trends and Research Areas:
The repository also includes discussions on future challenges and opportunities in color science and image processing, including:
- **White Balance under Mixed Illumination:** Current challenges with deep learning.
- **Denoising and Demosaicing in Pipelines:** Addressing denoising using deep learning and combining demosaicing and denoising tasks.
- **HDR and Moving Objects:** Challenges in HDR with moving subjects and the potential of deep learning.
- **Multispectral & Hyperspectral Imaging:** Emerging research topics like multispectral demosaicing and noise calibration in hyperspectral imaging.

## Repository Contents
- **Scripts:** Python tools for color processing and image transformation (e.g., demosaicing, white balancing).
- **Research Notes:** Detailed notes on key concepts in color processing, tone curves, and chromatic adaptation.
- **Future Trends & Thesis Ideas:** Exploratory research and potential thesis ideas for future development in color science and imaging pipelines.

## Getting Started
Ensure you have Python and PyCharm for working with the code in this repository.

### Key Dependencies:
- **Python** (version 3.7 or above)
- **Required Libraries:** `numpy`, `opencv-python`, `matplotlib`

```bash
pip install numpy opencv-python matplotlib
```

## Acknowledgments
Special thanks to DxO and Adobe for inspiring the research on advanced image pipelines, tone curves, and demosaicing methods, and to Professor Victor Francisco Rodriguez-Galiano for continuous guidance.
