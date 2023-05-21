## Objective

CycleGAN은 image-to-image translation을 개선한 논문이다. 하지만 그 탓에 object translation에서의 한계점이 보인다. 이를 해결하기 위해 이미지에 object가 있으면 Attention으로 object을 masking해서 object translation의 성능을 개선한다.

## Hypothesis

1. Attention을 이용해서 CycleGAN의 Network를 변경하면 object의 texture만 변경이 가능한가?
2. 만일 가능하다면 object가 없는 이미지에서는 학습이 잘 이루어 지는가?
3. 

## Method

1. Segmentation
2. Sementic supervision
3. Attention - AttentionGAN

## AttentionGAN Review

[AttentionGAN](https://www.notion.so/AttentionGAN-94cc9fb177844d9484714054fc509a46)

## Preliminary

- [x]  CycleGAN 환경설정하기
- [x]  maps data Train해보기
- [ ]  시각화 확인하기
- [ ]  maps dataset으로 학습 시켜보기
- [ ]  horse2zebra dataset으로 학습 시켜보기
- [ ]  maps dataset으로 학습 시켜보기
- [ ]  network 바꿔서 hose2zebra 다시 학습시켜보기