import os
import numpy as np
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image

class AugmentedPlantDataset(Dataset):
    def __init__(self, plant_dir, nonplant_dir):
        self.samples = []
        for d, label in [(plant_dir, 1), (nonplant_dir, 0)]:
            for fname in os.listdir(d):
                if fname.lower().endswith(('.jpg','jpeg','png')):
                    self.samples.append((os.path.join(d, fname), label))

        # make more data, getting good data sucks
        self.variants = [
            # 0: normal
            transforms.Compose([]),
            # 1:  blur
            transforms.Compose([transforms.GaussianBlur(kernel_size=5)]),
            # 2: replace white background with noise
            transforms.Compose([
                transforms.Lambda(self._replace_white_with_noise)
            ]),
            # 3: add general noise
            transforms.Compose([
                transforms.Lambda(self._add_random_noise)
            ]),
        ]

        # resize, norm stuff
        self.post = transforms.Compose([
            transforms.Resize((480,680)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485,0.456,0.406],
                                 std=[0.229,0.224,0.225])
        ])


    def __len__(self):
        return len(self.samples) * len(self.variants)


    def __getitem__(self, idx):
        n_variants = len(self.variants)
        sample_idx = idx // n_variants
        variant_idx = idx % n_variants

        path, label = self.samples[sample_idx]
        img = Image.open(path).convert('RGB')
        img = self.variants[variant_idx](img)
        img = self.post(img)
        return img, label


    @staticmethod
    def _replace_white_with_noise(pil_img, thresh=240):
        arr = np.array(pil_img)
        mask = np.all(arr > thresh, axis=-1)
        noise = (np.random.rand(*arr.shape) * 255).astype(np.uint8)
        arr[mask] = noise[mask]
        return Image.fromarray(arr)

    @staticmethod
    def _add_random_noise(pil_img, noise_level=0.05):
        arr = np.array(pil_img).astype(np.float32) / 255.0
        noise = np.random.randn(*arr.shape) * noise_level
        arr = np.clip(arr + noise, 0.0, 1.0)
        arr = (arr * 255).astype(np.uint8)
        return Image.fromarray(arr)
