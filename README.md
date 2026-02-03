This is the frontend for the Voxcribe application, a speech-to-text transcription service.

## Getting Started

To run this frontend application, you'll need to have the backend service running. See the [backend repository](https://github.com/MadhavR97/Voxcribe_Python_Whisper_Backend.git) for setup instructions.

## Prerequisites

- Node.js 18+
- Backend service running on http://localhost:8000 (or configured via environment variable)

## Configuration

Create a `.env.local` file based on `.env.example` and set the `BACKEND_URL` to match your backend service URL.

## Getting Started

First, run the development server:

```bash
# First, install dependencies
npm install

# Create an environment file based on the example
cp .env.example .env.local

# Edit .env.local to point to your backend URL
# Then run the development server
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
