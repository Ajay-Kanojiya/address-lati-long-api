from address_detail_api import app
import uvicorn


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)