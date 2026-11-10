]

CLASS_NAMES = ["Normal", "Warning", "Fault"]


def load_pump_data():
    """Create and return the pump dataset as a DataFrame."""
    return pd.DataFrame(PUMP_DATA, columns=COLUMNS)


def explore_pump_data(data):
    """Print dataset information and display the two data charts."""
    print("\nDATASET: 30 WATER PUMP RECORDS")
    print(data.to_string(index=False))

    print("\nCLASS DISTRIBUTION")
    print(data["Pump_Condition"].value_counts().sort_index().rename(
        index={0: "Normal", 1: "Warning", 2: "Fault"}
    ))

    print("\nDATA INFORMATION")
    data.info()

    print("\nSTATISTICAL DESCRIPTION")
    print(data.describe())

    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=data,
        x="Temperature_C",
        y="Vibration_mm_s",
        hue="Pump_Condition",
        style="Pump_Condition",
        s=100,
        palette="viridis",
    )
    plt.title("Water Pump Temperature vs. Vibration")
    plt.xlabel("Temperature (Celsius)")
    plt.ylabel("Vibration (mm/s)")
    plt.legend(title="0=Normal, 1=Warning, 2=Fault")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(9, 6))
    sns.heatmap(
        data.drop(columns=["Pump_ID"]).corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
    )
    plt.title("Correlation Matrix of Pump Measurements")
    plt.tight_layout()
    plt.show()


if name == "main":
    explore_pump_data(load_pump_data())