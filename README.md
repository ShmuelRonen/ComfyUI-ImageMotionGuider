# ComfyUI-ImageMotionGuider

A custom ComfyUI node designed to create seamless motion effects from single images by integrating with Hunyuan Video through latent space manipulation.

![image](https://github.com/user-attachments/assets/c62be207-2eb3-4d85-a3b2-d8542c050c6f)


https://github.com/user-attachments/assets/e6c770ed-f767-4beb-ae02-c61e9b8cfa5a


## Overview

The ComfyUI-ImageMotionGuider node creates smooth motion sequences from static images through intelligent mirroring techniques. Its primary purpose is to influence AI video generation models' behavior through latent space guidance, particularly designed for Hunyuan Video integration.

## Installation

Install from Custom Node Manager

or

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ShmuelRonen/ComfyUI-ImageMotionGuider.git
```

## Features

- **Bidirectional Motion**: Horizontal movement control (-150 to 150 pixels)
- **Variable Frame Generation**: Create 2 to 150 frame sequences
- **Dynamic Zoom**: Optional zoom effect (0.0 to 0.5)
- **Seamless Transitions**: Smart image mirroring for continuous motion
- **VAE Integration**: Direct compatibility with VAE encoders
- **Hunyuan Video Ready**: Designed for latent space guidance

## Parameters

| Parameter | Type | Range | Default | Description |
|-----------|------|--------|---------|-------------|
| image | IMAGE | - | - | Input image |
| move_range_x | INT | -150 to 150 | 0 | Motion range (positive = right, negative = left) |
| frame_num | INT | 2 to 150 | 10 | Number of frames to generate |
| zoom | FLOAT | 0.0 to 0.5 | 0.0 | Optional zoom intensity |

## Working with Hunyuan Video

This node is specifically designed to enhance Hunyuan Video generation through:

1. **Motion Generation**:
   - Creates frame sequences with consistent directional motion
   - Maintains original image orientation
   - Ensures smooth transitions between frames

2. **Latent Space Integration**:
   - Compatible with VAE encoders
   - Provides motion guidance through latent space
   - Influences video generation behavior

3. **Direction Control**:
   - Positive values: Right-moving sequence
   - Negative values: Left-moving sequence
   - Both maintain original image orientation

## Technical Implementation

### Motion Algorithm
- Preserves original image orientation
- Creates mirrored copies for seamless transitions
- Handles directional changes smoothly
- Combines motion with optional zoom

### Core Features
- PyTorch-based tensor operations
- CUDA acceleration support
- Efficient memory management
- Smart edge handling

## Usage Tips

### Image Selection
- Use images with balanced horizontal composition
- Avoid prominent features at edges
- Higher resolution images recommended

### Parameter Settings

1. **Motion Range (-150 to 150)**:
   - Start with ±50 for testing
   - Larger values for more dramatic motion
   - Consider image content when setting

2. **Frame Count (2-150)**:
   - 10-20 frames good for testing
   - Higher counts for smoother motion
   - Balance smoothness vs. processing time

3. **Zoom (0.0-0.5)**:
   - Use sparingly
   - Enhances motion effect
   - Combine with motion for dynamic results

### Hunyuan Integration

1. **Workflow Setup**:
   ```
   [Image Loader] → [ImageMotionGuider] → [VAE Encoder] → [Hunyuan Video]
   ```

2. **Best Practices**:
   - Adjust denoise levels in Hunyuan
   - Consider frame count impact
   - Test different motion ranges

## Requirements
- ComfyUI
- PyTorch
- VAE encoder (for latent conversion)
- Hunyuan Video (for intended usage)

## Contributing

We welcome contributions:
- Bug reports
- Feature requests
- Pull requests
- Usage examples

## License

MIT License

## Acknowledgments

- Developed for Hunyuan Video integration
- Built for the ComfyUI community
- Thanks to all contributors
