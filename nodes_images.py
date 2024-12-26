import torch
import nodes
import folder_paths

class ImageMotionGuider:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { 
            "image": ("IMAGE",),
            "move_range_x": ("INT", {"default": 0, "min": -150, "max": 150}),
            "frame_num": ("INT", {"default": 10, "min": 2, "max": 150}),
            "zoom": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 0.5, "step": 0.05}),
        }}
    
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "guide_motion"
    CATEGORY = "image/animation"

    def get_size(self, image):
        image_size = image.size()
        return int(image_size[2]), int(image_size[1])

    def guide_motion(self, image, move_range_x, frame_num, zoom):
        img_width, img_height = self.get_size(image)
        
        step_size = abs(move_range_x) / (frame_num - 1) if move_range_x != 0 else 0
        start_x = 0 if move_range_x > 0 else abs(move_range_x)
        
        # For negative motion, adjust the starting position to begin at 0,0
        if move_range_x < 0:
            start_x -= img_width
        
        batch = []
        mirrored = torch.flip(image, [2])
        
        for i in range(frame_num):
            x_pos = start_x + (step_size * i * (-1 if move_range_x < 0 else 1))
            x_pos = int(x_pos)
            x_pos = x_pos % img_width if move_range_x != 0 else 0
            
            current_zoom = (i / (frame_num - 1)) * zoom if zoom > 0 else 0
            if current_zoom > 0:
                crop_width = int(img_width * (1 - current_zoom))
                crop_height = int(img_height * (1 - current_zoom))
                x_start = (img_width - crop_width) // 2
                y_start = (img_height - crop_height) // 2
                
                zoomed_original = torch.nn.functional.interpolate(
                    image[:, y_start:y_start + crop_height, x_start:x_start + crop_width, :].permute(0, 3, 1, 2),
                    size=(img_height, img_width),
                    mode='bilinear'
                ).permute(0, 2, 3, 1)
                
                zoomed_mirror = torch.nn.functional.interpolate(
                    mirrored[:, y_start:y_start + crop_height, x_start:x_start + crop_width, :].permute(0, 3, 1, 2),
                    size=(img_height, img_width),
                    mode='bilinear'
                ).permute(0, 2, 3, 1)
            else:
                zoomed_original = image
                zoomed_mirror = mirrored
            
            canvas = torch.zeros((1, img_height, img_width, image.shape[3]))
            
            remaining_width = img_width
            current_x = x_pos
            use_flipped = False
            
            while remaining_width > 0:
                width = min(img_width - current_x, remaining_width)
                current_image = zoomed_mirror if use_flipped else zoomed_original
                
                canvas[0, :, img_width - remaining_width:img_width - remaining_width + width, :] = \
                    current_image[0, :, current_x:current_x + width, :]
                
                remaining_width -= width
                current_x = 0
                use_flipped = not use_flipped
            
            batch.append(canvas)
            
        return (torch.cat(batch, dim=0),)

NODE_CLASS_MAPPINGS = {
    "ImageMotionGuider": ImageMotionGuider,
}