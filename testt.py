import torch
import sys

print(torch.version.cuda)
print(sys.version)
print(torch.__version__)

print(torch.cuda.is_available())