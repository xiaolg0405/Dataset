import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# ================== Set Plot Style ==================
BASE_FONT_SIZE = 18
LABEL_FONT_SIZE = 20
LEGEND_FONT_SIZE = 18
LEGEND_TITLE_SIZE = 18
ANNO_FONT_SIZE = 18
MARKER_SIZE_JAN = 150
MARKER_SIZE_APR = 120
MONTH_LEG_ANCHOR = (0.02, 0.99)
ANNO_POS = (0.02, 0.82)

plt.rcParams['font.family'] = 'SimHei' # Note: Ensure SimHei is installed, or switch to Arial
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = BASE_FONT_SIZE

# ------------------ Data Definitions ------------------
# Note: Raw data is provided in S3 Dataset.xlsx. 
# Here we calculate statistics for visualization purposes.

data_jan = {
    'CK1': {
        'VC': np.mean([14.23, 14.42, 13.46, 14.23, 13.85]),
        'VC_std': np.std([14.23, 14.42, 13.46, 14.23, 13.85]),
        'Sugar': np.mean([1.9829, 2.0698, 2.0935, 2.02635, 2.0461]),
        'Sugar_std': np.std([1.9829, 2.0698, 2.0935, 2.02635, 2.0461]),
        'Acid': np.mean([0.9112, 0.938, 0.8844, 0.9112, 0.8844]),
        'Acid_std': np.std([0.9112, 0.938, 0.8844, 0.9112, 0.8844])
    },
    'CK2': {
        'VC': np.mean([5.38, 5.58, 5.58, 5.77, 5.77]),
        'VC_std': np.std([5.38, 5.58, 5.58, 5.77, 5.77]),
        'Sugar': np.mean([1.9355, 1.9592, 1.9829, 1.97105, 1.9987]),
        'Sugar_std': np.std([1.9355, 1.9592, 1.9829, 1.97105, 1.9987]),
        'Acid': np.mean([0.8576, 0.938, 0.9112, 0.8576, 0.938]),
        'Acid_std': np.std([0.8576, 0.938, 0.9112, 0.8576, 0.938])
    },
    'TK': {
        'VC': np.mean([14.04, 12.69, 13.27, 12.88, 13.85]),
        'VC_std': np.std([14.04, 12.69, 13.27, 12.88, 13.85]),
        'Sugar': np.mean([1.99475, 2.08955, 2.1251, 2.0461, 2.02635]),
        'Sugar_std': np.std([1.99475, 2.08955, 2.1251, 2.0461, 2.02635]),
        'Acid': np.mean([0.9112, 0.8844, 0.9112, 0.938, 0.8576]),
        'Acid_std': np.std([0.9112, 0.8844, 0.9112, 0.938, 0.8576])
    },
    'TC': {
        'VC': np.mean([3.27, 3.46, 3.27, 3.27, 3.08]),
        'VC_std': np.std([3.27, 3.46, 3.27, 3.27, 3.08]),
        'Sugar': np.mean([1.4141, 1.48125, 1.5089, 1.4378, 1.58395]),
        'Sugar_std': np.std([1.4141, 1.48125, 1.5089, 1.4378, 1.58395]),
        'Acid': np.mean([0.7772, 0.7772, 0.8308, 0.8576, 0.804]),
        'Acid_std': np.std([0.7772, 0.7772, 0.8308, 0.8576, 0.804])
    }
}

data_apr = {
    'CK1': {
        'VC': np.mean([11.35, 12.88, 12.12, 12.88, 12.50]),
        'VC_std': np.std([11.35, 12.88, 12.12, 12.88, 12.50]),
        'Sugar': np.mean([2.82425, 2.83215, 2.8914, 2.84795, 2.8835]),
        'Sugar_std': np.std([2.82425, 2.83215, 2.8914, 2.84795, 2.8835]),
        'Acid': np.mean([0.938, 0.9112, 0.938, 0.9648, 0.938]),
        'Acid_std': np.std([0.938, 0.9112, 0.938, 0.9648, 0.938])
    },
    'CK2': {
        'VC': np.mean([7.12, 7.88, 8.08, 7.50, 7.31]),
        'VC_std': np.std([7.12, 7.88, 8.08, 7.50, 7.31]),
        'Sugar': np.mean([2.9783, 2.9546, 2.98225, 2.99015, 2.91905]),
        'Sugar_std': np.std([2.9783, 2.9546, 2.98225, 2.99015, 2.91905]),
        'Acid': np.mean([0.9648, 0.938, 0.9648, 0.938, 0.9112]),
        'Acid_std': np.std([0.9648, 0.938, 0.9648, 0.938, 0.9112])
    },
    'TK': {
        'VC': np.mean([14.23, 13.85, 14.04, 14.04, 13.85]),
        'VC_std': np.std([14.23, 13.85, 14.04, 14.04, 13.85]),
        'Sugar': np.mean([2.7966, 2.85585, 2.8282, 2.77685, 2.86375]),
        'Sugar_std': np.std([2.7966, 2.85585, 2.8282, 2.77685, 2.86375]),
        'Acid': np.mean([0.9916, 0.9648, 0.9916, 1.0184, 0.9916]),
        'Acid_std': np.std([0.9916, 0.9648, 0.9916, 1.0184, 0.9916])
    },
    'TC': {
        'VC': np.mean([5.19, 6.15, 5.77, 5.58, 5.96]),
        'VC_std': np.std([5.19, 6.15, 5.77, 5.58, 5.96]),
        'Sugar': np.mean([2.85585, 2.86375, 2.7887, 2.89535, 2.84005]),
        'Sugar_std': np.std([2.85585, 2.86375, 2.7887, 2.89535, 2.84005]),
        'Acid': np.mean([1.0184, 1.0184, 0.9916, 0.9916, 0.9916]),
        'Acid_std': np.std([1.0184, 1.0184, 0.9916, 0.9916, 0.9916])
    }
}

# Calculate Sugar/Acid Ratio
def add_ratio(d):
    for k in d:
        ratio = d[k]['Sugar'] / d[k]['Acid']
        ratio_std = ratio * np.sqrt(
            (d[k]['Sugar_std'] / d[k]['Sugar'])**2 +
            (d[k]['Acid_std'] / d[k]['Acid'])**2
        )
        d[k]['Sugar_Acid_Ratio'] = ratio
        d[k]['Sugar_Acid_Ratio_std'] = ratio_std

add_ratio(data_jan)
add_ratio(data_apr)

# Colors and Markers
colors = {'CK1': '#1f77b4', 'CK2': '#ff7f0e', 'TK': '#2ca02c', 'TC': '#d62728'}
markers = {'Jan': 'o', 'Apr': 's'}

# ============================== Plotting ==============================
fig, ax = plt.subplots(figsize=(12, 8))

# January Plot
for t in ['CK1', 'CK2', 'TK', 'TC']:
    x = data_jan[t]['Sugar_Acid_Ratio']
    y = data_jan[t]['VC']
    ax.scatter(x, y, s=MARKER_SIZE_JAN, alpha=0.7, color=colors[t], marker=markers['Jan'],
               label=f'{t} (Jan)', edgecolors='black')
    ax.errorbar(x, y,
                xerr=data_jan[t]['Sugar_Acid_Ratio_std'],
                yerr=data_jan[t]['VC_std'],
                fmt='none', color=colors[t], alpha=0.5, capsize=3)

# April Plot
for t in ['CK1', 'CK2', 'TK', 'TC']:
    x = data_apr[t]['Sugar_Acid_Ratio']
    y = data_apr[t]['VC']
    ax.scatter(x, y, s=MARKER_SIZE_APR, alpha=0.7, color=colors[t], marker=markers['Apr'],
               label=f'{t} (Apr)', edgecolors='black')
    ax.errorbar(x, y,
                xerr=data_apr[t]['Sugar_Acid_Ratio_std'],
                yerr=data_apr[t]['VC_std'],
                fmt='none', color=colors[t], alpha=0.5, capsize=3)

# Trends
for t in ['CK1', 'CK2', 'TK', 'TC']:
    ax.plot([data_jan[t]['Sugar_Acid_Ratio'], data_apr[t]['Sugar_Acid_Ratio']],
            [data_jan[t]['VC'], data_apr[t]['VC']],
            color=colors[t], alpha=0.3, linestyle='--')

# Labels and Legend
ax.set_xlabel('Sugar–acid ratio', fontsize=LABEL_FONT_SIZE)
ax.set_ylabel('Ascorbic acid (mg/100 g)', fontsize=LABEL_FONT_SIZE)
ax.tick_params(axis='both', labelsize=BASE_FONT_SIZE)

legend_elements_month = [
    Line2D([0],[0], marker='o', color='w', markerfacecolor='gray', markersize=10, label='Jan'),
    Line2D([0],[0], marker='s', color='w', markerfacecolor='gray', markersize=10, label='Apr')
]
legend_elements_treat = [
    Line2D([0],[0], marker='o', color='w', markerfacecolor=colors[t], markersize=10, label=t)
    for t in ['CK1','CK2','TK','TC']
]

leg1 = ax.legend(handles=legend_elements_month, loc='upper left',
                 bbox_to_anchor=MONTH_LEG_ANCHOR, borderaxespad=0.0,
                 title='Month', prop={'size': LEGEND_FONT_SIZE},
                 title_fontsize=LEGEND_TITLE_SIZE, frameon=True)
ax.add_artist(leg1)

ax.legend(handles=legend_elements_treat, loc='lower right', title='Treatment',
          prop={'size': LEGEND_FONT_SIZE}, title_fontsize=LEGEND_TITLE_SIZE,
          frameon=True)

# Annotation
ax.text(ANNO_POS[0], ANNO_POS[1],
        'High Quality: High VC + High S/A Ratio',
        transform=ax.transAxes, fontsize=ANNO_FONT_SIZE,
        va='top', ha='left',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5, edgecolor='none'))

ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
