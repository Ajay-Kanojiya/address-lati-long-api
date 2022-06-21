from address_detail_api import app
import uvicorn


if __name__ == "__main__":
   uvicorn.run(app, debug=False)
