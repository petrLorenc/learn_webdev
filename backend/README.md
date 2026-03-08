# Learn React - FastAPI Backend

This is the Python FastAPI backend for the Learn React project.

## Setup

### Install UV

[UV](https://astral.sh/uv/) is a fast Python package installer and resolver. Install it first:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or on Windows:
```powershell
powershell -ExecutionPolicy BypassUser -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Install Dependencies

```bash
uv sync
```

This will create a virtual environment and install all dependencies from `pyproject.toml`.

## Running the Server

```bash
uv run main.py
```

Or activate the virtual environment and run:
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
python main.py
```

The API will be available at `http://localhost:8000`

## Deployment Configuration

Vercel's `pyproject.toml` script configuration tells Vercel where to find your FastAPI app:
```toml
[project.scripts]
app = "main:app"
```

This points to the `app` instance in `main.py`. No additional configuration needed!

### API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Example Endpoints

- `GET /` - Health check
- `GET /api/hello?name=YourName` - Simple greeting
- `GET /api/data` - Get sample structured data
- `POST /api/echo` - Echo back JSON data

## CORS Configuration

The backend is configured to accept requests from the Next.js frontend running on:
- localhost:3000
- localhost:3001
- 127.0.0.1:3000
- 127.0.0.1:3001

Modify the CORS settings in `main.py` for production deployments.

## Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

## Deployment

### Deploy to Vercel (Free Tier)

Vercel natively supports FastAPI with zero configuration:

1. Configure your FastAPI app in `pyproject.toml`:
```toml
[project.scripts]
app = "main:app"
```

2. Push to GitHub and connect repo to Vercel dashboard
3. Vercel auto-detects FastAPI and deploys it
4. Set environment variables in Vercel project settings
5. Your API is live on `https://your-project.vercel.app`

### Alternative Platforms

- [Railway](https://railway.app/) - Easy Python deployment
- [Render](https://render.com/) - Free tier available
- [Heroku](https://www.heroku.com/) - Paid plans
- [AWS](https://aws.amazon.com/) - EC2 or Elastic Beanstalk
- [Google Cloud](https://cloud.google.com/) - Cloud Run or App Engine

**Recommended**: Use Vercel for both frontend and backend to keep everything in one place!
