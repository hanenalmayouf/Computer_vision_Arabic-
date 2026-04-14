import json
import os

# Path to the lab notebook
p = r"c:\Users\nayef\Downloads\ultralytics\labs\04_evaluation.ipynb"

# Check if file exists
if not os.path.exists(p):
    print(f"Error: {p} not found.")
    exit(1)

with open(p, "r", encoding="utf-8") as f:
    nb = json.load(f)

# Define the new ROI section cells
nc = [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## 5. ROI-Driven Evaluation\n",
        "\n",
        "In the real world, not all errors are equal. A **False Negative** (missing a shoplifter) costs the price of the item, but a **False Positive** (wrongly accusing an innocent customer) can cost thousands in legal fees and brand damage.\n",
        "\n",
        "### Case Study: Shoplifting Detection\n",
        "- **FN Cost**: $50 (Average stolen item value)\n",
        "- **FP Cost**: $2,500 (Legal fees, lost loyalty, brand damage)\n",
        "\n",
        "Let's find the threshold that minimizes the **Total Financial Loss**."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "\n",
        "# Performance at different confidence thresholds\n",
        "data = {\n",
        "    'threshold': [0.1, 0.3, 0.5, 0.7, 0.8, 0.9],\n",
        "    'tp': [450, 400, 350, 250, 150, 50],\n",
        "    'fp': [1000, 200, 50, 10, 2, 0],\n",
        "    'fn': [50, 100, 150, 250, 350, 450]\n",
        "}\n",
        "\n",
        "df = pd.DataFrame(data)\n",
        "\n",
        "# Calculate Precision, Recall, and F1 for each row\n",
        "df['precision'] = df['tp'] / (df['tp'] + df['fp'])\n",
        "df['recall'] = df['tp'] / (df['tp'] + df['fn'])\n",
        "df['f1'] = 2 * (df['precision'] * df['recall']) / (df['precision'] + df['recall'])\n",
        "\n",
        "print(\"Model Performance Table:\")\n",
        "print(df[['threshold', 'precision', 'recall', 'f1']])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "### 💡 Exercise: Calculate Total Financial Loss\n",
        "\n",
        "Write a function to calculate the total loss and apply it to the dataframe to find the best threshold for the business."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "COST_FN = 50\n",
        "COST_FP = 2500\n",
        "\n",
        "def calculate_total_loss(row):\n",
        "    # TODO: Implement the formula: (FN * COST_FN) + (FP * COST_FP)\n",
        "    return 0\n",
        "\n",
        "df['total_loss'] = df.apply(calculate_total_loss, axis=1)\n",
        "\n",
        "best_f1_threshold = df.loc[df['f1'].idxmax(), 'threshold']\n",
        "best_roi_threshold = df.loc[df['total_loss'].idxmin(), 'threshold']\n",
        "\n",
        "print(f\"Best Threshold for F1:  {best_f1_threshold}\")\n",
        "print(f\"Best Threshold for ROI: {best_roi_threshold}\")\n",
        "\n",
        "print(\"\\nFull ROI Table:\")\n",
        "print(df[['threshold', 'f1', 'total_loss']])"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "<details>\n",
        "<summary>Solution</summary>\n",
        "\n",
        "```python\n",
        "def calculate_total_loss(row):\n",
        "    return (row['fn'] * COST_FN) + (row['fp'] * COST_FP)\n",
        "```\n",
        "\n",
        "</details>"
      ]
    }
]

# Insert the new cells before the last cell (End of Lab)
if len(nb['cells']) > 0:
    nb['cells'] = nb['cells'][:-1] + nc + nb['cells'][-1:]
else:
    nb['cells'] = nc

with open(p, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)

print(f"Successfully updated {p} with the ROI evaluation exercise.")
