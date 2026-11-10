[21, 83, 5.9, 1360, 5600, 1],
    [22, 98, 8.2, 1260, 8000, 1],
    [23, 75, 4.7, 1400, 4400, 1],
    [24, 89, 6.8, 1310, 6900, 1],
    [25, 85, 6.5, 1330, 6300, 1],
    [26, 101, 8.6, 1240, 8500, 1],
    [27, 79, 5.3, 1380, 4900, 1],
    [28, 92, 7.3, 1280, 7500, 1],
    [29, 82, 5.8, 1350, 5800, 1],
    [30, 96, 7.9, 1270, 7800, 1],
]

COLUMNS = [
    "Machine_ID",
    "Temperature_C",
    "Vibration_mm_s",
    "Speed_RPM",
    "Operating_Hours",
    "Failure_Risk",
]

FEATURE_COLUMNS = [
    "Temperature_C",
    "Vibration_mm_s",
    "Speed_RPM",
    "Operating_Hours",
]


def load_pump_data():
    """Return the 30 sample pump records as a pandas DataFrame."""
    return pd.DataFrame(PUMP_RECORDS, columns=COLUMNS)


def show_pump_data(data):
    """Print the dataset and display its class distribution and charts."""
    print("\nPUMP DATASET")
    print(data.to_string(index=False))
    print("\nClass distribution:")
    print(data["Failure_Risk"].value_counts().rename(
        index={0: "Normal", 1: "Failure risk"}
    ))

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=data,
        x="Temperature_C",
        y="Vibration_mm_s",
        hue="Failure_Risk",
        style="Failure_Risk",
        s=100,
    )
    plt.title("Pump Temperature vs. Vibration")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Vibration (mm/s)")
    plt.legend(title="0 = Normal, 1 = Failure risk")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    sns.heatmap(
        data[FEATURE_COLUMNS + ["Failure_Risk"]].corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
    )
    plt.title("Correlation of Pump Engineering Variables")
    plt.tight_layout()
    plt.show()


if name == "main":
    show_pump_data(load_pump_data())