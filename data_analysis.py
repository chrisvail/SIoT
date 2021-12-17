import boto3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf

def main():
    local_table_name = "SIOT_core_table"
    api_table_name = "SIoTWeather"

    dynamodb = boto3.resource("dynamodb")
    local_table = dynamodb.Table(local_table_name)
    api_table = dynamodb.Table(api_table_name)

    response = local_table.scan()
    # pprint(response.items())

    df = pd.DataFrame(list(response.items())[0][1], dtype="float32")
    df = df.apply(pd.to_numeric, errors='ignore')
    df.rename(columns={"temperature":"Water Temperature"}, inplace=True)
    df["date"] = pd.to_datetime(df["ts"], unit="ms")
    df.set_index("date", drop=True, inplace=True)
    df.drop("device_id", axis=1, inplace=True)
    df.drop("ts", axis=1, inplace=True)

    weather_resp = api_table.scan()
    json_data = pd.json_normalize(list(weather_resp.items())[0][1])
    weather_data = pd.DataFrame(json_data)
    weather_data = weather_data.apply(pd.to_numeric, errors='ignore')
    weather_data["date"] = pd.to_datetime(weather_data["timestamp"], unit="ms")
    weather_data = weather_data[["main.pressure", "clouds.all", "main.temp", "date"]]
    weather_data.set_index("date", drop=True, inplace=True)

    weather_data.rename(columns={"main.pressure":"Pressure",
                                 "main.temp":"Outside Temperature",
                                 "clouds.all":"Cloud Coverage"},inplace=True)


    fivemin_plant_data = df.resample(rule="5T").mean()
    fivemin_weather_data = weather_data.resample(rule="5T").bfill()

    hourly_plant_data = df.resample(rule="H").mean()
    hourly_weather_data = weather_data.resample(rule="H").mean()

    full_data = fivemin_plant_data.join(fivemin_weather_data).dropna(axis=0)
    full_data_hourly = hourly_plant_data.join(hourly_weather_data).dropna(axis=0)

    # print(full_data)

    full_data.hist(bins=40)

    plt.show()

    corr = full_data.corr(method="spearman")
    corr2 = corr[corr < 1].unstack().transpose().sort_values( ascending=False).drop_duplicates()

    fig, ax = plt.subplots()

    sns.heatmap(corr, cmap="coolwarm", vmin=-1, vmax=1, annot=True, ax=ax, square=True)
    ax.set_xticklabels(full_data.columns, fontsize=10, rotation=30)
    fig.gca().xaxis.tick_bottom()
    ax.set_yticklabels(full_data.columns, fontsize=10)

    plt.show()

    fig, ax = plt.subplots(3, 1)

    plot_acf(full_data_hourly["Water Temperature"], ax=ax[0], lags=24, title="Water Temperature Autocorrelation")
    plot_acf(full_data_hourly["pH"], ax=ax[1], lags=24, title="pH Autocorrelation")
    plot_acf(full_data_hourly["EC"], ax=ax[2], lags=24, title="EC Autocorrelation")
    # plot_acf(full_data_hourly["Outside Temperature"], ax=ax[3], lags=24, title="Outside Temperature Autocorrelation")

    plt.show()


    days = list(full_data.groupby(full_data.index.day))
    for day in days:
        components = pd.Series(day[1].index)
        components = components.apply(lambda x: x.hour*60*60 + x.minute*60 + x.second)
        print(components)
        # time = components["seconds"] + 60*components["minutes"] + 60*60*components["hours"]
        plt.plot(components, day[1]["EC"])
        
        

    plt.show()

if __name__ == "__main__":
    main()