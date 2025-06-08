import os
import torch
from torch.utils.data import random_split, DataLoader
from dataset import AugmentedPlantDataset
from architecture import PlantDetectorCNN, PlantDetectorCNNSimple, PlantDetectorCNNSimpleAF, PlantDetectorCNNEdges

plant_dir = r"E:\plant_images_weed_big"
nonplant_dir = r"E:\plant_images_weed_not_big"

batch_size = 16
lr = 0.0002
num_epochs = 4
split_ratios = [0.7, 0.15, 0.15]  # train, val, test


full_dataset = AugmentedPlantDataset(plant_dir, nonplant_dir)
total = len(full_dataset)
train_len = int(split_ratios[0] * total)
val_len = int(split_ratios[1] * total)
test_len = total - train_len - val_len
train_ds, val_ds, test_ds = random_split(full_dataset, [train_len, val_len, test_len])

dataloaders = {
    'train': DataLoader(train_ds, batch_size=batch_size, shuffle=True),
    'val': DataLoader(val_ds, batch_size=batch_size, shuffle=False),
    'test': DataLoader(test_ds, batch_size=batch_size, shuffle=False)
}

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = PlantDetectorCNNEdges().to(device)
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

best_val_acc = 0.0
print(len(dataloaders['train']))
print(len(dataloaders['val']))
print(len(dataloaders['test']))
print(full_dataset)
for epoch in range(num_epochs):

    model.train()  # only sets mode, has dropout
    running_loss = 0.0
    running_corrects = 0
    i = 0
    for inputs, labels in dataloaders['train']:
        print(f"Epoch {epoch}   -   {i}/{len(dataloaders['train'])}")
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)  # calculates gradients
        loss = criterion(outputs, labels)
        loss.backward()  # backpropagates loss according to gradients
        optimizer.step()  # actually adjust weights
        running_loss += loss.item() * inputs.size(0)
        preds = torch.argmax(outputs, 1)
        running_corrects += torch.sum(preds == labels.data)
        i += 1
    epoch_loss = running_loss / train_len
    epoch_acc = running_corrects.double() / train_len
    print(f"Epoch {epoch+1}/{num_epochs} - train loss: {epoch_loss:.4f}, acc: {epoch_acc:.4f}")

    # Validation
    model.eval()  # again just setting mode, no dropout, no gradients, no optimization stuff going on
    val_corrects = 0
    with torch.no_grad():
        for inputs, labels in dataloaders['val']:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            preds = torch.argmax(outputs, 1)
            val_corrects += torch.sum(preds == labels.data)
    val_acc = val_corrects.double() / val_len
    print(f"Validation acc: {val_acc:.4f}")
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        os.makedirs('saved_models', exist_ok=True)
        torch.save(model.state_dict(), 'saved_models/best_plant_detector3000.pth')
        print("Saved new best model")

# After training, evaluate on test set
model.load_state_dict(torch.load('saved_models/best_plant_detector.pth'))
model.eval()
test_corrects = 0
with torch.no_grad():
    for inputs, labels in dataloaders['test']:
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = model(inputs)
        preds = torch.argmax(outputs, 1)
        test_corrects += torch.sum(preds == labels.data)

test_acc = test_corrects.double() / test_len
print(f"Test accuracy: {test_acc:.4f}")
