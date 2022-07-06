import numpy as np
import sys

# 기본요금
BASIC = dict({
    "단일": np.array([730, 1260, 6060]),
    "종합": np.array([910, 1600, 7300])
})
# 전력량요금
ELEC = dict({
    "단일": np.array([73.3, 142.3, 210.6]),
    "종합": np.array([88.3, 182.9, 275.6])
})
# 분할 계산 설정 참고 VALUE
STEP_LIMITS_HOUSEHOLD = dict({
    "기타": np.array([200, 200]),
    "여름": np.array([300, 150])
})
