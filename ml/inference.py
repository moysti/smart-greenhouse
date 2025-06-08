import torch
from PIL import Image
from torchvision import transforms
from architecture import PlantDetectorCNN

def predict(image_path, model_path='saved_models/best_plant_detector.pth'):
    # load
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = PlantDetectorCNN().to(device)
    state_dict = torch.load(
        model_path,
        map_location=device,
        weights_only=True
    )
    model.load_state_dict(state_dict)
    model.eval()

    # size, norm
    preprocess = transforms.Compose([
        transforms.Resize((480, 680)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    # get input
    img = Image.open(image_path).convert('RGB')
    input_tensor = preprocess(img).unsqueeze(0).to(device)
    # awesome prediction
    with torch.no_grad():
        outputs = model(input_tensor)
        print(outputs)
        pred = torch.argmax(outputs, dim=1).item()
        classes = {0: 'non-plant', 1: 'plant'}
    print(f"Prediction: {classes[pred]}")

