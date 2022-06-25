import sentry_sdk
sentry_sdk.init(
    dsn="https://7ae8944ef0ce4192993136fc95051e9a@o1298570.ingest.sentry.io/6529702",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

a = []
b = a[1]