# Learn React - Full-Stack Project

A comprehensive learning project for React, web services, and full-stack development. Built with Next.js (React frontend) and FastAPI (Python backend). Deployable on Vercel and cloud platforms.

## Project Structure

This is a monorepo with separate frontend and backend:

```
learn_react/
├── frontend/           # Next.js React application
│   ├── src/app/        # App Router pages and layouts
│   ├── components/     # Reusable React components
│   ├── public/         # Static assets
│   └── package.json
└── backend/            # FastAPI Python server
    ├── main.py         # API routes
    ├── pyproject.toml  # Dependencies (managed by UV)
    └── .venv/          # Python virtual environment
```

## Overview

This project demonstrates full-stack development with:

- **Frontend**: Modern React with Next.js, TypeScript, Tailwind CSS
- **Backend**: FastAPI web services in Python
- **Learning Focus**: React patterns, API integration, full-stack architecture

Perfect for developers with a Python background learning React and modern web development.

## Quick Start

### 1. Start the Frontend (Next.js)

```bash
cd frontend
npm install  # Only needed first time
npm run dev
```

Frontend: http://localhost:3000

### 2. Start the Backend (FastAPI)

In a new terminal:

```bash
cd backend
# Install UV (first time only)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies and run
uv sync
uv run main.py
```

Backend API: http://localhost:8000
API Docs: http://localhost:8000/docs

## Frontend Development

See [frontend/README.md](frontend/README.md) for details.

**Key commands:**
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run lint` - Run ESLint

## Backend Development

See [backend/README.md](backend/README.md) for details.

**Key endpoints:**
- `GET /api/hello` - Simple greeting
- `GET /api/data` - Sample data
- `POST /api/echo` - Echo endpoint
- `/docs` - Interactive API documentation

## Connecting Frontend to Backend

Example fetch call from React component:

```typescript
// src/app/page.tsx
const response = await fetch('http://localhost:8000/api/hello?name=React');
const data = await response.json();
```

For production, update the API base URL to your deployed backend domain.

## Deployment

### Deploy Both to Vercel (Free)

Vercel supports both Next.js and FastAPI natively!

**Frontend:**
```bash
cd frontend
vercel
```

**Backend:**
No special setup needed! Vercel automatically detects the FastAPI app from `pyproject.toml`.

**Steps:**
1. Push entire monorepo to GitHub
2. Create two Vercel projects:
   - **Project 1** (Frontend): Root directory = `/frontend`
   - **Project 2** (Backend): Root directory = `/backend`
3. Set `NEXT_PUBLIC_API_URL` environment variable in frontend project
4. Both deploy automatically on git push!

### Environment Variables

In Vercel dashboard for frontend project:
```
NEXT_PUBLIC_API_URL=https://your-backend-project.vercel.app
```

### Alternative Platforms

If you want separate providers:
- **Frontend**: Vercel (free)
- **Backend**: Railway, Render, Heroku, or AWS (some have free tiers)

## Learning Path

1. **Frontend Basics**
   - Modify `frontend/src/app/page.tsx`
   - Create new pages in `frontend/src/app/`
   - Build components in `frontend/components/`

2. **Backend Basics**
   - Add new endpoints in `backend/main.py`
   - Implement business logic
   - Test with API docs at `/docs`

3. **Frontend-Backend Integration**
   - Fetch data from API endpoints
   - Handle async operations with React hooks
   - Implement error handling

4. **Deployment**
   - Deploy frontend to Vercel
   - Deploy backend to cloud platform
   - Update API URLs for production

## Resources

### Frontend
- [Next.js Documentation](https://nextjs.org/docs)
- [React Documentation](https://react.dev)
- [Tailwind CSS](https://tailwindcss.com/)

### Backend
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Web Services](https://docs.python.org/3/library/http.server.html)
- [CORS in Web APIs](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

### Full-Stack
- [API Design Best Practices](https://swagger.io/resources/articles/best-practices-in-api-design/)
- [REST API Standards](https://restfulapi.net/)

## Environment Variables

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Backend (.env)
```
BACKEND_PORT=8000
ENVIRONMENT=development
```

## Troubleshooting

### CORS Errors
If you see CORS errors in the browser, check that:
1. Backend is running on the correct port (8000)
2. Frontend URL is in the CORS allowed list in `backend/main.py`
3. Requests use correct API URL

### Module Not Found
```bash
# Frontend
cd frontend
npm install

# Backend
cd backend
uv sync
```

## License

This is a learning project. Feel free to modify and use for your own learning.
