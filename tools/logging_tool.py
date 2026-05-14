import mlflow


def log_query(query):

    mlflow.log_param(
        "query",
        query
    )



def log_response(response):

    mlflow.log_text(
        response,
        "response.txt"
    )