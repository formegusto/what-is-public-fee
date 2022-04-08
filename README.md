# what is public fee?

# 1. 전기요금의 기본구성 요소

> **한국전력공사(KEPCO)의 전기요금표 21.01.01을 기준으로 작성되었습니다.**

![Untitled](https://user-images.githubusercontent.com/52296323/162350260-657d6301-ea44-4339-990e-93a4d03760e0.png)

**전기요금의 기본구조**는 **기본요금, 전력량요금, 기후환경요금, 연료비조정요금**으로 구성이 되어 있다.

![Untitled 1](https://user-images.githubusercontent.com/52296323/162350266-9ee3b240-071f-458c-9f3a-4231e6d1e2ec.png)

전기요금은 구성요소들로 계산이 된 후, **최종적으로 부가가치세와 전력산업기반기금이 추가**되어 **최종청구금액이 산정**된다.

# 2. 단일계약과 종합계약

## 요금제

**아파트의 전기요금계약은 종합계약과 단일계약**으로 나누어진다. 해당 계약들은 전기요금 산정에 사용되는 **요금제에 차이**가 있으며, 아파트의 전기 사용 특성에 따라 요금제를 선택한다.

|          | 세대부            | 공용부            |
| -------- | ----------------- | ----------------- |
| 종합계약 | 주택용 전력(저압) | 일반용 전력(갑) 1 |
| 단일계약 | 주택용 전력(고압) | 주택용 전력(고압) |

**종합계약**의 경우에는 **세대부의 가구들에는 주택용전력(저압) 요금이 적용**되고, **공용부의 사용량에 대해서는 일반용 전력(갑) 1 요금이 적용**된다. 이에 반해 **단일계약**은 세대부와 공용부의 사용량이 모두 합해진 **아파트 전체 사용량에 대하여 주택용 전력(고압) 요금이 적용**된다.

단일계약은 아파트 전체 사용량에 대하여 산정된 아파트 전체 사용요금에서 **세대부의 가구들에게 각 사용량 만큼의 주택용 전력(고압) 요금을 적용하여 분배**한다. **세대부 분배가 끝난 후에 나머지 요금은 공용부의 요금**으로 한 번더 **가구들에게 $\frac{1}{n}$ 로 분배**가 된다.

## 순수 공용부 사용량에 대한 산정으로 구성되는 종합계약의 공용부 요금

![Untitled 2](https://user-images.githubusercontent.com/52296323/162350275-d3418d95-140a-4b7b-aff4-43b3ae992630.png)

일반용전력(갑) 1 요금표

![Untitled 3](https://user-images.githubusercontent.com/52296323/162350281-57bf3f42-4336-49fe-82c7-b1f10e4fad02.png)

**종합계약**은 위 요금표를 참고하여, **공용부를 전기요금 구성요소로 뚜렷하게 나타낼 수가 있다.** 즉, 순수 공용부 사용량에 대한 요금계산이 이루어진다는 것 이다. **_eq.공용부 요금의 투명성이 보장된다._**

## 단일계약의 공용부 요금

![Untitled 4](https://user-images.githubusercontent.com/52296323/162350288-5e717104-4031-44ca-9ce9-c87ec076846f.png)

주택용전력(고압) 요금표

![Untitled 5](https://user-images.githubusercontent.com/52296323/162350294-6a9fccfa-19ad-441d-bf55-d2a8bdf0e5d4.png)

**단일계약의 공용부 요금**은 **아파트 전체 사용요금에서 세대부의 가구들이 수거해 간 요금의 나머지**이기 때문에 **순수 공용부 사용량에 대한 산정이라고 보기는 어렵다.**

생김새를 알 수 없는 단일계약의 공용부 전기요금의 특징에 주택용전력(고압) 요금제의 누진세 특징까지 붙게되니 더 아리송해지는 것이 단일계약의 공용부 전기요금이다.

하지만 **공용부 요금을 산정하는 아파트 전체 사용요금과 세대부의 수거요금에 밀접한 관계**가 있으며, 본문에서는 이러한 **공용부의 요금을 전기요금의 구성요소로 나누어 분석하면서 단일계약상의 공용부 이론을 확립해보도록 한다.**
