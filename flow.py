from prefect import flow

@flow(log_prints=True)
def hello():
  print("hello!")

if __name__ == "__main__":
    hello.deploy(
        name="my-deployment",
        work_pool_name="my-managed-pool",
        image="caomaodjs/prefect_demo:2.0.0",
    )
