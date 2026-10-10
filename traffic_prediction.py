import mysql.connector
import pandas as pd
from database.db_config import DB_CONFIG


def predict_next_requests(window=5):
    connection = mysql.connector.connect(**DB_CONFIG)

    query = '''
        SELECT COUNT(*) AS requests, DATE_FORMAT(created_at, '%Y-%m-%d %H:%i') AS minute
        FROM traffic_logs
        GROUP BY minute
        ORDER BY minute
    '''

    data = pd.read_sql(query, connection)
    connection.close()

    if len(data) < window:
        print("Not enough traffic data for prediction.")
        return None

    recent = data["requests"].tail(window)
    prediction = recent.mean()

    print("Recent request counts:")
    print(recent.to_list())
    print("Predicted next-minute requests:", round(prediction, 2))

    return prediction


if __name__ == "__main__":
    predict_next_requests()
