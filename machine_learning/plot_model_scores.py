import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import os
import json

def plot_model_scores(plot_type = 'Daily'):
    model_scores_files = os.listdir('./data/Model_Scores/')
    model_scores = {}
    models = []
    for model_score_file in model_scores_files:
        model_name = model_score_file.split('.')[0]
        if(plot_type == 'Daily'):
            if(('Weekly' in model_name) | ('Monthly' in model_name)):
                continue
            else:
                models.append(model_name)
        else:
            if(plot_type not in model_name):
                continue
            else:
                models.append(model_name)
        with open(f'./data/Model_Scores/{model_score_file}', 'r') as load_file:
            score = json.load(load_file)
        if('1' in score):
            cats = score['1'].keys()
            for cat in cats:
                all_scores = []
                for day_num in range(1, 8):
                    for model_num in range(1, 4):
                        all_scores.append(score[f'{day_num}'][cat][f'{model_num}']['MAPE'])
                mean_score = np.mean(all_scores)
                if(cat in model_scores):
                    model_scores[cat][model_name] = mean_score
                else:
                    model_scores[cat] = {}
                    model_scores[cat][model_name] = mean_score
        else:
            cats = score.keys()
            for cat in cats:
                if(cat in model_scores):
                    model_scores[cat][model_name] = score[cat]['MAPE']
                else:
                    model_scores[cat] = {}
                    model_scores[cat][model_name] = score[cat]['MAPE']
    
    cols = ['blue', 'green', 'red', 'yellow', 'cyan', 'magenta', 'pink', 'brown', 'orange', 'black']
    models_col = dict(zip(models, cols[:len(models)]))
    models_lines = [Line2D([0], [0], color = models_col[x], lw = 4) for x in models_col]
    
    _, ax = plt.subplots(1, 1, figsize = (12, 7))
    total_scores = 0
    total_num = 0
    for cat_idx, cat in enumerate(model_scores):
        avail_models = model_scores[cat].keys()
        score_vals = model_scores[cat].values()
        total_scores = total_scores + np.sum(list(score_vals))
        total_num = total_num + len(score_vals)
        cols = [models_col[x] for x in avail_models]
        ax.scatter(np.repeat(cat_idx, len(avail_models)), score_vals, c = cols, facecolor = cols, s = 5)
    for v_idx in range(-1, len(model_scores)):
        ax.axvline(v_idx + 0.5, color = 'black', alpha = 0.25)
    ax.set_ylabel("MAPE")
    ax.set_xticks([])
    ax.set_xlabel("Categories")
    ax.legend(models_lines, models, loc = 'upper center', ncol = 4)
    ax.set_title(f"Forecasting Scores")
    ax.set_ylim(0, 50)
    plt.savefig(f'./images/{plot_type}_performance_comparison.png', bbox_inches = 'tight')
    print(f"{plot_type} Mean MAPE = {total_scores / total_num: .2f} %")

plot_model_scores('Daily')
plot_model_scores('Weekly')
plot_model_scores('Monthly')