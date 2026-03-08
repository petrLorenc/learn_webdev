# Learn React - Project Guidelines

Full-stack learning project with React (Vite) frontend and Python (FastAPI) backend. Deployable on Vercel (frontend + backend). The developer has a Python background. Focus explanations on React fundamentals, API integration, and full-stack architecture. Keep examples beginner-friendly with clear comments and documentation.

## Project Structure (Monorepo)

```
/frontend     - Next.js React application (TypeScript, Tailwind CSS)
/backend      - FastAPI Python web services
README.md     - Root documentation
```

## Frontend Stack

- **Next.js 16** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **React Hooks** - Modern state management
- **Vite** - Fast development server and build tool

## Backend Stack

- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **UV** - Fast Python package installer and resolver
- **CORS** - Cross-origin resource sharing configured

## Key Guidelines

- Frontend: Modern React patterns (hooks, functional components)
- Backend: RESTful API design with FastAPI
- Both: Keep examples beginner-friendly with clear explanations
- Leverage Python background for backend development
- Demonstrate frontend-backend communication patterns

## Development Workflow

### Frontend Development

1. `cd frontend && npm run dev` - Start Next.js server (localhost:3000)
2. Edit files in `frontend/src/app/` and `frontend/components/`
3. Use TypeScript for type safety
4. Test API integration with backend

### Backend Development

1. `cd backend && uv sync` - Install dependencies (first time)
2. `uv run main.py` - Start FastAPI server (localhost:8000)
3. Add endpoints to `src/routes`
4. Test at http://localhost:8000/docs (Swagger UI)

## Frontend Project Structure

- `src/app/` - App Router pages and layouts
- `components/` - Reusable React components
- `public/` - Static assets
- `package.json` - Frontend dependencies

## Backend Project Structure

- `main.py` - FastAPI application
- `src/routes/` - API route definitions
- `src/models/` - Pydantic models for data validation
- `src/utils/` - Utility functions
- `pyproject.toml` - Python dependencies
- `venv/` - Python virtual environment

## Learning Focus Areas

1. **React Fundamentals** - Components, hooks, state management
2. **API Integration** - Fetching data from backend
3. **Python FastAPI** - Building web services
4. **CORS and Middleware** - Security and communication
5. **Full-Stack Architecture** - Frontend-backend coordination
6. **Deployment** - Vercel (frontend) and cloud platforms (backend)

## Common Commands

### Frontend
- `cd frontend && npm run dev` - Development server
- `npm run build` - Production build
- `npm run lint` - Run ESLint

### Backend
- `uv sync` - Install dependencies
- `uv run main.py` - Start server
- Check http://localhost:8000/docs - API documentation

## CORS Configuration

Backend is pre-configured for localhost development. For production:
1. Update allowed origins in `backend/main.py`
2. Set frontend domain in CORS allowed_origins
3. Configure environment variables

## API Communication Example

In `frontend/src/app/page.tsx`:

```typescript
const response = await fetch('http://localhost:8000/api/hello?name=React');
const data = await response.json();
```

## Deployment

Both frontend and backend deploy to Vercel:

- **Frontend**: `npm run dev` or deploy to Vercel
- **Backend**: Deploys automatically via `pyproject.toml` script configuration
- Configure `NEXT_PUBLIC_API_URL` environment variable for production

### Quick Deploy to Vercel

1. Push monorepo to GitHub
2. Create two Vercel projects (one for `/frontend`, one for `/backend`)
3. Set environment variables in Vercel dashboard
4. Done! Auto-deploys on git push
