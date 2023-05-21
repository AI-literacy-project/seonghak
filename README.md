## Objective

---

CycleGAN은 image-to-image translation을 개선한 논문이다. 하지만 그 탓에 object translation에서의 한계점이 보인다. 이를 해결하기 위해 이미지에 object가 있으면 Attention으로 object을 masking해서 object translation의 성능을 개선한다.