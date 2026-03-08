# Frontend - Learn React

Next.js React application with TypeScript and Tailwind CSS.

## Getting Started

### Prerequisites

- Node.js 18+
- npm or yarn

### Installation

```bash
npm install
```

### Development

Start the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the application.

Changes in `src/app/` and `components/` will automatically hot-reload in the browser.

## Project Structure

- **`src/app/`** - App Router pages and layouts
  - `page.tsx` - Homepage component
  - `layout.tsx` - Root layout
  - `globals.css` - Global styles
- **`components/`** - Reusable React components
- **`public/`** - Static assets
- **`package.json`** - Dependencies and scripts

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint checks

## Learning: Building Your First Component

### Example: Create a Counter Component

Create `components/Counter.tsx`:

```typescript
'use client';

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div className="flex flex-col items-center gap-4">
      <p className="text-2xl font-bold">Count: {count}</p>
      <button
        onClick={() => setCount(count + 1)}
        className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
      >
        Increment
      </button>
    </div>
  );
}
```

Use it in `src/app/page.tsx`:

```typescript
import Counter from '@/components/Counter';

export default function Home() {
  return (
    <main className="min-h-screen p-8">
      <h1 className="text-4xl font-bold mb-8">Learn React</h1>
      <Counter />
    </main>
  );
}
```

## Learning: Fetch Data from Backend

### Example: Call Backend API

```typescript
'use client';

import { useEffect, useState } from 'react';

interface ApiData {
  message: string;
}

export default function ApiExample() {
  const [data, setData] = useState<ApiData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch('http://localhost:8000/api/hello?name=React');
        const json: ApiData = await response.json();
        setData(json);
      } catch (error) {
        console.error('Failed to fetch:', error);
      } finally {
        setLoading(false);
      }
    }

    fetchData();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (!data) return <p>Failed to load data</p>;

  return <p className="text-lg">{data.message}</p>;
}
```

## Key React Concepts

### Hooks

- **`useState`** - Manage component state
- **`useEffect`** - Run side effects after render
- **`useContext`** - Access context values
- **`useCallback`** - Memoize functions
- **`useMemo`** - Memoize values

### Best Practices

- Use functional components
- Keep components small and reusable
- Place 'use client' directive for client-side components
- Use TypeScript for type safety
- Leverage Tailwind CSS for styling

## Tailwind CSS

All styling uses Tailwind CSS utility classes. Examples:

```typescript
// Text styling
<h1 className="text-4xl font-bold">Title</h1>

// Spacing
<div className="p-4 mb-8">Content</div>

// Colors
<button className="bg-blue-500 hover:bg-blue-600">Button</button>

// Layout
<div className="flex justify-center items-center">Centered</div>
```

See [Tailwind CSS Documentation](https://tailwindcss.com/docs) for all utilities.

## Connecting to Backend

The backend API runs on `http://localhost:8000`.

**Key endpoints for learning:**
- `GET /api/hello?name=YourName` - Get a greeting
- `GET /api/data` - Get sample data
- `POST /api/echo` - Echo back data

**API Documentation**: http://localhost:8000/docs

## Deployment to Vercel

### Prerequisites

1. Sign up at [Vercel](https://vercel.com)
2. Install Vercel CLI: `npm install -g vercel`

### Deploy

```bash
vercel
```

Or connect your git repository:
1. Push code to GitHub/GitLab/Bitbucket
2. Log in to Vercel
3. Click "New Project" and import your repository
4. Vercel auto-detects Next.js and configures settings
5. Set environment variable for backend URL in Vercel dashboard

### Environment Variables for Production

Create `.env.local`:

```
NEXT_PUBLIC_API_URL=https://your-backend-domain.com
```

Update API calls:

```typescript
const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
const response = await fetch(`${apiUrl}/api/hello?name=React`);
```

## Resources

- [Next.js Documentation](https://nextjs.org/docs)
- [React Documentation](https://react.dev)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Tailwind CSS](https://tailwindcss.com/)
- [Vercel Deployment](https://vercel.com/docs)

## Troubleshooting

### Module Not Found

```bash
npm install
```

### CORS Errors

Make sure backend CORS is configured correctly in `../backend/main.py` and includes your frontend URL.

### Port 3000 Already in Use

```bash
npm run dev -- -p 3001
```

## EditorConfig

This project uses standard Node.js and React patterns. Install recommended VS Code extensions for better development experience.

## Next Steps

1. Modify the homepage in `src/app/page.tsx`
2. Create a new page in `src/app/about.tsx`
3. Build a component in `components/`
4. Fetch data from the backend API
5. Deploy to Vercel

Happy learning!
